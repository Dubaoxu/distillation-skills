# Journal Recommendations — Phase 8

**Paper**: "A Hierarchical Safe MPC-RL Framework for Adaptive Shared-Autonomy Navigation of Visually Impaired Pedestrians"
**Date**: 2026-05-23
**Version**: v0.3

---

## Recommendation Summary

The paper now has:
- Provable safety guarantee (Lemmas 1-3, Proposition 1, MRC)
- Extensive simulation (10K trials, 5 envs, 5 profiles, 6 baselines)
- Strong theoretical contribution (cost-function-parameterization decoupling)
- Honest limitations (simulation-only, no user study)

### Primary Recommendation: IEEE Robotics and Automation Letters (RA-L)

| Dimension | Assessment |
|-----------|-----------|
| **CAA Level** | A类 |
| **CAS Quartile** | 2区 |
| **IF** | ~5.3 |
| **Review Speed** | ~8 weeks (fastest among robotics journals) |
| **Scope Match** | ★★★★ — robotics, automation, assistive systems |
| **Method Match** | ★★★★ — values system implementation + strong experiments |
| **Innovation Level** | ★★★ — significant advance but not paradigm-defining |
| **Format Fit** | 6-8 pages, two-column IEEE format. Current ~10K words ≈ 7-8 IEEE pages |

**Why RA-L**: The paper's strengths align well with RA-L's preferences:
- Strong experimental validation (10K trials meets RA-L standards)
- Practical system design with detailed implementation
- Real-time performance data on actual (simulated) hardware
- RA-L accepts simulation-only work when experiments are thorough and limitations are honest
- Fast review cycle lets authors iterate quickly
- Accepted papers can present at ICRA/IROS

**What to emphasize**: Real-time performance (§5.2.3), ablation studies (§5.2.4), and implementation details (§4.5).

### Stretch Target: IEEE Transactions on Robotics (T-RO)

| Dimension | Assessment |
|-----------|-----------|
| **CAA Level** | A类 |
| **CAS Quartile** | 1区 TOP |
| **IF** | ~10.5 |
| **Review Speed** | ~4-6 months |
| **Scope Match** | ★★★ — T-RO prefers hardware validation |
| **Method Match** | ★★★★ — values theoretical depth + rigorous experiments |
| **Innovation Level** | ★★★ — strong but would benefit from real-world validation |

**Risk**: T-RO reviewers will likely request hardware experiments or user study data. The current simulation-only validation is a significant weakness for T-RO standards. Consider submitting to T-RO only after completing the CaBot hardware integration (mentioned as future work).

### Theory-Focused Alternative: Automatica

| Dimension | Assessment |
|-----------|-----------|
| **CAA Level** | A+类 |
| **CAS Quartile** | 1区 |
| **IF** | ~6.2 |
| **Review Speed** | ~6 months |
| **Scope Match** | ★★★★ — control theory flagship |
| **Method Match** | ★★★★★ — Proposition 1 + Lemmas are textbook Automatica material |
| **Innovation Level** | ★★★ — Tube MPC application to new domain |

**What to modify for Automatica**: Expand the theoretical sections (§3-4), compress experiments (§5), add more formal definitions and proofs. Automatica values theoretical elegance over experimental breadth. The safety proof (Lemmas 1-3 → Proposition 1) is the strongest part of the paper from an Automatica perspective.

### BVI/Accessibility Focus: ACM ASSETS or IEEE TACCESS

| Venue | CAS | IF | Scope |
|-------|-----|-----|-------|
| **ACM ASSETS** | Conference (no CAS) | — | Accessibility and assistive technology |
| **IEEE TACCESS** | Journal | ~3.0 | Accessibility, human-centered computing |

These venues are worth considering if the authors complete a BVI user study. The current paper's lack of user validation makes it a poor fit for these accessibility-focused venues at present.

### Conference Option: ICRA / IROS

| Venue | CCF | CAA | Acceptance | Scope Match |
|-------|-----|-----|-----------|-------------|
| **ICRA** | B (AI) | A | ~40-45% | ★★★★ — robotics systems |
| **IROS** | C (AI) | A | ~45-50% | ★★★ — intelligent systems |

Conference papers are typically 6 pages. Our 10K-word manuscript would need significant compression. The simulation experiments and theoretical contributions are strong enough for ICRA. IROS is a good backup.

### Not Recommended (at current state)

- **IEEE TAC**: expects fundamental theoretical advances; our Tube MPC application, while rigorous, applies existing theory
- **Science Robotics**: requires hardware validation and breakthrough significance
- **IJRR**: similar to T-RO but even more selective
- **NeurIPS/ICLR/ICML**: learning component (CQL+IRL) is not the primary novel contribution

## Recommended Strategy

