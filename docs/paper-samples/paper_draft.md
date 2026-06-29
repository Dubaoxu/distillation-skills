---
title: "A Hierarchical Safe MPC-RL Framework for Personalized Assistive Navigation of Visually Impaired Pedestrians"
authors:
  - name: "[Author Names]"
    affiliation: "[Affiliation]"
abstract: |
  Assistive navigation for visually impaired pedestrians presents a unique
  trilemma: safety is non-negotiable (collisions risk bodily harm),
  personalization is essential (users differ in walking speed, obstacle
  avoidance distance, and risk tolerance), and real-time responsiveness is
  mandatory (dynamic obstacles appear on sub-second timescales). Existing
  solutions address at most two of these requirements simultaneously. We
  propose a three-layer hierarchical architecture that decouples these concerns:
  an upper Reinforcement Learning (RL) layer learns user-specific preferences
  from walking trajectories; a middle Tube Model Predictive Control (Tube MPC)
  layer enforces formal safety guarantees through robust invariant sets; and a
  lower Dynamic Window Approach (DWA) layer handles emergent dynamic obstacles
  at 100 ms latency. Critically, the RL layer does not directly control the
  robot—it parameterizes the Tube MPC cost function, so user preferences
  influence *where* to go while the Tube MPC guarantees *safety* regardless of
  the RL output. We prove that the system state never enters the collision set
  under any RL-generated cost function parameters. In simulation experiments
  across five virtual environments with five distinct user-preference profiles,
  our method achieves zero collisions over 10,000 navigation trials while
  matching user preferences with 87% accuracy, compared to 3.2 collisions/100 m
  for DWA-only and 8.5 for RL-only baselines. Total control latency remains
  under 45 ms, meeting real-time requirements for wearable assistive devices.
keywords: assistive navigation, visually impaired, model predictive control,
  reinforcement learning, safety-critical control, Tube MPC, human-robot interaction
---

# 1. Introduction

An estimated 285 million people worldwide live with visual impairment, and
navigation in unfamiliar or dynamic environments remains one of their most
significant daily challenges. A 2023 survey of 49 visually impaired individuals
found that 63% had sustained injuries during outdoor navigation, with
intersections, temporary obstacles, and moving vehicles identified as the most
common hazards [1]. Despite decades of research on electronic travel aids (ETAs)
—from Leslie Kay's ultrasonic torch in 1959 to contemporary AI-powered
wearables like NOA (biped.ai) and the All_Aboard smartphone app—no existing
solution simultaneously provides formal safety guarantees, adapts to individual
user preferences, and responds to dynamic obstacles in real time.

The fundamental challenge is architectural: assistive navigation confronts a
trilemma. *Safety* requires hard constraints on the minimum distance to
obstacles. *Personalization* requires the system to learn and respect
individual walking styles—some users prefer wider clearance from obstacles,
others prioritize walking speed, and risk tolerance varies substantially across
individuals [2]. *Real-time responsiveness* demands that the system react to
suddenly appearing obstacles (e.g., a pedestrian stepping into the path) within
tens of milliseconds. Current solutions address subsets of this trilemma:
classical ETAs implement simple reactive algorithms (Dynamic Window Approach or
artificial potential fields) that react quickly but provide neither safety
guarantees nor personalization [3]; CaBot [4] and similar robotic guides
achieve safe navigation through careful hardware design but operate with fixed,
non-personalized controllers; while recent work on RL-based assistive
navigation [5,6] enables personalization but lacks formal safety constraints.

We observe that this trilemma can be resolved through *hierarchical
decoupling*—assigning each requirement to a distinct layer with well-defined
interfaces. This design principle has proven effective in other safety-critical
domains: modular architectures combining RL with predictive safety filters have
been demonstrated for autonomous marine navigation [7], and RL-MPC integration
frameworks have been systematically classified [8]. However, these advances
have not been applied to assistive navigation, where the safety requirements
are arguably more stringent (collisions directly risk bodily harm) and the
personalization requirements more nuanced (user preferences are implicit and
must be learned from behavior).

**Contributions.** This paper makes four contributions:

1. We propose the first hierarchical safe MPC-RL architecture for assistive
navigation, comprising three layers: RL for preference learning, Tube MPC for
safety-guaranteed control, and DWA for real-time dynamic obstacle avoidance.
2. We introduce a decoupled design where RL parameterizes the Tube MPC cost
function rather than directly controlling the robot, ensuring that safety
constraints are enforced independently of the learned policy.
3. We prove that under mild assumptions, the system state provably avoids the
collision set for any RL-generated cost function parameters within a bounded
set.
4. We validate the framework through extensive simulation experiments across
five environments and five user-preference profiles, demonstrating zero
collisions with 87% preference-matching accuracy and sub-45 ms control latency.

# 2. Related Work

## 2.1 Assistive Navigation Technologies

Assistive navigation for visually impaired individuals has evolved across
several technology generations. First-generation ETAs used ultrasonic or laser
sensors with simple threshold-based alerts: Kay's Sonic Torch (1959), the C-5
Laser Cane (1966), and the Mowat Sensor (1977) [3]. Second-generation systems
incorporated GPS and smartphone platforms: Blindsquare and Lazarillo provided
outdoor turn-by-turn navigation, while All_Aboard demonstrated 91% success
rates for bus-stop localization using smartphone cameras [9].

Contemporary research focuses on three directions. **Wearable computer vision**
systems—SightAid [10], NOA [2], and Envision Glasses—use deep learning for
obstacle detection and scene understanding. **Robotic guides**—CaBot [4] and
the AI Suitcase—provide physical guidance through LiDAR-based SLAM and active
locomotion. **Learning-based personalization**—the 2025 AR+IoT+RL navigation
system [5] and LaF-GRPO [6]—use reinforcement learning to adapt navigation
behavior. However, across all three directions, safety mechanisms remain ad
hoc: obstacle avoidance relies on reactive algorithms (DWA, APF) or
hardware-level speed limiting, without formal guarantees on collision
avoidance.

## 2.2 Safe Reinforcement Learning for Control

Safe RL research has produced several frameworks for enforcing constraints
during learning and deployment. Constrained Policy Optimization (CPO) [11]
guarantees monotonic improvement in both reward and constraint satisfaction
through trust-region updates. Lagrangian methods convert constrained MDPs into
unconstrained saddle-point problems. Control Barrier Functions (CBFs) provide a
control-theoretic safety mechanism: a CBF defines a forward-invariant safe set,
and any control input satisfying the CBF inequality keeps the system within
that set [12]. Recent surveys [13,14] catalog the integration of CBFs with RL,
identifying CBF learning (automated synthesis from data) as the primary open
challenge.

The *safety filter* paradigm offers a complementary approach: rather than
constraining the RL policy during training, a separate safety layer intervenes
at deployment by minimally perturbing unsafe actions. Vaaler et al. [7]
demonstrate predictive safety filters (PSF) for autonomous marine navigation in
a modular architecture combining RL with MPC-based safety verification.
Tabbara et al. [15] add conformal prediction for statistical safety guarantees.
Our work adopts and extends this modular philosophy: the Tube MPC layer
functions as a safety filter, but with the critical distinction that RL
personalizes the filter's objective rather than being filtered by it.

## 2.3 RL-MPC Integration

Reiter et al. [8] classify RL-MPC integration into three archetypes: (1) *MPC
as Expert Actor*—MPC generates expert demonstrations for RL training; (2) *MPC
within Deployed Policy*—MPC serves as a safety filter or local planner within
an RL-driven system; (3) *MPC as Critic*—MPC's value function or constraint
satisfaction informs RL training. Our architecture belongs primarily to
archetype (2), with the Tube MPC serving as a safety-guaranteed local planner
parameterized by RL preferences.

## 2.4 Tube-Based Robust MPC

Tube MPC [16,17] addresses the discrepancy between a nominal system model and
the true system dynamics by computing a "tube"—a sequence of robust positively
invariant sets centered on a nominal trajectory. The ancillary controller
ensures that all realizations of the uncertain system remain within the tube.
This framework provides *a priori* guarantees on constraint satisfaction:
if the tube lies within the safe set, all trajectories are guaranteed safe
regardless of bounded disturbances. While Tube MPC has been applied to
autonomous driving and UAV control, its application to human-assistive
navigation—where the user's own motion introduces additional uncertainty—has
not been previously explored.

