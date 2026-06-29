# 鲁棒控制领域权威论文调研

> 调研时间：2026-05-19 | 涵盖 H∞、μ综合、滑模控制、LMI、鲁棒MPC

## 综述论文 (Survey Papers)

| 论文 | 作者 | 年 | 出处 | 要点 |
|------|------|----|------|------|
| **H∞ Sliding Mode Control: A Recent Review** | Mhmood AH, Mahyuddin MN | 2025 | *IEEE Access*, 13:136687-136715 | H∞-SMC设计方法与应用最新综述 |
| **A Review on Data-Driven Model-Free Sliding Mode Control** | Castellanos-Cárdenas D, et al. | 2024 | *Algorithms*, 17(12):543 | 文献计量系统综述，256篇参考文献，19引用 |
| **Sliding-Mode Control Strategies for PMSM: Comprehensive Review** | Ajasa A, et al. | 2025 | *arXiv:2510.18420* | PMSM滑模策略分类综述 |

## 奠基性经典 (Foundational Works)

| 论文 | 作者 | 年 | 出处 | 引用 | 核心贡献 |
|------|------|----|------|------|---------|
| **State-space solutions to standard H₂ and H∞ control problems** | Doyle J, Glover K, Khargonekar P, Francis B | 1989 | *IEEE TAC*, 34(8) | 10000+ | **H∞控制基石**：DGKF论文，给出标准H₂/H∞状态空间解 |
| **Feedback and optimal sensitivity** | Zames G | 1981 | *IEEE TAC* | 5000+ | H∞控制的起源概念论文 |
| **Sliding Modes in Control and Optimization** | Utkin VI | 1992 | *Springer* | 专著 | **SMC创立者**：滑模控制奠基性专著 |
| **Sliding Mode Control: Theory and Applications** | Edwards C, Spurgeon SK | 1998 | *Taylor & Francis* | 3000+ | SMC权威教材，定义性参考书 |
| **A Control Engineer's Guide to Sliding Mode Control** | Young KD, Utkin VI, Ozguner U | 1999 | *IEEE TCST*, 7(3) | 2500+ | SMC经典教程，入门必读 |

## H∞ 控制

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **The H∞ control problem: A state space approach** | Doyle J, Glover K, Khargonekar P, Francis B | 1989 | DGKF解法，2-Riccati方程法 |
| **A loop shaping design procedure using H∞ synthesis** | McFarlane D, Glover K | 1992 | H∞环路成形法设计 |
| **Multivariable Feedback Design** | Maciejowski JM | 1989 | 多变量反馈设计 |
| **Multivariable Feedback Control (2nd ed.)** | Skogestad S, Postlethwaite I | 2005 | H∞控制的标准教材 |

## μ综合 (Mu-Synthesis)

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Analysis of feedback systems with structured uncertainties** | Doyle J | 1982 | 结构化奇异值μ的提出 |
| **The complex structured singular value** | Packard A, Doyle J | 1993 | D-K迭代方法 |
| **μ-Analysis and Synthesis Toolbox** | Balas G, et al. | 1994 | MATLAB工具包 |

## 滑模控制 (Sliding Mode Control)

### 经典奠基

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Variable Structure Systems with Sliding Modes** | Utkin VI | 1977 | VSS滑模理论的系统阐述 |
| **Sliding Modes in Control and Optimization** | Utkin VI | 1992 | 滑模控制奠基专著 |
| **Applied Nonlinear Control** | Slotine JJE, Li W | 1991 | SMC+自适应，广泛应用教材 |
| **Sliding Mode Control: Theory and Applications** | Edwards C, Spurgeon SK | 1998 | SMC权威专著 |

### 高阶滑模 (Higher-Order SMC)

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Higher-order sliding modes, differentiation and output-feedback control** | Levant A | 2003 | 任意阶滑模微分器 |
| **Sliding Mode Control and Observation** | Shtessel Y, Edwards C, Fridman L, Levant A | 2014 | 现代SMC综合教材 |
| **Second order twisting algorithms** | Sira-Ramírez H, et al. | 2024 | Utkin追随者，一阶→二阶微分几何推导 |

### 积分滑模

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **LMI-Based Sliding Surface Design for Integral SMC** | Choi HH | 2007 | LMI+ISMC用于失配不确定系统 |

### 2024 纪念 Utkin 特刊

| 期刊 | 年 | 覆盖主题 |
|------|----|---------|
| *Journal of the Franklin Institute* 特刊 | 2024 | 预定时间收敛(2篇)、高阶滑模(4篇)、滑模观测器(3篇)、神经网络SMC(2篇)、应用(6篇) |

## LMI 方法

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Linear Matrix Inequalities in System and Control Theory** | Boyd S, El Ghaoui L, Feron E, Balakrishnan V | 1994 | LMI方法论的标准参考书 |
| **Multiobjective output-feedback control via LMI optimization** | Scherer C, Gahinet P, Apkarian P | 1997 | 多目标输出反馈LMI方法 |
| **Robust pole placement in LMI regions** | Chilali M, Gahinet P | 1996 | LMI极点配置 |

## 鲁棒 MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Min-max feedback MPC for constrained linear systems** | Scokaert POM, Mayne DQ | 1998 | Min-max鲁棒MPC |
| **Tube-based robust MPC** | Mayne DQ, Seron M, Raković S | 2005 | Tube法鲁棒MPC |
| **The scenario approach to robust control design** | Calafiore GC, Campi MC | 2006 | 场景法鲁棒设计 |
| **An overview of systems-theoretic guarantees in data-driven MPC** | Berberich J, Allgöwer F | 2025 | 数据驱动鲁棒MPC理论保证综述 |

## 重要教材与专著

| 教材 | 作者 | 年 | 出版商 |
|------|------|----|--------|
| **Robust and Optimal Control** | Zhou K, Doyle JC, Glover K | 1996 | Prentice Hall |
| **Multivariable Feedback Control** | Skogestad S, Postlethwaite I | 2005 | Wiley |
| **Essentials of Robust Control** | Zhou K, Doyle JC | 1998 | Prentice Hall |
| **Feedback Control Theory** | Doyle JC, Francis BA, Tannenbaum AR | 1992 | Macmillan |
| **Robust Control Design with MATLAB** | Gu DW, Petkov PH, Konstantinov MM | 2005 | Springer |
| **A Course in Robust Control Theory** | Dullerud GE, Paganini F | 2000 | Springer |
| **Road Map for Sliding Mode Control Design** | Utkin VI, Poznyak A, Orlov Y, Polyakov A | 2020 | Springer |

## 应用论文

| 领域 | 代表性论文 | 方法 | 应用场景 |
|------|----------|------|---------|
| **航空控制** | — | H∞/μ | 飞行控制系统、导弹自动驾驶 |
| **汽车控制** | — | SMC/H∞ | 主动悬挂、防抱死制动 |
| **机器人** | — | SMC/鲁棒自适应 | 不确定性下的稳定操作 |
| **电力电子** | — | SMC | DC-DC转换器、逆变器 |
| **过程控制** | — | 鲁棒MPC | 化工过程不确定性 |
