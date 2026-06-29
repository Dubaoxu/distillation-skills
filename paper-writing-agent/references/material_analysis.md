# Material Analysis — Phase 1

**Paper**: "A Hierarchical Safe MPC-RL Framework for Adaptive Shared-Autonomy Navigation of Visually Impaired Pedestrians"
**Date**: 2026-05-23
**Version**: v0.2 (post-first-revision)

---

## Core Claims (1-3 sentences)

A properly architected three-layer hierarchical controller (RL for preference learning, Tube MPC for provable safety, DWA for real-time dynamic obstacle response) can simultaneously achieve the trilemma of safety, adaptivity, and real-time performance in assistive navigation — and the decoupling of RL from safety constraints is **provable**: safety guarantees hold uniformly over all preference weights in the feasible set.

## Innovation Points (vs existing work)

1. **First application of Tube MPC to assistive navigation** with formal safety guarantees that are provably independent of learned user preferences
2. **Cost-function-parameterization interface** (not action interface) between RL and MPC — RL tells the MPC *what to optimize*, not *what to do*
3. **Shared-autonomy framing**: user modeled as active collaborator with nonholonomic walking dynamics, not as a disturbance to be rejected
4. **Minimal Risk Condition (MRC)**: explicit, provably safe fallback strategy for the rare infeasibility case
5. **Multi-rate stability analysis**: bounds maximum state displacement during RL update intervals, relating tube radius to the three-layer temporal hierarchy

## Research Questions

**Main**: How can we simultaneously guarantee formal safety, adapt to individual user preferences, and respond to dynamic obstacles in real-time for visually impaired navigation?

**Sub-questions**:
1. Can RL-learned preference parameters be decoupled from safety constraints such that safety is provably independent of the learned policy?
2. How should the human user be modeled — as a disturbance or as a collaborative agent?
3. What happens when the MPC becomes infeasible (rare case) — is there a safe fallback?
4. Does the multi-rate hierarchy (1 Hz / 10 Hz / 100 Hz) remain stable, or can the state drift outside the tube between RL updates?

## Method Framework

| Component | Method | Role |
|-----------|--------|------|
| L1: Preference RL | CQL (offline pretrain) + MaxEnt IRL (online) | Learn user cost function weights |
| L2: Tube MPC | CasADi + qpOASES, RPI set, tightened constraints | Safety-guaranteed trajectory generation |
| L3: DWA | Tube-constrained search space + emergency braking | Real-time dynamic obstacle avoidance |
| Safety Proof | Lemma 1 (RPI) → Lemma 2 (W_bounded) → Lemma 3 (Recursive Feasibility) → Proposition 1 (Safety ∀w) | Formal guarantee |
| MRC Fallback | u=0, relaxed horizon N=5, slack on tube constraints | Safe degradation |

## Data Sources

- Habitat-Sim with Matterport3D dataset (photorealistic indoor environments)
- ORCA model for dynamic pedestrians
- 5 simulated environments (Corridor, Office, Shopping Mall, Outdoor Sidewalk, Intersection)
- 5 synthetic user preference profiles (Cautious, Fast, Smooth, Right-hugging, Balanced)
- CQL pretrained on 1,000 simulated user trajectories with known ground-truth preferences

## Key Assumptions

1. Bounded uncertainty set D (user deviations bounded by biomechanics, environmental noise bounded by domain)
2. Nominal dynamics linearizable around trajectory (linearization error bounded and incorporated into tube radius)
3. Preference stationarity over K=50 step window
4. Static obstacle map available at L2
5. Dynamic obstacles detectable at L3 (100 Hz)
6. Recursive feasibility holds under tightened constraints with terminal set (standard MPC assumptions)

## Domain Mapping (to 5-Layer Tech Stack)

| Layer | Paper Component | Match |
|-------|----------------|-------|
| L1: Physical Modeling | Nonholonomic dynamics + uncertainty decomposition | Direct |
| L2: Perception/Estimation | State estimation, obstacle detection (assumed, not built) | Implicit |
| L3: Control Synthesis | Tube MPC + DWA + ancillary controller K | Core contribution |
| L4: Constraint Safety | RPI set, tightened constraints, MRC fallback | Core contribution |
| L5: Decision/Planning | RL preference learning, MaxEnt IRL | Core contribution |

## Methodological Consensus Alignment

The paper aligns with all 7 core consensuses from the knowledge framework:
1. **Feedback is the soul of control** — All three layers are feedback-driven
2. **Model role spectrum** — Uses both model-based (MPC) and learning-based (RL) components
3. **Constraint handling is the first gate** — Safety constraints are the central architectural concern
4. **Uncertainty quantification** — Tube radius explicitly bounds uncertainty
5. **Data-model fusion** — CQL/IRL (data) + Tube MPC (model) in the same framework
6. **Real-time as hard constraint** — 50ms budget with measured 20.4ms latency
7. **Hierarchical architecture** — Three-layer decoupling is the core insight

## School Divergence Alignment

The paper sits at the convergence of several divergent schools:
- **Model precision vs Robustness**: Chooses robustness (Tube MPC's bounded uncertainty) + learning (RL adapts cost)
- **Online optimization vs Offline training**: Hybrid — offline CQL pretrain + online IRL fine-tune + online MPC optimization
- **Control theory vs ML**: Explicitly bridges both — Lyapunov/RPI (control theory) + CQL/MaxEnt IRL (ML)
