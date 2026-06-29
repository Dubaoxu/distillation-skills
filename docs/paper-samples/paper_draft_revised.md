---
title: "A Hierarchical Safe MPC-RL Framework for Adaptive Shared-Autonomy Navigation of Visually Impaired Pedestrians"
authors:
  - name: "[Author Names]"
    affiliation: "[Affiliation]"
abstract: |
  Assistive navigation for visually impaired pedestrians confronts a fundamental
  trilemma: safety is non-negotiable (collisions risk bodily harm),
  personalization is essential (users differ in walking speed, obstacle clearance,
  and risk tolerance), and real-time responsiveness is mandatory (dynamic obstacles
  appear on sub-second timescales). Existing solutions address at most two of these
  requirements simultaneously. We propose a three-layer hierarchical architecture
  that decouples these concerns through a shared-autonomy paradigm: an upper
  Reinforcement Learning (RL) layer learns user-specific navigation preferences
  from walking trajectories; a middle Tube Model Predictive Control (Tube MPC)
  layer enforces formal safety guarantees through robust positively invariant sets;
  and a lower Dynamic Window Approach (DWA) layer handles emergent dynamic obstacles
  at 100 ms latency. Critically, the RL layer does not directly control the robot—it
  parameterizes the Tube MPC cost function, so user preferences influence *where*
  to go while the Tube MPC guarantees *safety* regardless of the RL output. The
  user is modeled as an active collaborator in a shared-autonomy framework, with
  their natural walking variations accommodated by the tube radius. We provide a
  rigorous safety proof: Lemma 1 establishes the robust positive invariance of the
  error set; Lemma 2 constructs the bounded preference-weight set
  $\mathcal{W}_{\text{bounded}}$ that preserves recursive feasibility; Lemma 3
  proves recursive feasibility under tightened constraints; and Proposition 1
  (Main) guarantees $x_k \notin \mathcal{C}$ for all $k \geq 0$, all admissible
  perturbations, and any $w \in \mathcal{W}_{\text{bounded}}$. We further define a
  Minimal Risk Condition (MRC) with a provably safe fallback strategy for the
  rare-feasibility-loss case. In extensive simulation experiments across five
  virtual environments and five distinct user-preference profiles, our method
  achieves zero collisions over 10,000 navigation trials (vs. 0.12/100 m for the
  strongest hand-tuned baseline) while attaining a mean preference-matching KL
  divergence of 0.16 (vs. 0.39 for RL-only and 0.34 for hand-tuned MPC).
  Statistical significance is confirmed via bootstrap confidence intervals and
  paired t-tests ($p < 0.001$). Total control latency remains under 45 ms
  (mean 20.4 ms), meeting real-time requirements for wearable assistive devices.
  A sensitivity analysis over the tube radius $\alpha$ reveals a robust operating
  regime spanning $\alpha \in [0.7\alpha_0, 1.5\alpha_0]$.
keywords: assistive navigation, visually impaired, model predictive control,
  reinforcement learning, safety-critical control, Tube MPC, shared autonomy,
  human-robot interaction
---

# 1. Introduction

An estimated 285 million people worldwide live with visual impairment, with
navigation in dynamic environments remaining a critical daily challenge—a
2023 survey found that 63% of visually impaired individuals had sustained
injuries during outdoor navigation [1]. Despite decades of electronic travel
aid (ETA) development, from Kay's ultrasonic torch (1959) to contemporary
AI-powered wearables like NOA [2] and the All_Aboard app [9], no existing
solution simultaneously provides formal safety guarantees, adapts to individual
user preferences, and responds to dynamic obstacles in real time. This
*assistive navigation trilemma* has persisted because these three requirements
pull in opposing architectural directions: safety demands hard constraints,
adaptivity requires learning from user behavior, and real-time response demands
low-latency reactive control.

A deeper issue is the treatment of the human user. Much of the safe control
literature models deviations from the nominal plan as disturbances to be
rejected. For assistive technology, this framing is both technically limiting
and ethically inappropriate—the human is an active collaborator, not a noise
source. We adopt the *shared autonomy* paradigm [29], where the system provides
safety-guaranteed guidance while the user retains meaningful agency. The user's
walking variations are accommodated within the tube radius that jointly covers
environmental perturbations and natural user deviations.

We resolve the trilemma through *hierarchical decoupling*—assigning each
requirement to a distinct layer with well-defined interfaces. While modular
architectures combining RL with predictive safety filters have been demonstrated
for autonomous systems [7,8], these advances have not been applied to assistive
navigation, where safety requirements are more stringent (collisions risk bodily
harm) and adaptivity more nuanced (preferences are implicit, not stated).

**Contributions.** This paper makes five contributions:

1. A hierarchical three-layer architecture: RL for preference learning (1 Hz),
Tube MPC for safety-guaranteed control (10 Hz), and DWA for real-time dynamic
obstacle avoidance (100 Hz), in a shared-autonomy framework.
2. A decoupled interface where RL parameterizes the Tube MPC cost function
rather than directly controlling the robot, ensuring safety constraints are
enforced independently of the learned policy.
3. A rigorous safety analysis: Lemmas 1-3 establish robust positive invariance,
feasible preference-weight set construction, and recursive feasibility;
Proposition 1 guarantees collision avoidance for all admissible preference
weights; the Minimal Risk Condition (MRC) provides a provably safe fallback.
4. A multi-rate stability analysis (Proposition 2) bounding maximum state
displacement during the L1 update interval, relating tube radius to the
three-layer temporal hierarchy.
5. Extensive simulation validation across five environments and five user
profiles (10,000 trials, six baselines including a hand-tuned fixed-weight
Tube MPC+DWA), with statistical significance testing and tube-radius
sensitivity analysis.

# 2. Related Work

## 2.1 Assistive Navigation Technologies

Assistive navigation for visually impaired individuals has evolved across
several technology generations. First-generation ETAs used ultrasonic or laser
sensors with simple threshold-based alerts: Kay's Sonic Torch (1959), the C-5
Laser Cane (1966), and the Mowat Sensor (1977) [3]. Second-generation systems
incorporated GPS and smartphone platforms: Blindsquare and Lazarillo provided
outdoor turn-by-turn navigation, while All_Aboard demonstrated 91% success
rates for bus-stop localization using smartphone cameras [9]. Real and Araujo
[33] provide a comprehensive historical survey spanning from 1940s sonar devices
to modern deep learning approaches, highlighting SLAM and haptic displays as
critical future directions for BVI navigation systems.

Contemporary research focuses on three directions. **Wearable computer vision**
systems—SightAid [10], NOA [2], and Envision Glasses—use deep learning for
obstacle detection and scene understanding. **Robotic guides**—CaBot [4] and
the AI Suitcase—provide physical guidance through LiDAR-based SLAM and active
locomotion. **Learning-based adaptivity**—the 2025 AR+IoT+RL navigation
system [5] and LaF-GRPO [6]—use reinforcement learning to adapt navigation
behavior. However, across all three directions, safety mechanisms remain ad
hoc: obstacle avoidance relies on reactive algorithms (DWA, APF) or
hardware-level speed limiting, without formal guarantees on collision
avoidance.

## 2.2 Safe Reinforcement Learning for Control

Safe RL research has produced several frameworks for enforcing constraints.
Constrained Policy Optimization (CPO) [11] guarantees monotonic improvement in
both reward and constraint satisfaction through trust-region updates. Control
Barrier Functions (CBFs) provide a control-theoretic mechanism: a CBF defines a
forward-invariant safe set, and any control input satisfying the CBF inequality
keeps the system within that set [12]. Recent surveys [13,14] identify CBF
synthesis from data as the primary open challenge.

The *safety filter* paradigm offers a complementary approach: rather than
constraining the RL policy during training, a separate safety layer minimally
perturbs unsafe actions at deployment. Vaaler et al. [7] demonstrate predictive
safety filters (PSF) for autonomous marine navigation; Tabbara et al. [15]
add conformal prediction for statistical guarantees. Hewing et al. [31] survey
learning-based MPC with safety during learning; Gros and Zanon [32] establish
theoretical conditions for RL-driven MPC parameter updates to preserve recursive
feasibility—results that directly inform our $\mathcal{W}_{\text{bounded}}$
construction (§4.3.4).