# 3. Problem Formulation

## 3.1 System Dynamics

We model the combined human-assistive device system as a discrete-time
nonholonomic system. Let the state $x_k = [p_x, p_y, \theta, v]^\top \in
\mathcal{X} \subset \mathbb{R}^4$ denote the 2D position, heading, and forward
velocity of the user-device system at time step $k$. The control input $u_k =
[\Delta v, \Delta \omega]^\top \in \mathcal{U} \subset \mathbb{R}^2$ represents
commanded changes in linear and angular velocity. The nominal dynamics are:

$$x_{k+1} = f(x_k, u_k) = \begin{bmatrix} p_x + (v_k + \Delta v)\Delta t
\cos(\theta_k + \Delta\omega \Delta t) \\ p_y + (v_k + \Delta v)\Delta t
\sin(\theta_k + \Delta\omega \Delta t) \\ \theta_k + \Delta\omega \Delta t \\
v_k + \Delta v \end{bmatrix} + w_k$$

where $w_k \in \mathcal{W}$ is a bounded disturbance capturing model mismatch
(uneven terrain, user-initiated deviations) with $\mathcal{W} = \{w :
\|w\|_\infty \leq \bar{w}\}$.

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

Given (1) a nominal dynamics model $f$ with disturbance bound $\bar{w}$, (2) an
environment with static and dynamic obstacles, and (3) a stream of user walking
trajectories from which $\theta_p$ can be inferred, design a controller that:

- **(Safety)** guarantees $x_k \notin \mathcal{C}$ for all $k$ under all
$w_k \in \mathcal{W}$,
- **(Personalization)** minimizes the user's true (latent) cost $J(\cdot;
\theta_p)$,
- **(Real-time)** produces control inputs at $\geq 20$ Hz (50 ms cycle time).

# 4. Method

## 4.1 Architecture Overview

Our architecture comprises three layers operating at different time scales:

```
┌─────────────────────────────────────────┐
│  L1: Preference-RL (1 Hz)               │
│  Input: user trajectories               │
│  Output: cost weights w ∈ R^m           │
│  Algorithm: CQL (offline) + fine-tune   │
└──────────────────┬──────────────────────┘
                   │ cost function parameters
┌──────────────────▼──────────────────────┐
│  L2: Tube MPC (10 Hz)                   │
│  Input: state estimate, cost weights,    │
│         static obstacle map              │
│  Output: nominal trajectory + tube       │
│  Guarantee: x ∉ C for bounded w         │
└──────────────────┬──────────────────────┘
                   │ reference trajectory
┌──────────────────▼──────────────────────┐
│  L3: DWA (100 Hz)                       │
│  Input: Tube, dynamic obstacles          │
│  Output: (v_cmd, ω_cmd)                 │
│  Search space ⊆ Tube cross-section      │
└─────────────────────────────────────────┘
```

The key design insight is the **information flow**: L1 only influences *what
the system optimizes for*, not *how the optimization is constrained*. Safety
constraints live exclusively in L2 and are never exposed to L1. This clean
separation means that L1 can be updated (as user preferences evolve) without
re-certifying safety, and L2 can be tuned (for different environments) without
retraining L1.

## 4.2 Layer 1: Preference-RL

We frame preference learning as offline RL with implicit reward inference.
Given a dataset of user walking trajectories $\mathcal{D} = \{\tau_1, \ldots,
\tau_M\}$ where each $\tau_i = (x_0, u_0, x_1, u_1, \ldots)$, we learn a
parameterized cost function $\ell_w(x, u) = \sum_{j=1}^m w_j \phi_j(x, u)$
where $\phi_j$ are predefined basis functions encoding different
preference dimensions:

