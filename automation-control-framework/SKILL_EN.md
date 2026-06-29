---
name: automation-control-framework
description: |
  Knowledge distillation framework for the automation and control domain. Built on deep research across 6 dimensions 
  (Navigation, Blind Guidance, Robust Control, Adaptive Control, RL Control, MPC), covering 300+ authoritative papers, 
  distilling 7 core methodological consensuses, 6 school divergences & convergence trends, and a 5-layer technology stack model.
  Purpose: Serves as a research navigator and knowledge index for the automation and control domain, 
  enabling quick access to core papers and methodologies.
---

# Automation & Control Domain · Knowledge Distillation Framework

> "The essence of control is not eliminating error, but managing uncertainty."
> — In the spirit of Karl J. Åström, not a direct quote

## Domain Panorama

The automation and control knowledge map covered by the six-dimensional research:

```
                    ┌─────────────────────────────┐
                    │   Reinforcement Learning (RL) │
                    │  PPO · SAC · Safe RL · MBRL  │
                    │      2025: RL+MPC Fusion     │
                    └──────────────┬──────────────┘
                                   │ Strategy Layer
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
  ┌─────┴──────┐          ┌────────┴────────┐         ┌──────┴──────┐
  │   Robust    │          │    Adaptive      │         │     MPC      │
  │   Control   │          │    Control       │         │              │
  │ H∞ · μ ·  │◄────────►│ MRAC · Backstep  │◄───────►│ Linear/NMPC  │
  │ SMC · LMI  │Complement│ ILC · L1 · ESC   │Complement│ Tube/Data-Drv│
  └─────┬──────┘          └────────┬────────┘         └──────┬──────┘
        │                          │                          │
        └──────────────────────────┼──────────────────────────┘
                                   │ Control Layer
                    ┌──────────────┴──────────────┐
                    │    Blind Visually Impaired   │
                    │        Assistance (BVI)      │
                    │  CV · Sensor Fusion · Wearable│
                    │  HCI Feedback · Indoor Loc.  │
                    └──────────────┬──────────────┘
                                   │ Application Layer
                    ┌──────────────┴──────────────┐
                    │     Autonomous Navigation    │
                    │ SLAM · Path Planning · Fusion│
                    │        · Learning            │
                    └─────────────────────────────┘
                                   │ Execution Layer
```

## I. Core Methodological Consensuses

> The underlying unified paradigm that cuts across all six domains — the "hard core" recognized by every school of thought

### Consensus 1: Feedback is the Soul of Control

**Cross-domain evidence**:
- **Robust Control**: Feedback compresses the impact of uncertainty on output (Small Gain Theorem)
- **Adaptive Control**: Online feedback adjusts controller parameters for self-tuning
- **MPC**: Receding horizon feedback corrects open-loop prediction errors
- **RL Control**: Value functions and policy gradients are both formalizations of feedback signals
- **Navigation**: SLAM loop closure is global feedback correcting accumulated drift

**Core claim**: Regardless of the mathematical tool used, the essence of control = observe → compare → correct → re-observe feedback loop

### Consensus 2: The Role of Models Ranges from "Optional" to "The More Precise the Better"

**Cross-domain evidence**:
- **Model-free RL** (SAC/PPO): Can control without any model, but sample efficiency is low
- **Model-based RL** (Dreamer/MBPO): World models significantly improve sample efficiency
- **MPC**: Explicit model-predictive optimization is the standard approach for optimal control
- **Adaptive Control**: Online modeling is critical (parameter estimation / system identification)
- **Robust Control**: Doesn't require a precise model, but does require bounds on uncertainty

**Core claim**: The model question is not "whether to use one," but "how much" and "at what granularity."

### Consensus 3: Constraint Handling is the First Gatekeeper for Real-World Deployment

**Cross-domain evidence**:
- **MPC**: Naturally handles input/state/output constraints (directly encoded in the optimization problem)
- **Safe RL**: CPO/CBF/Lagrangian methods — constraints as the formalization of safety
- **Robust Control**: H∞ transforms constraints into weighted mixed sensitivity
- **Navigation**: DWA's "dynamic window" is essentially optimization under velocity constraints
- **Blind Guidance**: User safety is the highest-priority constraint, non-negotiable

**Core claim**: Satisfying constraints is more important than optimizing performance — an optimal controller that violates constraints is equivalent to no controller at all

### Consensus 4: Uncertainty Quantification Defines the Reliability Boundary of a Controller

