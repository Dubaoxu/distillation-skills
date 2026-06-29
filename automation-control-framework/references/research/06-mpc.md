# MPC 模型预测控制领域权威论文调研

> 调研时间：2026-05-19 | 涵盖线性/非线性/鲁棒/随机/经济/分布式/学习驱动/数据驱动MPC

## 综述论文 (Survey Papers)

| 论文 | 作者 | 年 | 出处 | 要点 |
|------|------|----|------|------|
| **An overview of systems-theoretic guarantees in data-driven MPC** | Berberich J, Allgöwer F | 2025 | *Annual Review of Control, Robotics, and Autonomous Systems*, 8:77-100 | **最权威2025综述**：数据驱动MPC稳定性/鲁棒性/约束满足理论保证 |
| **A tutorial review of ML-based MPC methods** | Wu Z, Christofides PD, et al. | 2025 | *Reviews in Chemical Engineering*, 41(4):359-400 | RNN/深度学习MPC全面教程，含开源代码 |
| **LSTM and GRU type RNNs in MPC: A Review** | Ławryńczuk M, Zarzycki K | 2025 | *Neurocomputing*, 632:129712 | LSTM/GRU MPC架构系统综述+pH反应器对比 |
| **Efficient data-driven predictive control of nonlinear systems: Review** | Zhang X, et al. | 2025 | *Digital Chemical Engineering*, 14:100219 | **Koopman MPC + DeePC**，非线性→凸QP |
| **Data Science and MPC: A survey on data-driven MPC algorithms** | — | 2024 | *J. Process Control*, 103327 | 数据驱动MPC四类：RL/自适应/行为理论/轨迹表示 |
| **Synthesis of MPC and RL: Survey and Classification** | Reiter R, Hoffmann J, Diehl M, Gros S | 2025 | *arXiv:2502.02133* | RL-MPC融合三分类~25引用 |
| **Model predictive control for complicated dynamic systems: a survey** | Song, Zhang, Wen, Wang, Wei | 2025 | *Int. J. Systems Science*, 2168-2193 | 网络化/马尔可夫跳跃/T-S模糊系统MPC |
| **Control based on the Koopman operator: A comprehensive review** | — | 2025 | *The Franklin Institute* | DMD/SINDy/DNN Kosman+统一Koopman MPC框架 |
| **A survey of industrial MPC technology** | Qin SJ, Badgwell TA | 2003 | *Control Engineering Practice* | 工业MPC经典综述 |

## 历史起源 (Historical Foundations)

| 论文 | 作者 | 年 | 出处 | 核心贡献 |
|------|------|----|------|---------|
| **Model Predictive Heuristic Control (IDCOM)** | Richalet J, Rault A, Testud JL, Papon J | 1978 | *Automatica* | **MPC起源**：基于脉冲响应模型的工业预测控制 |
| **Dynamic Matrix Control (DMC)** | Cutler CR, Ramaker BL | 1979/1980 | *AIChE / ACC* | DMC算法，基于阶跃响应模型 |
| **Generalized Predictive Control (GPC)** | Clarke DW, Mohtadi C, Tuffs PS | 1987 | *Automatica* | 广义预测控制，统一自校正+MPC框架 |
| **Internal Model Control (IMC)** | Garcia CE, Morari M | 1982 | *I&EC Process Design* | 内模控制，MPC与鲁棒性联系 |

## 线性MPC理论

| 论文 | 作者 | 年 | 出处 | 要点 |
|------|------|----|------|------|
| **Model Predictive Control with Linear Models** | Muske KR, Rawlings JB | 1993 | *AIChE J.* | 无穷时域LQ-MPC稳定性分析 |
| **The stability of constrained receding horizon control** | Rawlings JB, Muske KR | 1993 | *IEEE TAC* | 稳定性保证：终端约束+终端代价 |
| **Constrained model predictive control: Stability and optimality** | Mayne DQ, Rawlings JB, Rao CV, Scokaert POM | 2000 | *Automatica*, 36:789-814 | **MPC里程碑综述**(10000+引用)，约束MPC稳定性与最优性 |
| **The explicit linear quadratic regulator for constrained systems** | Bemporad A, Morari M, Dua V, Pistikopoulos EN | 2002 | *Automatica* | **显式MPC**：多参数二次规划离线求解 |
| **A survey on explicit MPC** | Alessio A, Bemporad A | 2009 | *Int. J. Control* | 显式MPC方法综述 |

## 非线性MPC (NMPC)

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Receding horizon control of nonlinear systems** | Mayne DQ, Michalska H | 1990 | 非线性滚动时域控制稳定性 |
| **Nonlinear model predictive control: Challenges and opportunities** | Allgöwer F, Findeisen R, Nagy Z | 2004 | NMPC挑战综述 |
| **A real-time iteration scheme for nonlinear optimization in optimal feedback control** | Diehl M, Bock HG, Schlöder JP, Findeisen R, Nagy Z, Allgöwer F | 2002 | RTI方案→NMPC实时优化 |
| **CasADi: A software framework for nonlinear optimization and optimal control** | Andersson JAE, Gillis J, Horn G, Rawlings JB, Diehl M | 2019 | NMPC关键开源工具 |