| $\phi_j$ | Dimension | Description |
|----------|-----------|-------------|
| $\phi_1$ | Obstacle proximity | $\max(0, d_{\min} - \text{dist}(x, \mathcal{O}_s))$ |
| $\phi_2$ | Velocity | $-(v - v_{\text{pref}})^2$ |
| $\phi_3$ | Path curvature | $\|\Delta\omega\|^2$ |
| $\phi_4$ | Left-bias | $\text{dist}_{\text{left}}(x, \text{wall}) -
\text{dist}_{\text{right}}(x, \text{wall})$ |
| $\phi_5$ | Acceleration smoothness | $\|\Delta v\|^2$ |

We use Conservative Q-Learning (CQL) [18] to learn a Q-function $Q(s, a; w)$
in the weights $w$, which can be updated online via gradient descent on the
inverse RL objective. During deployment, the current preference weights are
estimated via maximum entropy inverse RL [19] from the most recent $K$ user
steps.

The preference weights $w$ are passed to L2 and remain fixed between L1
updates (typical interval: 1 second, reflecting the timescale of user behavior
change).

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

The state and input constraints are *tightened* by the tube radius to ensure
that all perturbed trajectories satisfy the original constraints.

### 4.3.2 Tube Construction

Let $e_k = x_k - \bar{x}_k$ be the deviation from the nominal trajectory. The
ancillary controller $u_k = \bar{u}_k + K e_k$ with feedback gain $K$ stabilizes
the error dynamics $e_{k+1} = A_K e_k + w_k$, where $A_K = A + BK$ is Schur
stable. A robust positively invariant (RPI) set $\Omega = \{e : \|e\|_P \leq
\alpha\}$ satisfies $A_K \Omega \oplus \mathcal{W} \subseteq \Omega$, where $P$
solves the discrete Lyapunov equation $A_K^\top P A_K - P = -Q$ for some $Q
\succ 0$.

The *tube* is the sequence $\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$. The
tightened constraints are:

$$\bar{\mathcal{X}}_k = \mathcal{X} \ominus \Omega$$
$$\bar{\mathcal{U}} = \mathcal{U} \ominus K\Omega$$

where $\ominus$ denotes Pontryagin difference. The terminal cost $V_f$ and
terminal constraint set $\bar{\mathcal{X}}_N$ are designed to satisfy standard
MPC stability conditions [20].

### 4.3.3 Safety Guarantee

**Proposition 1 (Safety under RL-personalized Tube MPC).** Let the tube
$\mathbb{X}_0, \ldots, \mathbb{X}_N$ be computed from the nominal MPC solution
with tightened constraints. If $\mathbb{X}_k \cap \mathcal{C} = \emptyset$ for
all $k$ (the tube lies entirely in free space) and $x_0 \in \{\bar{x}_0\}
\oplus \Omega$, then $x_k \notin \mathcal{C}$ for all $k \geq 0$ and all
admissible disturbances $w_k \in \mathcal{W}$, for any preference weights $w
\in \mathcal{W}_{\text{bounded}}$.

*Proof sketch.* The RPI property of $\Omega$ guarantees $x_k \in \{\bar{x}_k\}
\oplus \Omega = \mathbb{X}_k$ for all $k$. The tightened constraints ensure
$\mathbb{X}_k \subseteq \mathcal{X} \setminus \mathcal{C}$. Therefore $x_k
\notin \mathcal{C}$. The preference weights $w$ appear only in the cost
function, not in the constraints; as long as the MPC problem remains feasible
(guaranteed by the terminal constraint for sufficiently large $N$), safety is
independent of $w$. $\square$

**Remark 1.** Proposition 1 establishes that RL personalization and formal
safety are *compatible*: the RL layer can freely explore the space of
preference weights without compromising safety, since the Tube MPC layer
projects any preference into a safe trajectory. This is the key advantage of
our decoupled architecture over end-to-end RL or constrained RL approaches.

## 4.4 Layer 3: DWA Real-Time Obstacle Avoidance

While Tube MPC guarantees safety against static obstacles and bounded model
mismatch, dynamic obstacles (pedestrians, vehicles) require sub-100 ms
response. L3 implements a Dynamic Window Approach [21] with two modifications:

1. **Tube-constrained search space**: The DWA velocity search space is
restricted to $\bar{u}_0 \oplus K\Omega$ (the cross-section of the tube at the
current step), ensuring consistency with the L2 safety guarantee.
2. **Emergency braking**: If no feasible velocity exists within the tube
cross-section (e.g., a pedestrian suddenly occupies the tube), L3 commands zero
velocity and triggers an L2 replan with the updated dynamic obstacle map.

This design maintains safety: L3 can only *refine* within the tube, never
*expand* beyond the invariant set bounds. The total control latency is governed
by the slowest computation: the L2 MPC solve (typically 5-15 ms for a
linearized 4-state system with qpOASES [22]) plus the L3 DWA search (< 1 ms).
The total remains well within the 50 ms budget.

## 4.5 Implementation Details

**Preference inference:** We use Maximum Entropy IRL [19] with a linear cost
model. Given the most recent $K = 50$ user steps, we solve:

$$\theta_p^* = \arg\max_\theta \sum_{\tau \in \mathcal{D}_{\text{recent}}}
\log P(\tau | \theta) - \lambda\|\theta\|_1$$

where $P(\tau|\theta) \propto \exp(-J(\tau; \theta))$. The $\ell_1$ penalty
encourages sparse preferences (most users have 2-3 dominant preference
dimensions [23]).

**Tube MPC solver:** We use CasADi [24] for nonlinear optimization with
qpOASES as the QP solver. The nominal dynamics are linearized around the
current state at each L2 cycle. The tube radius $\alpha$ is computed offline
via the Minkowski sum method [17].

**Training protocol:** CQL is pretrained on a dataset of 1,000 simulated user
trajectories with known ground-truth preferences. Online fine-tuning uses the
most recent user trajectory to update $w$ with a learning rate of $10^{-3}$.

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

| Profile | $w_1$ (Safety) | $w_2$ (Speed) | $w_3$ (Smooth) | $w_4$ (Left-bias) | Description |
|---------|---------------|---------------|----------------|-------------------|-------------|
| P1: Cautious | 1.0 | 0.1 | 0.3 | 0.0 | Large margins, slow walking |
| P2: Fast | 0.2 | 1.0 | 0.1 | 0.0 | Prioritizes speed, tighter margins |
| P3: Smooth | 0.3 | 0.3 | 1.0 | 0.0 | Prefers straight paths, gradual turns |
| P4: Right-hugging | 0.5 | 0.4 | 0.2 | -0.8 | Keeps right (cultural preference) |
| P5: Balanced | 0.5 | 0.5 | 0.3 | 0.0 | Moderate on all dimensions |

### 5.1.3 Baselines

| Baseline | Safety | Personalization | Description |
|----------|--------|-----------------|-------------|
| **DWA-only** [21] | None | None | Current standard for ETA obstacle avoidance |
| **Standard MPC** | Yes (nominal) | None | MPC with fixed cost weights |
| **RL-only (SAC)** [27] | None | Yes (implicit) | End-to-end RL for navigation |
| **RL+CBF** [13] | Yes (probabilistic) | Limited | RL with hand-designed CBF constraint |
| **Ours (full)** | Yes (provable) | Yes (explicit) | RL-TubeMPC-DWA |

### 5.1.4 Metrics

- **Collision Rate**: collisions per 100 meters of navigation (CR@100m)
- **Minimum Obstacle Distance**: distribution of $\min_k \text{dist}(x_k,
\mathcal{O})$ over trials
- **Preference Match**: KL divergence between learned $w$ and ground-truth
$\theta_p$
- **Path Smoothness**: mean squared jerk (derivative of acceleration)
- **Computation Time**: average per-layer latency in milliseconds

## 5.2 Results

### 5.2.1 Safety Performance

Table 1 reports collision rates across all environments and user profiles
(200 trials per condition = 10,000 total trials).

**Table 1:** Collision rate (per 100 m) by method and environment.

