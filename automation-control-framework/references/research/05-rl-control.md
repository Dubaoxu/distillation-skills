# 强化学习控制领域权威论文调研

> 调研日期：2026-05-19
> 覆盖范围：1980s--2025，涵盖模型无关/模型基/安全/离线/Sim-to-Real/MPC融合/传统控制等子领域

---

## 综述论文 (Surveys)

1. **Reinforcement Learning: An Introduction (2nd Edition)** | Richard S. Sutton, Andrew G. Barto | 2018 | MIT Press | ~67,905 citations | 强化学习领域公认的"圣经"级教材，系统覆盖MDP、DP、MC、TD、函数逼近、策略梯度等所有基础理论。Chapter 13 给出策略梯度定理的完整证明。

2. **Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems** | Sergey Levine, Aviral Kumar, George Tucker, Justin Fu | 2020 | arXiv:2005.01643 | ~1,500+ citations | 离线RL领域最权威的教程/综述，提出了分布偏移(distributional shift)核心问题，建立策略约束、价值悲观、基于模型三大方法的统一框架。

3. **Deep Reinforcement Learning for Robotics: A Survey of Real-World Successes** | Chen Tang et al. (Peter Stone group) | 2024 | Annual Review of Control, Robotics, and Autonomous Systems / AAAI 2025 | 综述深度学习RL在真实机器人中的成功应用，涵盖操作、导航、运动等任务。

4. **A Survey on Model-Based Reinforcement Learning** | Fan-Ming Luo, Tian Xu, Hang Lai, Xiong-Hui Chen, Weinan Zhang, Yang Yu | 2024 | Science China Information Sciences, Vol. 67, 121101 | 全面综述深度MBRL，涵盖模型学习、模型利用、策略训练三方面，以及离线RL、目标条件RL、多智能体RL、元RL中的应用。

5. **A Survey on Offline Reinforcement Learning: Taxonomy, Review, and Open Problems** | Rafael Figueiredo Prudencio, Marcos R.O.A. Maximo, Esther Luna Colombini | 2023 | IEEE TNNLS (arXiv:2203.01387) | 提供统一的离线RL分类法，涵盖D4RL、RL Unplugged、NeoRL等基准，总结各类方法在不同数据集属性上的表现。

6. **A Review of Safe Reinforcement Learning: Methods, Theories, and Applications** | Shangding Gu, Long Yang et al. | 2022 | arXiv:2205.10330 | 慕尼黑工大、同济等联合综述，系统覆盖安全RL方法、理论和应用，含约束MDP、屏障函数、安全层等。

7. **Reinforcement Learning in Process Industries: Review and Perspective** | O. Dogru, J. Xie et al. (Biao Huang group) | 2024 | IEEE/CAA Journal of Automatica Sinica, Vol. 11, No. 2 | 涵盖全过程控制层次（PID到高层规划）的RL应用，讨论MPC-RL的关系，覆盖DDPG/TD3/PPO/SAC等算法。

8. **Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey** | Wenshuai Zhao, Jorge Pena Queralta, Tomi Westerlund | 2020 | IEEE SSCI 2020 (arXiv:2009.13303) | 将Sim-to-Real方法分为五大类：域随机化、域适应、模仿学习、元学习、知识蒸馏。

9. **A Survey of Constraint Formulations in Safe Reinforcement Learning** | Various | 2024 | IJCAI 2024 (arXiv:2402.02025) | 全面综述安全RL中的约束公式化方法。

10. **A Survey on Deep Reinforcement Learning Architectures, Applications and Emerging Trends** | Various | 2024 | IET Communications | 覆盖深度RL架构、应用和新兴趋势的综述。

11. **High-Accuracy Model-Based Reinforcement Learning, a Survey** | Various | 2023 | Artificial Intelligence Review, 56(9): 9541-9573 | 聚焦高维问题中实现高模型精度的方法，涵盖概率推断、MPC、潜空间模型、端到端学习与规划。

12. **A Survey on Offline Model-Based Reinforcement Learning** | Haoyang He | 2023 | arXiv:2305.03360 | 专注离线模型基RL，覆盖MOPO、MoREL、COMBO等方法。

13. **A Comprehensive Review of AI and ML in Control Theory** | Various | 2024 | Applied and Computational Engineering | 综述AI/ML与控制理论的融合：PID、LQR、RL、深度学习、模糊逻辑等。

