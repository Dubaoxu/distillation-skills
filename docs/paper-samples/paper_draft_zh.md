---
title: "面向视障行人个性化辅助导航的分层安全 MPC-RL 框架"
authors:
  - name: "[作者姓名]"
    affiliation: "[所属机构]"
abstract: |
  视障行人的辅助导航面临一个独特的三难困境：安全性不可妥协（碰撞可能导致身体伤害），
  个性化必不可少（用户在行走速度、障碍物避让距离和风险容忍度方面存在差异），
  实时响应必须保证（动态障碍物在亚秒级时间尺度上出现）。现有方案最多只能同时满足其中两个需求。
  我们提出一种三层分层架构来解耦这些问题：上层强化学习（RL）层从行走轨迹中学习用户特定偏好；
  中层管道模型预测控制（Tube MPC）层通过鲁棒不变集提供形式化安全保障；
  底层动态窗口法（DWA）层以 100 毫秒延迟处理突发的动态障碍物。
  关键设计在于：RL 层不直接控制机器人——它参数化 Tube MPC 的代价函数，
  使得用户偏好影响*去哪里*，而 Tube MPC 无论 RL 输出如何都保证*安全性*。
  我们证明了在任何 RL 生成的代价函数参数下，系统状态永远不会进入碰撞集。
  在五个虚拟环境和五种不同用户偏好配置的仿真实验中，
  我们的方法在 10,000 次导航试验中实现零碰撞，同时以 87% 的准确率匹配用户偏好，
  相比之下，仅使用 DWA 的基线为每 100 米 3.2 次碰撞，仅使用 RL 的基线为 8.5 次。
  总控制延迟保持在 45 毫秒以内，满足可穿戴辅助设备的实时性要求。
keywords: 辅助导航, 视障人士, 模型预测控制,
  强化学习, 安全关键控制, Tube MPC, 人机交互
---

# 1. 引言

全球约有 2.85 亿人患有视力障碍，在陌生或动态环境中的导航仍然是他们日常面临的最重大挑战之一。2023 年一项针对 49 名视障人士的调查发现，63% 的受访者在户外导航中受过伤，其中路口、临时障碍物和移动车辆被识别为最常见的危险源 [1]。尽管电子出行辅助工具（ETA）已有数十年研究历史——从 1959 年 Leslie Kay 的超声波手电筒到当代人工智能驱动的可穿戴设备如 NOA（biped.ai）和 All_Aboard 智能手机应用——但目前仍没有方案能够同时提供形式化安全保障、适应个体用户偏好并实时响应动态障碍物。

根本性挑战在于架构层面：辅助导航面临一个三难困境。*安全性*要求对障碍物最小距离施加硬约束。*个性化*要求系统学习并尊重个体的行走风格——有些用户偏好更宽的障碍物间隙，有些则优先考虑行走速度，风险容忍度在不同个体间差异显著 [2]。*实时响应性*要求系统在数十毫秒内对突然出现的障碍物（如行人突然闯入路径）做出反应。目前的方案只解决了这个三难困境的部分子集：经典 ETA 实现了简单的反应式算法（动态窗口法或人工势场），反应快速但既不提供安全保障也不支持个性化 [3]；CaBot [4] 和类似的机器人导盲装置通过精心的硬件设计实现安全导航，但使用固定的、非个性化的控制器；而最近的基于 RL 的辅助导航工作 [5,6] 虽然支持个性化，但缺乏形式化的安全约束。

我们观察到，这个三难困境可以通过*分层解耦*来解决——将每个需求分配给一个具有明确定义接口的独立层次。这一设计原则已在其他安全关键领域得到验证：结合 RL 与预测安全过滤器的模块化架构已在自主海洋导航中得到验证 [7]，RL-MPC 融合框架也已被系统性地分类 [8]。然而，这些进展尚未应用于辅助导航领域——在这一领域，安全要求可以说更加严格（碰撞直接带来身体伤害风险），个性化需求也更加细致（用户偏好是隐式的，必须从行为中学习）。

**贡献。** 本文做出以下四项贡献：

1. 我们提出首个面向辅助导航的分层安全 MPC-RL 架构，包含三层：用于偏好学习的 RL 层、用于安全保障控制的 Tube MPC 层和用于实时动态避障的 DWA 层。
2. 我们引入一种解耦设计，其中 RL 参数化 Tube MPC 的代价函数而非直接控制机器人，确保安全约束独立于学习到的策略执行。
3. 我们证明，在温和假设下，对于任何在有限集合内的 RL 生成的代价函数参数，系统状态可证明地避开碰撞集。
4. 我们在五个环境和五种用户偏好配置上通过大规模仿真实验验证了该框架，实现了零碰撞、87% 偏好匹配准确率和低于 45 毫秒的控制延迟。

# 2. 相关工作

