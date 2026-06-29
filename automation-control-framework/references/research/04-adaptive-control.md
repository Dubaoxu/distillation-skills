# 自适应控制领域权威论文调研

> 调研日期：2026-05-19
> 涵盖范围：MRAC、自校正调节、自适应反步法、神经网络/模糊自适应控制、迭代学习控制、L1 自适应控制、极值搜索控制

---

## 综述论文 (Surveys)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **A Survey of Iterative Learning Control: A Learning-Based Method for High-Performance Tracking Control** | D. A. Bristow, M. Tharayil, A. G. Alleyne | 2006 | *IEEE Control Systems Magazine*, 26(3):96-114 | ~2,500+ | ILC 领域最广泛引用的综述，涵盖频域、提升系统、范数最优和2D设计范式，系统总结理论与实践 |
| 2 | **Iterative Learning Control: Brief Survey and Categorization** | H.-S. Ahn, Y. Q. Chen, K. L. Moore | 2007 | *IEEE Trans. Systems, Man, and Cybernetics — Part C*, 37(6):1099-1121 | ~1,800+ | 对 1998-2004 年 ILC 文献进行系统分类，涵盖鲁棒性、单调收敛和区间系统 |
| 3 | **L1 Adaptive Controller for Safety Critical Systems: Guaranteed Robustness with Fast Adaptation** | N. Hovakimyan, C. Cao, E. Kharisov, E. Xargay, I. M. Gregory | 2011 | *IEEE Control Systems Magazine*, 31(5):54-104 | ~800+ | L1 自适应控制的权威杂志综述，覆盖航空航天、无人机等安全关键系统应用 |
| 4 | **Recent Progress in Reinforcement Learning and Adaptive Dynamic Programming for Advanced Control Applications** | D. Wang, N. Gao, D. Liu, J. Li, F. L. Lewis | 2024 | *IEEE/CAA Journal of Automatica Sinica*, 11:18-36 | ~50+ (新) | ADP/RL 框架下自适应控制最新进展，涵盖事件触发、鲁棒镇定、无人系统等 |
| 5 | **Composite Adaptation and Learning for Robot Control: A Survey** | K. Guo, Y. Pan | 2023 | *Annual Reviews in Control*, 55 | ~50+ (新) | 首次系统综述机器人控制中的复合自适应与学习：回归滤波复合自适应、误差滤波复合自适应 |
| 6 | **A Survey of Modularized Backstepping Control Design Approaches to Nonlinear ODE Systems** | 多作者 | 2023 | *arXiv:2305.02066* | ~10+ (新) | 模块化反步法综述，涵盖 ISS 小增益、无源性、切换和自适应模块化设计 |
| 7 | **Advancements in Data-Driven Evolving Fuzzy and Neuro-Fuzzy Control: A Comprehensive Survey** | G. Andonovski, D. Leite, R.-E. Precup 等 | 2026 | *Applied Soft Computing*, 186:114058 | ~5+ (极新) | 数据驱动进化模糊/神经模糊控制全面综述，97 篇论文手动筛选，含 Lyapunov 稳定性分析 |
| 8 | **A Review of Unmanned Vehicle Control with Adaptive Dynamic Programming Implementations** | H. Liu, X. Yi, D. Liu, K. P. Valavanis | 2025 | *J. Intelligent & Robotic Systems*, 111(10) | ~5+ (极新) | ADP 最优控制在无人机/无人艇/无人车中的应用综述，含鲁棒 ADP、事件触发控制 |
| 9 | **Survey on ILC, Repetitive Control, and Run-to-Run Control** | Y. Wang, F. Gao, F. J. Doyle III | 2009 | *J. Process Control*, 19(10) | ~1,200+ | 统一 ILC、重复控制与批次控制的流程工业视角综述 |

---

## 奠基性经典 (Foundational Works)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Design of Model-Reference Adaptive Control Systems for Aircraft** | H. P. Whitaker, J. Yamron, A. Kezer | 1958 | MIT Instrumentation Lab, Report R-164 | N/A (奠基) | 提出 **MIT 规则**——第一个模型参考自适应控制律，基于梯度下降/灵敏度导数实时更新控制器参数，开创 MRAC 领域 |
| 2 | **On Self-Tuning Regulators** | K. J. Astrom, B. Wittenmark | 1973 | *Automatica*, 9:185-199 | ~5,000+ | 提出自校正调节器：结合递推最小二乘参数估计与最小方差控制律，开创自校正控制领域 |
| 3 | **Self-Tuning Controller** | D. W. Clarke, P. J. Gawthrop | 1975 | *Proc. IEE*, 122(9):929-934 | ~2,500+ | 提出**广义最小方差 (GMV)** 自校正器，引入对输入/输出/跟踪误差加权的控制代价，可处理非最小相位系统 |