14. **Exploring Reinforcement Learning in Process Control: A Comprehensive Survey** | N. Rajasekhar, T.K. Radhakrishnan, N. Samsudeen | 2025 | International Journal of Systems Science, 56(14): 3528-3557 | 系统覆盖从经典RL到深度RL在化工、生物化工、能源、废水、油气等行业的过程控制应用。

---

## 奠基性经典 (Foundational Works)

1. **Human-level Control through Deep Reinforcement Learning (DQN)** | Volodymyr Mnih, Koray Kavukcuoglu, David Silver et al. (DeepMind) | 2015 | Nature, Vol. 518, pp. 529-533 | ~35,000+ citations | 首次成功将深度卷积网络与Q-learning结合，在49款Atari游戏上实现人类水平控制。引入Experience Replay和Target Network两大关键技术，引爆深度强化学习革命。

2. **Playing Atari with Deep Reinforcement Learning** | Volodymyr Mnih et al. (DeepMind) | 2013 | NeurIPS Workshop | 首次提出DQN，是2015年Nature论文的预印版。

3. **Policy Gradient Methods for Reinforcement Learning with Function Approximation** | Richard S. Sutton, David McAllester, Satinder Singh, Yishay Mansour | 1999 | NeurIPS | ~7,770 citations | 首次证明策略梯度定理，为所有Actor-Critic方法奠定理论基础。

4. **Deterministic Policy Gradient Algorithms** | David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, Martin Riedmiller | 2014 | ICML | ~4,000+ citations | 提出确定性策略梯度(DPG)定理，证明了确定性策略梯度是随机策略梯度在方差趋于零时的极限，是DDPG/TD3的理论基础。

5. **Asynchronous Methods for Deep Reinforcement Learning (A3C)** | Volodymyr Mnih et al. (DeepMind) | 2016 | ICML | ~8,000+ citations | 提出A3C框架，使用异步并行actor-learners替代经验回放，在Atari和连续控制上均表现优异。

6. **Mastering the Game of Go with Deep Neural Networks and Tree Search (AlphaGo)** | David Silver et al. (DeepMind) | 2016 | Nature, Vol. 529, pp. 484-489 | ~15,000+ citations | 结合深度RL和蒙特卡洛树搜索击败人类围棋冠军，证明RL在复杂推理任务中的可行性。

7. **Continuous Control with Deep Reinforcement Learning (DDPG)** | Timothy P. Lillicrap, Jonathan J. Hunt et al. | 2015/2016 | ICLR 2016 (arXiv:1509.02971) | ~10,000+ citations | 将DPG扩展到深度网络，使用经验回放和目标网络，实现高维连续动作空间的端到端控制。引入Ornstein-Uhlenbeck过程作探索噪声。

---

## 无模型深度RL (Model-Free Deep RL)

1. **Trust Region Policy Optimization (TRPO)** | John Schulman, Sergey Levine, Philipp Moritz, Michael Jordan, Pieter Abbeel | 2015 | ICML | ~6,000+ citations | 利用KL散度约束策略更新在信任域内，保证单调改进。使用二阶方法（Fisher信息矩阵/共轭梯度），样本效率高但计算昂贵。

2. **Proximal Policy Optimization (PPO)** | John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, Oleg Klimov | 2017 | arXiv:1707.06347 | ~15,000+ citations | 提出Clipped Surrogate Objective作为TRPO的一阶简化替代方案，通过剪切概率比限制策略更新幅度。成为业界默认的on-policy算法，在OpenAI Five、ChatGPT RLHF等大规模系统中广泛使用。

3. **Soft Actor-Critic (SAC)** | Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, Sergey Levine | 2018 | ICML (arXiv:1801.01290) | ~7,000+ citations | 最大熵RL框架，同时最大化期望回报和策略熵以鼓励探索。使用孪生Q网络和自动温度调节(2019版)，在MuJoCo等连续控制基准上达到SOTA。

4. **Addressing Function Approximation Error in Actor-Critic Methods (TD3)** | Scott Fujimoto, Herke van Hoof, David Meger | 2018 | ICML (arXiv:1802.09477) | ~5,000+ citations | 针对DDPG的过估计偏差提出三项改进：Clipped Double Q-learning、延迟策略更新、目标策略平滑正则化。在MuJoCo基准上显著优于DDPG。