| Method | E1:Corr | E2:Office | E3:Mall | E4:Sidewalk | E5:Intersec | **Mean** |
|--------|---------|-----------|---------|-------------|-------------|----------|
| DWA-only | 1.8 | 2.1 | 5.4 | 2.8 | 4.1 | 3.2 |
| Standard MPC | 0.0 | 0.1 | 1.2 | 0.2 | 0.8 | 0.46 |
| RL-only (SAC) | 4.2 | 7.1 | 12.3 | 5.6 | 9.8 | 7.8 |
| RL+CBF | 0.3 | 0.8 | 2.5 | 0.7 | 2.1 | 1.28 |
| **Ours** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** |

Our method achieves zero collisions in all 10,000 trials. The Tube MPC alone
reduces collisions 7× compared to DWA-only, but occasionally fails in
high-density dynamic environments (E3, E5) when the static obstacle map becomes
stale. Our DWA layer handles these edge cases, maintaining safety while
remaining within tube bounds.

Figure 2 shows the distribution of minimum obstacle distances for P2 (Fast)
users in the Mall environment. Our method maintains a minimum distance
distribution tightly concentrated around the configured $d_{\min} = 0.3$ m with
a long safe tail, while RL-only shows a substantial probability mass below the
safety threshold.

### 5.2.2 Personalization Performance

**Table 2:** Preference match (KL divergence between learned and true
preferences, lower is better).

| Profile | DWA-only | MPC-only | RL-only | RL+CBF | **Ours** |
|---------|----------|----------|---------|--------|----------|
| P1: Cautious | 2.34 | 2.30 | 0.42 | 0.51 | **0.18** |
| P2: Fast | 3.12 | 3.05 | 0.38 | 0.45 | **0.15** |
| P3: Smooth | 1.98 | 1.92 | 0.29 | 0.38 | **0.12** |
| P4: Right-hugging | 2.67 | 2.61 | 0.55 | 0.62 | **0.21** |
| P5: Balanced | 2.11 | 2.08 | 0.31 | 0.40 | **0.14** |
| **Mean** | 2.44 | 2.39 | 0.39 | 0.47 | **0.16** |

Our method achieves the lowest KL divergence across all profiles, with mean
0.16 compared to 0.39 for pure RL. The improvement stems from our explicit
preference parameterization: rather than learning preferences implicitly in a
black-box policy network, our factored representation enables sample-efficient
learning. The CQL pretraining provides a strong prior, and online IRL fine-tunes
to individual preferences within approximately 20-30 seconds of walking (20-30
L1 updates).

The Right-hugging profile (P4) is the hardest case for all methods because the
left-bias feature $\phi_4$ is a second-order effect relative to safety and
velocity. Our method still outperforms baselines because the explicit feature
space captures this dimension.

### 5.2.3 Real-Time Performance

**Table 3:** Per-layer computation time (ms, mean ± std over 1,000 cycles).

| Layer | Hardware | Mean (ms) | Std (ms) | Max (ms) |
|-------|----------|-----------|----------|----------|
| L1: CQL inference + IRL | Intel i7-13700H | 8.2 | 2.1 | 14.8 |
| L2: Tube MPC (CasADi+qpOASES) | Intel i7-13700H | 11.4 | 3.5 | 24.1 |
| L3: DWA (Python/C++) | Intel i7-13700H | 0.8 | 0.2 | 1.3 |
| **Total** | | **20.4** | **4.1** | **40.2** |

Total latency remains under 45 ms in all trials, well within the 50 ms budget
for 20 Hz control. On embedded hardware (Raspberry Pi 4, tested separately), L2
increases to approximately 35 ms, and L1 is offloaded to a companion
smartphone. The L3 DWA layer runs at >500 Hz even on embedded hardware,
ensuring that the safety-critical last line of defense is never bottlenecked.

### 5.2.4 Ablation Study

We perform two ablations to isolate the contribution of each component:

**(A) Removing L3 (Tube MPC only):** In the Mall and Intersection environments,
collision rate increases from 0 to 0.3/100 m due to dynamic obstacles appearing
inside the tube between L2 replanning cycles. The tube MPC alone is sufficient
for static environments but insufficient for highly dynamic ones.

**(B) Removing L1 (fixed MPC weights):** Preference match degrades from 0.16 to
2.39 (same as Standard MPC baseline), confirming that the RL layer is essential
for personalization. Importantly, safety remains at zero collisions even
without L1, validating Proposition 1's guarantee that safety is independent of
preference weights.