---

## MRAC (模型参考自适应控制)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Stable Adaptive Schemes for System Identification and Control — Parts I & II** | K. S. Narendra, P. Kudva | 1974 | *IEEE Trans. Systems, Man, Cybernetics*, SMC-4:541-560 | ~800+ | 早期基础工作，建立稳定自适应辨识和控制方案，为后续 MRAC 理论奠定基础 |
| 2 | **Stable Model Reference Adaptive Control in the Presence of Bounded Disturbances** | G. Kreiselmeier, K. S. Narendra | 1982 | *IEEE Trans. Automatic Control*, AC-27:1169-1175 | ~600+ | 有界扰动下稳定 MRAC 的早期基础性工作，提出持续激励条件下全局有界性条件 |
| 3 | **Direct and Indirect Adaptive Control** | K. S. Narendra, L. S. Valavani | 1979 | *Automatica*, 15(6):653-664 | ~900+ | 正式区分**直接 MRAC**（直接调整控制器参数）与**间接 MRAC**（先辨识对象参数），成为标准分类 |
| 4 | **Robust Adaptive Control in the Presence of Bounded Disturbances** | K. S. Narendra, A. M. Annaswamy | 1986 | *IEEE Trans. Automatic Control*, 31(4):306-315 | ~500+ | 分析有界扰动下线性对象 MRAC，推导参考输入持续激励的充分条件以保证全局信号有界 |
| 5 | **A New Adaptive Law for Robust Adaptation without Persistent Excitation** | K. S. Narendra, A. M. Annaswamy | 1987 | *IEEE Trans. Automatic Control*, AC-32:134-145 | ~800+ | 提出无需持续激励的鲁棒自适应律——输出误差双重角色驱动参数更新，采用 σ-修正等鲁棒修正方案 |
| 6 | **Discrete-Time Model Reference Adaptive Control** | G. C. Goodwin, P. J. Ramadge, P. E. Caines | 1980 | *IEEE Trans. Automatic Control*, 25(3):449-456 | ~1,200+ | 离散时间 MRAC 的奠基性工作，提出基于随机逼近和 Martingale 收敛理论的全局收敛证明 |
| 7 | **L1-Adaptive Control: Stability, Robustness, and Interpretations** | P. A. Ioannou, A. M. Annaswamy, K. S. Narendra 等 | 2014 | *IEEE Trans. Automatic Control*, 59(11):3075-3080 | ~300+ | 分析 L1 自适应控制是否优于标准 MRAC，结论：插入 L1 滤波器可能恶化工况性能和鲁棒稳定裕度 |
| 8 | **Lyapunov Design of MRAC** | P. C. Parks | 1966 | *Electronics Letters*, 2(10):364-365 | ~700+ | 首次使用 **Lyapunov 稳定性理论**设计 MRAC，取代 MIT 规则的梯度方法，解决稳定性保证问题 |
| 9 | **Hyperstability Approach to MRAC** | I. D. Landau | 1979 | *Automatica*, 15(3):353-361 | ~800+ | 使用 **Popov 超稳定性理论**设计 MRAC 系统，为离散时间自适应控制提供严格稳定性证明框架 |

---