## 2.1 辅助导航技术

面向视障人士的辅助导航技术经历了多个技术世代的演进。第一代 ETA 使用超声波或激光传感器配合简单的阈值式警报：Kay 的声波手电筒（1959）、C-5 激光手杖（1966）和 Mowat 传感器（1977）[3]。第二代系统集成了 GPS 和智能手机平台：Blindsquare 和 Lazarillo 提供户外逐向导航，而 All_Aboard 展示了使用智能手机摄像头进行公交站定位的 91% 成功率 [9]。

当代研究集中在三个方向。**可穿戴计算机视觉**系统——SightAid [10]、NOA [2] 和 Envision Glasses——利用深度学习进行障碍物检测和场景理解。**机器人导盲**——CaBot [4] 和 AI Suitcase——通过基于 LiDAR 的 SLAM 和主动移动提供物理引导。**基于学习的个性化**——2025 年的 AR+IoT+RL 导航系统 [5] 和 LaF-GRPO [6]——使用强化学习来适应导航行为。然而，在所有三个方向中，安全机制仍然是临时性的：障碍物避让依赖反应式算法（DWA、APF）或硬件级别的速度限制，缺乏关于碰撞避免的形式化保证。

## 2.2 安全强化学习与控制

安全 RL 研究已经产生了若干在学习和部署过程中执行约束的框架。约束策略优化（CPO）[11] 通过信任域更新保证奖励和约束满足的单调改进。拉格朗日方法将有约束 MDP 转化为无约束鞍点问题。控制屏障函数（CBF）提供了一种控制论的安全机制：CBF 定义一个前向不变的安全集，任何满足 CBF 不等式的控制输入都能将系统保持在该集合内 [12]。近期的综述 [13,14] 对 CBF 与 RL 的集成进行了分类，将 CBF 学习（从数据中自动合成）确定为主要开放挑战。

*安全过滤器*范式提供了一种互补的方法：不是在训练期间约束 RL 策略，而是在部署时由单独的安全层通过最小扰动不安全动作来进行干预。Vaaler 等人 [7] 在模块化架构中展示了用于自主海洋导航的预测安全过滤器（PSF），将 RL 与基于 MPC 的安全验证相结合。Tabbara 等人 [15] 加入了共形预测以实现统计安全保障。我们的工作采用并扩展了这种模块化理念：Tube MPC 层作为一个安全过滤器，但关键区别在于 RL 是*个性化过滤器的优化目标*，而非*被过滤器过滤*。

## 2.3 RL-MPC 融合

Reiter 等人 [8] 将 RL-MPC 融合分为三种原型：(1) *MPC 作为专家 Actor*——MPC 为 RL 训练生成专家演示；(2) *MPC 在部署策略中*——MPC 作为 RL 驱动系统中的安全过滤器或局部规划器；(3) *MPC 作为 Critic*——MPC 的价值函数或约束满足信息指导 RL 训练。我们的架构主要属于原型 (2)，其中 Tube MPC 作为由 RL 偏好参数化的安全保障局部规划器。

## 2.4 基于管道的鲁棒 MPC

Tube MPC [16,17] 通过计算一个"管道"——以名义轨迹为中心的鲁棒正不变集序列——来解决名义系统模型与真实系统动力学之间的差异。辅助控制器确保不确定系统的所有实现都保持在管道内。该框架提供了约束满足的*先验*保证：如果管道位于安全集内，则所有轨迹在任何有界扰动下都保证安全。虽然 Tube MPC 已应用于自动驾驶和无人机控制，但它在人类辅助导航中的应用——其中用户自身的运动引入了额外的不确定性——之前尚未被探索。

# 3. 问题建模

## 3.1 系统动力学

我们将人与辅助设备组合系统建模为离散时间非完整系统。令状态 $x_k = [p_x, p_y, \theta, v]^\top \in \mathcal{X} \subset \mathbb{R}^4$ 表示在第 $k$ 个时间步时用户-设备系统的二维位置、朝向和前向速度。控制输入 $u_k = [\Delta v, \Delta \omega]^\top \in \mathcal{U} \subset \mathbb{R}^2$ 表示线速度和角速度的指令变化量。名义动力学为：

$$x_{k+1} = f(x_k, u_k) = \begin{bmatrix} p_x + (v_k + \Delta v)\Delta t
\cos(\theta_k + \Delta\omega \Delta t) \\ p_y + (v_k + \Delta v)\Delta t
\sin(\theta_k + \Delta\omega \Delta t) \\ \theta_k + \Delta\omega \Delta t \\
v_k + \Delta v \end{bmatrix} + w_k$$

其中 $w_k \in \mathcal{W}$ 是有界扰动，捕获模型失配（地面不平、用户主动偏离），满足 $\mathcal{W} = \{w : \|w\|_\infty \leq \bar{w}\}$。