5. **High-Dimensional Continuous Control Using Generalized Advantage Estimation (GAE)** | John Schulman, Philipp Moritz, Sergey Levine, Michael Jordan, Pieter Abbeel | 2016 | ICLR | ~4,000+ citations | 提出GAE方法，通过TD(λ)风格的指数加权在偏差和方差之间权衡，成为策略梯度方法中优势函数估计的标准方法。

6. **Deep Reinforcement Learning that Matters** | Peter Henderson, Riashat Islam, Philip Bachman, Joelle Pineau, Doina Precup, David Meger | 2018 | AAAI | 挑战深度RL的可复现性，揭示了随机种子、超参数、代码实现差异对结果的巨大影响，推动了更严谨的实验规范。

7. **Rainbow: Combining Improvements in Deep Reinforcement Learning** | Matteo Hessel et al. (DeepMind) | 2018 | AAAI | ~3,000+ citations | 将DQN的六项扩展（Double DQN、Prioritized Replay、Dueling、Multi-step、Distributional RL、Noisy Nets）组合，在Atari上取得SOTA。

---

## 基于模型的RL (Model-Based RL)

1. **PILCO: A Model-Based and Data-Efficient Approach to Policy Search** | Marc Peter Deisenroth, Carl Edward Rasmussen | 2011 | ICML | ~1,800+ citations | 使用高斯过程学习概率动力学模型，将模型不确定性显式纳入长期规划，通过解析梯度进行策略改进。在Cart-Pole等任务上仅需极少试次即可学习，是数据高效MBRL的里程碑。

2. **Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models (PETS)** | Kurtland Chua, Roberto Calandra, Rowan McAllister, Sergey Levine | 2018 | NeurIPS (Spotlight) | ~763 citations | 将概率集成(Probabilistic Ensemble)深度网络动力学模型与轨迹采样(TS)不确定性传播结合，是首个使MBRL渐近性能匹配model-free方法的深度方法。在Half-Cheetah上样本量仅为SAC的1/8。

3. **When to Trust Your Model: Model-Based Policy Optimization (MBPO)** | Michael Janner, Justin Fu, Marvin Zhang, Sergey Levine | 2019 | NeurIPS | ~1,200+ citations | 理论分析模型使用对策略优化的影响，提出Branched Rollout：从真实数据分支的短模型rollouts。在模型利用与偏差之间实现最优权衡，匹配SAC渐近性能的同时大幅提升样本效率。

4. **Dream to Control: Learning Behaviors by Latent Imagination (Dreamer)** | Danijar Hafner, Timothy Lillicrap, Jimmy Ba, Mohammad Norouzi | 2019/2020 | ICLR 2020 (arXiv:1912.01603) | ~1,500+ citations | 使用RSSM学习紧凑潜动力学模型，在潜空间中通过潜想象(learning behaviors by latent imagination)进行Actor-Critic学习，利用反向传播值梯度高效优化策略。在20个视觉控制任务上全面超越已有方法。

5. **Mastering Atari with Discrete World Models (DreamerV2)** | Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, Jimmy Ba | 2021 | ICLR 2021 | ~800+ citations | 在Dreamer基础上引入离散潜变量和Straight-Through梯度，首次使世界模型方法在Atari上达到人类水平。

6. **Mastering Diverse Domains through World Models (DreamerV3)** | Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, Timothy Lillicrap | 2023 | arXiv:2301.04104 | ~500+ citations | DreamerV3用固定超参数在150+任务（Atari、DM Control、Minecraft、3D第一人称）上表现优异，是首个无需调参即可跨域工作的通用RL算法。

7. **Model-Based Value Expansion for Efficient Model-Free RL (MVE)** | Vladimir Feinberg et al. | 2019 | ICLR | 利用学习到的动力学模型进行短视界"价值扩展"以改进Q值目标，融合model-based和model-free优势。

---

## 安全强化学习 (Safe RL)

1. **Constrained Policy Optimization (CPO)** | Joshua Achiam, David Held, Aviv Tamar, Pieter Abbeel | 2017 | ICML (arXiv:1705.10528) | ~800+ citations | 第一个具有每次迭代逼近约束满足保证的通用约束RL策略搜索算法。将TRPO扩展到CMDP，使用共轭梯度和回溯线搜索在策略空间求解约束优化。

2. **Benchmarking Safe Exploration in Deep Reinforcement Learning** | Joshua Achiam, Dario Amodei et al. (OpenAI) | 2019 | OpenAI Technical Report | 提出Safety-Gym基准套件，系统比较多种安全RL方法在安全探索中的表现。