## 自校正调节 (Self-Tuning Regulators)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **On Self-Tuning Regulators** | K. J. Astrom, B. Wittenmark | 1973 | *Automatica*, 9:185-199 | ~5,000+ | 自校正调节器开山之作，最小二乘+最小方差控制 |
| 2 | **Self-Tuning Controller** | D. W. Clarke, P. J. Gawthrop | 1975 | *Proc. IEE*, 122(9):929-934 | ~2,500+ | GMV 自校正器——可处理非最小相位系统并扩展代价函数 |
| 3 | **Generalisation of the Self-Tuning Regulator** | D. W. Clarke, P. J. Gawthrop | 1975 | *Electronics Letters*, 11(2):40-41 | ~500+ | 自校正调节器推广的概要性短文，正式提出输入/输出/设定值联合最小化策略 |
| 4 | **Self-Tuning Control** (Survey) | D. W. Clarke, P. J. Gawthrop | 1979 | *Proc. IEE*, Pt. D, 126(6):633-640 | ~800+ | 自校正控制领域的权威综述：闭环特性分析、收敛概念、工程实现问题 |
| 5 | **Analysis of a Self-Tuning Regulator for Non-Minimum Phase Plants** | K. J. Astrom, B. Wittenmark | 1974 | *IFAC Symp. Stochastic Control*, Budapest | ~500+ | 揭示原始最小方差自校正器在非最小相位对象上的不稳定性问题 |
| 6 | **On the Stability and Convergence of a Self-Tuning Controller** | P. J. Gawthrop | 1980 | *Int. J. Control*, 31(5):973-998 | ~400+ | 自校正控制器严格的输入输出稳定性分析与依概率一收敛证明 |
| 7 | **Theory and Applications of Self-Tuning Regulators** | K. J. Astrom, U. Borisson, L. Ljung, B. Wittenmark | 1977 | *Automatica*, 13:457-476 | ~900+ | STR 理论与工业应用（矿石破碎、造纸等）的桥梁性综述 |
| 8 | **Pole-Zero Placement Self-Tuning Controller** | P. E. Wellstead, J. M. Edmunds, D. Prager, P. Zanker | 1979 | *Int. J. Control*, 30(1):1-26 | ~600+ | 提出**零极点配置自校正控制**，通过显式处理闭环零极点位置扩展 STR 适用范围 |
| 9 | **Generalized Predictive Control — Parts I & II** | D. W. Clarke, C. Mohtadi, P. S. Tuffs | 1987 | *Automatica*, 23(2):137-160 | ~5,000+ | GPC——将 GMV 推广到长预测时域，兼具自校正和预测控制的优点，在工业中广泛应用 |

---

## 自适应反步法 (Adaptive Backstepping)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Adaptive Nonlinear Control without Overparametrization** | M. Krstic, I. Kanellakopoulos, P. V. Kokotovic | 1992 | *Systems & Control Letters*, 19(3):177-185 | ~1,100+ | 提出 **tuning functions** 方法——用单一参数更新律取代多估计器，消除过参数化问题，成为自适应反步法的标准技术 |
| 2 | **Nonlinear and Adaptive Control Design** | M. Krstic, I. Kanellakopoulos, P. V. Kokotovic | 1995 | Wiley-Interscience (563 pp.) | ~4,500+ | 自适应反步法的权威教材，系统阐述 tuning functions 设计、模块化设计（无源标识器/交换标识器）、输出反馈等 |
| 3 | **Systematic Design of Adaptive Controllers for Feedback Linearizable Systems** | I. Kanellakopoulos, P. V. Kokotovic, A. S. Morse | 1991 | *IEEE Trans. Automatic Control*, 36(11):1241-1253 | ~1,500+ | 第一个正式的**自适应反步法**论文，提出参数严格反馈系统设计框架，但存在过参数化问题 |
| 4 | **Adaptive Backstepping Control of a Class of Uncertain Nonlinear Systems** | M. M. Polycarpou, P. A. Ioannou | 1996 | *IEEE Trans. Automatic Control*, 41(10):1490-1495 | ~600+ | 将自适应反步法扩展至含未知虚拟控制系数的系统，引入 Nussbaum 增益处理控制方向未知 |
| 5 | **Robust Adaptive Control of Nonlinear Systems** | R. A. Freeman, P. V. Kokotovic | 1996 | *Automatica*, 32(2):183-198 | ~500+ | 逆最优鲁棒自适应反步法设计，使系统同时具备最优性和鲁棒性 |
| 6 | **Adaptive Backstepping with Tuning Functions for Uncertain Systems** | M. Krstic, P. V. Kokotovic | 1995 | *IEEE Trans. Automatic Control*, 40(9):1563-1568 | ~400+ | tuning functions 方法的简明总结性期刊论文 |
| 7 | **Tuning Function Design for Nonlinear Adaptive Control Systems with Multiple Unknown Control Directions** | 多作者 | 2018 | *Automatica*, 89:259-265 | ~100+ | tuning functions 方法的现代扩展——处理**多个未知控制方向**，结合逻辑切换机制 |
| 8 | **Modular Approach to Adaptive Nonlinear Stabilization** | M. Krstic, P. V. Kokotovic | 1996 | *Automatica*, 32(4):485-493 | ~350+ | 模块化自适应反步法——将控制律设计 (ISS 反步) 和参数辨识解耦，允许灵活选择辨识器类型 |

---