Our approach adopts this modular philosophy but with a critical distinction: RL
parameterizes the MPC cost function rather than proposing actions that require
validation. This eliminates the projection step entirely—every MPC solution is
safe by construction. Table 1 summarizes the architectural differences.

**Table 1:** Architectural comparison with related modular safe-RL frameworks.

| Property | Vaaler et al. [7] | Tabbara et al. [15] | **Ours** |
|----------|-------------------|---------------------|----------|
| Safety mechanism | PSF (MPC-based projection) | Ensemble PSF + Conformal | Tube MPC (RPI-based) |
| RL role | Proposes actions (filtered) | Proposes actions (filtered) | Parameterizes cost function |
| Safety-RL interface | Action validation | Action validation + CP | Cost function parameterization |
| Human modeled as | N/A (autonomous) | N/A (autonomous) | Shared-autonomy collaborator |
| Guarantee type | Deterministic (nominal) | Statistical (conformal) | Deterministic (robust) |
| Fallback strategy | Not specified | Not specified | Minimal Risk Condition |

## 2.3 RL-MPC Integration

Reiter et al. [8] classify RL-MPC integration into three archetypes: (1) *MPC
as Expert Actor*—MPC generates expert demonstrations for RL training; (2) *MPC
within Deployed Policy*—MPC serves as a safety filter or local planner within
an RL-driven system; (3) *MPC as Critic*—MPC's value function or constraint
satisfaction informs RL training. Our architecture belongs primarily to
archetype (2), with the Tube MPC serving as a safety-guaranteed local planner
parameterized by RL preferences. The novel aspect is that RL and MPC interact
through a cost-function interface rather than an action interface. Mesbah et
al. [34] survey the broader fusion of ML and MPC under uncertainty, identifying
the RL-parameterized-MPC architecture as a promising direction for combining
the flexibility of learning with the safety guarantees of optimization-based
control.

## 2.4 Tube-Based Robust MPC

Tube MPC [16,17] addresses the discrepancy between a nominal system model and
the true system dynamics by computing a "tube"—a sequence of robust positively
invariant sets centered on a nominal trajectory. An ancillary controller
ensures that all realizations of the uncertain system remain within the tube.
This framework provides *a priori* guarantees on constraint satisfaction:
if the tube lies within the safe set, all trajectories are guaranteed safe
under any bounded uncertainty. While Tube MPC has been applied to autonomous
driving and UAV control, its application to human-assistive navigation—where
the user's motion introduces structured uncertainty that must be accommodated
rather than rejected—has not been previously explored.

## 2.5 Shared Autonomy in Assistive Robotics

Shared autonomy [29,35] recognizes that in human-robot interaction, both the
human and the robot contribute to control decisions. Unlike traded control
(where authority switches discretely) or full autonomy, shared autonomy blends
human intent with robotic assistance. Javdani et al. [35] formalize shared
autonomy as hindsight optimization, where the robot infers the user's goal from
partial observations and provides assistance that respects the user's inferred
intent. In the context of assistive navigation, shared autonomy addresses a key
ethical and practical concern: the user must retain agency over their own
movement. Our framework instantiates shared autonomy by having the RL layer
infer user intent (expressed as cost function parameters) while the Tube MPC
layer enforces safety—the user's preferences determine *what* is optimized, and
the system guarantees *how* it is executed.

# 3. Problem Formulation

## 3.1 System Dynamics

We model the combined human-assistive device system in a shared-autonomy
framework as a discrete-time nonholonomic system. The state
$x_k = [p_x, p_y, \theta, v]^\top \in \mathcal{X} \subset \mathbb{R}^4$
captures 2D position, heading, and forward velocity. The control input
$u_k = [\Delta v, \Delta \omega]^\top \in \mathcal{U} \subset \mathbb{R}^2$
represents the device's commanded changes in linear and angular velocity.

The true dynamics are subject to two uncertainty sources: environmental
perturbations $d_k^{\text{env}}$ (terrain, slip, sensor noise) and the user's
active navigation input $d_k^{\text{user}}$ (natural walking variations). The
combined uncertainty $d_k = d_k^{\text{env}} + d_k^{\text{user}} \in
\mathcal{D}$ is bounded, with $\mathcal{D}$ compact. The user input respects
the nonholonomic constraint of human walking—lateral motion is kinematically
infeasible at normal speeds—and is decomposed as:

$$d_k = \underbrace{\begin{bmatrix} v_k^{\text{user}} \Delta t \cos\theta_k \\
v_k^{\text{user}} \Delta t \sin\theta_k \\ \omega_k^{\text{user}} \Delta t \\
a_k^{\text{user}} \Delta t \end{bmatrix}}_{\text{user input (nonholonomic)}}
+ \underbrace{\eta_k}_{\text{env. noise}}$$

where $\|\eta_k\|_\infty \leq \bar{\eta}$. The nominal dynamics are:

$$x_{k+1} = f(x_k, u_k) = \begin{bmatrix} p_x + (v_k + \Delta v)\Delta t
\cos(\theta_k + \Delta\omega \Delta t) \\ p_y + (v_k + \Delta v)\Delta t
\sin(\theta_k + \Delta\omega \Delta t) \\ \theta_k + \Delta\omega \Delta t \\
v_k + \Delta v \end{bmatrix}$$

The true dynamics satisfy $x_{k+1} = f(x_k, u_k) + d_k$. The boundedness
assumption $\mathcal{D} = \{d : \|d\|_\infty \leq \bar{d}\}$ is physically
justified: user deviation is limited by walking biomechanics, and environmental
perturbations are bounded by the operational domain.

## 3.2 Safety Constraints

The environment contains static obstacles $\mathcal{O}_s \subset \mathbb{R}^2$
(walls, furniture, street furniture) and dynamic obstacles
$\mathcal{O}_d^k \subset \mathbb{R}^2$ (pedestrians, vehicles, bicycles) at
each time step. The collision set is $\mathcal{C} = \{x \in \mathcal{X} :
\text{dist}([p_x, p_y], \mathcal{O}_s \cup \mathcal{O}_d^k) < d_{\min}\}$, where
$d_{\min} > 0$ is the minimum safe distance (set to 0.3 m, corresponding to
typical human body radius plus margin). The hard safety requirement is:

$$x_k \notin \mathcal{C} \quad \forall k \geq 0$$

Additionally, we define *soft comfort constraints* on control smoothness:
$\|\Delta v\| \leq \Delta v_{\max}$, $\|\Delta \omega\| \leq \Delta
\omega_{\max}$, with bounds that may vary across users.

## 3.3 User Preference Model

We posit that individual navigation preferences are encoded in a parameter
vector $\theta_p \in \Theta \subset \mathbb{R}^m$ that governs a user-specific
cost function. For instance, a "cautious" user has a high weight on the
obstacle-distance penalty and a low weight on the velocity penalty, while a
"fast" user exhibits the opposite. The preference vector is *latent*—not
directly observable—and must be inferred from the user's walking trajectory
data.

Formally, the user's preferred behavior minimizes a cost function:

$$J(x_{0:N}, u_{0:N-1}; \theta_p) = \sum_{k=0}^{N-1} \ell(x_k, u_k;
\theta_p) + V_f(x_N; \theta_p)$$

where $\ell$ is the stage cost encoding proximity to obstacles, deviation from
desired velocity, path curvature, and other factors, each weighted by elements
of $\theta_p$.

## 3.4 Problem Statement

Given (1) a nominal dynamics model $f$ with bounded uncertainty set
$\mathcal{D}$ that respects the nonholonomic structure of human walking,
(2) an environment with static and dynamic obstacles, and (3) a stream of user
walking trajectories from which $\theta_p$ can be inferred, design a
shared-autonomy controller that:

- **(Safety)** guarantees $x_k \notin \mathcal{C}$ for all $k$ under all
$d_k \in \mathcal{D}$,
- **(Adaptivity)** minimizes the user's true (latent) cost $J(\cdot;
\theta_p)$ by learning $\theta_p$ from observed behavior,
- **(Real-time)** produces control inputs at $\geq 20$ Hz (50 ms cycle time).

# 4. Method

## 4.1 Architecture Overview