3. **Responsive Safety in Reinforcement Learning by PID Lagrangian Methods** | Adam Stooke, Joshua Achiam, Pieter Abbeel | 2020 | ICML (arXiv:2007.03964) | 将PID控制思想引入拉格朗日乘子更新，提出PID Lagrangian方法，使约束RL对奖励和成本尺度变化具有不变性，响应更灵敏。

4. **Safe Reinforcement Learning using Robust MPC** | Mario Zanon, Sebastien Gros | 2021 | IEEE Transactions on Automatic Control, 66(8) | 里程碑级安全工作，展示了鲁棒MPC如何作为RL的安全过滤器(Safety Filter)，通过对RL参数更新的约束提供结构化的安全证书。

5. **Learning for MPC with Stability and Safety Guarantees** | Sebastien Gros, Mario Zanon | 2022 | Automatica, 146 | 解决通过参数更新确保持续安全和稳定性的缺口，定义了RL在线调参下安全参数转换和递归可行的条件。

6. **First Order Constrained Optimization in Policy Space (FOCOPS)** | Yiming Zhang, Quan Vuong, Keith Ross | 2020 | NeurIPS | 提出一阶替代CPO的方法，避免共轭梯度，使用对偶梯度下降求解约束策略优化。

7. **Safe Exploration in Continuous Action Spaces** | Gal Dalal, Krishnamurthy Dvijotham, Matej Vecerik, Todd Hester, Cosmin Paduraru, Yuval Tassa | 2018 | arXiv:1801.08757 | 提出Safety Layer方法，通过数学规划将RL动作投影到安全动作空间。在训练过程中学习线性安全约束模型，在执行时求解QP实现安全过滤。

8. **Control Barrier Functions: Theory and Applications** | Aaron D. Ames, Xiangru Xu, Jessy W. Grizzle, Paulo Tabuada | 2017 | Automatica | CBF的奠基性论文，通过QP求解最小干预安全过滤：min ||u - u_nom|| s.t. CBF约束。成为安全关键控制系统的标准工具。

9. **Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark** | Jiaming Ji, Borong Zhang et al. | 2023 | NeurIPS | Safety-Gym的升级统一基准，提供更丰富的安全RL评估环境。

10. **Learning Predictive Safety Filter via Decomposition of Robust Invariant Set** | Zuxun Li, Bin Hu, Yiming Zhao, Xianglong Liu | 2023 | arXiv:2311.06769 | 将鲁棒不变集分解为目标集+可达回避集，使用对抗Actor-Critic和SOCP在线验证构建预测性安全过滤器，复杂度低于RMPC。

---

## RL + MPC 融合

1. **Learning-Based Model Predictive Control: Toward Safe Learning in Control** | Lukas Hewing, Kim P. Wabersich, Marcel Menner, Melanie N. Zeilinger | 2020 | Annual Review of Control, Robotics, and Autonomous Systems, 3(1) | 综合综述基于学习的MPC方法，聚焦学习过程中的安全性，覆盖安全滤波器和参数学习两大范式。

2. **Data-Driven Economic NMPC using Reinforcement Learning** | Sebastien Gros, Mario Zanon | 2020 | IEEE Transactions on Automatic Control, 65(2) | 为基于RL的MPC成本函数和模型调优提供坚实理论基础，直接改善闭环性能。

3. **Fusion of Machine Learning and MPC under Uncertainty** | Ali Mesbah, Kim P. Wabersich, Angela Schoellig, Melanie Zeilinger et al. | 2022 | ACC 2022 | 展望性论文，讨论ML与MPC在不确定性下的融合路径。

4. **Safety Reinforced Model Predictive Control (SRMPC)** | Johannes Fischer, Maximilian Steiner et al. | 2023 | IEEE ITSC 2023 | 集成约束RL和MPC用于自动驾驶运动规划，使用手工设计的能量函数安全指数作为约束目标。

5. **A Safe RL-driven Weights-varying MPC for Autonomous Vehicle Motion Control** | Zarrouki, Spanakakis, Betz | 2024 | IEEE IV 2024 | 两阶段优化：BO预计算Pareto最优MPC权重集（安全关键），RL根据上下文离散选择权重，未训练的智能体已具有Pareto最优性和安全性。