## 神经网络自适应控制

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Neural Net Robot Controller with Guaranteed Tracking Performance** | F. L. Lewis, K. Liu, A. Yesildirek | 1995 | *IEEE Trans. Neural Networks*, 6(3):703-715 | ~860+ | 首次提出**滤波误差/无源性方法**用于 NN 机器人控制：修正 delta 规则+鲁棒信号保证有界跟踪与有界权值 |
| 2 | **Feedback Linearization Using Neural Networks** | A. Yesildirek, F. L. Lewis | 1995 | *Automatica*, 31(11):1659-1664 | ~530+ | SISO 连续时间系统：两个 NN 完成输出反馈线性化+鲁棒项，Lyapunov 证明 UUB，无需离线训练 |
| 3 | **Multilayer Neural-Net Robot Controller with Guaranteed Tracking Performance** | F. L. Lewis, A. Yesildirek, K. Liu | 1996 | *IEEE Trans. Neural Networks*, 7(2):388-399 | ~1,230+ | 前文的扩展版：多层 NN 结合鲁棒控制信号，提出**无源 NN、耗散 NN、鲁棒 NN**的概念 |
| 4 | **Neural Network Control of Robot Manipulators and Nonlinear Systems** | F. L. Lewis, S. Jagannathan, A. Yesildirek | 1998 | CRC Press (Taylor & Francis), 468 pp. | ~2,300+ | 该领域的权威教科书，统一连续/离散时间 NN 控制理论，涵盖柔性臂、力控制等 |
| 5 | **Multilayer Discrete-Time Neural-Net Controller with Guaranteed Performance** | S. Jagannathan, F. L. Lewis | 1996 | *IEEE Trans. Neural Networks*, 7(1):107-130 | ~170+ | 定义**离散时间 NN 控制框架**：修正 delta 规则、投影算法、多层 NN 持续激励条件 |
| 6 | **Gaussian Networks for Direct Adaptive Control** | R. M. Sanner, J.-J. E. Slotine | 1992 | *IEEE Trans. Neural Networks*, 3(6):837-863 | ~1,200+ | 首次在自适应控制中用**高斯径向基网络**进行函数逼近，结合滑模与 Lyapunov 稳定性 |
| 7 | **Stable Adaptive Neural Network Control** | M. M. Polycarpou | 1996 | *IEEE Trans. Systems, Man, Cybernetics*, 26(2):314-324 | ~400+ | 早期的稳定自适应 NN 控制：用 RBF 逼近非线性系统中的未知函数，Lyapunov 分析保证全局有界 |
| 8 | **Adaptive Neural Control of Uncertain Nonlinear Systems** | S. S. Ge, C. C. Hang, T. H. Lee, T. Zhang | 2002 | *Automatica*, 38(10):1631-1641 | ~600+ | 提出**自适应 NN 反步法**框架，将 NN 函数逼近集成到反步法设计中处理参数化不确定性 |
| 9 | **Adaptive Neural Control of Nonlinear Time-Delay Systems** | S. S. Ge, C. Wang | 2002 | *Automatica*, 38(8):1287-1295 | ~500+ | 扩展至含时滞的非线性系统：以 NN 逼近未知非线性泛函，Lyapunov-Krasovskii 泛函分析 |

---