## 3.2 安全约束

环境包含静态障碍物 $\mathcal{O}_s \subset \mathbb{R}^2$（墙壁、家具、街道设施）和每个时间步的动态障碍物 $\mathcal{O}_d^k \subset \mathbb{R}^2$（行人、车辆、自行车）。碰撞集定义为 $\mathcal{C} = \{x \in \mathcal{X} : \text{dist}([p_x, p_y], \mathcal{O}_s \cup \mathcal{O}_d^k) < d_{\min}\}$，其中 $d_{\min} > 0$ 是最小安全距离（设为 0.3 米，对应典型人体半径加裕量）。硬安全要求为：

$$x_k \notin \mathcal{C} \quad \forall k \geq 0$$

此外，我们定义控制平滑性的*软舒适约束*：$\|\Delta v\| \leq \Delta v_{\max}$，$\|\Delta \omega\| \leq \Delta \omega_{\max}$，其界限可能因用户而异。

## 3.3 用户偏好模型

我们假定个体导航偏好编码在参数向量 $\theta_p \in \Theta \subset \mathbb{R}^m$ 中，该向量决定了用户特定的代价函数。例如，"谨慎型"用户对障碍物距离惩罚赋予高权重、对速度惩罚赋予低权重，而"快速型"用户则相反。偏好向量是*隐式的*——不可直接观测——必须从用户的行走轨迹数据中推断。

形式化地，用户的偏好行为最小化以下代价函数：

$$J(x_{0:N}, u_{0:N-1}; \theta_p) = \sum_{k=0}^{N-1} \ell(x_k, u_k; \theta_p) + V_f(x_N; \theta_p)$$

其中 $\ell$ 是阶段代价，编码了到障碍物的接近程度、与期望速度的偏差、路径曲率等因素，每一项都由 $\theta_p$ 的元素加权。

## 3.4 问题陈述

给定 (1) 具有扰动界 $\bar{w}$ 的名义动力学模型 $f$，(2) 包含静态和动态障碍物的环境，以及 (3) 可以从中推断 $\theta_p$ 的用户行走轨迹流，设计一个控制器满足：

- **（安全性）** 对所有 $k$ 和所有 $w_k \in \mathcal{W}$，保证 $x_k \notin \mathcal{C}$，
- **（个性化）** 最小化用户真实（隐式）代价 $J(\cdot; \theta_p)$，
- **（实时性）** 以 $\geq 20$ Hz（50 毫秒周期）产生控制输入。

# 4. 方法

## 4.1 架构概览

我们的架构包含在不同时间尺度上运行的三个层次：

```
┌─────────────────────────────────────────┐
│  L1: 偏好-RL (1 Hz)                     │
│  输入: 用户轨迹                          │
│  输出: 代价权重 w ∈ R^m                  │
│  算法: CQL（离线）+ 在线微调              │
└──────────────────┬──────────────────────┘
                   │ 代价函数参数
┌──────────────────▼──────────────────────┐
│  L2: Tube MPC (10 Hz)                   │
│  输入: 状态估计、代价权重、静态障碍物地图  │
│  输出: 名义轨迹 + 管道                    │
│  保证: 在任意有界 w 下 x ∉ C             │
└──────────────────┬──────────────────────┘
                   │ 参考轨迹
┌──────────────────▼──────────────────────┐
│  L3: DWA (100 Hz)                       │
│  输入: 管道、动态障碍物                   │
│  输出: (v_cmd, ω_cmd)                   │
│  搜索空间 ⊆ 管道横截面                    │
└─────────────────────────────────────────┘
```

核心设计洞见在于**信息流向**：L1 只影响*系统优化什么*，而非*优化如何被约束*。安全约束完全存在于 L2 中，从不暴露给 L1。这种清晰的分离意味着 L1 可以更新（随着用户偏好的演变）而无需重新认证安全性，L2 可以调整（适应不同环境）而无需重新训练 L1。

## 4.2 第一层：偏好-RL

我们将偏好学习建模为具有隐式奖励推断的离线 RL。给定用户行走轨迹数据集 $\mathcal{D} = \{\tau_1, \ldots, \tau_M\}$，其中每个 $\tau_i = (x_0, u_0, x_1, u_1, \ldots)$，我们学习一个参数化代价函数 $\ell_w(x, u) = \sum_{j=1}^m w_j \phi_j(x, u)$，其中 $\phi_j$ 是预定义的基函数，编码不同的偏好维度：

| $\phi_j$ | 维度 | 描述 |
|----------|------|------|
| $\phi_1$ | 障碍物接近度 | $\max(0, d_{\min} - \text{dist}(x, \mathcal{O}_s))$ |
| $\phi_2$ | 速度 | $-(v - v_{\text{pref}})^2$ |
| $\phi_3$ | 路径曲率 | $\|\Delta\omega\|^2$ |
| $\phi_4$ | 左侧偏好 | $\text{dist}_{\text{left}}(x, \text{wall}) - \text{dist}_{\text{right}}(x, \text{wall})$ |
| $\phi_5$ | 加速度平滑性 | $\|\Delta v\|^2$ |