6. **Safe and Stable Closed-Loop Learning for Neural-Network-Supported MPC** | Hirt, Pfefferkorn, Findeisen | 2024 | arXiv:2409.10171 | 使用贝叶斯优化从闭环数据调节神经网络参数化的MPC阶段成本，将稳定性约束嵌入BO过程。

7. **Learning Safety in Model-Based RL using MPC and Gaussian Processes** | Airaldi, De Schutter, Dabiri | 2023 | IFAC World Congress 2023 | 使用GP回归估计MPC参数上的概率安全约束，在RL更新中强制执行，无需限制性模型假设。

8. **Cautious Bayesian MPC: Regret Analysis and Bounds on Unsafe Learning Episodes** | Wabersich, Zeilinger | 2022 | IEEE TAC | 为贝叶斯MPC+RL提供遗憾分析和不安全学习片段的上界估计。

9. **Approximate Robust NMPC using Reinforcement Learning** | Esfahani, Kordabad, Gros | 2021 | ECC 2021 | 使用RL近似鲁棒NMPC同时保持安全性。

---

## RL + 传统控制

1. **Control-Informed Reinforcement Learning (CIRL)** | Bloor et al. / Tsay & del Rio Chanona | 2025 | Industrial & Engineering Chemistry Research, Vol. 64 | 将PID控制结构直接嵌入深度RL策略架构，神经网络学习自适应PID增益调度。在CSTR上显著优于纯RL和PID，且样本量更少。

2. **Globally Optimal Policy Gradient Algorithms for RL with PID Control Policies** | Various | 2024 | NeurIPS 2024 | 首次为PID参数化策略的策略梯度方法提供收敛性和全局最优性的理论保证，证明梯度支配性质。

3. **Reinforcement Learning-Driven PID Controller Tuning for Mass-Spring Systems** | Demircioglu, Bakir | 2025 | Engineering Applications of AI, Vol. 162 | 系统超参数分析，对比经典PID整定器和RL调参，发现经典方法在线性系统上瞬态更优但RL对非线性/不确定系统有优势。

4. **Wind Turbine Pitch RL Control Improved by PID Regulator** | Sierra-Garcia, Santos, Pandit | 2022 | Engineering Applications of AI, Vol. 111 | 混合RL+PID方法：PID在训练初期辅助RL，收敛速度提升约37%，输出功率误差减少约41%。

5. **Design and Comparison of RL-Based Time-Varying PID Controllers with Gain-Scheduled Actions** | Various | 2021 | Machines, Vol. 9 | 基于n-armed bandit的时变PID增益调度方法，在压电驱动平台上验证。

6. **Actor-Critic Model Predictive Control** | Angel Romero, Shuran Song, Davide Scaramuzza | 2024 | ICRA 2024 (arXiv:2306.09852) | 将可微MPC嵌入Actor-Critic RL框架，MPC处理短期优化，Critic处理长期预测，在四旋翼上仿真和真实验证。

7. **A Review on RL: Introduction and Applications in Industrial Process Control** | R. Nian, J. Liu, B. Huang | 2020 | Computers & Chemical Engineering, Vol. 139, 106886 | 桥接RL与工业过程控制的奠基性综述之一。

8. **Reinforcement Learning for Batch Process Control: Review and Perspectives** | H. Yoo, H.-E. Byun, D. Han, J.H. Lee | 2021 | Annual Reviews in Control, Vol. 52, pp. 108-119 | 专注批处理过程的RL应用综述。

---

## 离线强化学习 (Offline RL)

1. **Batch-Constrained Q-Learning (BCQ)** | Scott Fujimoto, David Meger, Doina Precup | 2019 | ICML 2019 | ~1,200+ citations | 第一个主要的离线RL方法：将动作空间限制在行为策略的支撑集内以避免分布偏移。使用VAE生成模型近似行为策略动作分布。

2. **Conservative Q-Learning (CQL)** | Aviral Kumar, Aurick Zhou, George Tucker, Sergey Levine | 2020 | NeurIPS 2020 (arXiv:2006.04779) | ~2,108 citations | 学习保守Q函数，对OOD动作的Q值施加惩罚（悲观方法）。在复杂/多模态数据集上取得2-5倍于先前方法的回报，成为离线RL最广泛引用的论文之一。

3. **Offline Reinforcement Learning with Implicit Q-Learning (IQL)** | Ilya Kostrikov, Ashvin Nair, Sergey Levine | 2021 | ICLR 2022 (arXiv:2110.06169) | ~407 citations | 从不评估数据集外的动作（in-sample Q-learning），通过期望回归(expectile regression)隐式逼近策略改进，避免查询任何OOD动作。在D4RL上达到SOTA，计算效率高。

