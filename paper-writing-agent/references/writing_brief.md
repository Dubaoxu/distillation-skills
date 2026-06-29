# Writing Brief — Phase 5

**Date**: 2026-05-23
**Target**: Second revision of "A Hierarchical Safe MPC-RL Framework for Adaptive Shared-Autonomy Navigation of Visually Impaired Pedestrians"

---

## Current Status

The paper has completed one round of Major Revision, successfully addressing all 6 Tier-1 issues from the initial review. The revised draft is substantially stronger but still has gaps to address.

## Recommended Modification Priorities (This Round)

### Priority 1: Complete Reference Authors and Formatting
- Fill in missing author names for all references
- Ensure consistent formatting (conference proceedings with "Proc." prefix, journal volumes/pages)
- Add DOIs where available
- Consider adding 3-5 new references from local knowledge base to strengthen literature review

### Priority 2: Add Visual Elements (Placeholders with Captions)
- **Figure 1**: Three-layer architecture diagram (replace ASCII art with formal figure)
- **Figure 2**: Minimum obstacle distance distribution (referenced in text but not included)
- **Figure 3**: Tube radius sensitivity analysis plot (data exists in Table 7)
- **Figure 4**: Preference convergence over time (KL divergence vs L1 updates)
- Add figure descriptions in Appendix or figure captions section

### Priority 3: Strengthen Related Work with Additional Citations
From local knowledge base, add:
- Hewing et al. (2020) — Learning-Based MPC survey (positions our work)
- Gros & Zanon (2022) — Learning for MPC with Safety Guarantees (theoretical alignment)
- Real & Araujo (2019) — Comprehensive BVI navigation survey
- Li et al. (2023) — Competing predictive safety filter approach

### Priority 4: Format for Target Venue
Based on the project analysis, recommended target: **IEEE RA-L** (2区 + CAA A类 + fast review)
- Convert to IEEE two-column format
- Ensure abstract length < 250 words
- 6-8 pages target (current ~15 single-column pages ≈ 7-8 IEEE pages)
- Add "IEEE Robotics and Automation Letters" submission header

### Priority 5: Ethics and Impact Statement
- Add a brief section on broader impacts
- Explicitly address ethical considerations of AI-guided assistive navigation
- Discuss potential for over-reliance and the importance of preserving user agency

## Recommended Paper Structure

Maintain current IMRaD structure:
1. Introduction (with Contributions)
2. Related Work (5 subsections)
3. Problem Formulation
4. Method (5 subsections)
5. Experiments (3 subsections)
6. Discussion (Limitations + Future Work)
7. Conclusion
8. References

## Target Journal Adaptation

**Primary target**: IEEE Robotics and Automation Letters (RA-L)
- Emphasize: system implementation, real-time performance, extensive simulation
- Format: two-column, ≤8 pages
- Required: multimedia attachment showing navigation examples (optional but recommended)
- Review timeline: ~8 weeks

## What's NOT Being Changed This Round

1. Simulation-only validation (acknowledged limitation, requires hardware + user study)
2. Core architecture (stable after first revision, all proofs strengthened)
3. Experimental results (already comprehensive with 6 baselines, 5 envs, 5 profiles)
4. BVI user study (deferred to future work, properly gated in Limitations)

## Expected Output

- Revised manuscript with complete references
- Figure placeholders with detailed captions
- Additional citations from local knowledge base
- Journal-formatted version (IEEE RA-L style)
- Updated journal recommendations