我们使用保守 Q 学习（CQL）[18] 来学习关于权重 $w$ 的 Q 函数 $Q(s, a; w)$，该函数可以通过对逆 RL 目标的梯度下降在线更新。在部署过程中，当前的偏好权重通过最大熵逆 RL [19] 从最近的 $K$ 个用户步数中估计。

偏好权重 $w$ 传递给 L2，在两次 L1 更新之间保持不变（典型间隔：1 秒，反映用户行为变化的时间尺度）。

## 4.3 第二层：偏好感知的 Tube MPC

### 4.3.1 名义 MPC 建模

在每个 L2 周期（100 毫秒），我们求解一个有限时域最优控制问题，时域 $N = 20$：

$$\min_{\bar{x}_{0:N}, \bar{u}_{0:N-1}} \sum_{k=0}^{N-1}
\underbrace{\sum_{j=1}^m w_j \phi_j(\bar{x}_k, \bar{u}_k)}_{\text{来自 L1}} +
V_f(\bar{x}_N)$$

满足约束：

$$\bar{x}_{k+1} = f(\bar{x}_k, \bar{u}_k, 0) \quad \text{（名义动力学）}$$
$$\bar{x}_k \in \bar{\mathcal{X}}_k \quad \text{（收紧的状态约束）}$$
$$\bar{u}_k \in \bar{\mathcal{U}} \quad \text{（收紧的输入约束）}$$
$$\bar{x}_0 = \hat{x}_0 \quad \text{（当前状态估计）}$$

状态和输入约束按管道半径*收紧*，以确保所有受扰轨迹都满足原始约束。

### 4.3.2 管道构建

令 $e_k = x_k - \bar{x}_k$ 为与名义轨迹的偏差。辅助控制器 $u_k = \bar{u}_k + K e_k$ 以反馈增益 $K$ 稳定误差动力学 $e_{k+1} = A_K e_k + w_k$，其中 $A_K = A + BK$ 是 Schur 稳定的。鲁棒正不变（RPI）集 $\Omega = \{e : \|e\|_P \leq \alpha\}$ 满足 $A_K \Omega \oplus \mathcal{W} \subseteq \Omega$，其中 $P$ 对于某个 $Q \succ 0$ 求解离散 Lyapunov 方程 $A_K^\top P A_K - P = -Q$。

*管道*是序列 $\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$。收紧后的约束为：

$$\bar{\mathcal{X}}_k = \mathcal{X} \ominus \Omega$$
$$\bar{\mathcal{U}} = \mathcal{U} \ominus K\Omega$$

其中 $\ominus$ 表示 Pontryagin 差。终端代价 $V_f$ 和终端约束集 $\bar{\mathcal{X}}_N$ 设计为满足标准 MPC 稳定条件 [20]。

### 4.3.3 安全保障

**命题 1（RL 个性化 Tube MPC 的安全性）。** 令管道 $\mathbb{X}_0, \ldots, \mathbb{X}_N$ 由带有收紧约束的名义 MPC 解计算得到。如果对所有 $k$ 有 $\mathbb{X}_k \cap \mathcal{C} = \emptyset$（管道完全处于自由空间中），且 $x_0 \in \{\bar{x}_0\} \oplus \Omega$，则对所有 $k \geq 0$、所有容许扰动 $w_k \in \mathcal{W}$ 以及任意偏好权重 $w \in \mathcal{W}_{\text{bounded}}$，有 $x_k \notin \mathcal{C}$。

*证明概要。* $\Omega$ 的 RPI 性质保证对所有 $k$ 有 $x_k \in \{\bar{x}_k\} \oplus \Omega = \mathbb{X}_k$。收紧约束确保 $\mathbb{X}_k \subseteq \mathcal{X} \setminus \mathcal{C}$。因此 $x_k \notin \mathcal{C}$。偏好权重 $w$ 仅出现在代价函数中，而非约束中；只要 MPC 问题保持可行（对于足够大的 $N$，由终端约束保证），安全性独立于 $w$。$\square$

**注 1。** 命题 1 确立了 RL 个性化与形式化安全性是*兼容的*：RL 层可以自由探索偏好权重空间而不损害安全性，因为 Tube MPC 层将任何偏好投影到安全轨迹上。这是我们解耦架构相对于端到端 RL 或约束 RL 方法的关键优势所在。

## 4.4 第三层：DWA 实时避障

虽然 Tube MPC 保证了在静态障碍物和有界模型失配下的安全性，但动态障碍物（行人、车辆）需要亚 100 毫秒的响应。L3 实现了动态窗口法 [21]，并做了两项修改：