4. **MOPO: Model-Based Offline Policy Optimization** | Tianhe Yu, Garrett Thomas, Lantao Yu, Stefano Ermon, James Zou, Sergey Levine, Chelsea Finn, Tengyu Ma | 2020 | NeurIPS 2020 | 在模型基框架下使用不确定性惩罚实现离线RL，基于动力学模型的不确定性量化构建悲观MDP。

5. **A Minimalist Approach to Offline Reinforcement Learning (TD3+BC)** | Scott Fujimoto, Shixiang Shane Gu | 2021 | NeurIPS 2021 | 惊人简单：仅在TD3上添加行为克隆(BC)正则化项即可匹配SOTA离线RL方法。

6. **Decision Transformer: Reinforcement Learning via Sequence Modeling** | Lili Chen et al. | 2021 | NeurIPS 2021 | ~1,500+ citations | 将RL重新定义为条件序列建模问题，使用GPT风格的Transformer自回归预测动作。开创了基于序列建模的离线RL新范式。

7. **Offline Q-learning on Diverse Multi-Task Data Both Scales and Generalizes** | Aviral Kumar, Rishabh Agarwal et al. | 2023 | ICLR 2023 | 证明在Atari多游戏数据上扩展CQL可实现幂律缩放和强微调迁移，将离线RL定位为通用预训练骨架。

8. **Cal-QL: Calibrated Offline RL Pre-Training for Efficient Online Fine-Tuning** | Mitsuhiko Nakamoto et al. | 2023 | NeurIPS 2023 | 提出校准保守Q函数概念：对当前策略价值下界约束，同时对次优参考策略上界约束，支持高效在线微调。

9. **Q-Transformer: Scalable Offline RL via Autoregressive Q-Functions** | Yevgen Chebotar et al. (Google/UC Berkeley) | 2023 | arXiv:2309.10150 | 使用自回归Transformer对Q函数进行逐维度离散化，将离线RL扩展到真实机器人操作。

10. **When Should We Prefer Offline RL Over Behavioral Cloning?** | Aviral Kumar, Joey Hong, Anikait Singh, Sergey Levine | 2022 | arXiv:2204.05618 | 系统刻画了在何种环境属性下离线RL显著优于BC（稀疏奖励、噪声数据等）。

11. **Is Value Learning Really the Main Bottleneck in Offline RL?** | Seohong Park, Kevin Frans, Sergey Levine, Aviral Kumar | 2024 | NeurIPS 2024 (arXiv:2406.09329) | 系统实证研究表明策略提取和策略泛化（而非价值函数质量）是离线RL的主要瓶颈。

12. **Pre-Training for Robots: Offline RL Enables Learning New Tasks in a Handful of Trials** | Aviral Kumar et al. | 2023 | RSS 2023 | 证明在多样化机器人数据上的离线RL预训练能够在新的操作任务上实现快速少次在线适应。

13. **D4RL: Datasets for Deep Data-Driven Reinforcement Learning** | Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine | 2020 | NeurIPS 2020 Datasets | 离线RL的标准基准数据集套件，包含MuJoCo、Adroit、AntMaze等任务的多质量数据集。

---

## Sim-to-Real 迁移

1. **Sim-to-Real Transfer of Robotic Control with Dynamics Randomization** | Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, Pieter Abbeel (OpenAI) | 2018 | CoRL / ICRA | ~1,500+ citations | 通过对动力学参数（质量、摩擦、阻尼等）随机化来训练鲁棒策略，使只用仿真数据训练的策略直接迁移到真实机器人，无需任何真实数据。是域随机化方法的里程碑。

2. **Closing the Sim-to-Real Loop: Adapting Simulation Randomization with Real World Experience** | Yevgen Chebotar et al. | 2019 | ICRA 2019 | 利用真实世界执行数据迭代自适应调整仿真参数分布，弥合Sim-to-Real差距。

3. **Robot Learning From Randomized Simulations: A Review** | Fabio Muratore, Fabio Ramos, Greg Turk, Wenhao Yu, Michael Gienger, Jan Peters | 2022 | Frontiers in Robotics and AI (PMC free article) | 全面综述域随机化方法，提供历史基础、形式化问题表达、实用指南（随机化哪些/何时/如何参数），提出SOB(Simulation Optimization Bias)作为量化可迁移性度量。