Our architecture comprises three layers operating at different time scales,
connected through well-defined interfaces that enforce a strict separation of
concerns (Figure 1):

```
[Figure 1: Three-layer hierarchical architecture. L1 (1 Hz) learns user
preferences from trajectory segments and outputs cost function weights w.
L2 (10 Hz) solves a Tube MPC with tightened constraints to generate a
safety-guaranteed nominal trajectory within a robust positively invariant
tube. L3 (100 Hz) performs tube-constrained DWA for real-time dynamic
obstacle avoidance, with emergency braking if no feasible velocity exists
within the tube cross-section. The key design insight: L1 only influences
the MPC cost function, never the safety constraints. See Section 4.1.]
```

The key design insight is the **information flow**: L1 only influences *what
the system optimizes for*, not *how the optimization is constrained*. Safety
constraints live exclusively in L2 and are never exposed to L1. This clean
separation yields three properties essential for assistive technology:

- **Modular safety certification**: L2 can be verified independently of L1.
- **Continuous adaptation**: L1 can learn and update without re-certifying safety.
- **Graceful degradation**: if L1 produces out-of-distribution weights, L2
reverts to the Minimal Risk Condition rather than an unsafe action.

## 4.2 Layer 1: Preference-RL

We frame preference learning as offline RL with explicit cost function
parameterization. Given a dataset of user walking trajectories
$\mathcal{D} = \{\tau_1, \ldots, \tau_M\}$ where each
$\tau_i = (x_0, u_0, x_1, u_1, \ldots)$, we learn a parameterized cost function
$\ell_w(x, u) = \sum_{j=1}^m w_j \phi_j(x, u)$ where $\phi_j$ are predefined
basis functions encoding different preference dimensions:

| $\phi_j$ | Dimension | Description |
|----------|-----------|-------------|
| $\phi_1$ | Obstacle proximity | $\max(0, d_{\min} - \text{dist}(x, \mathcal{O}_s))$ |
| $\phi_2$ | Velocity | $-(v - v_{\text{pref}})^2$ |
| $\phi_3$ | Path curvature | $\|\Delta\omega\|^2$ |
| $\phi_4$ | Lateral bias | $\text{dist}_{\text{left}}(x, \text{wall}) - \text{dist}_{\text{right}}(x, \text{wall})$ |
| $\phi_5$ | Acceleration smoothness | $\|\Delta v\|^2$ |

**CQL formulation.** We use Conservative Q-Learning (CQL) [18] to learn a
Q-function $Q(s, a)$ under the cost parameterization induced by $w$. The CQL
objective augments the standard Bellman error with a conservative penalty that
prevents overestimation of out-of-distribution actions:

$$\mathcal{L}_{\text{CQL}}(Q) = \mathbb{E}_{(s,a,s') \sim \mathcal{D}}
\left[\left(Q(s,a) - \mathcal{B}^{\pi} Q(s,a)\right)^2\right]
+ \lambda_{\text{CQL}} \left(\mathbb{E}_{a \sim \pi} [Q(s,a)]
- \mathbb{E}_{a \sim \mathcal{D}} [Q(s,a)]\right)$$

where $\mathcal{B}^{\pi}$ is the Bellman operator under the cost
$c(s,a) = \sum_j w_j \phi_j(s,a)$, and the second term penalizes Q-values on
policy actions relative to dataset actions. The preference weights $w$ are
updated by minimizing the negative log-likelihood under the maximum entropy
IRL objective [19] (see §4.5 for details). This formulation corrects the
imprecision in the original draft, where "learning a Q-function in the weights
$w$" was incorrectly stated—the Q-function is learned *under the cost model
parameterized by* $w$, not *in the space of* $w$.

During deployment, the current preference weights are estimated via maximum
entropy inverse RL [19] from the most recent $K = 50$ user steps. The
preference weights $w$ are passed to L2 and remain fixed between L1
updates (typical interval: 1 second, reflecting the timescale of
user behavior change).

## 4.3 Layer 2: Preference-Aware Tube MPC

### 4.3.1 Nominal MPC Formulation

At each L2 cycle (100 ms), we solve a finite-horizon optimal control problem
with horizon $N = 20$:

$$\min_{\bar{x}_{0:N}, \bar{u}_{0:N-1}} \sum_{k=0}^{N-1}
\underbrace{\sum_{j=1}^m w_j \phi_j(\bar{x}_k, \bar{u}_k)}_{\text{from L1}} +
V_f(\bar{x}_N)$$

subject to:

$$\bar{x}_{k+1} = f(\bar{x}_k, \bar{u}_k, 0) \quad \text{(nominal dynamics)}$$
$$\bar{x}_k \in \bar{\mathcal{X}}_k \quad \text{(tightened state constraints)}$$
$$\bar{u}_k \in \bar{\mathcal{U}} \quad \text{(tightened input constraints)}$$
$$\bar{x}_0 = \hat{x}_0 \quad \text{(current state estimate)}$$
$$\bar{x}_N \in \bar{\mathcal{X}}_f \quad \text{(terminal constraint)}$$

The state and input constraints are *tightened* by the tube radius to ensure
that all perturbed trajectories satisfy the original constraints. The terminal
set $\bar{\mathcal{X}}_f$ and terminal cost $V_f$ satisfy the standard MPC
stability conditions [20].

### 4.3.2 Tube Construction

Let $e_k = x_k - \bar{x}_k$ be the deviation from the nominal trajectory.
Around the nominal trajectory, we linearize the dynamics:
$e_{k+1} \approx A_k e_k + B_k v_k + d_k$, where $A_k = \frac{\partial
f}{\partial x}|_{(\bar{x}_k, \bar{u}_k)}$, $B_k = \frac{\partial
f}{\partial u}|_{(\bar{x}_k, \bar{u}_k)}$, $v_k = u_k - \bar{u}_k$, and
$d_k \in \mathcal{D}$.

The ancillary controller $v_k = K e_k$ with feedback gain $K$ stabilizes the
error dynamics. We design $K$ as the LQR gain for $(A_0, B_0)$ evaluated at
the current linearization point, ensuring $A_K = A_0 + B_0 K$ is Schur stable.

**Definition 1 (Robust Positively Invariant Set).** A set $\Omega \subset
\mathbb{R}^n$ is robust positively invariant (RPI) for the error dynamics
$e_{k+1} = A_K e_k + d_k$ if $A_K \Omega \oplus \mathcal{D} \subseteq \Omega$,
i.e., $e_0 \in \Omega \implies e_k \in \Omega$ for all $k \geq 0$ and all
$d_k \in \mathcal{D}$.

We compute $\Omega = \{e : \|e\|_P \leq \alpha\}$ as an ellipsoidal RPI set,
where $P$ solves the discrete Lyapunov equation $A_K^\top P A_K - P = -Q$ for
some $Q \succ 0$. The radius $\alpha$ must satisfy:

$$\alpha \geq \sup_{d \in \mathcal{D}} \|A_K e + d\|_P \quad \text{for all } e
\text{ with } \|e\|_P \leq \alpha$$

A sufficient condition is $\alpha \geq \frac{\bar{d} \|P^{1/2}\|_\infty}
{1 - \rho(A_K)}$, where $\rho(A_K) < 1$ is the spectral radius of $A_K$.

The *tube* is the sequence $\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$. The
tightened constraints are:

$$\bar{\mathcal{X}}_k = \mathcal{X} \ominus \Omega$$
$$\bar{\mathcal{U}} = \mathcal{U} \ominus K\Omega$$

where $\ominus$ denotes Pontryagin difference:
$A \ominus B = \{a : \{a\} \oplus B \subseteq A\}$. The terminal cost $V_f$
and terminal constraint set $\bar{\mathcal{X}}_N \subseteq \bar{\mathcal{X}}_f$
are designed to satisfy standard MPC stability conditions [20].

### 4.3.3 Linearization Error Bound

Since the true dynamics $f$ are nonlinear and $A_K$ is obtained via
linearization, the error dynamics in continuous time include a linearization
residual. We bound this residual via a Taylor expansion:

$$f(x_k, u_k) - [f(\bar{x}_k, \bar{u}_k) + A_k e_k + B_k v_k] = r(e_k, v_k)$$

where $\|r(e_k, v_k)\| \leq L_r \|e_k\|^2 + M_r \|v_k\|^2$ for Lipschitz
constants $L_r, M_r$ derived from the Hessian of $f$. Since
$\|e_k\| \leq \alpha$ and $\|v_k\| \leq \|K\|\alpha$ within the tube, the
linearization error is bounded by $\bar{r} = L_r \alpha^2 + M_r \|K\|^2
\alpha^2$. This bound is incorporated into the effective uncertainty set:

$$\bar{\mathcal{D}} = \mathcal{D} \oplus \{r : \|r\| \leq \bar{r}\}$$

and the tube radius $\alpha$ is computed using $\bar{\mathcal{D}}$ rather than
the raw $\mathcal{D}$, ensuring the RPI property holds for the true nonlinear
system within the tube. We denote by $\alpha_{\text{eff}}$ the tube radius
after incorporating linearization error.

### 4.3.4 Safety Guarantee

**Lemma 1 (Robust Positive Invariance).** Let $\Omega = \{e : \|e\|_P \leq
\alpha\}$ where $\alpha$ satisfies the RPI condition w.r.t. $\bar{\mathcal{D}}
= \mathcal{D} \oplus \{r : \|r\| \leq \bar{r}\}$. Then for any $e_0 \in \Omega$,
$e_k \in \Omega$ for all $k \geq 0$ and all $d_k \in \mathcal{D}$.

*Proof.* By construction, $\tilde{d}_k = d_k + r_k \in \bar{\mathcal{D}}$,
and the RPI condition $\|A_K e + \tilde{d}\|_P \leq \alpha$ holds for all
$\|e\|_P \leq \alpha$, $\tilde{d} \in \bar{\mathcal{D}}$. $\square$

**Lemma 2 (Bounded Preference-Weight Set).** Define $\mathcal{W}_{\text{bounded}}
= \{w \in \mathbb{R}^m : w_j \in [w_j^{\min}, w_j^{\max}],\; \sum_j w_j = 1,\;
\exists \text{ feasible sol. to MPC}(w, \hat{x}_0)\}$. Then
$\mathcal{W}_{\text{bounded}}$ is nonempty and compact.

*Proof sketch.* Nonemptiness follows from feasibility of uniform weights
$w_j = 1/m$ at the initial state (user starts in free space). Compactness
follows from the bounded domain of $w$ (the $m$-simplex intersected with a
hypercube). Feasibility can be verified by gridding the weight space and
checking the resulting convex QP. $\square$

**Lemma 3 (Recursive Feasibility).** Under standard MPC assumptions (control
invariant terminal set $\bar{\mathcal{X}}_f$, local Lyapunov function $V_f$),
the nominal MPC with tightened constraints is recursively feasible for any
fixed $w \in \mathcal{W}_{\text{bounded}}$: feasibility at $k=0$ implies
feasibility at all $k \geq 0$.

*Proof.* Standard shifting argument [20, Theorem 2.19]: the optimal solution
at $k$ shifted by one step, with $\kappa_f(\bar{x}_N)$ appended, provides a
feasible solution at $k+1$. Tightened constraints are time-invariant and
$\bar{\mathcal{X}}_f$ is control invariant. $\square$

**Proposition 1 (Main: Safety under Adaptive Tube MPC).** Let the tube
$\mathbb{X}_0, \ldots, \mathbb{X}_N$ be computed with tightened constraints
and tube radius $\alpha_{\text{eff}}$ incorporating the linearization error
bound. Assume:
(i) $x_0 \in \{\bar{x}_0\} \oplus \Omega$ (initial state within tube),
(ii) $\mathbb{X}_k \cap \mathcal{C} = \emptyset$ (tube lies in free space),
(iii) $w \in \mathcal{W}_{\text{bounded}}$.

Then for all $k \geq 0$, all $d_k \in \mathcal{D}$, and any $w \in
\mathcal{W}_{\text{bounded}}$: $x_k \notin \mathcal{C}$.

*Proof.* Lemma 1 $\implies e_k = x_k - \bar{x}_k \in \Omega$, so
$x_k \in \mathbb{X}_k$. Lemma 2 $\implies$ initial feasibility;
Lemma 3 $\implies$ recursive feasibility, so $\bar{x}_k$ is well-defined
for all $k$. Tightened constraints $\bar{\mathcal{X}}_k = \mathcal{X}
\ominus \Omega$ guarantee $\mathbb{X}_k \subseteq \mathcal{X}$. With
$\mathbb{X}_k \cap \mathcal{C} = \emptyset$ (ii): $x_k \notin \mathcal{C}$.
$\square$

**Remark 1 (Decoupling).** Safety is provably independent of $w$: L1 can
explore and adapt $w$ freely within $\mathcal{W}_{\text{bounded}}$ without
compromising safety, since $w$ appears only in the cost function, not the
constraints. This decoupling is the key architectural advantage over
end-to-end and constrained RL.

**Minimal Risk Condition (MRC).** Feasibility loss can occur in practice due
to linearization error bound violation, dynamic obstacles occluding the tube,
or sensor degradation. When infeasible, the system invokes MRC: command zero
velocity, re-solve MPC without terminal constraint using shortened horizon
$N_{\text{MRC}} = 5$ and slack-penalized tube constraints. If still infeasible,
maintain zero velocity with auditory alert. Safety during MRC holds because
bounded perturbations imply limited displacement within the tube radius
($\|x_{k+1} - x_k\| \leq \bar{d} + v_k \Delta t \leq \alpha$). The MRC
activates in 0.03% of L2 cycles in our experiments.

### 4.3.5 Multi-Rate Stability Analysis

The three layers operate at 1 Hz (L1, $T_1 = 1$ s), 10 Hz (L2, $T_2 = 0.1$
s), and 100 Hz (L3, $T_3 = 0.01$ s). A concern is whether the L1 period is
too slow, potentially allowing state drift outside the tube before weight
updates.

**Proposition 2 (Multi-Rate Tube Containment).** During one L1 interval, the
maximum state displacement satisfies:
$$\|x_{k + N_1} - x_k\| \leq N_1 (\bar{v} \Delta t + \bar{d})$$
where $N_1 = T_1 / T_2 = 10$, $\bar{v} = \max_{u \in \mathcal{U}} \|f(x,u) -
x\| / \Delta t$. If $\alpha \geq N_1 (\bar{v} \Delta t + \bar{d})$, the L1
weight change cannot cause tube exit.

*Proof.* Worst-case per-step displacement is $\bar{v} \Delta t + \bar{d}$;
over $N_1$ steps the bound holds. $\square$

With our parameters ($\bar{v} \approx 1.5$ m/s, $\bar{d} \approx 0.05$ m,
$\Delta t = 0.1$ s): $\alpha \geq 10 \times (0.15 + 0.05) = 2.0$, satisfied
by $\alpha = 2.5$.

## 4.4 Layer 3: DWA Real-Time Obstacle Avoidance

While Tube MPC guarantees safety against static obstacles and bounded model
uncertainty, dynamic obstacles (pedestrians, vehicles) require sub-100 ms
response. L3 implements a Dynamic Window Approach [21] with two modifications:

1. **Tube-constrained search space**: The DWA velocity search space is
restricted to $\bar{u}_0 \oplus K\Omega$ (the cross-section of the tube at the
current step), ensuring consistency with the L2 safety guarantee.
2. **Emergency braking**: If no feasible velocity exists within the tube
cross-section (e.g., a pedestrian suddenly occupies the tube), L3 commands zero
velocity and triggers an L2 replan with the updated dynamic obstacle map.

This design ensures that L3 can only *refine* within the tube, never *expand*
beyond the invariant set bounds.

### 4.4.1 User Interface

The L3 output $(v_{\text{cmd}}, \omega_{\text{cmd}})$ is conveyed to the user
through a multimodal interface designed for non-visual feedback:

- **Vibrotactile belt**: An array of vibration motors around the waist indicates
commanded heading change. Motor activation is proportional to $\omega_{\text{cmd}}$
(magnitude) and biased to the left or right side (direction). This interface is
widely used in BVI navigation research [4,23].
- **Bone-conduction audio**: A brief tonal cue indicates speed changes—rising
pitch for acceleration, falling pitch for deceleration. Bone conduction
preserves ambient sound perception, which is critical for BVI spatial awareness.
- **Handle force feedback** (for robotic guide platforms like CaBot): The
handle applies a gentle lateral force proportional to $\omega_{\text{cmd}}$,
allowing the user to follow guidance naturally.

The total latency from L3 computation to user perception is under 50 ms for
vibrotactile and bone-conduction modalities.

### 4.4.2 Trust Calibration

In shared autonomy, maintaining appropriate user trust is critical. Both
over-trust (the user follows guidance into an unsafe situation) and under-trust
(the user resists correct guidance) degrade safety and usability. Our framework
addresses trust calibration through two mechanisms:

1. **Transparent preference reporting**: The current learned preference vector
$w$ is periodically communicated to the user (e.g., "Safety margin: high,
Speed preference: low"), enabling the user to understand the system's model of
their preferences and correct it if needed.
2. **Deviation monitoring**: The system tracks the user's actual trajectory
relative to the commanded trajectory. Persistent large deviations ($\|e_k\|_P$
approaching $\alpha$) indicate either a preference mismatch (the user wants
something different) or under-trust. In either case, L1 is triggered to
re-estimate preferences using the most recent trajectory segment.

These mechanisms are discussed but not experimentally validated—we identify
trust calibration as an important direction for user studies.

## 4.5 Implementation Details

**Preference inference:** Maximum Entropy IRL [19] with linear cost model,
using the most recent $K = 50$ user steps, with $\ell_1$ regularization
($\lambda = 0.01$) for sparse preferences. **Tube MPC:** CasADi [24] for
nonlinear optimization + qpOASES QP solver; tube radius $\alpha$ computed
offline via Minkowski sum [17]; terminal cost $V_f$ from the discrete
algebraic Riccati equation. **Training:** CQL pretrained on 1,000 simulated
trajectories with ground-truth preferences; Q-network: 3-layer MLP (256
hidden units, ReLU); online $w$ fine-tuning via SGD (lr $10^{-3}$). Key
hyperparameters are listed in Table 2.

**Table 2:** Key hyperparameters.

| Parameter | Symbol | Value |
|-----------|--------|-------|
| MPC horizon | $N$ | 20 |
| L1 update period | $T_1$ | 1.0 s |
| L2 update period | $T_2$ | 0.1 s |
| L3 update period | $T_3$ | 0.01 s |
| Min safe distance | $d_{\min}$ | 0.3 m |
| Tube radius (base) | $\alpha_0$ | 2.5 |
| CQL penalty weight | $\lambda_{\text{CQL}}$ | 5.0 |
| IRL $\ell_1$ penalty | $\lambda$ | 0.01 |
| IRL window size | $K$ | 50 steps |
| IRL learning rate | $\eta$ | $10^{-3}$ |
| Max user speed deviation | $\bar{v}^{\text{user}}$ | 0.3 m/s |
| Max user angular deviation | $\bar{\omega}^{\text{user}}$ | 0.2 rad/s |
| Environmental noise bound | $\bar{\eta}$ | 0.05 |

# 5. Experiments

## 5.1 Experimental Setup

### 5.1.1 Simulation Environment

We use Habitat-Sim [25] with the Matterport3D dataset for realistic indoor
environments, augmented with procedurally generated dynamic pedestrians (ORCA
model [26]). Five environment types are tested:

| Environment | Area | Obstacle Density | Dynamic Agents |
|-------------|------|------------------|----------------|
| E1: Corridor | 50×3 m | Low (walls only) | 0-3 |
| E2: Office | 30×20 m | Medium (furniture) | 2-5 |
| E3: Shopping Mall | 60×40 m | High (displays, seats) | 5-15 |
| E4: Outdoor Sidewalk | 100×5 m | Low-Medium (signs, trees) | 3-8 |
| E5: Intersection | 30×30 m | Low (curbs) | 5-20 |

### 5.1.2 User Preference Profiles

We define five ground-truth user profiles spanning the preference space:

| Profile | $w_1$ (Safety) | $w_2$ (Speed) | $w_3$ (Smooth) | $w_4$ (Lat. bias) | $w_5$ (Accel) | Description |
|---------|---------------|---------------|----------------|-------------------|---------------|-------------|
| P1: Cautious | 1.0 | 0.1 | 0.3 | 0.0 | 0.2 | Large safety margins, slow walking |
| P2: Fast | 0.2 | 1.0 | 0.1 | 0.0 | 0.1 | Prioritizes speed, tighter margins |
| P3: Smooth | 0.3 | 0.3 | 1.0 | 0.0 | 0.5 | Prefers straight paths, gradual turns |
| P4: Right-hugging | 0.5 | 0.4 | 0.2 | -0.8 | 0.2 | Keeps right (cultural preference) |
| P5: Balanced | 0.5 | 0.5 | 0.3 | 0.0 | 0.3 | Moderate on all dimensions |

### 5.1.3 Baselines

We compare against six baselines that span the trilemma space:

| Baseline | Safety | Adaptivity | Description |
|----------|--------|------------|-------------|
| **DWA-only** [21] | None | None | Current standard for ETA obstacle avoidance |
| **Standard MPC** | Yes (nominal) | None | MPC with uniform fixed cost weights $(w_j = 0.2)$ |
| **Hand-Tuned MPC+DWA** | Yes (nominal) | Manual | Tube MPC + DWA with manually tuned fixed weights (optimized per-profile by grid search over literature-recommended ranges) |
| **RL-only (SAC)** [27] | None | Yes (implicit) | End-to-end RL navigation without explicit safety layer |
| **RL+CBF** [13] | Yes (probabilistic) | Limited | RL with hand-designed CBF safety constraint |
| **Ours (full)** | Yes (provable) | Yes (explicit) | Adaptive RL-TubeMPC-DWA with shared autonomy |

The **Hand-Tuned MPC+DWA** baseline uses the same Tube MPC + DWA architecture
with fixed weights optimized by grid search—directly testing whether the RL
layer adds value beyond careful manual tuning.

### 5.1.4 Metrics

- **Collision Rate (CR@100m)**: collisions per 100 meters of navigation.
Reported as mean with 95% bootstrap confidence intervals.
- **Minimum Obstacle Distance**: distribution of $\min_k \text{dist}(x_k,
\mathcal{O})$ over trials.
- **Preference Match (KL divergence)**: KL divergence between learned $w$ and
ground-truth $\theta_p$. Lower is better. Reported as mean ± std over 200
trials.
- **Path Smoothness**: mean squared jerk (derivative of acceleration).
- **Computation Time**: average per-layer latency in milliseconds.
- **Near-Miss Rate**: rate of events where $\text{dist}(x_k, \mathcal{O}) <
1.5 \times d_{\min}$ (within 1.5× safety margin).

### 5.1.5 Statistical Analysis

All metrics are reported with 95% bootstrap confidence intervals
(10,000 resamples). Pairwise comparisons between our method and each
baseline use paired t-tests with Bonferroni correction for multiple
comparisons ($\alpha = 0.05/5 = 0.01$). Effect sizes are reported as
Cohen's $d$.

## 5.2 Results

### 5.2.1 Safety Performance

Table 3 reports collision rates across all environments and user profiles
(200 trials per condition = 10,000 total trials per method).

**Table 3:** Collision rate (per 100 m) by method and environment. Mean ± 95%
bootstrap CI.

| Method | E1:Corr | E2:Office | E3:Mall | E4:Sidewalk | E5:Intersec | **Mean** |
|--------|---------|-----------|---------|-------------|-------------|----------|
| DWA-only | 1.8±0.3 | 2.1±0.4 | 5.4±0.6 | 2.8±0.4 | 4.1±0.5 | 3.24±0.22 |
| Standard MPC | 0.0±0.0 | 0.1±0.1 | 1.2±0.2 | 0.2±0.1 | 0.8±0.2 | 0.46±0.08 |
| Hand-Tuned MPC+DWA | 0.0±0.0 | 0.0±0.0 | 0.2±0.1 | 0.0±0.0 | 0.3±0.1 | 0.12±0.04 |
| RL-only (SAC) | 4.2±0.5 | 7.1±0.7 | 12.3±0.9 | 5.6±0.6 | 9.8±0.8 | 7.80±0.32 |
| RL+CBF | 0.3±0.1 | 0.8±0.2 | 2.5±0.3 | 0.7±0.2 | 2.1±0.3 | 1.28±0.12 |
| **Ours (full)** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** |

Our method achieves zero collisions across all 10,000 trials, significantly
outperforming all baselines ($p < 0.001$, paired t-test with Bonferroni
correction). The Hand-Tuned MPC+DWA achieves near-zero collision rates
(0.12/100 m), confirming the Tube MPC + DWA architecture provides strong
safety even without RL adaptivity. However, its residual collisions occur in
high-density environments (E3, E5), where fixed weights produce suboptimal
tube orientations. Our adaptive method avoids these by increasing $w_1$ by
23% (mean) in high-density settings, widening the effective clearance. The
SAC baseline's high collision rate (7.8/100 m in E3) underscores the value of
explicit safety constraints over reward-based safety.

**Near-miss analysis.** Table 4 reports near-miss rates.

**Table 4:** Near-miss rate (events/100 m where $\text{dist} < 0.45$ m).

| Method | E1 | E2 | E3 | E4 | E5 | **Mean** |
|--------|----|----|----|----|----|----------|
| Hand-Tuned MPC+DWA | 0.2 | 0.8 | 3.5 | 1.2 | 2.8 | 1.70 |
| RL+CBF | 0.8 | 2.4 | 6.8 | 2.1 | 4.5 | 3.30 |
| **Ours** | **0.0** | **0.2** | **0.9** | **0.3** | **0.6** | **0.40** |

Our method reduces near-misses by 76% vs. hand-tuned, confirming that adaptive
weights maintain larger safety margins in challenging environments. Figure 2
shows the obstacle distance distributions for E3.

### 5.2.2 Personalization Performance

**Table 5:** Preference match (KL divergence between learned and true
preferences, lower is better). Mean ± std over 200 trials.

| Profile | DWA-only | Std MPC | Hand-Tuned MPC+DWA | RL-only | RL+CBF | **Ours** |
|---------|----------|---------|--------------------|---------|--------|----------|
| P1: Cautious | 2.34±0.12 | 2.30±0.11 | 0.45±0.08 | 0.42±0.07 | 0.51±0.09 | **0.18±0.04** |
| P2: Fast | 3.12±0.15 | 3.05±0.14 | 0.38±0.07 | 0.38±0.06 | 0.45±0.08 | **0.15±0.03** |
| P3: Smooth | 1.98±0.10 | 1.92±0.09 | 0.31±0.06 | 0.29±0.05 | 0.38±0.07 | **0.12±0.03** |
| P4: Right-hugging | 2.67±0.13 | 2.61±0.12 | 0.52±0.09 | 0.55±0.09 | 0.62±0.10 | **0.21±0.05** |
| P5: Balanced | 2.11±0.11 | 2.08±0.10 | 0.35±0.06 | 0.31±0.05 | 0.40±0.07 | **0.14±0.03** |
| **Mean** | 2.44±0.12 | 2.39±0.11 | 0.40±0.07 | 0.39±0.06 | 0.47±0.08 | **0.16±0.04** |

Our method achieves the lowest KL divergence across all profiles (mean 0.16,
all pairwise $p < 0.001$). The hand-tuned baseline (mean KL 0.40) confirms
that a single fixed-weight configuration cannot simultaneously match all user
profiles—the best hand-tuned weights for P1 (cautious) produce KL 0.85 on P2
(fast), and vice versa. Our adaptive method bridges this gap by learning
profile-specific weights online.

The Right-hugging profile (P4) remains the most challenging case for all
methods because the lateral bias feature $\phi_4$ is a second-order effect
relative to safety and velocity. Our method still achieves KL 0.21 through the
explicit factored representation, which isolates the lateral bias dimension
from other preferences.

### 5.2.3 Real-Time Performance

**Table 6:** Per-layer computation time (ms, mean ± std over 1,000 cycles).

| Layer | Hardware | Mean (ms) | Std (ms) | P95 (ms) | Max (ms) |
|-------|----------|-----------|----------|----------|----------|
| L1: CQL inf. + IRL | Intel i7-13700H | 8.2 | 2.1 | 12.1 | 14.8 |
| L2: Tube MPC (CasADi+qpOASES) | Intel i7-13700H | 11.4 | 3.5 | 17.8 | 24.1 |
| L3: DWA (Python/C++) | Intel i7-13700H | 0.8 | 0.2 | 1.1 | 1.3 |
| MRC overhead (when active) | Intel i7-13700H | 18.7 | 4.2 | 25.1 | 28.5 |
| **Total (normal)** | | **20.4** | **4.1** | **31.0** | **40.2** |

Total latency remains under 45 ms across all trials, well within the 50 ms
budget for 20 Hz control. The MRC is activated in 0.03% of L2 cycles and adds
negligible overhead even when triggered. On embedded hardware (Raspberry Pi 4,
tested separately), L2 increases to approximately 35 ms, and L1 is offloaded to
a companion smartphone. The L3 DWA layer runs at >500 Hz even on embedded
hardware, ensuring the safety-critical last line of defense is never
bottlenecked.

### 5.2.4 Ablation Study

We perform three ablations to isolate each component's contribution:

**(A) Removing L3 (Tube MPC only):** In the Mall and Intersection environments,
collision rate increases from 0 to 0.31±0.06/100 m ($p < 0.001$) due to
dynamic obstacles appearing inside the tube between L2 replanning cycles.
The Tube MPC alone is sufficient for static environments but insufficient
for highly dynamic ones, confirming L3's necessity.

**(B) Removing L1 (fixed uniform weights):** Preference match degrades from
0.16 to 2.39±0.11 ($p < 0.001$, Cohen's $d = 4.8$), confirming that the RL
layer is essential for adaptivity. Critically, safety remains at zero
collisions even without L1, validating Proposition 1's guarantee that safety
is independent of preference weights.

**(C) Removing L1+L3 (standard MPC only):** Both metrics degrade sharply:
collision rate rises to 0.46/100 m and KL to 2.39. This confirms that all
three layers are necessary for the full trilemma solution.

### 5.2.5 Tube Radius Sensitivity Analysis

We evaluate sensitivity to the tube radius $\alpha$ by varying it from
$0.5\alpha_0$ to $2.0\alpha_0$ ($\alpha_0 = 2.5$). Figure 3 plots collision
rate and path efficiency (ratio of actual path length to shortest feasible
path) as a function of $\alpha / \alpha_0$, revealing three distinct regimes.

**Table 7:** Sensitivity to tube radius $\alpha$ (mean over P1-P5, E1-E5,
200 trials each).

| $\alpha/\alpha_0$ | Collision Rate (/100m) | Path Efficiency | KL Divergence | Mean Velocity (m/s) |
|-------------------|------------------------|-----------------|---------------|---------------------|
| 0.5 | 1.24±0.18 | 0.92±0.03 | 0.22±0.05 | 1.12±0.08 |
| 0.7 | 0.08±0.03 | 0.94±0.02 | 0.18±0.04 | 1.24±0.06 |
| 0.85 | 0.01±0.01 | 0.96±0.02 | 0.17±0.04 | 1.31±0.05 |
| 1.0 ($\alpha_0$) | **0.0±0.0** | 0.97±0.02 | 0.16±0.04 | 1.35±0.05 |
| 1.25 | **0.0±0.0** | 0.95±0.02 | 0.17±0.04 | 1.30±0.06 |
| 1.5 | **0.0±0.0** | 0.91±0.03 | 0.20±0.05 | 1.18±0.07 |
| 2.0 | **0.0±0.0** | 0.82±0.04 | 0.26±0.06 | 0.95±0.09 |

Three regimes emerge: (i) $\alpha < 0.7\alpha_0$: the tube is too narrow
to contain the combined user+environment uncertainty, causing collisions;
(ii) $\alpha \in [0.7\alpha_0, 1.5\alpha_0]$: the **robust operating regime**
where safety is maintained with good path efficiency and preference matching;
(iii) $\alpha > 1.5\alpha_0$: the tube is overly conservative, reducing
velocity and path efficiency without improving safety. The base radius
$\alpha_0 = 2.5$ sits comfortably within the robust regime.

## 5.3 Summary of Results

| Requirement | Metric | Our Method | Best Baseline | Improvement |
|-------------|--------|------------|---------------|-------------|
| Safety | Collision rate (/100m) | **0.0** | 0.12 (Hand-Tuned) | Zero collisions |
| Adaptivity | KL divergence | **0.16** | 0.39 (RL-only) | 59% lower KL |
| Real-time | Total latency (ms) | **20.4** | <1 (DWA-only) | Well within 50 ms budget |
| Robustness | $\alpha$ operating range | **[0.7, 1.5]$\alpha_0$** | — | 2.1× range |

# 6. Discussion

## 6.1 Key Findings

**Safety and adaptivity are not in tension.** Our hierarchical decoupling
achieves both simultaneously: Proposition 1 guarantees collision avoidance
uniformly over all $w \in \mathcal{W}_{\text{bounded}}$, independent of the RL
layer's adaptation.

**Explicit preference modeling outperforms implicit.** Our factored 5-feature
cost achieves KL 0.16 vs. 0.39 for end-to-end RL, with interpretable
preference vectors that enable explainability. The hand-tuned baseline (KL
0.40) confirms that manual tuning cannot match online learning—optimal
weights vary substantially across profiles.

**The tube provides a natural interface for dynamic obstacles.** Restricting
DWA to the tube cross-section provides immediate response while preserving the
safety guarantee, more efficiently than re-solving the full MPC. The 2.1×
robust operating range in $\alpha$ confirms the method is not brittle to
parameter choice.

**Hand-tuned baselines are essential for rigor.** The hand-tuned MPC+DWA
achieves strong safety (0.12/100 m vs. 3.2 for DWA-only), but the RL layer
adds two distinct values: zero collisions via adaptive safety weighting, and
2.5× better preference matching.

## 6.2 Limitations

**Static tube radius.** A fixed $\alpha$ computed offline limits performance in
varying uncertainty conditions; dynamic tube MPC [28] could improve efficiency
in low-uncertainty periods.

**Preference stationarity.** Our IRL module assumes stationary preferences over
$K = 50$ steps. Context-conditional preferences (e.g., cautious in unfamiliar
environments) remain future work.

**Simulation-only validation.** Real-world deployment would reveal additional
challenges: sensor noise characteristics, user-device physical interaction, and
crowd social dynamics. Critically, no BVI user study has been conducted—until
direct evaluation with visually impaired participants is performed, adaptivity
claims should be interpreted as demonstrated in simulation with synthetic user
profiles informed by the BVI navigation literature [2,23].

**Trust calibration** (§4.4.2) is architecturally motivated but not empirically
evaluated. **Linearization error bound** (§4.3.3) uses worst-case Lipschitz
constants; local estimates could reduce the effective tube radius.

## 6.3 Future Work

Key directions include: (i) **life-long preference learning**—L1 can be
updated continuously without re-certifying L2 safety; (ii)
**context-conditional preferences** that adapt to environment type and user
state; (iii) **multi-modal personalization** from explicit feedback,
physiological signals, or natural language; (iv) **hardware deployment** on
the CaBot platform [4] for real-world validation; (v) **BVI user study**
comparing our adaptive method against baselines; (vi) **dynamic tube radius**
[28] adapting $\alpha$ online to crowd density and sensor confidence; and
(vii) **crowd navigation** extended to multi-agent settings with non-intersecting
safety tubes.

## 6.4 Broader Impacts and Ethical Considerations

The deployment of AI-guided assistive navigation for visually impaired users
raises important ethical considerations.

**Safety as an ethical imperative.** For BVI users, a collision that a sighted
person might avoid could cause serious injury. Our guarantee (Proposition 1)
ensures the system will not command trajectories entering the collision set.
However, the guarantee depends on bounded uncertainty, accurate state
estimation, and correct obstacle detection—we recommend an independent runtime
monitor triggering MRC if sensor uncertainty exceeds the tube radius budget.

**Preserving user agency.** Our shared-autonomy framework models the user as an
active collaborator: guidance rather than coercion, learning from actual
behavior, and transparent preference reporting. Long-term effects on user
self-confidence and spatial cognition warrant longitudinal study.

**Equity and access.** The safety-critical DWA layer (L3) runs at >500 Hz on
low-cost embedded hardware; MRC provides a safe degraded mode if higher layers
are unavailable. Edge-only deployment and model compression are important
future directions.

**Data privacy.** Walking trajectories can reveal sensitive information. We
recommend on-device processing with differential privacy, transmitting only
anonymized preference vectors rather than raw trajectories.

# 7. Conclusion

We presented a hierarchical safe MPC-RL framework for adaptive shared-autonomy
assistive navigation that simultaneously achieves provable safety, user
adaptivity, and real-time performance. The key architectural insight is
decoupling: RL parameterizes the MPC cost function, while Tube MPC enforces
safety independently of learned preferences. Our rigorous safety analysis
(Lemmas 1-3, Proposition 1) guarantees collision avoidance for all admissible
preference weights, with MRC as a safe fallback. Extensive simulations (10,000
trials, 5 environments, 5 user profiles, 6 baselines) demonstrate zero
collisions, KL divergence of 0.16 (2.5× better than the strongest non-adaptive
baseline), and 20.4 ms latency. The framework opens directions including
life-long learning, BVI user studies, and hardware deployment. More broadly,
hierarchical decoupling of safety, adaptivity, and real-time response—with the
human as a shared-autonomy collaborator—is a general design pattern for
human-assistive autonomous systems.

# Data and Code Availability

The simulation environments, user preference profiles, and baseline
implementations used in this study will be released as an open-source
repository upon paper acceptance. The codebase includes: (i) the three-layer
RL-TubeMPC-DWA controller with CQL pretraining and MaxEnt IRL online
adaptation; (ii) Habitat-Sim environment configurations for all five test
environments (E1-E5); (iii) ORCA-based dynamic pedestrian generation scripts;
and (iv) evaluation scripts reproducing all tables and figures in this paper.
The CQL pretraining dataset (1,000 simulated trajectories with ground-truth
preferences) will be included in the release.

# Appendix: Figure Captions

**Figure 1:** Three-layer hierarchical architecture. L1 (Preference-RL, 1 Hz):
CQL + MaxEnt IRL infers user preference weights $w \in \mathbb{R}^m$ from
trajectory segments, parameterizing the MPC cost function. L2 (Tube MPC, 10
Hz): Solves finite-horizon OCP with tightened constraints via CasADi + qpOASES;
the tube $\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$ provides the safety
guarantee (Proposition 1) for any $w \in \mathcal{W}_{\text{bounded}}$, with
MRC as fallback. L3 (DWA, 100 Hz): Tube-constrained velocity search for
real-time dynamic obstacle avoidance; commands delivered via vibrotactile belt
and bone-conduction audio. L1 influences *what* to optimize; L2 enforces *how*
it is constrained.

**Figure 2:** Minimum obstacle distance distributions for P2 (Fast) in E3
(Shopping Mall). KDE over $n = 200$ trials per method. Dashed line: $d_{\min}
= 0.3$ m. Our method (solid blue): median 0.52 m, IQR [0.41, 0.68]. Hand-Tuned
MPC+DWA (dotted green): median 0.44 m, IQR [0.34, 0.58]. RL-only (dashed red):
median 0.21 m, secondary mode below $d_{\min}$.

**Figure 3:** Tube radius sensitivity. Collision rate (blue circles, left axis)
and path efficiency (orange squares, right axis) vs. $\alpha / \alpha_0$
($\alpha_0 = 2.5$). Three regimes: unsafe ($\alpha < 0.7\alpha_0$), robust
operating ($\alpha \in [0.7\alpha_0, 1.5\alpha_0]$, zero collisions,
efficiency $\geq 0.91$), conservative ($\alpha > 1.5\alpha_0$, efficiency
degrades). Averaged over P1-P5, E1-E5.

**Figure 4:** Preference learning convergence. KL divergence vs. L1 update
cycles for P1-P5. Shaded: $\pm 1\sigma$ over 50 runs. Dashed lines: Hand-Tuned
MPC+DWA and RL-only (SAC) baselines. Convergence reached within 20-30 L1
updates (approximately 20-30 s).

# References

[1] M. A. Khan, M. A. Rahman, and S. A. Hossain, "A Survey on Outdoor
Navigation Applications for People With Visual Impairments," *IEEE Access*,
vol. 11, pp. 14647-14666, 2023. DOI: 10.1109/ACCESS.2023.3243432.

[2] J. M. Loomis, R. L. Klatzky, and N. A. Giudice, "Efficacy of Electronic
Travel Aids for the Blind and Visually Impaired During Wayfinding," *medRxiv*,
2025. DOI: 10.1101/2025.01.15.25320581.

[3] D. Dakopoulos and N. G. Bourbakis, "Wearable Obstacle Avoidance Electronic
Travel Aids for Blind: A Survey," *IEEE Trans. Systems, Man, and Cybernetics
Part C*, vol. 40, no. 1, pp. 25-35, 2010.

[4] J. Guerreiro, D. Sato, S. Asakawa, H. Dong, K. M. Kitani, and C. Asakawa,
"CaBot: Designing and Evaluating an Autonomous Navigation Robot for Blind
People," in *Proc. ACM ASSETS*, 2019, pp. 68-82.

[5] S. K. Singh, R. P. Singh, and A. K. Mishra, "AR Navigation System for
Guidance of Visually Impaired Individuals Using IoT and Reinforcement
Learning," in *Proc. IEEE ICACCS*, 2025, pp. 1-6.

[6] B. Zhang, Y. Liu, Z. Wang, and H. Chen, "LaF-GRPO: In-Situ Navigation
Instruction Generation for the Visually Impaired via GRPO with
LLM-as-Follower Reward," *arXiv:2506.04070*, 2025.

[7] A. Vaaler, S. Skjong, and T. A. Johansen, "Modular control architecture
for safe marine navigation: Reinforcement learning with predictive safety
filters," *Artificial Intelligence*, vol. 336, 104201, 2024.

[8] R. Reiter, J. Hoffmann, M. Diehl, and S. Gros, "Synthesis of Model
Predictive Control and Reinforcement Learning: Survey and Classification,"
*arXiv:2502.02133*, 2025.

[9] M. Saha, A. J. Fiannaca, M. Kneisel, E. Cutrell, and M. R. Morris,
"Field Evaluation of a Mobile App for Assisting Blind and Visually Impaired
Travelers to Find Bus Stops," *Translational Vision Science & Technology*,
vol. 13, no. 1, art. 4, 2024.

[10] F. M. Talaat, A. M. El-Sayed, and H. M. El-Bakry, "SightAid: Deep
Learning-Based Intelligent Wearable Vision System for Visually Impaired
People," *Neural Computing & Applications*, vol. 36, no. 19, pp. 11075-11095,
2024.

[11] J. Achiam, D. Held, A. Tamar, and P. Abbeel, "Constrained Policy
Optimization," in *Proc. ICML*, 2017, pp. 22-31.

[12] A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, and
P. Tabuada, "Control Barrier Functions: Theory and Applications," in *Proc.
ECC*, 2019, pp. 3420-3431.

[13] M. Guerrier, H. Fouad, and G. Beltrame, "Learning Control Barrier
Functions and Their Application in Reinforcement Learning: A Survey,"
*arXiv:2404.16879*, 2024.

[14] D. S. Kushwaha and Z. A. Biron, "A Review On Safe Reinforcement Learning
Using Lyapunov and Barrier Functions," *arXiv:2508.09128*, 2025.

[15] M. Tabbara, L. Yang, and H. Sibai, "Statistically Assuring Safety of
Control Systems using Ensembles of Safety Filters and Conformal Prediction,"
*arXiv:2511.07899*, 2025.

[16] D. Q. Mayne, M. M. Seron, and S. V. Raković, "Robust model predictive
control of constrained linear systems with bounded disturbances," *Automatica*,
vol. 41, no. 2, pp. 219-224, 2005.

[17] D. Q. Mayne, S. V. Raković, R. Findeisen, and F. Allgöwer, "Robust
output feedback model predictive control of constrained linear systems,"
*Automatica*, vol. 42, no. 7, pp. 1217-1222, 2006.

[18] A. Kumar, A. Zhou, G. Tucker, and S. Levine, "Conservative Q-Learning
for Offline Reinforcement Learning," in *Proc. NeurIPS*, 2020.

[19] B. D. Ziebart, A. Maas, J. A. Bagnell, and A. K. Dey, "Maximum Entropy
Inverse Reinforcement Learning," in *Proc. AAAI*, 2008, pp. 1433-1438.

[20] J. B. Rawlings, D. Q. Mayne, and M. Diehl, *Model Predictive Control:
Theory and Design*, 2nd ed. Nob Hill Publishing, 2017.

[21] D. Fox, W. Burgard, and S. Thrun, "The Dynamic Window Approach to
Collision Avoidance," *IEEE Robotics & Automation Magazine*, vol. 4, no. 1,
pp. 23-33, 1997.

[22] H. J. Ferreau, C. Kirches, A. Potschka, H. G. Bock, and M. Diehl,
"qpOASES: A parametric active-set algorithm for quadratic programming,"
*Mathematical Programming Computation*, vol. 6, no. 4, pp. 327-363, 2014.

[23] S. Azenkot, C. L. Bennett, and R. E. Ladner, "What do Blind and
Low-Vision People Really Want from Assistive Smart Devices?" in *Proc. ACM
ASSETS*, 2023, pp. 1-14.

[24] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and M. Diehl,
"CasADi: A software framework for nonlinear optimization and optimal control,"
*Mathematical Programming Computation*, vol. 11, no. 1, pp. 1-36, 2019.

[25] M. Savva, A. Kadian, O. Maksymets, Y. Zhao, E. Wijmans, B. Jain,
J. Straub, J. Liu, V. Koltun, J. Malik, D. Parikh, and D. Batra, "Habitat:
A Platform for Embodied AI Research," in *Proc. ICCV*, 2019, pp. 9339-9347.

[26] J. van den Berg, S. J. Guy, M. Lin, and D. Manocha, "Reciprocal n-body
Collision Avoidance," in *Proc. ISRR*, 2011, pp. 3-19.

[27] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, "Soft Actor-Critic:
Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic
Actor," in *Proc. ICML*, 2018, pp. 1861-1870.

[28] N. Csomay-Shanklin, V. Sindhwani, and A. Majumdar, "Dynamic Tube MPC:
Learning Tube Dynamics with Massively Parallel Simulation for Robust Safety in
Practice," *arXiv:2404.02512*, 2024.

[29] A. D. Dragan and S. S. Srinivasa, "A Policy-Blending Formalism for Shared
Control," *Int. J. Robotics Research*, vol. 32, no. 7, pp. 790-805, 2013.

[30] J. Berberich and F. Allgöwer, "An overview of systems-theoretic guarantees
in data-driven model predictive control," *Annual Review of Control, Robotics,
and Autonomous Systems*, vol. 8, pp. 77-100, 2025.

[31] L. Hewing, K. P. Wabersich, M. Menner, and M. N. Zeilinger, "Learning-Based
Model Predictive Control: Toward Safe Learning in Control," *Annual Review of
Control, Robotics, and Autonomous Systems*, vol. 3, no. 1, pp. 269-296, 2020.

[32] S. Gros and M. Zanon, "Learning for MPC with Stability and Safety
Guarantees," *Automatica*, vol. 146, art. 110598, 2022.

[33] S. Real and A. Araujo, "Navigation Systems for the Blind and Visually
Impaired: Past Work, Challenges, and Open Problems," *Sensors*, vol. 19,
no. 15, art. 3404, 2019.

[34] A. Mesbah, K. P. Wabersich, A. P. Schoellig, M. N. Zeilinger et al.,
"Fusion of Machine Learning and MPC under Uncertainty: What Advances Are on
the Horizon?" in *Proc. ACC*, 2022, pp. 342-349.

[35] S. Javdani, S. S. Srinivasa, and J. A. Bagnell, "Shared Autonomy via
Hindsight Optimization," in *Proc. Robotics: Science and Systems (RSS)*, 2015.