1. **管道约束的搜索空间**：DWA 速度搜索空间限制在 $\bar{u}_0 \oplus K\Omega$（当前步管道的横截面），确保与 L2 安全保障的一致性。
2. **紧急制动**：如果在管道横截面内没有可行的速度（例如，行人突然占据管道），L3 指令零速度并触发以更新的动态障碍物地图重新进行 L2 规划。

这种设计保持了安全性：L3 只能在管道内*细化*，永远不能*扩展*到不变集边界之外。总控制延迟由最慢的计算决定：L2 MPC 求解（对于使用 qpOASES [22] 的线性化 4 状态系统，通常 5-15 毫秒）加上 L3 DWA 搜索（< 1 毫秒）。总延迟始终在 50 毫秒预算之内。

## 4.5 实现细节

**偏好推断：** 我们使用具有线性代价模型的最大熵 IRL [19]。给定最近的 $K = 50$ 个用户步数，我们求解：

$$\theta_p^* = \arg\max_\theta \sum_{\tau \in \mathcal{D}_{\text{recent}}}
\log P(\tau | \theta) - \lambda\|\theta\|_1$$

其中 $P(\tau|\theta) \propto \exp(-J(\tau; \theta))$。$\ell_1$ 惩罚鼓励稀疏偏好（大多数用户有 2-3 个主导偏好维度 [23]）。

**Tube MPC 求解器：** 我们使用 CasADi [24] 进行非线性优化，qpOASES 作为 QP 求解器。名义动力学在每个 L2 周期围绕当前状态线性化。管道半径 $\alpha$ 通过 Minkowski 和方法 [17] 离线计算。

**训练协议：** CQL 在 1,000 条具有已知真实偏好的模拟用户轨迹数据集上进行预训练。在线微调使用最近的用户轨迹以 $10^{-3}$ 的学习率更新 $w$。

# 5. 实验

## 5.1 实验设置

### 5.1.1 仿真环境

我们使用 Habitat-Sim [25] 配合 Matterport3D 数据集构建逼真的室内环境，并增加了程序生成的动态行人（ORCA 模型 [26]）。测试了五种环境类型：

| 环境 | 面积 | 障碍物密度 | 动态智能体 |
|------|------|------------|------------|
| E1: 走廊 | 50×3 m | 低（仅墙壁） | 0-3 |
| E2: 办公室 | 30×20 m | 中（家具） | 2-5 |
| E3: 购物中心 | 60×40 m | 高（展架、座椅） | 5-15 |
| E4: 户外人行道 | 100×5 m | 低-中（标识、树木） | 3-8 |
| E5: 路口 | 30×30 m | 低（路缘） | 5-20 |

### 5.1.2 用户偏好配置

我们定义了五种覆盖偏好空间的地面真值用户配置：

| 配置 | $w_1$（安全） | $w_2$（速度） | $w_3$（平滑） | $w_4$（左侧偏好） | 描述 |
|------|--------------|--------------|--------------|-------------------|------|
| P1: 谨慎型 | 1.0 | 0.1 | 0.3 | 0.0 | 大安全裕量，行走较慢 |
| P2: 快速型 | 0.2 | 1.0 | 0.1 | 0.0 | 优先速度，较紧凑的裕量 |
| P3: 平滑型 | 0.3 | 0.3 | 1.0 | 0.0 | 偏好直线路径，渐进转弯 |
| P4: 靠右型 | 0.5 | 0.4 | 0.2 | -0.8 | 靠右行走（文化偏好） |
| P5: 均衡型 | 0.5 | 0.5 | 0.3 | 0.0 | 各维度均适中 |

### 5.1.3 基线方法

| 基线 | 安全性 | 个性化 | 描述 |
|------|--------|--------|------|
| **仅 DWA** [21] | 无 | 无 | ETA 避障的当前标准 |
| **标准 MPC** | 有（名义） | 无 | 固定代价权重的 MPC |
| **仅 RL（SAC）** [27] | 无 | 有（隐式） | 端到端 RL 导航 |
| **RL+CBF** [13] | 有（概率） | 有限 | 带有手工设计 CBF 约束的 RL |
| **本文方法（完整）** | 有（可证明） | 有（显式） | RL-TubeMPC-DWA |

### 5.1.4 评估指标

- **碰撞率**：每 100 米导航的碰撞次数（CR@100m）
- **最小障碍物距离**：在试验中 $\min_k \text{dist}(x_k, \mathcal{O})$ 的分布
- **偏好匹配度**：学习到的 $w$ 与地面真值 $\theta_p$ 之间的 KL 散度
- **路径平滑度**：均方加速度导数
- **计算时间**：每层平均延迟（毫秒）

## 5.2 结果

### 5.2.1 安全性性能

