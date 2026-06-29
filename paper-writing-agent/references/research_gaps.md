# Research Gap Analysis — Phase 4

**Date**: 2026-05-23

---

## Gap 1: Formal Safety Guarantees in Assistive Navigation → PARTIALLY RESOLVED

**Status**: Addressed by our Tube MPC layer, but only **in simulation**.

**Why existing methods fail**:
- ETAs/DWA: no formal guarantees, purely reactive
- CaBot: hardware-level safety (speed limits), no formal proof
- RL methods: no safety constraints
- RL+CBF: probabilistic only, not deterministic

**Our contribution**: Proposition 1 provides deterministic safety guarantee. However, the guarantee depends on assumptions that must be validated in hardware (bounded uncertainty, accurate state estimation).

**Remaining gap**: The proof is complete in theory but untested on physical hardware. Sensor noise characteristics, user-device physical interaction, and real-time constraint satisfaction on embedded hardware remain unvalidated.

---

## Gap 2: User Preference Learning vs Safety Decoupling → LARGELY RESOLVED

**Status**: Our core contribution — the cost-function-parameterization interface between RL and MPC — directly addresses this gap.

**Why existing methods fail**:
- End-to-end RL: safety and preference entangled in one policy
- Constrained RL: safety constraints change with policy updates
- Fixed MPC: no adaptivity

**Our contribution**: Decoupling RL (preferences) from MPC (safety), with formal proof (Proposition 1) that safety is independent of preference weights.

**Remaining gap**: The stationarity assumption (preferences constant over K=50 steps). Context-dependent preferences (user more cautious in unfamiliar environments) are not modeled.

---

## Gap 3: Human Modeling in Safety-Critical Control → PARTIALLY RESOLVED

**Status**: Addressed by shared-autonomy framing and nonholonomic uncertainty decomposition.

**Why existing methods fail**:
- Safety filter literature: human absent (fully autonomous)
- ETA literature: human present but not modeled formally
- "Human as disturbance" framing: technically limiting and ethically inappropriate

**Our contribution**: Shared-autonomy framework with the user as active collaborator, nonholonomic uncertainty decomposition respecting human walking biomechanics, and tube radius accommodating human variability.

**Remaining gap**: No real BVI user validation. The shared-autonomy interface (vibrotactile belt + bone-conduction audio) is architecturally designed but not user-tested.

---

## Gap 4: Real-Time Dynamic Obstacle Handling → LARGELY RESOLVED

**Status**: Addressed by L3 DWA with tube-constrained search space and emergency braking.

**Why existing methods fail**:
- Pure Tube MPC: too slow for sub-100ms dynamic obstacle response
- Pure DWA: no safety guarantees
- Stochastic MPC: computationally expensive

**Our contribution**: L3 refines within tube cross-section at 100 Hz. DWA search space is constrained by tube, so safety guarantee is maintained.

**Remaining gap**: If a dynamic obstacle completely occludes the tube cross-section, L3 brakes and triggers replan, which takes up to 100ms. During this interval, the user could potentially move (though bounded by MRC).

---

## Gap 5: Comprehensive Real-World Validation → UNRESOLVED

**Status**: This is the most significant remaining gap. All results are simulation-only.

**What's needed**:
- Hardware deployment on a physical assistive device (CaBot or similar)
- User study with BVI participants to validate preference learning and shared-autonomy interface
- Sensor noise characterization and real-time constraint satisfaction verification
- Comparison with existing commercial ETAs in real-world environments

**Why this matters**: Simulation results, even with photorealistic rendering (Habitat-Sim), cannot capture:
- Real sensor noise characteristics
- User-device physical interaction dynamics
- Social navigation dynamics in crowded spaces
- Long-term user preference drift

---

## 未解决问题 → need/ 标注

| # | Gap | Need Type | Urgency | File |
|---|-----|-----------|---------|------|
| 1 | BVI user study data | experiment | blocking (for human-subject claims) | `need/bvi_user_study.md` |
| 2 | Hardware deployment results | experiment | important | `need/hardware_deployment.md` |
| 3 | Complete author names for refs [1][2][5][9][23] | literature | important | `need/missing_author_names.md` |

---

## Contribution Positioning

| Gap | Current Paper Coverage | Strength | Weakness |
|-----|----------------------|----------|----------|
| Formal safety in assistive nav | Proposition 1 proof + 10K zero-collision trials | Strong theory + extensive sim | No hardware validation |
| RL-MPC safe decoupling | Cost-function interface + W_bounded + MRC | Novel architecture + proof | Stationarity assumption |
| Human as collaborator | Shared autonomy + nonholonomic decomposition | Ethically appropriate framing | No user study |
| Real-time performance | 20.4ms total latency | Well within 50ms budget | Embedded hardware partially tested |
| Comprehensive validation | 5 envs × 5 profiles × 10K trials | Extensive simulation | All synthetic |