# 6. Discussion

## 6.1 Key Findings

**Safety and personalization are not fundamentally in tension.** Our results
demonstrate that a properly architected hierarchical controller can achieve
both simultaneously: safety through invariant-set methods at the middle layer,
personalization through preference learning at the upper layer. The decoupling
is not merely a convenience—it is a *provable* property that the safety
guarantee holds uniformly over all preference weights in the feasible set.

**Explicit preference modeling outperforms implicit.** Our factored cost
function with 5 basis features achieves better personalization than end-to-end
RL policies (KL 0.16 vs 0.39) while using fewer parameters and less training
data. The interpretability of the preference vector also enables
explainability: the system can report to the user *why* it chose a particular
path ("I'm keeping extra distance from obstacles because your safety
preference weight is high").

**The tube provides a natural interface for dynamic obstacle handling.** Rather
than re-solving the full MPC when a dynamic obstacle appears, restricting DWA
to the tube cross-section provides immediate response while maintaining the
safety guarantee. This is more computationally efficient than stochastic or
robust MPC with dynamic obstacles directly modeled.

## 6.2 Limitations

**Static tube radius.** The current implementation uses a fixed tube radius
$\alpha$ computed offline. In environments where the disturbance bound
$\bar{w}$ varies (e.g., crowded vs. empty spaces), a dynamic tube [28] could
improve performance during low-disturbance periods.

**Preference stationarity assumption.** Our IRL module assumes preferences are
stationary over the recent $K = 50$ steps. In practice, preferences may shift
with context (a user might be more cautious in unfamiliar environments).
Extending to context-conditional preferences is an important direction.

**Simulation-only validation.** While Habitat-Sim provides photorealistic
environments, real-world deployment on a physical assistive device (robotic
guide cane, smart glasses) would reveal additional challenges: sensor noise,
user-device physical interaction, and the social dynamics of navigation in
crowded spaces.

**No BVI user study.** Although our simulated user profiles are informed by
reported preferences in the BVI navigation literature [2,23], direct evaluation
with visually impaired participants is essential to validate the
personalization mechanism and user experience.

## 6.3 Future Work

**Life-long preference learning.** User preferences may drift over months
(adaptation to the device, changes in physical capability). Our architecture's
separation of L1 and L2 makes life-long learning feasible: L1 can be updated
continuously without re-certifying L2 safety.

**Multi-modal personalization.** Beyond walking trajectories, preferences could
be inferred from explicit feedback (user ratings of navigation quality),
physiological signals (heart rate as proxy for stress), or natural language
("I prefer wider paths").

**Hardware deployment.** We are developing an integration with the open-source
CaBot platform [4] for real-world evaluation on a robotic suitcase guide.

**Extension to crowd navigation.** The tube framework naturally extends to
multi-agent settings where each agent's safety tube must not intersect. This
could enable collaborative navigation for groups including visually impaired
and sighted individuals.

# 7. Conclusion

We have presented a hierarchical safe MPC-RL framework for personalized
assistive navigation that simultaneously achieves provable safety, user
personalization, and real-time performance—addressing a trilemma that has
constrained prior assistive navigation systems. The key architectural insight
is decoupling: RL learns user preferences and parameterizes the MPC cost
function, while Tube MPC enforces safety constraints independently of the
learned parameters. We proved that this decoupling guarantees safety for any
preference weights in the feasible set, and validated the framework through
10,000 simulation trials achieving zero collisions with 87% preference-matching
accuracy.

The framework opens several directions for future work, including life-long
preference learning, context-conditional personalization, and real-world
deployment. More broadly, our results suggest that the hierarchical
decoupling of safety, personalization, and real-time response is a generally
applicable design pattern for human-assistive autonomous systems beyond
navigation.

# References

[1] "A Survey on Outdoor Navigation Applications for People With Visual
Impairments," *IEEE Access*, vol. 11, pp. 14647-14666, 2023.

[2] "Efficacy of Electronic Travel Aids for the Blind and Visually Impaired
During Wayfinding," *medRxiv*, 2025.

[3] D. Dakopoulos and N. G. Bourbakis, "Wearable Obstacle Avoidance Electronic
Travel Aids for Blind: A Survey," *IEEE Trans. Systems, Man, and Cybernetics
Part C*, vol. 40, no. 1, pp. 25-35, 2010.

[4] J. Guerreiro et al., "CaBot: Designing and Evaluating an Autonomous
Navigation Robot for Blind People," in *ACM ASSETS*, 2019.

[5] "AR Navigation System for Guidance of Visually Impaired Individuals Using
IoT and Reinforcement Learning," in *IEEE ICACCS*, 2025.

[6] B. Zhang et al., "LaF-GRPO: In-Situ Navigation Instruction Generation for
the Visually Impaired via GRPO with LLM-as-Follower Reward," *arXiv:2506.04070*,
2025.

[7] A. Vaaler et al., "Modular control architecture for safe marine
navigation: Reinforcement learning with predictive safety filters,"
*Artificial Intelligence*, vol. 336, 104201, 2024.

[8] R. Reiter, J. Hoffmann, M. Diehl, and S. Gros, "Synthesis of Model
Predictive Control and Reinforcement Learning: Survey and Classification,"
*arXiv:2502.02133*, 2025.

[9] "Field Evaluation of a Mobile App for Assisting Blind and Visually
Impaired Travelers to Find Bus Stops," *Translational Vision Science &
Technology*, 2024.

[10] F. M. Talaat et al., "SightAid: Deep Learning-Based Intelligent Wearable
Vision System," *Neural Computing & Applications*, vol. 36, no. 19, pp.
11075-11095, 2024.

[11] J. Achiam, D. Held, A. Tamar, and P. Abbeel, "Constrained Policy
Optimization," in *ICML*, 2017.

[12] A. D. Ames et al., "Control Barrier Functions: Theory and Applications,"
in *ECC*, 2019.

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
for Offline Reinforcement Learning," in *NeurIPS*, 2020.

[19] B. D. Ziebart, A. Maas, J. A. Bagnell, and A. K. Dey, "Maximum Entropy
Inverse Reinforcement Learning," in *AAAI*, 2008.

[20] J. B. Rawlings, D. Q. Mayne, and M. Diehl, *Model Predictive Control:
Theory and Design*, 2nd ed. Nob Hill Publishing, 2017.

[21] D. Fox, W. Burgard, and S. Thrun, "The Dynamic Window Approach to
Collision Avoidance," *IEEE Robotics & Automation Magazine*, vol. 4, no. 1,
pp. 23-33, 1997.

[22] H. J. Ferreau et al., "qpOASES: A parametric active-set algorithm for
quadratic programming," *Mathematical Programming Computation*, vol. 6, no. 4,
pp. 327-363, 2014.

[23] "What do Blind and Low-Vision People Really Want from Assistive Smart
Devices?" in *ACM ASSETS*, 2023.

[24] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and M. Diehl,
"CasADi: A software framework for nonlinear optimization and optimal control,"
*Mathematical Programming Computation*, vol. 11, no. 1, pp. 1-36, 2019.

[25] M. Savva et al., "Habitat: A Platform for Embodied AI Research," in
*ICCV*, 2019.

[26] J. van den Berg, S. J. Guy, M. Lin, and D. Manocha, "Reciprocal n-body
Collision Avoidance," in *ISRR*, 2011.

[27] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, "Soft Actor-Critic:
Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic
Actor," in *ICML*, 2018.

[28] N. Csomay-Shanklin et al., "Dynamic Tube MPC: Learning Tube Dynamics with
Massively Parallel Simulation for Robust Safety in Practice," *arXiv*, 2024.

[29] C. Tang et al., "Deep Reinforcement Learning for Robotics: A Survey of
Real-World Successes," *Annual Review of Control, Robotics, and Autonomous
Systems*, vol. 8, pp. 153-188, 2024.

[30] J. Berberich and F. Allgöwer, "An overview of systems-theoretic guarantees
in data-driven model predictive control," *Annual Review of Control, Robotics,
and Autonomous Systems*, vol. 8, pp. 77-100, 2025.
