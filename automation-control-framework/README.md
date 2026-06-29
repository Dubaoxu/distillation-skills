# Automation & Control · Knowledge Distillation Framework

[中文版](README_ZH.md)

A Claude Code skill that distills the core knowledge of the **automation & control engineering** domain into a navigable framework — covering 6 subfields, 300+ papers, 7 methodological consensuses, 6 school-of-thought divergences, and a 5-layer technology stack.

---

## What This Is

This is a **research navigator and knowledge index** for the automation & control domain. It doesn't generate new content — it helps you quickly locate the right papers, understand the methodological landscape, and identify where your work fits.

## Domain Coverage (6 Dimensions)

```
   Reinforcement Learning Control  ← Strategy Layer
   Robust · Adaptive · MPC         ← Control Layer
   Blind Guidance (BVI)            ← Application Layer
   Autonomous Navigation           ← Execution Layer
```

| Dimension | Key Topics |
|-----------|-----------|
| **Navigation** | SLAM, path planning, sensor fusion, learned navigation |
| **Blind Guidance** | CV, wearable sensors, HMI feedback, indoor localization |
| **Robust Control** | H∞, μ-synthesis, SMC, LMI, small-gain theorem |
| **Adaptive Control** | MRAC, backstepping, ILC, L1, ESC |
| **MPC** | Linear/NMPC, tube-based, data-driven, RL+MPC fusion |
| **RL Control** | PPO, SAC, Safe RL, MBRL, sim-to-real |

## Distilled Insights

### 7 Core Methodological Consensuses
1. **Feedback is the soul of control** — cross-domain invariant
2. **Model uncertainty bounds performance** — from robust to RL
3. **Stability + optimality trade-off** — the fundamental tension
4. **Learning complements, doesn't replace, structure** — hybrid wins
5. **Safety requires explicit constraints** — not just reward shaping
6. **Data quality > data quantity** — especially in adaptive/learning control
7. **Real-world validation is non-negotiable** — sim-to-real gap is real

### 6 School Divergences & Convergence Trends
1. Model-based vs. model-free → converging on **model-informed**
2. Robust vs. adaptive → converging on **robust-adaptive**
3. Centralized vs. decentralized → task-dependent, no universal winner
4. Linear vs. nonlinear → **gain-scheduled + LPV** as pragmatic bridge
5. Optimality vs. tractability → **MPC + learning** as emerging resolution
6. Theory-first vs. experiment-first → **simulation-in-the-loop** hardening

### 5-Layer Technology Stack
| Layer | Function | Key Methods |
|-------|----------|-------------|
| **Strategy** | High-level decision & learning | RL, game theory, meta-learning |
| **Planning** | Trajectory & path generation | MPC, optimization, sampling-based |
| **Control** | Low-level actuation & stabilization | Robust, adaptive, nonlinear |
| **Perception** | State estimation & sensing | SLAM, CV, sensor fusion |
| **Execution** | Physical embodiment & actuation | Motor control, haptics, kinematics |

---

## When to Use

- Navigating the automation & control research landscape
- Understanding where your work fits in the methodological spectrum
- Finding core papers in any of the 6 subfields
- Identifying research gaps at consensus/divergence boundaries
- As a knowledge base for downstream paper writing (via [paper-writing-agent](../paper-writing-agent/))

## When NOT to Use

- Writing a paper directly → use [academic-paper](../academic-research-skills/academic-paper/) or [paper-writing-agent](../paper-writing-agent/)
- Conducting new literature search → use [deep-research](../academic-research-skills/deep-research/)
- Reviewing a paper → use [academic-paper-reviewer](../academic-research-skills/academic-paper-reviewer/)

---

## File Structure

```
automation-control-framework/
├── README.md                    # This file (EN)
├── README_ZH.md                 # Chinese version
├── SKILL.md                     # Skill definition (Chinese, 309 lines)
├── SKILL_EN.md                  # Skill definition (English, 315 lines)
└── references/
    └── research/
        ├── 01-navigation.md     # Autonomous navigation survey
        ├── 02-blind-guidance.md # Assistive technology survey
        ├── 03-robust-control.md # Robust control survey
        ├── 04-adaptive-control.md # Adaptive control survey
        ├── 05-rl-control.md     # RL for control survey
        └── 06-mpc.md            # Model predictive control survey
```

## Installation

```bash
# Clone into Claude Code skills directory
git clone <this-repo> ~/.claude/skills/automation-control-framework

# Or symlink
ln -s $(pwd)/automation-control-framework ~/.claude/skills/automation-control-framework
```

## Dependencies

- Claude Code v3.7.0+
- No Python dependencies required
- References are self-contained markdown files

## Related Skills

- [academic-research-skills](../academic-research-skills/) — Full academic pipeline (research → write → review)
- [paper-writing-agent](../paper-writing-agent/) — Domain-specialized paper writing coordinator
- [nuwa-skill](../nuwa-skill/) — Distill any person's thinking framework

## License

See [SKILL.md](SKILL.md) frontmatter for license declaration.