## 鲁棒MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Min-max feedback MPC** | Scokaert POM, Mayne DQ | 1998 | 最坏情况MPC优化 |
| **Tube-based robust MPC** | Mayne DQ, Seron M, Raković S | 2005 | 管状鲁棒MPC框架 |
| **Robust MPC of constrained linear systems with bounded disturbances** | Mayne DQ, Raković SV, Findeisen R, Allgöwer F | 2006 | 管状MPC系统理论 |
| **The scenario approach to robust control design** | Calafiore GC, Campi MC | 2006 | 随机场景法鲁棒设计 |

## 随机MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Stochastic MPC: A critical review** | Mesbah A | 2016 | 随机MPC批评性综述 |
| **Chance-constrained MPC** | Schwarm AT, Nikolaou M | 1999 | 机会约束MPC |
| **Scenario-based MPC** | Bernardini D, Bemporad A | 2011 | 场景法求解机会约束 |

## 经济MPC (Economic MPC)

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Economic optimization using MPC with a terminal cost** | Rawlings JB, Amrit R | 2009 | 经济MPC基础框架 |
| **On average performance and stability of economic MPC** | Angeli D, Amrit R, Rawlings JB | 2012 | 经济MPC平均性能理论 |

## 分布式MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Architectures for distributed and hierarchical MPC: A review** | Scattolini R | 2009 | 分布式MPC架构综述 |
| **Cooperative distributed MPC** | Stewart BT, Venkat AN, Rawlings JB, Wright SJ, Pannocchia G | 2010 | 协作分布式MPC |

## 学习驱动MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Gaussian Process MPC** | Deisenroth MP, Fox D, Rasmussen CE | 2015 | GP动力学模型MPC |
| **Neural Network MPC: A tutorial review** | Wu Z, Christofides PD | 2025 | NN-MPC全面教程 |
| **Generative Model Predictive Control in Manufacturing** | Lee, Stone, et al. | 2025 | 生成式ML+MPC制造应用 |
| **LSTM and GRU in MPC** | Ławryńczuk M, Zarzycki K | 2025 | RNN-MPC系统综述 |

## 数据驱动MPC

| 论文 | 作者 | 年 | 要点 |
|------|------|----|------|
| **Data-enabled predictive control (DeePC)** | Coulson J, Lygeros J, Dörfler F | 2019 | **DeePC**：基于Willems行为理论的纯数据驱动MPC |
| **Data-driven MPC: closed-loop guarantees** | Berberich J, Köhler J, Müller MA, Allgöwer F | 2020 | 数据驱动MPC闭环保证 |
| **Koopman-based MPC** | Korda M, Mezić I | 2018 | Koopman算子+线性MPC预测非线性系统 |
| **An overview of systems-theoretic guarantees in data-driven MPC** | Berberich J, Allgöwer F | 2025 | 数据驱动MPC最新综述 |
| **Efficient data-driven PC of nonlinear systems** | Zhang X, et al. | 2025 | Koopman+DeePC统一框架 |

## 重要教材与专著

| 教材 | 作者 | 年 | 出版商 | 特点 |
|------|------|----|--------|------|
| **Model Predictive Control: Theory and Design** | Rawlings JB, Mayne DQ, Diehl M | 2017 | Nob Hill | **MPC权威教材** |
| **Predictive Control with Constraints** | Maciejowski JM | 2002 | Prentice Hall | 约束MPC经典入门 |
| **Predictive Control for Linear and Hybrid Systems** | Borrelli F, Bemporad A, Morari M | 2017 | Cambridge | 线性/混合系统MPC |
| **Model Predictive Control (2nd ed.)** | Camacho EF, Bordons C | 2007 | Springer | 工业MPC视角 |
| **Nonlinear Model Predictive Control** | Grüne L, Pannek J | 2017 | Springer | NMPC理论专著 |

## 软件工具

| 工具 | 用途 | 特点 |
|------|------|------|
| **CasADi** | 非线性优化与最优控制 | 符号/自动微分，NMPC首选 |
| **ACADO Toolkit** | 最优控制代码生成 | 实时NMPC C代码生成 |
| **FORCES Pro** | 嵌入式MPC求解器 | 商业级实时求解 |
| **YALMIP** | MATLAB优化建模 | 多求解器接口 |
| **OSQP** | QP求解 | 高速二次规划求解器 |
| **qpOASES** | 在线QP | 在线参数QP |
| **Gurobi** | 商业优化器 | MILP/MIQP高效求解 |
| **do-mpc** | Python MPC工具包 | 基于CasADi的Python框架 |

## 应用论文

| 领域 | 代表性方法 | 典型场景 |
|------|----------|---------|
| **自动驾驶** | NMPC+Tube MPC | 路径跟踪、避障、车道保持 |
| **机器人** | NMPC+WBC | 全身运动控制、操作 |
| **化工过程** | 线性MPC+EMPC | 精馏塔、反应器优化 |
| **能源系统** | MPC+分布式MPC | 微电网、建筑能效 |
| **航空航天** | NMPC+鲁棒MPC | 无人机控制、卫星姿态 |