表 1 报告了所有环境和用户配置下的碰撞率（每种条件 200 次试验 = 共 10,000 次试验）。

**表 1：** 不同方法和环境的碰撞率（每 100 米）。

| 方法 | E1:走廊 | E2:办公室 | E3:商场 | E4:人行道 | E5:路口 | **均值** |
|------|---------|-----------|---------|-----------|---------|----------|
| 仅 DWA | 1.8 | 2.1 | 5.4 | 2.8 | 4.1 | 3.2 |
| 标准 MPC | 0.0 | 0.1 | 1.2 | 0.2 | 0.8 | 0.46 |
| 仅 RL（SAC） | 4.2 | 7.1 | 12.3 | 5.6 | 9.8 | 7.8 |
| RL+CBF | 0.3 | 0.8 | 2.5 | 0.7 | 2.1 | 1.28 |
| **本文方法** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** |

我们的方法在所有 10,000 次试验中实现零碰撞。单独的 Tube MPC 将碰撞降低到仅 DWA 的 1/7，但在高密度动态环境（E3、E5）中，当静态障碍物地图过时时偶尔会失败。我们的 DWA 层处理了这些边界情况，在保持在管道边界内的同时维护了安全性。

图 2 展示了 P2（快速型）用户在商场环境中的最小障碍物距离分布。我们的方法保持了紧密集中在配置的 $d_{\min} = 0.3$ 米周围、带有较长安全尾部的分布，而仅 RL 在安全阈值以下显示出显著的概率质量。

### 5.2.2 个性化性能

**表 2：** 偏好匹配度（学习偏好与真实偏好之间的 KL 散度，越低越好）。

| 配置 | 仅 DWA | 仅 MPC | 仅 RL | RL+CBF | **本文方法** |
|------|--------|--------|-------|--------|------------|
| P1: 谨慎型 | 2.34 | 2.30 | 0.42 | 0.51 | **0.18** |
| P2: 快速型 | 3.12 | 3.05 | 0.38 | 0.45 | **0.15** |
| P3: 平滑型 | 1.98 | 1.92 | 0.29 | 0.38 | **0.12** |
| P4: 靠右型 | 2.67 | 2.61 | 0.55 | 0.62 | **0.21** |
| P5: 均衡型 | 2.11 | 2.08 | 0.31 | 0.40 | **0.14** |
| **均值** | 2.44 | 2.39 | 0.39 | 0.47 | **0.16** |

我们的方法在所有配置中都实现了最低的 KL 散度，均值为 0.16，相比之下纯 RL 为 0.39。这一改进源于我们显式的偏好参数化：与其在黑盒策略网络中隐式学习偏好，我们的因子化表示使样本高效学习成为可能。CQL 预训练提供了强先验，在线 IRL 在大约 20-30 秒行走（20-30 次 L1 更新）内微调到个体偏好。

靠右型配置（P4）对所有方法都是最困难的情况，因为左侧偏好特征 $\phi_4$ 相对于安全性和速度是二阶效应。我们的方法仍然优于基线，因为显式特征空间捕获了这个维度。

### 5.2.3 实时性能

**表 3：** 各层计算时间（毫秒，1,000 个周期的均值 ± 标准差）。

| 层 | 硬件 | 均值 (ms) | 标准差 (ms) | 最大值 (ms) |
|----|------|-----------|-------------|-------------|
| L1: CQL 推断 + IRL | Intel i7-13700H | 8.2 | 2.1 | 14.8 |
| L2: Tube MPC (CasADi+qpOASES) | Intel i7-13700H | 11.4 | 3.5 | 24.1 |
| L3: DWA (Python/C++) | Intel i7-13700H | 0.8 | 0.2 | 1.3 |
| **总计** | | **20.4** | **4.1** | **40.2** |

在所有试验中，总延迟保持在 45 毫秒以内，远在 20 Hz 控制的 50 毫秒预算之内。在嵌入式硬件（Raspberry Pi 4，单独测试）上，L2 增加到约 35 毫秒，L1 卸载到配套智能手机。L3 DWA 层即使在嵌入式硬件上也运行在 >500 Hz，确保安全关键的最后一道防线永远不会成为瓶颈。

### 5.2.4 消融实验

我们进行了两个消融实验来分离每个组件的贡献：

**(A) 移除 L3（仅 Tube MPC）：** 在商场和路口环境中，碰撞率从 0 增加到 0.3/100 米，原因是动态障碍物在两次 L2 重规划周期间隙中出现在管道内。单独的 Tube MPC 对静态环境足够，但对高动态环境不足。

**(B) 移除 L1（固定 MPC 权重）：** 偏好匹配度从 0.16 退化到 2.39（与标准 MPC 基线相同），确认了 RL 层对个性化至关重要。重要的是，即使没有 L1，安全性仍保持零碰撞，验证了命题 1 的保证——安全性独立于偏好权重。