## 模糊自适应控制

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Stable Adaptive Fuzzy Control of Nonlinear Systems** | L.-X. Wang | 1993 | *IEEE Trans. Fuzzy Systems*, 1(2):146-155 | ~1,500+ | **开创性论文**：首次将模糊系统与 Lyapunov 自适应控制理论结合，提出直接自适应模糊控制并证明全局稳定性与渐近跟踪 |
| 2 | **Adaptive Fuzzy Systems and Control: Design and Stability Analysis** | L.-X. Wang | 1994 | Prentice Hall (xvii+232 pp.) | ~2,600+ | 模糊自适应控制权威教材：间接/直接自适应模糊控制、输入输出线性化法、模糊辨识器和滤波器 |
| 3 | **A Supervisory Controller for Fuzzy Control Systems that Guarantees Stability** | L.-X. Wang | 1994 | *IEEE Trans. Automatic Control*, 39(9):1845-1847 | ~400+ | 提出**监督控制器**概念：在模糊系统可能越界时介入，保证全局稳定性 |
| 4 | **Stable Adaptive Fuzzy Controllers with Application to Inverted Pendulum Tracking** | L.-X. Wang | 1996 | *IEEE Trans. SMC — Part B*, 26(5):677-691 | ~500+ | 模糊自适应控制器的实验验证——倒立摆轨迹跟踪，展示理论与实际结合 |
| 5 | **Fuzzy Basis Functions, Universal Approximation, and Orthogonal Least-Squares Learning** | L.-X. Wang, J. M. Mendel | 1992 | *IEEE Trans. Neural Networks*, 3(5):807-814 | ~3,000+ | 证明**模糊基函数构成通用逼近器**，为模糊自适应控制提供理论基础 |
| 6 | **Stable Multi-Input Multi-Output Adaptive Fuzzy/Neural Control** | R. Ordonez, K. M. Passino | 1999 | *IEEE Trans. Fuzzy Systems*, 7(3):345-353 | ~350+ | 将 Wang 的 SISO 框架扩展到 **MIMO 非线性系统** |
| 7 | **Adaptive Fuzzy Control of a Class of MIMO Nonlinear Systems** | S. Labiod, M. S. Boucherit, T. M. Guerra | 2005 | *Fuzzy Sets and Systems*, 151:59-77 | ~400+ | MIMO 系统模糊自适应控制的系统化设计 |
| 8 | **Fuzzy Adaptive Sliding-Mode Control for MIMO Nonlinear Systems** | S. Tong, H.-X. Li | 2003 | *IEEE Trans. Fuzzy Systems*, 11(3):354-360 | ~600+ | 将模糊逼近与滑模控制结合用于 MIMO 系统自适应跟踪 |
| 9 | **Adaptive Fuzzy Backstepping Control of Pure-Feedback Nonlinear Systems** | S. Tong, Y. Li, S. Sui | 2011 | *Automatica*, 47(4):677-684 | ~600+ | 将模糊逼近与反步法集成处理纯反馈系统，结合指令滤波避免"计算膨胀" |
| 10 | **Observer-Based Adaptive Fuzzy Backstepping Control** | S. Tong, T. Wang, Y. Li | 2014 | *IEEE Trans. Fuzzy Systems*, 22(2):202-213 | ~500+ | 输出反馈模糊自适应反步法：结合状态观测器处理不可测状态 |

---

## 迭代学习控制 (ILC)

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Bettering Operation of Robots by Learning** | S. Arimoto, S. Kawamura, F. Miyazaki | 1984 | *J. Robotic Systems*, 1(2):123-140 | ~3,000+ | **ILC 开山之作**：提出用前次迭代误差信息改善重复任务跟踪性能，最初面向机器人操控 |
| 2 | **A Survey of Iterative Learning Control** | D. A. Bristow, M. Tharayil, A. G. Alleyne | 2006 | *IEEE Control Systems Magazine*, 26(3):96-114 | ~2,500+ | ILC 最权威综述 |
| 3 | **Iterative Learning Control: Brief Survey and Categorization** | H.-S. Ahn, Y. Q. Chen, K. L. Moore | 2007 | *IEEE Trans. SMC — Part C*, 37(6):1099-1121 | ~1,800+ | 系统分类综述 |
| 4 | **Iterative Learning Control: Robustness and Monotonic Convergence for Interval Systems** | H.-S. Ahn, K. L. Moore, Y. Q. Chen | 2007 | Springer | ~600+ | 鲁棒 ILC 专著：区间系统单调收敛的严格理论 |
| 5 | **Iterative Learning Control for Discrete-Time Systems with Exponential Rate of Convergence** | N. Amann, D. H. Owens, E. Rogers | 1996 | *IEE Proc. Control Theory & Applications*, 143(2):217-224 | ~600+ | 提出**范数最优 ILC (NO-ILC)** 框架，以优化指标最小化实现指数收敛率 |
| 6 | **Iterative Learning Control Using Optimal Feedback and Feedforward Actions** | N. Amann, D. H. Owens, E. Rogers | 1996 | *Int. J. Control*, 65(2):277-293 | ~500+ | 将前馈+反馈优化结构统一到 ILC 框架 |
| 7 | **Time and Frequency Domain Convergence Properties in Iterative Learning Control** | M. Norrlof, S. Gunnarsson | 2002 | *Int. J. Control*, 75(14):1114-1126 | ~350+ | 统一时域/频域 ILC 收敛性分析，Linkoping 学派代表工作 |
| 8 | **Iterative Learning Control for Uncertain Systems: Robust Monotonic Convergence Analysis** | J. van de Wijdeven, T. Donkers, O. Bosgra | 2009 | *Automatica*, 45(10):2383-2391 | ~300+ | 提出不确定性系统的**鲁棒单调收敛 (RMC)** 理论框架 |
| 9 | **Discrete-Time Inverse Model-Based Iterative Learning Control: Stability, Monotonicity and Robustness** | T. J. Harte, J. J. Hatonen, D. H. Owens | 2005 | *Int. J. Control*, 78(8):577-586 | ~200+ | 基于逆模型 ILC 的稳定性、单调性与鲁棒性关键分析 |
| 10 | **Iterative Learning Control: An Optimization Paradigm** | D. H. Owens | 2016 | Springer | ~300+ | Owens 学派 ILC 专著：以优化视角统一参数最优 ILC 与范数最优 ILC |
| 11 | **A Norm Optimal Approach to Time-Varying ILC with Application to a Multi-Axis Robotic Testbed** | K. L. Barton, A. G. Alleyne | 2011 | *IEEE Trans. Control Systems Technology*, 19(1):166-180 | ~250+ | 范数最优 ILC 在时变多轴机器人系统的工程实现 |
| 12 | **Model-Based Iterative Learning Control with a Quadratic Criterion for Time-Varying Linear Systems** | J. H. Lee, K. S. Lee, W. C. Kim | 2000 | *Automatica*, 36(5):641-657 | ~600+ | 将二次最优准则用于批量过程 ILC 设计 |
| 13 | **Linear and Nonlinear Iterative Learning Control** | J.-X. Xu, Y. Tan | 2003 | Springer | ~500+ | 覆盖线性和非线性 ILC 的专著，含非线性系统中的复合能量函数方法 |