1. **Immediate**: Submit to **IEEE RA-L** (with ICRA presentation option)
   - Format to 6-8 pages IEEE two-column
   - Reduce word count to ~6K by compressing Related Work and implementation details
   - Keep all safety proofs (they distinguish the paper)
2. **After RA-L + hardware**: Revise and submit to **T-RO** with added hardware results
3. **After user study**: Submit user-study version to **ASSETS** or **TACCESS**
4. **Alternate path**: If RA-L is rejected, expand theory for **Automatica** submission

## Format Conversion Notes

For IEEE RA-L submission:
- Convert to `\documentclass[journal]{IEEEtran}` for LaTeX
- Two-column, 10pt font
- Figures in vector format (PDF/EPS)
- References in IEEE numeric style [1], [2], ...
- Abstract ≤ 250 words (current: ~220 words — fits)
- 6-8 pages including references and author bios
- Mandatory: Data availability statement, code availability statement

---

## Submission Checklist (Updated 2026-05-23)

### Completed Items

| # | Item | Status | Notes |
|---|------|--------|-------|
| 1 | Safety proof (Lemmas 1-3, Proposition 1, MRC) | ✅ Done | Rigorous, publishable level |
| 2 | Hand-tuned MPC+DWA baseline | ✅ Done | Statistical significance confirmed ($p < 0.001$) |
| 3 | Shared autonomy reframing | ✅ Done | Title, abstract, §2.5, §3.1, §4.4 |
| 4 | Multi-rate stability (Proposition 2) | ✅ Done | §4.3.5, numerical verification |
| 5 | Tube radius sensitivity (Table 7) | ✅ Done | §5.2.5, Figure 3 |
| 6 | User interface design | ✅ Done | §4.4.1, vibrotactile + audio |
| 7 | Trust calibration | ✅ Done | §4.4.2 (not validated) |
| 8 | Ethics/Broader Impacts | ✅ Done | §6.4 |
| 9 | Reference completeness | ✅ Done | All 35 refs with full author names, DOIs |
| 10 | Data & Code Availability statement | ✅ Done | After Conclusion |
| 11 | Figures 1-4 generated | ✅ Done | PDF (vector) + PNG in `paper/figures/` |
| 12 | Limitations honestly stated | ✅ Done | §6.2: simulation-only, no BVI study |
| 13 | **Word count reduced** | ✅ Done | **~7,200 body words (down from ~9,100)** |
| 14 | Appendix figure captions | ✅ Done | Detailed captions for Figures 1-4 |

### Before Submission

| # | Item | Priority | Notes |
|---|------|----------|-------|
| 1 | Convert to IEEEtran LaTeX | **BLOCKING** | Current format is Markdown; must convert to `\documentclass[journal]{IEEEtran}` |
| 2 | Fill in author names/affiliations | **BLOCKING** | Currently "[Author Names]" and "[Affiliation]" |
| 3 | Figure placement in LaTeX | **BLOCKING** | Insert PDF figures at appropriate locations |
| 4 | IEEE reference format | **BLOCKING** | Convert `[N]` references to IEEE `\cite{}` format with .bib file |
| 5 | Page count verification | RECOMMENDED | Compile LaTeX and verify 6-8 pages |
| 6 | Code repository URL | RECOMMENDED | Replace "will be released upon acceptance" with actual URL if available |
| 7 | ORCID iDs | RECOMMENDED | Add author ORCID identifiers |
| 8 | Supplementary video | OPTIONAL | Screen-capture of navigation examples for multimedia attachment |
| 9 | Adversarial dynamic agents | OPTIONAL | Note as future work (already partially in §6.2) |

### File Manifest

| File | Location | Purpose |
|------|----------|---------|
| Compressed manuscript | `paper/paper_draft_revised.md` | IEEE RA-L body (~7,200 words) |
| IEEE RA-L archive | `.claude/skills/paper-writing-agent/manuscript_ieee_ral_v1.0.md` | Archived compressed version |
| v0.3.1 archive | `.claude/skills/paper-writing-agent/manuscript_v0.3.1.md` | Pre-compression full version |
| Figure 1 (architecture) | `paper/figures/figure1_architecture.pdf` | Vector, 53 KB |
| Figure 2 (obstacle dist.) | `paper/figures/figure2_obstacle_distance.pdf` | Vector, 55 KB |
| Figure 3 (tube sensitivity) | `paper/figures/figure3_tube_sensitivity.pdf` | Vector, 36 KB |
| Figure 4 (preference conv.) | `paper/figures/figure4_preference_convergence.pdf` | Vector, 35 KB |
| Figure generation script | `paper/generate_figures.py` | Reproducible figure generation |
| Review (Round 2) | `.claude/skills/paper-writing-agent/review_round2.md` | Re-review report (78/100) |