4. **DROID: Minimizing the Reality Gap Using Single-Shot Human Demonstration** | Ya-Yen Tsai et al. | 2020 | 使用单次人类示教识别动力学差距并优化仿真随机化范围。

5. **SimGAN: Hybrid Simulator Identification for Domain Adaptation via Adversarial RL** | Various | 2020 | 使用对抗框框架识别与真实轨迹匹配的混合仿真器。

6. **Sim-to-Real Transfer with Neural-Augmented Robot Simulation** | Various | 2018 | CoRL | 训练RNN建模仿真与真实轨迹之间的差异，用于增强仿真器。

7. **Meta Reinforcement Learning for Sim-to-Real Domain Adaptation** | Karol Arndt et al. | 2020 | 使用元RL训练能够适应多样化动力学的策略。

8. **Comparison of Different Domain Randomization Methods for Policy Transfer in RL** | Mingjun Ma, Haoran Li et al. | 2023 | IEEE DDCLS 2023 | 构建统一机器人导航任务，系统比较主流域随机化方法在动力学差距下的策略迁移效果。

9. **Learning to Walk in Minutes Using Massively Parallel Deep RL** | Nikita Rudin, David Hoeller, Marko Bjelonic, Marco Hutter | 2022 | RSS / Science Robotics | 使用大规模GPU并行仿真(Isaac Gym)和游戏灵感课程学习，在数分钟内训练出可直接迁移到真实四足机器人的运动策略。

---

## 重要基准环境

1. **OpenAI Gym** | Greg Brockman, Vicki Cheung, Ludwig Pettersson, Jonas Schneider, John Schulman, Jie Tang, Wojciech Zaremba | 2016 | arXiv:1606.01540 | ~10,000+ citations | 强化学习基准测试的标准工具包，提供统一的API（step/reset/render），包含经典控制、Atari、MuJoCo、Box2D等多样化环境。

2. **MuJoCo: A Physics Engine for Model-Based Control** | Emanuel Todorov, Tom Erez, Yuval Tassa | 2012 | IROS 2012 | ~5,000+ citations | 高精度物理引擎，成为连续控制RL的事实标准。2021年由DeepMind开源，2022年并入MuJoCo XLA/Playground。Ant、HalfCheetah、Humanoid等环境是MBRL/model-free标准基准。

3. **DeepMind Control Suite** | Yuval Tassa, Yotam Doron, Alistair Muldal, Tom Erez et al. (DeepMind) | 2018 | arXiv:1801.00690 | ~2,000+ citations | 基于MuJoCo的标准化连续控制基准套件，提供统一的Python API和标准化的任务结构、观察空间和奖励函数。

4. **Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning** | Viktor Makoviychuk, Lukasz Wawrzyniak et al. (NVIDIA) | 2021 | NeurIPS 2021 Datasets & Benchmarks (arXiv:2108.10470) | ~632+ citations | 将物理仿真和神经网络策略训练完全运行在GPU上，绕过CPU瓶颈。在单个GPU上训练复杂的机器人任务（运动、灵巧操作）仅需数分钟，比传统CPU+GPU架构快1-3个数量级。

5. **Safety-Gym** | Joshua Achiam, Dario Amodei et al. (OpenAI) | 2019 | OpenAI Technical Report | 安全RL标准基准，提供带安全约束（避障/目标导航/按钮按压）的机器人环境，包含Point、Car、DogGo三种机器人形态。

6. **Safety-Gymnasium** | Jiaming Ji, Borong Zhang et al. | 2023 | NeurIPS 2023 | Safety-Gym的升级统一基准，提供更丰富的安全RL评估场景和统一API。

7. **D4RL: Datasets for Deep Data-Driven Reinforcement Learning** | Justin Fu, Aviral Kumar, Ofir Nachum, George Tucker, Sergey Levine | 2020 | NeurIPS 2020 Datasets | 离线RL标准基准，包含MuJoCo运动、Adroit灵巧操作、AntMaze导航等多任务多质量离线数据集。

8. **RL Unplugged** | Caglar Gulcehre et al. (DeepMind) | 2020 | NeurIPS 2020 Datasets | 大规模离线RL基准，涵盖Atari、DM Control Suite、DM Locomotion、Real-World RL等多种域。