---

## L1 自适应控制

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Design and Analysis of a Novel L1 Adaptive Control Architecture, Part I: Control Signal and Asymptotic Stability** | C. Cao, N. Hovakimyan | 2006 | *American Control Conference (ACC)*, Minneapolis, 3397-3402 | ~400+ | L1 自适应控制**首次提出**——引入低通滤波器到控制通道，从架构上解耦自适应与鲁棒性 |
| 2 | **Design and Analysis of a Novel L1 Adaptive Control Architecture, Part II: Guaranteed Transient Performance** | C. Cao, N. Hovakimyan | 2006 | *American Control Conference (ACC)*, Minneapolis, 3403-3408 | ~400+ | 完整体现 L1 框架的瞬态性能保证——自适应增益任意高但滤波器保证鲁棒性 |
| 3 | **Design and Analysis of a Novel L1 Adaptive Control Architecture with Guaranteed Transient Performance** | C. Cao, N. Hovakimyan | 2008 | *IEEE Trans. Automatic Control*, 53(2):586-591 | ~600+ | 第一部分期刊版：状态反馈 L1 控制，含严谨的 Lyapunov 证明 |
| 4 | **L1 Adaptive Output Feedback Controller for Systems of Unknown Dimension** | C. Cao, N. Hovakimyan | 2008 | *IEEE Trans. Automatic Control*, 53(3):815-821 | ~400+ | 扩展至输出反馈：含非严格正实系统、任意维未知对象 |
| 5 | **L1 Adaptive Control Theory: Guaranteed Robustness with Fast Adaptation** | N. Hovakimyan, C. Cao | 2010 | SIAM (mathematical monograph) | ~1,500+ | **L1 权威专著**：状态/输出反馈、时变参考、未匹配不确定性、时滞裕度 |
| 6 | **Stability Margins of L1 Adaptive Control Architecture** | C. Cao, N. Hovakimyan | 2010 | *IEEE Trans. Automatic Control*, 55(2):480-487 | ~350+ | 解析计算 L1 控制的**时滞裕度**——经典 MRAC 无法定量分析的属性 |
| 7 | **L1 Adaptive Controller for Systems with Unknown Time-Varying Parameters and Disturbances** | C. Cao, N. Hovakimyan | 2008 | *Int. J. Control*, 81(7):1147-1161 | ~300+ | 扩展至**时变**参数和扰动，包含非零初始化跟踪误差分析 |
| 8 | **L1 Adaptive Controller for a Class of Systems with Unknown Nonlinearities: Part I** | C. Cao, N. Hovakimyan | 2008 | *ACC*, Seattle, 4093-4098 | ~250+ | 扩展至**未知非线性**系统类，保持 L1 范数体现 |
| 9 | **L1 Adaptive Control for Nonlinear Systems in the Presence of Unmodeled Dynamics: Part II** | C. Cao, N. Hovakimyan | 2008 | *ACC*, Seattle, 4099-4104 | ~200+ | 处理**未建模动态**下的鲁棒 L1 控制 |
| 10 | **L1 Adaptive Control with Switched Reference Models: Application to Learn-to-Fly** | 多作者 | 2022 | *J. Guidance, Control, and Dynamics*, 45(1) | ~30+ | L1 控制在航空航天中的应用：切换参考模型实现 Learn-to-Fly 能力 |
| 11 | **L1 Adaptive Control for Safety-Critical Systems** | N. Hovakimyan, C. Cao 等 | 2011 | *IEEE Control Systems Magazine*, 31(5):54-104 | ~800+ | 安全关键系统的 L1 综合杂志综述 |

