# Literature Map — Phase 2

**Date**: 2026-05-23

---

## Local KB Search Results

Search source: `learning/references/research/` (6 domains, ~380 papers)

### Core Citations (directly support paper claims)

| # | Paper | Domain | Relation to Paper |
|---|-------|--------|-------------------|
| 1 | Reiter et al. (2025) "Synthesis of MPC and RL: Survey and Classification" | MPC+RL | **Architecture classification** — our method belongs to Archetype 2 (MPC within Deployed Policy) |
| 2 | Vaaler et al. (2024) "Modular control architecture for safe marine navigation: RL with PSF" | Safe RL | **Direct architectural predecessor** — modular RL+safety filter pattern |
| 3 | Mayne et al. (2005, 2006) Tube MPC papers | MPC | **Theoretical foundation for L2** — RPI sets, tube construction |
| 4 | Hewing et al. (2020) "Learning-Based MPC: Toward Safe Learning in Control" | MPC+RL | **Surveys safety filter and parameter learning paradigms** |
| 5 | Zanon & Gros (2021) "Safe RL using Robust MPC" | Safe RL+MPC | **Key safety filter reference** — robust MPC as safety layer |
| 6 | Gros & Zanon (2022) "Learning for MPC with Stability and Safety Guarantees" | MPC+RL | **Theoretical guarantee** — safe parameter updates, recursive feasibility |
| 7 | Guerreiro et al. (2019) "CaBot" | BVI Navigation | **Target hardware platform** |
| 8 | Ames et al. (2017/2019) CBF papers | Safe Control | **Alternative safety approach we compare against** |
| 9 | Kumar et al. (2020) CQL | RL | **L1 algorithm foundation** |
| 10 | Ziebart et al. (2008) MaxEnt IRL | IRL | **L1 preference inference** |

### Comparison Baselines (SOTA methods for experimental comparison)

| # | Paper | Method | In our baselines? |
|---|-------|--------|-------------------|
| 1 | Fox et al. (1997) DWA | Reactive obstacle avoidance | Yes (DWA-only baseline) |
| 2 | Haarnoja et al. (2018) SAC | End-to-end RL | Yes (RL-only baseline) |
| 3 | Achiam et al. (2017) CPO | Constrained RL | Referenced [11] |
| 4 | Guerrier et al. (2024) CBF+RL Survey | CBF-based safety | Yes (RL+CBF baseline) |
| 5 | Tabbara et al. (2025) Ensemble PSF + Conformal | Statistical safety | Yes (compared in Table 1) |
| 6 | Csomay-Shanklin et al. (2024) Dynamic Tube MPC | Adaptive tube radius | Referenced [28] |
| 7 | Zanon & Gros (2021) RMPC Safety Filter | MPC safety filter | Referenced in discussion |
| 8 | Dalal et al. (2018) Safety Layer | QP-based safety projection | Alternative approach |

### Background Literature (domain context)

#### BVI Navigation (from 02-blind-guidance.md)
- Dakopoulos & Bourbakis (2010) — foundational ETA survey [already cited as [3]]
- Real & Araujo (2019) "Navigation Systems for BVI: Past Work, Challenges, Open Problems" *Sensors* — **could add**
- Xu et al. (2023) PRISMA systematic review of wearable ETAs — **could add as updated survey**
- Okolo et al. (2024) "Assistive Systems for Visually Impaired Persons" *Sensors* — **could add**
- Elmannai & Elleithy (2017) sensor-based assistive devices survey — comprehensive sensor coverage
- Bamdad et al. (2024) SLAM for Visually Impaired Navigation — relevant for localization context

#### MPC (from 06-mpc.md)
- Berberich & Allgöwer (2025) data-driven MPC guarantees — **highly relevant 2025 survey**
- Coulson et al. (2019) DeePC — data-driven MPC reference
- Rawlings, Mayne, Diehl (2017) MPC textbook — already cited [20]
- Mayne et al. (2000) MPC stability survey — foundational

#### Safe RL + Control (from 05-rl-control.md)
- Gu et al. (2022) "A Review of Safe RL" — comprehensive survey
- Ji et al. (2023) Safety-Gymnasium benchmark
- Li et al. (2023) "Learning Predictive Safety Filter via Decomposition of Robust Invariant Set" — **direct competitor approach**
- Mesbah et al. (2022) "Fusion of ML and MPC under Uncertainty" — ACC position paper
- Fischer et al. (2023) SRMPC — safety reinforced MPC for autonomous driving

#### Robust Control (from 03-robust-control.md)
- Mhmood & Mahyuddin (2025) H∞-SMC review — recent survey
- Castellanos-Cárdenas et al. (2024) data-driven SMC review

## Citation Gaps Identified

### Missing Author Information (must fix)
References [1], [2], [5], [9], [23] lack author names. These need to be completed.

### Recommended Additions from Local KB

1. **Hewing et al. (2020)** — "Learning-Based Model Predictive Control: Toward Safe Learning in Control" — surveys exactly the RL+MPC safety paradigm we use
2. **Gros & Zanon (2022)** — "Learning for MPC with Stability and Safety Guarantees" — directly addresses the theoretical gap we fill
3. **Li et al. (2023)** — "Learning Predictive Safety Filter via Decomposition of Robust Invariant Set" — competing approach worth citing
4. **Xu et al. (2023)** — PRISMA systematic review of wearable ETAs (2020-2023) — more recent survey than Dakopoulos 2010
5. **Real & Araujo (2019)** — comprehensive BVI navigation survey — strengthens Related Work §2.1
6. **Mesbah et al. (2022)** — ML+MPC fusion under uncertainty — positions our work
7. **Berberich & Allgöwer (2025)** — latest data-driven MPC survey — supports future work discussion

### External Search Recommendations
- arXiv: search "safe RL assistive navigation" (2024-2025)
- Google Scholar: "Tube MPC human robot interaction" (last 5 years)
- Search for completed author names for [1], [2], [5], [9], [23]