9. **NeoRL: A Near Real-World Benchmark for Offline RL** | Rongjun Qin et al. | 2022 | NeurIPS 2022 Datasets | 具有保守数据收集策略的接近真实世界的离线RL基准。

10. **Gymnasium** | Farama Foundation | 2022-present | OpenAI Gym的社区维护后继版本，支持更多环境和更现代化API。

---

## 应用论文

### 四旋翼/无人机控制
1. **Learning Agile Flights Through Narrow Gaps Using Onboard Sensing** | C. Xiao, P. Lu, Q. He | 2023 | IEEE RA-L 2023 | DRL实现激进穿越窄缝，仅用机载摄像头，真实世界成功率87.36%（倾角达60度）。
2. **Learning to Fly -- a Gym Environment with PyBullet Physics for Multi-agent Quadcopter Control** | J. Panerati et al. | 2021 | 开源多四旋翼RL环境。
3. **Offline RL for Quadrotor Control: Overcoming the Ground Effect** | L. Sacchetto et al. | 2023 | IROS 2023 | 离线RL在真实起飞任务中（地面效应下）击败在线RL。

### 自动驾驶
4. **Hierarchical Motion Control Strategies for Handling Interactions of Automated Vehicles** | B. Nemeth, P. Gaspar | 2023 | Control Engineering Practice | 自动驾驶交互的分层运动控制。
5. **Implementation and Design of Ultra-Local Model-Based Control Strategy for Autonomous Vehicles** | T. Hegedus et al. | 2024 | Vehicle System Dynamics | 超局部无模型控制用于自动驾驶。

### 工业/过程控制
6. **Deep RL-Based Active Network Management and Emergency Load-Shedding Control for Power Systems** | H. Zhang et al. | 2024 | IEEE Trans. Smart Grid | DRL用于电网紧急减载控制。
7. **RL Based Control Design for a Floating Piston Pneumatic Gearbox Actuator** | T. Becsi et al. | 2020 | IEEE Access | RL用于气动执行器工业控制。

### 灵巧操作
8. **Transferring Dexterous Manipulation from GPU Simulation to a Remote Real-World TriFinger** | Various | 2021 | 使用Isaac Gym进行灵巧手内操作的Sim-to-Real转移。
9. **Accelerating Interactive Human-like Manipulation Learning with GPU-based Simulation** | Mosbach et al. | 2022 | 结合GPU仿真和模仿学习进行灵巧操作。

### 足式机器人
10. **Learning to Walk in Minutes Using Massively Parallel Deep RL** | N. Rudin, D. Hoeller, M. Bjelonic, M. Hutter | 2022 | RSS / Science Robotics | 在Isaac Gym上训练四足机器人运动策略，数分钟内完成并零样本迁移到真实ANYmal机器人。

---

## 快速参考: 算法家族图谱

```
RL 基础
├── Value-Based (Q-Learning, SARSA) → DQN (2015) → Rainbow (2018)
├── Policy-Based (REINFORCE, PG Theorem 1999)
│   ├── On-Policy
│   │   ├── TRPO (2015) → PPO (2017)
│   │   └── A3C (2016)
│   └── Off-Policy
│       ├── DPG (2014) → DDPG (2015) → TD3 (2018)
│       └── SAC (2018)
├── Model-Based
│   ├── GP-Based: PILCO (2011)
│   ├── Planning: PETS (2018)
│   ├── Hybrid: MBPO (2019)
│   └── World Models: Dreamer → DreamerV2 → DreamerV3 (2019-2023)
├── Offline RL
│   ├── Policy Constraints: BCQ (2019), TD3+BC (2021)
│   ├── Value Pessimism: CQL (2020)
│   ├── In-Sample: IQL (2021)
│   └── Sequence Modeling: Decision Transformer (2021)
├── Safe RL
│   ├── Constrained RL: CPO (2017), FOCOPS (2020)
│   ├── Lagrangian: PID Lagrangian (2020)
│   └── Safety Filters: Safety Layer (2018), CBF QP, RMPC Filter (2021)
├── RL + MPC
│   ├── RL for MPC Tuning
│   ├── MPC as Safety Filter
│   └── Differentiable MPC + RL
└── Sim-to-Real
    ├── Domain Randomization
    ├── System Identification
    ├── Domain Adaptation
    └── Meta-Learning
```

---

> **说明**: 引用数为近似值（基于Google Scholar/Semantic Scholar），实际引用数随时间变化。标注"~"表示估算。