---

## 极值搜索控制

| # | 标题 | 作者 | 年份 | 出处 | 引用 | 核心贡献 |
|---|------|------|------|------|------|----------|
| 1 | **Stability of Extremum Seeking Feedback for General Nonlinear Dynamic Systems** | M. Krstic, H.-H. Wang | 2000 | *Automatica*, 36(4):595-601 | ~900+ | 首次为一般非线性系统的极值搜索控制提供严格的**平均化理论稳定性证明**，复兴 ESC 领域 |
| 2 | **Real-Time Optimization by Extremum-Seeking Control** | K. B. Ariyur, M. Krstic | 2003 | Wiley-Interscience (236 pp.) | ~1,260+ | **ESC 权威专著**：SISO/多参数/斜率搜索、离散时间分析、非线性/极限环分析，应用遍及 ABS、生物反应器、飞行控制 |
| 3 | **Extremum Seeking from 1922 to 2010** | Y. Tan, W. H. Moase, C. Manzie, D. Nesic, I. M. Y. Mareels | 2010 | *Int. J. Robust & Nonlinear Control*, 20(3):213-237 | ~500+ | **历史综述**：从 Leblanc 1922 年至今 ESC 百年发展，统一多种方法的数学框架 |
| 4 | **Slope Seeking: A Generalization of Extremum Seeking** | K. B. Ariyur, M. Krstic | 2004 | *Int. J. Adaptive Control & Signal Processing*, 18(3):195-217 | ~150+ | 将 ESC 从极值点搜索推广到**任意参考斜率**的跟踪 |
| 5 | **Extremum Seeking Control for Discrete-Time Systems** | J.-Y. Choi, M. Krstic, K. B. Ariyur, J. S. Lee | 2002 | *IEEE Trans. Automatic Control*, 47(2):318-323 | ~200+ | 离散时间 ESC 的理论奠基 |
| 6 | **Extremum Seeking for Infinite-Dimensional Systems** | T. R. Oliveira, M. Krstic | 2023 | *Annual Reviews in Control*, 55 | ~30+ | ESC 扩展至**无穷维/分布参数系统 (PDE)** 的最新综述 |
| 7 | **Lie Bracket Approximation-Based Extremum Seeking** | H.-B. Durr, M. Krstic, C. Ebenbauer 等 | 2013 | *IEEE Trans. Automatic Control*, 58(11):2775-2787 | ~200+ | 使用 **Lie 括号近似**对 ESC 进行严密分析，提供新的收敛性视角 |
| 8 | **Nash Equilibrium Seeking via Extremum Seeking** | P. Frihauf, M. Krstic, T. Basar | 2012 | *Automatica*, 48(5):732-745 | ~250+ | 将 ESC 用于**多智能体博弈 Nash 均衡**的在线搜索 |

---

## 重要教材与专著