**Cross-domain evidence**:
- **Robust Control**: Structured/unstructured uncertainty explicitly modeled (Small Gain / μ-synthesis)
- **MPC**: Tube MPC / Stochastic MPC / Chance-Constrained MPC
- **RL Control**: Domain randomization / Distributionally robust optimization
- **Adaptive Control**: Parametric uncertainty → online parameter estimation

**Core claim**: Admitting "I don't know" is more reliable than pretending "I know everything"

### Consensus 5: Data-Driven and Model-Driven Are Converging, Not Opposing

**Cross-domain evidence**:
- **DeePC (2019)**: Purely data-driven MPC, based on Willems' behavioral theory
- **Koopman MPC (2025)**: Learn Koopman operators from data → lift dimension → linearize nonlinear systems
- **Offline RL + Control**: CQL/IQL learn safe policies from historical data
- **Data-Driven SMC (2024)**: Systematic literature review with 256 references
- **Sim-to-Real**: Core methodology for transferring simulation data to real systems

**Core claim**: Data tells you what happened in the past; models tell you why it happened — only by combining both can you predict the future

### Consensus 6: Real-Time Performance is a Non-Negotiable Hard Constraint

**Cross-domain evidence**:
- **Explicit MPC (Bemporad, 2002)**: Offline-ize online optimization → online = table lookup
- **RTI (Diehl, 2002)**: NMPC real-time iteration, trading optimality for speed
- **Event-Triggered Control**: Compute control only when necessary, saving communication/computation
- **SLAM**: PTAM (2007)'s parallel tracking + mapping architecture defined the real-time SLAM paradigm
- **SMC**: Sliding mode control is naturally suited for real-time execution (simple switching law)

**Core claim**: The best controller means nothing if it cannot execute in real time

### Consensus 7: Hierarchical Architecture is the Inevitable Choice for Large-Scale Systems

**Cross-domain evidence**:
- **MPC**: Upper-level planning + lower-level tracking (e.g., path planning → MPC tracking)
- **RL + Classical Control**: RL for high-level decisions, PID/MPC for low-level control
- **Navigation**: Global A*/RRT + local DWA/TEB
- **Distributed MPC**: Subsystem-independent MPC + coordination layer

**Core claim**: Divide and conquer — decompose complex problems into sub-problems at different time scales

---

## II. School Divergences & Evolution Paths

### Divergence 1: Model Precision vs. Robustness — The Ancient Dilemma

| Camp | Position | Representative Methods |
|------|----------|------------------------|
| **Model Precision Camp** | More precise models → better control; worth investing computation | NMPC, Gaussian Process MPC, Dreamer |
| **Robustness-First Camp** | Models always have errors; design controllers insensitive to error directly | H∞, SMC, Tube MPC |
| **Middle-Ground Camp (2020s mainstream)** | Learn a usable model + robust constraint handling | Learning-based MPC + Safety Filter |

### Divergence 2: Online Optimization vs. Offline Training

| Camp | Position | Representative Methods |
|------|----------|------------------------|
| **Online Optimization** | Re-solve the optimization problem each step; strong adaptability to changing scenarios | MPC, NMPC, Tube MPC |
| **Offline Training** | Pre-train policy/controller; online only requires forward inference | RL (PPO/SAC), Explicit MPC, ILC |
| **Convergence Trend (hottest in 2025)** | Offline-trained policy + online MPC safety supervision | Three RL+MPC fusion architectures |

### Divergence 3: Control Theory vs. Machine Learning — The Methodological Debate

| Classical Control | Machine Learning |
|-------------------|------------------|
| **Stability proof first** | Empirical performance first |
| **Mathematical guarantees** (Lyapunov/invariant sets/ISS) | **Statistical guarantees** (PAC/regret) |
| **Model = physical equations** | **Model = neural networks** |
| **Reps**: Robust/Adaptive/H∞/MPC stability theory | **Reps**: DRL/end-to-end learning/imitation learning |

**2025 Convergence Trends**:
- CBF + RL: Control theory provides safety certificates; RL enhances performance
- Koopman operator: Data-driven methods to map nonlinear systems to linear (provable)
- DeePC: Purely data-driven MPC from behavioral theory (mathematical guarantees + data-driven)

### Divergence 4: Implementation Paths for Adaptive Mechanisms

| Path | Approach | Advantages | Limitations |
|------|----------|------------|-------------|
| **Parametric Adaptation** | MRAC/STR/Backstepping | Theoretically complete, rich stability proofs | Requires parametric structural assumptions |
| **Function Approximation Adaptation** | Neural network adaptation / RKHS MRAC | No parametric assumptions needed | High computational cost, stability hard to prove |
| **Learning-based Adaptation** | RL + System ID | Flexible and general | Low sample efficiency |
| **L1 Adaptive Control** | Cao/Hovakimyan | Fast adaptation + guaranteed robustness | High gain may amplify noise |

