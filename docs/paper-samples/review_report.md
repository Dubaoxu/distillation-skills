# ARS Academic Paper Reviewer — Full Review Report

**Paper:** "A Hierarchical Safe MPC-RL Framework for Personalized Assistive Navigation of Visually Impaired Pedestrians"
**Date:** 2026-05-19
**Mode:** full (7-agent: field_analyst + EIC + 3 peer reviewers + devil's advocate + editorial synthesizer)
**Decision:** **MAJOR REVISION** (5/5 reviewers)

---

## Reviewer Panel

| Reviewer | Role | Recommendation |
|----------|------|----------------|
| Prof. Elena Vasconcelos | EIC, IEEE T-RO | Major Revision |
| Prof. Kenji Taniguchi | R1: Methodology (Tube MPC, control theory) | Major Revision |
| Dr. Sarah Okafor | R2: Domain (BVI navigation, accessibility) | Major Revision |
| Prof. Martin Lindqvist | R3: Cross-Disciplinary (safety systems, HRI) | Major Revision |
| Prof. David Rosenfeld | Devil's Advocate | Major Revision |

---

## Consensus Map

### CRITICAL Issues (≥3/5 agreement)

| # | Issue | Consensus | Reviewers |
|---|-------|-----------|-----------|
| C1 | No real-world/BVI user validation; synthetic data is circular | 5/5 | All |
| C2 | Proposition 1 proof insufficient (no recursive feasibility, linearization error unbounded, W_bounded undefined) | 4/5 | EIC, R1, R3, DA |
| C3 | "Human as disturbance" framing inappropriate for assistive technology | 4/5 | EIC, R2, R3, DA |
| C4 | Trilemma framing is a strawman; no hand-tuned baseline to prove RL necessity | 3/5 | DA, EIC, R2 |
| C5 | "87% accuracy" undefined/misleading | 3/5 | EIC, R1, DA |

---

## Tier 1 Revision Roadmap (MUST fix)

1. **T1-1**: Add hand-tuned fixed-weight Tube MPC + DWA baseline (new experiments, 2-3 weeks)
2. **T1-2**: Either collect real human data OR remove "Personalized" from title and moderate claims
3. **T1-3**: Make Proposition 1 rigorous — define W_bounded, prove recursive feasibility, bound linearization error
4. **T1-4**: Revise "human as disturbance" framing → shared autonomy language
5. **T1-5**: Define Minimal Risk Condition and fallback strategy
6. **T1-6**: Define "87% accuracy" or remove it

## Tier 2 (SHOULD fix)

7. Multi-rate stability analysis (quantify max displacement vs tube radius)
8. Fix disturbance model to respect nonholonomic constraint
9. Specify user interface (haptic/audio/handle)
10. Sensitivity analysis for tube radius alpha
11. Trust calibration and automation surprise discussion
12. Clarify CQL-RL formulation

## Tier 3 (CONSIDER)

13-20. Pontryagin difference details, adversarial agents, near-miss stats, Vaaler comparison, uncited references, code release, hyperparameters, sensor noise

---

## Viability

**Salvageable for T-RO:** Yes, with substantial revision (~4 months).
**Recommended strategy:** Narrow scope — remove "Personalized" from title, reframe as adaptive architecture paper, add hand-tuned baseline, fix mathematical rigor.

Full detailed reports for each reviewer and the editorial decision letter are in the conversation above.