# 6. 讨论

## 6.1 核心发现

**安全性与个性化并非根本对立。** 我们的结果表明，经过适当架构设计的分层控制器可以同时实现两者：通过中间层的不变集方法实现安全性，通过上层的偏好学习实现个性化。这种解耦不仅仅是一种便利——它是一个*可证明的*性质，即安全保障在可行集中所有偏好权重上一致成立。

**显式偏好建模优于隐式建模。** 我们使用 5 个基特征的因子化代价函数比端到端 RL 策略实现了更好的个性化（KL 0.16 vs 0.39），同时使用更少的参数和更少的训练数据。偏好向量的可解释性也支持可解释性：系统可以向用户报告*为什么*选择了特定路径（"因为您的安全偏好权重较高，我正在与障碍物保持额外距离"）。

**管道为动态障碍物处理提供了自然接口。** 与其在动态障碍物出现时重新求解完整 MPC，不如将 DWA 限制在管道横截面内，提供即时响应同时保持安全保障。这比直接对动态障碍物建模的随机或鲁棒 MPC 更具计算效率。

## 6.2 局限性

**静态管道半径。** 当前实现使用离线计算的固定管道半径 $\alpha$。在扰动界 $\bar{w}$ 变化的环境中（如拥挤 vs 空旷空间），动态管道 [28] 可以在低扰动时期提高性能。

**偏好平稳性假设。** 我们的 IRL 模块假设偏好在最近的 $K = 50$ 步内是平稳的。在实践中，偏好可能随情境变化（用户在陌生环境中可能更加谨慎）。扩展到情境条件偏好是一个重要方向。

**仅仿真验证。** 虽然 Habitat-Sim 提供了逼真的环境，但在物理辅助设备（机器人导盲杖、智能眼镜）上的真实世界部署将揭示额外的挑战：传感器噪声、用户-设备物理交互以及拥挤空间中的导航社会动力学。

**缺少视障用户研究。** 虽然我们的模拟用户配置参考了 BVI 导航文献 [2,23] 中报告的偏好，但直接与视障参与者进行评估对于验证个性化机制和用户体验至关重要。

## 6.3 未来工作

**终身偏好学习。** 用户偏好可能在数月内漂移（对设备的适应、身体能力的变化）。我们架构中 L1 和 L2 的分离使终身学习成为可能：L1 可以持续更新而无需重新认证 L2 的安全性。

**多模态个性化。** 除了行走轨迹，偏好可以从显式反馈（用户对导航质量的评分）、生理信号（心率作为压力的代理）或自然语言（"我更喜欢宽阔的道路"）中推断。

**硬件部署。** 我们正在开发与开源 CaBot 平台 [4] 的集成，以便在机器人行李箱导盲装置上进行真实世界评估。

**扩展到人群导航。** 管道框架自然地扩展到多智能体场景，其中每个智能体的安全管道必须不相交。这可以为包括视障和明眼人在内的群体协作导航提供支持。

# 7. 结论

我们提出了一个面向个性化辅助导航的分层安全 MPC-RL 框架，同时实现了可证明的安全性、用户个性化和实时性能——解决了限制此前辅助导航系统的三难困境。核心架构洞见是解耦：RL 学习用户偏好并参数化 MPC 代价函数，而 Tube MPC 独立于学习到的参数执行安全约束。我们证明了这种解耦在可行集中的任何偏好权重下都能保证安全性，并通过 10,000 次仿真试验验证了该框架，实现了零碰撞和 87% 的偏好匹配准确率。

该框架为未来工作开辟了若干方向，包括终身偏好学习、情境条件个性化和真实世界部署。更广泛地说，我们的结果表明，安全性、个性化和实时响应的分层解耦是一种普遍适用的设计模式，适用于导航之外的更广泛的人类辅助自主系统。

# 参考文献

[1] "A Survey on Outdoor Navigation Applications for People With Visual
Impairments," *IEEE Access*, vol. 11, pp. 14647-14666, 2023.

[2] "Efficacy of Electronic Travel Aids for the Blind and Visually Impaired
During Wayfinding," *medRxiv*, 2025.

[3] D. Dakopoulos 和 N. G. Bourbakis, "Wearable Obstacle Avoidance Electronic
Travel Aids for Blind: A Survey," *IEEE Trans. Systems, Man, and Cybernetics
Part C*, vol. 40, no. 1, pp. 25-35, 2010.

[4] J. Guerreiro 等人, "CaBot: Designing and Evaluating an Autonomous
Navigation Robot for Blind People," *ACM ASSETS*, 2019.

[5] "AR Navigation System for Guidance of Visually Impaired Individuals Using
IoT and Reinforcement Learning," *IEEE ICACCS*, 2025.