### Divergence 5: The SLAM Paradigm Debate (From Filtering to Optimization)

| Paradigm | Representative | Era | Core Idea |
|----------|---------------|-----|-----------|
| **Filtering SLAM** | EKF-SLAM → FastSLAM | 1990s–2000s | Bayesian filtering / particle filtering |
| **Keyframe BA SLAM** | PTAM → ORB-SLAM | 2007–present | Sparse nonlinear optimization (Bundle Adjustment) |
| **Direct SLAM** | LSD-SLAM → DSO | 2014–present | Direct photometric error optimization |
| **Learning SLAM** | NeRF-SLAM/3DGS-SLAM | 2022–present | Neural implicit representations replacing traditional maps |

### Divergence 6: Technology Roadmap Divergence for Assistive Navigation

| Approach | Advantages | Limitations |
|----------|------------|-------------|
| **Pure CV (smartphone)** | Low cost, fast adoption | Sensitive to lighting/angle |
| **Dedicated Hardware (smart glasses/vests)** | High-quality sensors, designed for the blind | High cost (NOA ~$2000+) |
| **Infrastructure-dependent (BLE/UWB)** | High indoor accuracy | Requires pre-deployment |
| **Guide Robots** | Most comprehensive functionality | Large size, social acceptance yet to be validated |

---

## III. Five-Layer Technology Stack Model

```
┌──────────────────────────────────────────────────────┐
│ Layer 5: Decision & Planning Layer                    │
│ Path Planning (A*/RRT) · Task Planning · RL High-Level│
│ Policy                                                │
│ Reps: Global Navigation, MPC Receding Optimization, RL│
├──────────────────────────────────────────────────────┤
│ Layer 4: Constraint & Safety Layer                    │
│ CBF · CPO · Safety Filter · Robust Invariant Sets     │
│ Reps: Safe RL, Tube MPC, Blind Guidance Safety Verif. │
├──────────────────────────────────────────────────────┤
│ Layer 3: Control Synthesis Layer                      │
│ H∞ · SMC · MRAC · MPC · PPO/SAC                      │
│ Reps: Robust/Adaptive/Optimal/Learning Controllers    │
├──────────────────────────────────────────────────────┤
│ Layer 2: Perception & Estimation Layer                │
│ SLAM · Sensor Fusion (EKF/UKF/PF) · State Observers   │
│ Reps: Localization, Mapping, Object Detection, Depth  │
│ Estimation                                            │
├──────────────────────────────────────────────────────┤
│ Layer 1: Physical Modeling Layer                      │
│ Kinematics/Dynamics · Koopman Operator · System ID    │
│ Reps: Mathematical Models of Robots/Vehicles/Aircraft  │
└──────────────────────────────────────────────────────┘
```

**Inter-layer dependencies**:
- Layer 1 determines the state-space dimensionality and observability of Layer 2
- Layer 2 provides feedback signals (state estimate + uncertainty) for Layer 3
- Layer 3's outputs must pass through Layer 4's safety checks
- Layer 4's safety constraints define the feasible region boundary for Layer 5's planning

---

## IV. Key Methodological Papers Quick Reference

### If You Care About "How to Fuse Control Theory with Machine Learning"

| Entry Point | Paper | Year |
|-------------|-------|------|
| **RL+MPC Overview** | Reiter et al., *Synthesis of MPC and RL (arXiv:2502.02133)* | 2025 |
| **Data-Driven MPC + Guarantees** | Berberich & Allgöwer, *Annual Reviews in Control* | 2025 |
| **Safe RL Survey** | Kushwaha & Biron, *Safe RL via Lyapunov & Barrier (arXiv:2508.09128)* | 2025 |
| **Koopman Control Survey** | *The Franklin Institute* 2025 | 2025 |
| **RL+ADP Control** | Wang et al., *IEEE/CAA JAS* | 2024 |

### If You Care About "Modern Developments in Robust and Adaptive Control"

| Entry Point | Paper | Year |
|-------------|-------|------|
| **SMC Survey** | Castellanos-Cárdenas et al., *Algorithms* 17(12):543 | 2024 |
| **H∞-SMC Survey** | Mhmood & Mahyuddin, *IEEE Access* 2025 | 2025 |
| **Nonparametric MRAC** | Kurdila et al., *Annual Reviews in Control* 58 (Part I & II) | 2024 |