| # | 标题 | 作者 | 年份 | 出版社 | 引用 | 特点与覆盖范围 |
|---|------|------|------|------|------|---------------|
| 1 | **Stable Adaptive Systems** | K. S. Narendra, A. M. Annaswamy | 1989 / Dover 2005 | Prentice Hall / Dover, 494 pp. | ~2,100-2,960 | 最经典的稳定性理论教材——误差模型、持续激励、鲁棒 MRAC、多变量系统、5 个应用案例 |
| 2 | **Robust Adaptive Control** | P. A. Ioannou, J. Sun | 1996 / Dover 2012 | Prentice Hall / Dover, ~825 pp. | ~7,200+ | 鲁棒自适应控制**最全面**的教材——参数模型、在线估计、MRAC、自适应极点配置、MATLAB 代码 |
| 3 | **Adaptive Control** (2nd Edition) | K. J. Astrom, B. Wittenmark | 1995 / Dover 2008 | Addison-Wesley / Dover | ~6,000+ | 确定性+随机自适应控制——STR、MRAS、MV、LQ STR、鲁棒性，兼顾连续和高散时间 |
| 4 | **Nonlinear and Adaptive Control Design** | M. Krstic, I. Kanellakopoulos, P. V. Kokotovic | 1995 | Wiley-Interscience, 563 pp. | ~4,500+ | 自适应反步法权威教材——tuning functions、模块化设计（无源/交换标识器）、输出反馈 |
| 5 | **Applied Nonlinear Control** | J.-J. E. Slotine, W. Li | 1991 | Prentice Hall | ~20,000+ | 非线性控制入门经典教材——第 8 章自适应控制深入浅出，Lyapunov 几何直观法，机器人领域最受欢迎 |
| 6 | **Robust and Adaptive Control: With Aerospace Applications** (2nd Edition) | E. Lavretsky, K. A. Wise | 2013 / 2024 | Springer, 710 pp. | ~1,500+ | 面向航空航天的现代状态空间 MRAC 教材——LQR/H-inf/LQG-LTR/MRAC/鲁棒 MRAC/近似自适应控制，含大量 MATLAB 案例 |
| 7 | **L1 Adaptive Control Theory: Guaranteed Robustness with Fast Adaptation** | N. Hovakimyan, C. Cao | 2010 | SIAM | ~1,500+ | L1 控制唯一权威专著——全面含状态/输出反馈、时变参考、未匹配不确定性、时滞裕度 |
| 8 | **Neural Network Control of Robot Manipulators and Nonlinear Systems** | F. L. Lewis, S. Jagannathan, A. Yesildirek | 1998 | CRC Press, 468 pp. | ~2,300+ | NN 自适应控制权威教材——连续/离散时间统一框架，涵盖柔性臂、力控制 |
| 9 | **Adaptive Fuzzy Systems and Control: Design and Stability Analysis** | L.-X. Wang | 1994 | Prentice Hall, 232 pp. | ~2,600+ | 模糊自适应控制权威教材——间接/直接自适应模糊、输入输出线性化法、辨识与滤波 |
| 10 | **Real-Time Optimization by Extremum-Seeking Control** | K. B. Ariyur, M. Krstic | 2003 | Wiley-Interscience, 236 pp. | ~1,260+ | ESC 唯一权威专著 |
| 11 | **Adaptive Control Tutorial** | P. A. Ioannou, B. Fidan | 2006 | SIAM | ~1,200+ | Ioannou 的教学版——Matlab/Simulink 配套，适合入门学习 |
| 12 | **Iterative Learning Control: An Optimization Paradigm** | D. H. Owens | 2016 | Springer | ~300+ | ILC 以优化视角系统化呈现的专著 |
| 13 | **Linear and Nonlinear Iterative Learning Control** | J.-X. Xu, Y. Tan | 2003 | Springer | ~500+ | 线性和非线性 ILC 的专著——含复合能量函数 (CEF) 方法 |
| 14 | **Adaptive Control** (2nd Edition) | G. Tao | 2003 | Wiley | ~1,500+ | 全面的自适应控制教材——涵盖执行器故障、非线性、反冲、时滞等复杂情况 |
| 15 | **Adaptive Control: Stability, Convergence, and Robustness** | S. Sastry, M. Bodson | 1989 / Dover 2010 | Prentice Hall / Dover | ~2,500+ | 经典严谨教材——MRAC 确定性/随机系统、鲁棒性分析 |
| 16 | **Adaptive Control of Systems with Actuator and Sensor Nonlinearities** | G. Tao, P. V. Kokotovic | 1996 | Wiley | ~1,000+ | 执行器和传感器非线性的自适应补偿专著 |
| 17 | **Model-Reference Adaptive Control: A Primer** | N. T. Nguyen | 2018 | Springer | ~300+ | 现代 MRAC 入门教材，面向航空航天应用和工程实践 |

---

## 重要期刊与会议

### 核心期刊
- **Automatica** (IFAC)
- **IEEE Transactions on Automatic Control**
- **International Journal of Adaptive Control and Signal Processing**
- **Systems & Control Letters**
- **IEEE Transactions on Neural Networks and Learning Systems**
- **IEEE Transactions on Fuzzy Systems**
- **International Journal of Control**
- **IEEE Control Systems Magazine**

### 核心会议
- **IEEE Conference on Decision and Control (CDC)**
- **American Control Conference (ACC)**
- **IFAC World Congress**
- **IFAC Symposium on System Identification (SYSID)**
- **IFAC Workshop on Adaptive and Learning Control Systems (ALCOS)**

---

*本调研基于 2026 年 5 月的多轮网络学术搜索，引用量数据来自 Semantic Scholar / Google Scholar / zbMATH 的近似值，实际引用可能有所偏差。*