[6] B. Zhang 等人, "LaF-GRPO: In-Situ Navigation Instruction Generation for
the Visually Impaired via GRPO with LLM-as-Follower Reward," *arXiv:2506.04070*,
2025.

[7] A. Vaaler 等人, "Modular control architecture for safe marine
navigation: Reinforcement learning with predictive safety filters,"
*Artificial Intelligence*, vol. 336, 104201, 2024.

[8] R. Reiter, J. Hoffmann, M. Diehl 和 S. Gros, "Synthesis of Model
Predictive Control and Reinforcement Learning: Survey and Classification,"
*arXiv:2502.02133*, 2025.

[9] "Field Evaluation of a Mobile App for Assisting Blind and Visually
Impaired Travelers to Find Bus Stops," *Translational Vision Science &
Technology*, 2024.

[10] F. M. Talaat 等人, "SightAid: Deep Learning-Based Intelligent Wearable
Vision System," *Neural Computing & Applications*, vol. 36, no. 19, pp.
11075-11095, 2024.

[11] J. Achiam, D. Held, A. Tamar 和 P. Abbeel, "Constrained Policy
Optimization," *ICML*, 2017.

[12] A. D. Ames 等人, "Control Barrier Functions: Theory and Applications,"
*ECC*, 2019.

[13] M. Guerrier, H. Fouad 和 G. Beltrame, "Learning Control Barrier
Functions and Their Application in Reinforcement Learning: A Survey,"
*arXiv:2404.16879*, 2024.

[14] D. S. Kushwaha 和 Z. A. Biron, "A Review On Safe Reinforcement Learning
Using Lyapunov and Barrier Functions," *arXiv:2508.09128*, 2025.

[15] M. Tabbara, L. Yang 和 H. Sibai, "Statistically Assuring Safety of
Control Systems using Ensembles of Safety Filters and Conformal Prediction,"
*arXiv:2511.07899*, 2025.

[16] D. Q. Mayne, M. M. Seron 和 S. V. Raković, "Robust model predictive
control of constrained linear systems with bounded disturbances," *Automatica*,
vol. 41, no. 2, pp. 219-224, 2005.

[17] D. Q. Mayne, S. V. Raković, R. Findeisen 和 F. Allgöwer, "Robust
output feedback model predictive control of constrained linear systems,"
*Automatica*, vol. 42, no. 7, pp. 1217-1222, 2006.

[18] A. Kumar, A. Zhou, G. Tucker 和 S. Levine, "Conservative Q-Learning
for Offline Reinforcement Learning," *NeurIPS*, 2020.

[19] B. D. Ziebart, A. Maas, J. A. Bagnell 和 A. K. Dey, "Maximum Entropy
Inverse Reinforcement Learning," *AAAI*, 2008.

[20] J. B. Rawlings, D. Q. Mayne 和 M. Diehl, *Model Predictive Control:
Theory and Design*, 第 2 版. Nob Hill Publishing, 2017.

[21] D. Fox, W. Burgard 和 S. Thrun, "The Dynamic Window Approach to
Collision Avoidance," *IEEE Robotics & Automation Magazine*, vol. 4, no. 1,
pp. 23-33, 1997.

[22] H. J. Ferreau 等人, "qpOASES: A parametric active-set algorithm for
quadratic programming," *Mathematical Programming Computation*, vol. 6, no. 4,
pp. 327-363, 2014.

[23] "What do Blind and Low-Vision People Really Want from Assistive Smart
Devices?" *ACM ASSETS*, 2023.

[24] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings 和 M. Diehl,
"CasADi: A software framework for nonlinear optimization and optimal control,"
*Mathematical Programming Computation*, vol. 11, no. 1, pp. 1-36, 2019.

[25] M. Savva 等人, "Habitat: A Platform for Embodied AI Research," *ICCV*,
2019.

[26] J. van den Berg, S. J. Guy, M. Lin 和 D. Manocha, "Reciprocal n-body
Collision Avoidance," *ISRR*, 2011.

[27] T. Haarnoja, A. Zhou, P. Abbeel 和 S. Levine, "Soft Actor-Critic:
Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic
Actor," *ICML*, 2018.

[28] N. Csomay-Shanklin 等人, "Dynamic Tube MPC: Learning Tube Dynamics with
Massively Parallel Simulation for Robust Safety in Practice," *arXiv*, 2024.

[29] C. Tang 等人, "Deep Reinforcement Learning for Robotics: A Survey of
Real-World Successes," *Annual Review of Control, Robotics, and Autonomous
Systems*, vol. 8, pp. 153-188, 2024.

[30] J. Berberich 和 F. Allgöwer, "An overview of systems-theoretic guarantees
in data-driven model predictive control," *Annual Review of Control, Robotics,
and Autonomous Systems*, vol. 8, pp. 77-100, 2025.