### If You Care About "The Academic Genealogy of Navigation & SLAM"

| Entry Point | Paper | Year |
|-------------|-------|------|
| **SLAM Tutorial (Part I)** | Durrant-Whyte & Bailey, *IEEE RAM* | 2006 |
| **SLAM Tutorial (Part II)** | Bailey & Durrant-Whyte, *IEEE RAM* | 2006 |
| **ORB-SLAM** | Mur-Artal et al., *IEEE TRO* | 2015 |
| **Autonomous Navigation Survey** | Nahavandi et al., *ACM Computing Surveys* 57(9) | 2025 |
| **SLAM+BVI Survey** | *IEEE Access* 2024 | 2024 |

### If You Care About "MPC from Fundamentals to Frontiers"

| Entry Point | Paper | Year |
|-------------|-------|------|
| **MPC Textbook** | Rawlings, Mayne, Diehl, *MPC: Theory and Design* | 2017 |
| **MPC Stability Survey** | Mayne et al., *Automatica* 36:789-814 (10,000+ citations) | 2000 |
| **NMPC Real-Time Iteration RTI** | Diehl et al., 2002 | 2002 |
| **DeePC** | Coulson, Lygeros, Dörfler, 2019 | 2019 |
| **ML-MPC Tutorial** | Wu & Christofides, *Reviews in Chemical Engineering* | 2025 |

---

## V. Honest Boundaries

This framework is based on a literature survey conducted in May 2026 and has the following limitations:

1. **Scope of Survey**: Covers 6 domains, but sub-directions within each domain cannot be exhaustive. For example, multi-model adaptive control and fuzzy adaptive control within adaptive control received only representative coverage
2. **Temporal Cutoff**: The latest preprints from 2025 onward may not be fully incorporated
3. **Depth-First vs. Breadth-First**: This survey emphasized breadth to establish cross-domain connections; deep-dive papers for each sub-domain require consulting the complete lists in each research file
4. **RL Domain**: RL evolves extremely rapidly (hundreds of arXiv papers per month); this survey only covers control-relevant RL papers
5. **Blind Guidance Domain**: Focused primarily on survey and system-level papers; low-level sensor hardware papers were not deeply covered
6. **Chinese-Language Literature**: This survey focused on English-language academic papers; coverage of Chinese academic journals (Acta Automatica Sinica, Control Theory & Applications, etc.) is insufficient
7. **Patents and Commercial Products**: Patent literature and commercial product technical specifications were not included
8. **Mathematical Theory Depth**: Discussion of foundational control mathematics (e.g., ISS, passivity theory, dissipative systems) is primarily citation-based without chapter-level expansion

---

## VI. Appendix: Research Sources

### Research Files

| Domain | File | Paper Count |
|--------|------|-------------|
| Navigation (SLAM + Path Planning + Fusion) | `references/research/01-navigation.md` | ~100+ |
| Blind Guidance (Wearable + CV + Feedback) | `references/research/02-blind-guidance.md` | ~30+ |
| Robust Control (H∞ + SMC + LMI) | `references/research/03-robust-control.md` | ~40+ |
| Adaptive Control (MRAC + Backstepping + ILC) | `references/research/04-adaptive-control.md` | ~80+ |
| RL Control (RL + Safety + Sim2Real) | `references/research/05-rl-control.md` | ~80+ |
| MPC (Linear / NMPC / Robust / Data-Driven) | `references/research/06-mpc.md` | ~50+ |

### Primary Sources (Original Papers, Monographs)
- Sutton & Barto (RL Bible), Rawlings/Mayne/Diehl (MPC Textbook)
- Doyle et al. 1989 (DGKF H∞), Utkin 1992 (SMC Foundation)
- Krstić et al. 1995 (Adaptive Backstepping), Åström & Wittenmark 1995 (Adaptive Control)
- Mur-Artal et al. 2015 (ORB-SLAM), Durrant-Whyte & Bailey 2006 (SLAM Tutorials)
- Schulman et al. 2017 (PPO), Haarnoja et al. 2018 (SAC)

### Secondary Sources (Survey Papers, Review Articles)
- All 2023–2025 survey papers cited in this research are secondary sources
- See individual research files for detailed lists

---

> This knowledge distillation framework is powered by the [Nüwa · Skill Creation](https://github.com/alchaincyf/nuwa-skill) methodology
> Created: 2026-05-19 | Research Agents: 6 | Total Source Papers: ~380+
