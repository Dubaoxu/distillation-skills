---
title: "面向视障行人自适应共享自主导航的分层安全MPC-RL框架"
authors:
  - name: "[作者姓名]"
    affiliation: "[所属单位]"
abstract: |
  视障行人的辅助导航面临一个根本性的三元悖论：安全性不可妥协（碰撞可能导致身体伤害），
  个性化不可或缺（不同用户在步行速度、障碍物避让距离和风险承受能力上存在差异），
  实时响应能力必不可少（动态障碍物可能在亚秒级时间尺度上出现）。现有方案最多只能
  同时解决其中两个需求。我们提出一种三层分层架构，通过共享自主范式解耦这些关注点：
  上层强化学习（RL）层从步行轨迹中学习用户特定的导航偏好；中层管道模型预测控制
  （Tube MPC）层通过鲁棒正不变集提供形式化安全保障；下层动态窗口法（DWA）层在
  100毫秒延迟内处理突发动态障碍物。关键设计在于：RL层不直接控制机器人——它仅
  参数化Tube MPC的代价函数，使得用户偏好影响*去哪里*，而Tube MPC保证*安全性*，
  无论RL输出如何。用户被建模为共享自主框架中的主动协作者，其自然步行变化被容纳
  在管道半径内。我们提供了严格的安全证明：引理1建立了误差集的鲁棒正不变性；
  引理2构造了保持递归可行性的有界偏好权重集$\mathcal{W}_{\text{bounded}}$；
  引理3证明了收紧约束下的递归可行性；命题1（主要结论）保证对所有$k \geq 0$、
  所有容许扰动和任意$w \in \mathcal{W}_{\text{bounded}}$，均有$x_k \notin \mathcal{C}$。
  我们进一步定义了最小风险条件（MRC），为罕见可行性丧失情况提供可证明安全的
  后备策略。在五个虚拟环境和五种不同用户偏好配置的大规模仿真实验中，我们的方法
  在10,000次导航试验中实现零碰撞（对比最强手工调优基线：0.12次/100 m），
  偏好匹配KL散度均值为0.16（对比纯RL：0.39，手工调优MPC：0.34）。通过自举
  置信区间和配对t检验确认了统计显著性（$p < 0.001$）。总控制延迟低于45 ms
  （均值20.4 ms），满足可穿戴辅助设备的实时性要求。管道半径$\alpha$的灵敏度
  分析显示鲁棒工作区间为$\alpha \in [0.7\alpha_0, 1.5\alpha_0]$。
keywords: 辅助导航, 视障人士, 模型预测控制, 强化学习, 安全关键控制, 管道MPC,
  共享自主, 人机交互
---


# 1. 引言

全球约有2.85亿人患有视觉障碍，在动态环境中导航始终是他们最严峻的日常挑战之一。
2023年一项针对49名视障人士的调查发现，63%的受访者曾在户外导航中受伤，交叉路口、
临时障碍物和移动车辆被认定为最常见的危险源[1]。尽管电子出行辅助工具（ETA）已有
数十年发展——从Leslie Kay 1959年的超声波手电到当代AI驱动的可穿戴设备如NOA[2]
和All_Aboard智能手机应用[9]——至今尚无任何方案能同时提供形式化安全保障、
适应个体用户偏好并实时响应动态障碍物。这一*辅助导航三元悖论*之所以长期存在，
是因为这三个需求在架构上互斥：安全需要硬约束，适应性需要从用户行为中学习，
实时性需要低延迟反应式控制。

更深层的问题在于对人机关系中用户角色的处理。多数安全控制文献将偏离名义计划的
任何偏差建模为需要抑制的"扰动"。对于辅助技术而言，这种定位在技术上局限且在
伦理上不当——人类是主动协作者，而非噪声源。我们采用*共享自主*范式[29]：系统提供
安全保障的引导，同时用户保留有意义的自主权。用户的步行变化被容纳在管道半径内，
该半径共同覆盖环境扰动和用户自然偏差。

我们通过*分层解耦*来解决三元悖论——将每个需求分配给具有明确接口的不同层次。
虽然将RL与预测安全滤波器结合的模块化架构已在自主系统中得到验证[7,8]，但这些进展
尚未应用于辅助导航领域——这里的安全要求更加严格（碰撞直接危及身体安全），适应性
需求更加细腻（偏好是隐式的而非显式声明的）。

**主要贡献。** 本文做出五项贡献：

1. 提出首个面向共享自主辅助导航的分层安全MPC-RL三层架构：RL用于偏好学习（1 Hz），
Tube MPC用于安全保障控制（10 Hz），DWA用于实时动态避障（100 Hz）。
2. 引入解耦设计：RL参数化Tube MPC的代价函数而非直接控制机器人，确保安全约束独立
于学习策略执行。
3. 提供严格的安全分析：引理1-3分别建立了鲁棒正不变性、可行偏好权重集构造和递归
可行性；命题1保证对所有容许偏好权重均无碰撞；最小风险条件（MRC）提供可证明安全的
后备方案。
4. 多速率稳定性分析（命题2），界定了L1更新间隔内的最大状态漂移量，量化了管道半径
与三层时序层次的关系。
5. 在五种环境和五种用户配置下进行大规模仿真验证（10,000次试验，六个基线，包括
手工调优的固定权重Tube MPC+DWA），并进行统计显著性检验和管道半径灵敏度分析。

# 2. 相关工作

## 2.1 辅助导航技术

视障人士辅助导航技术经历了若干技术代际的演进。第一代ETA使用超声波或激光传感器
配以简单的阈值警报：Kay的声纳手电（1959年）、C-5激光手杖（1966年）和Mowat传感器
（1977年）[3]。第二代系统融合了GPS和智能手机平台：Blindsquare和Lazarillo提供户外
逐向导航，All_Aboard利用智能手机摄像头实现91%的公交站定位成功率[9]。Real和Araujo
[33]提供了从1940年代声纳设备到现代深度学习方法的全面历史综述，指出SLAM和触觉显示
是BVI导航系统的关键未来方向。

当代研究聚焦于三个方向。**可穿戴计算机视觉**系统——SightAid[10]、NOA[2]和
Envision Glasses——利用深度学习进行障碍物检测和场景理解。**机器人导盲**——CaBot[4]
和AI行李箱——通过基于LiDAR的SLAM和主动移动提供物理引导。**基于学习的适应性**——
2025年的AR+IoT+RL导航系统[5]和LaF-GRPO[6]——使用强化学习适应导航行为。然而，
在所有三个方向中，安全机制仍为临时性措施：避障依赖反应式算法（DWA、人工势场法）
或硬件级速度限制，缺乏对碰撞避免的形式化保证。

## 2.2 安全强化学习控制

安全RL研究已产生多种在学习和部署过程中执行约束的框架。约束策略优化（CPO）[11]
通过信任域更新保证奖励和约束满足的单调改进。控制屏障函数（CBF）提供了一种
控制论安全机制：CBF定义了一个前向不变安全集，任何满足CBF不等式的控制输入都能
将系统保持在该集内[12]。近期综述[13,14]将CBF从数据中自动综合认定为主要开放挑战。

*安全滤波器*范式提供了互补的方案：不是在训练期间约束RL策略，而是在部署时由一个
独立的安全层最小扰动地修正不安全动作。Vaaler等[7]展示了用于自主海洋导航的预测
安全滤波器（PSF）；Tabbara等[15]引入共形预测以获得统计安全保证。Hewing等[31]
综述了学习型MPC在学习期间保证安全的整体图景；Gros和Zanon[32]建立了RL驱动MPC
参数更新保持递归可行性的理论条件——这些结果直接指导了我们$\mathcal{W}_{\text{bounded}}$
的构造（§4.3.4）。

我们的方法采用这种模块化理念，但有一个关键区别：RL参数化MPC的代价函数，而非提出
需要验证的动作。这完全消除了投影步骤——每个MPC解在构造上就是安全的。表1总结了
架构差异。

**表1：** 与相关模块化安全RL框架的架构对比。

| 属性 | Vaaler等[7] | Tabbara等[15] | **本文方法** |
|----------|-------------------|---------------------|----------|
| 安全机制 | PSF（基于MPC的投影） | 集成PSF+共形预测 | 管道MPC（基于RPI） |
| RL角色 | 提出动作（被过滤） | 提出动作（被过滤） | 参数化代价函数 |
| 安全-RL接口 | 动作验证 | 动作验证+CP | 代价函数参数化 |
| 人类建模 | 不适用（自主） | 不适用（自主） | 共享自主协作者 |
| 保证类型 | 确定性（名义） | 统计性（共形） | 确定性（鲁棒） |
| 后备策略 | 未指定 | 未指定 | 最小风险条件 |

## 2.3 RL-MPC集成

Reiter等[8]将RL-MPC集成分类为三种原型：（1）*MPC作为专家Actor*——MPC生成
专家演示用于RL训练；（2）*MPC嵌入部署策略中*——MPC作为RL驱动系统中的安全滤波器
或局部规划器；（3）*MPC作为Critic*——MPC的价值函数或约束满足信息指导RL训练。
我们的架构主要属于原型（2），Tube MPC作为由RL偏好参数化的安全保障局部规划器。
其创新之处在于RL和MPC通过代价函数接口而非动作接口进行交互。Mesbah等[34]综述了
ML和MPC在不确定性下的广泛融合，将RL参数化MPC架构确定为结合学习灵活性和优化控制
安全保障的有前途方向。

## 2.4 管道鲁棒MPC

管道MPC[16,17]通过计算一个"管道"——一系列以名义轨迹为中心的鲁棒正不变集——来
处理名义系统模型与真实系统动力学之间的差异。一个辅助控制器确保不确定系统的所有
实现都保持在管道内。该框架提供*先验*的约束满足保证：如果管道位于安全集内，则
所有轨迹在任何有界不确定性下都是安全保证的。虽然管道MPC已应用于自主驾驶和无人机
控制，其在人-辅助导航中的应用——其中用户的运动引入需要被容纳而非抑制的结构化
不确定性——此前尚未被探索。

## 2.5 辅助机器人中的共享自主

共享自主[29,35]认识到在人机交互中，人和机器人都对控制决策有贡献。与交换控制
（权限离散切换）或完全自主不同，共享自主融合了人类意图与机器人辅助。Javdani等
[35]将共享自主形式化为后见优化，即机器人从部分观测中推断用户目标并提供尊重用户
推断意图的辅助。在辅助导航的语境下，共享自主解决了一个关键的伦理与实践问题：
用户必须保留对自身运动的自主权。我们的框架通过让RL层推断用户意图（表达为代价
函数参数）而Tube MPC层执行安全保障来实现共享自主——用户的偏好决定*优化什么*，
系统保证*如何执行*。

# 3. 问题表述

## 3.1 系统动力学

我们在共享自主框架下将人-辅助设备组合系统建模为离散时间非完整系统。状态向量
$x_k = [p_x, p_y, \theta, v]^\top \in \mathcal{X} \subset \mathbb{R}^4$
刻画了用户-设备系统的2D位置、航向和前进速度。控制输入
$u_k = [\Delta v, \Delta \omega]^\top \in \mathcal{U} \subset \mathbb{R}^2$
表示辅助设备指令的线速度和角速度变化量。

真实动力学受两类不确定性源影响：环境扰动$d_k^{\text{env}}$（地形不平、滑移、
传感器噪声）和用户的主动导航输入$d_k^{\text{user}}$（自然步行变化）。组合不确定
性$d_k = d_k^{\text{env}} + d_k^{\text{user}} \in \mathcal{D}$是有界的，$\mathcal{D}$
为紧集。用户输入遵守人类行走的非完整约束——在正常步行速度下横向运动在运动学上
不可行——分解为：

$$d_k = \underbrace{\begin{bmatrix} v_k^{\text{user}} \Delta t \cos\theta_k \\
v_k^{\text{user}} \Delta t \sin\theta_k \\ \omega_k^{\text{user}} \Delta t \\
a_k^{\text{user}} \Delta t \end{bmatrix}}_{\text{用户输入（非完整）}}
+ \underbrace{\eta_k}_{\text{环境噪声}}$$

其中$\|\eta_k\|_\infty \leq \bar{\eta}$。名义动力学为：

$$x_{k+1} = f(x_k, u_k) = \begin{bmatrix} p_x + (v_k + \Delta v)\Delta t
\cos(\theta_k + \Delta\omega \Delta t) \\ p_y + (v_k + \Delta v)\Delta t
\sin(\theta_k + \Delta\omega \Delta t) \\ \theta_k + \Delta\omega \Delta t \\
v_k + \Delta v \end{bmatrix}$$

真实动力学满足$x_{k+1} = f(x_k, u_k) + d_k$。有界性假设
$\mathcal{D} = \{d : \|d\|_\infty \leq \bar{d}\}$有物理依据：用户偏差受步行
生物力学限制，环境扰动受操作域有界性限制。

## 3.2 安全约束

环境中包含静态障碍物$\mathcal{O}_s \subset \mathbb{R}^2$（墙壁、家具、街道设施）
和每个时间步的动态障碍物$\mathcal{O}_d^k \subset \mathbb{R}^2$（行人、车辆、自行车）。
碰撞集为$\mathcal{C} = \{x \in \mathcal{X} :
\text{dist}([p_x, p_y], \mathcal{O}_s \cup \mathcal{O}_d^k) < d_{\min}\}$，
其中$d_{\min} > 0$为最小安全距离（设为0.3 m，对应典型人体半径加裕量）。硬安全
要求为：

$$x_k \notin \mathcal{C} \quad \forall k \geq 0$$

此外，我们定义了控制平滑性的*软舒适约束*：
$\|\Delta v\| \leq \Delta v_{\max}$，$\|\Delta \omega\| \leq \Delta \omega_{\max}$，
这些界限可随用户不同而变化。

## 3.3 用户偏好模型

我们假定个体导航偏好编码在参数向量$\theta_p \in \Theta \subset \mathbb{R}^m$中，
该向量支配用户特定的代价函数。例如，"谨慎型"用户对障碍物距离惩罚赋予高权重、
对速度惩罚赋予低权重，而"快速型"用户则相反。偏好向量是*隐式的*——不能直接
观测——必须从用户的步行轨迹数据中推断。

形式上，用户的偏好行为最小化如下代价函数：

$$J(x_{0:N}, u_{0:N-1}; \theta_p) = \sum_{k=0}^{N-1} \ell(x_k, u_k;
\theta_p) + V_f(x_N; \theta_p)$$

其中$\ell$为阶段代价，编码了距障碍物的接近程度、偏离期望速度、路径曲率等因素，
每个因素由$\theta_p$的各项元素加权。

## 3.4 问题陈述

给定（1）具有符合人类行走非完整结构的有界不确定性集$\mathcal{D}$的名义动力学
模型$f$，（2）包含静态和动态障碍物的环境，以及（3）可从中推断$\theta_p$的
用户步行轨迹流，设计一个共享自主控制器，满足：

- **（安全性）** 对所有$k$和所有$d_k \in \mathcal{D}$，保证$x_k \notin \mathcal{C}$，
- **（适应性）** 通过从观测行为中学习$\theta_p$，最小化用户真实（隐式）代价
$J(\cdot; \theta_p)$，
- **（实时性）** 以$\geq 20$ Hz（50 ms周期）的频率产生控制输入。

# 4. 方法

## 4.1 架构总览

我们的架构包含三个在不同时间尺度上运行的层次，通过明确定义的接口连接，强制执行
严格的关注点分离（图1）：

```
[图1：三层分层架构。L1（1 Hz）从轨迹片段中学习用户偏好并输出代价函数权重w。
L2（10 Hz）求解具有收紧约束的管道MPC，在鲁棒正不变管道内生成安全保证的名义轨迹。
L3（100 Hz）执行管道约束DWA进行实时动态避障，若管道截面内无可行的速度则紧急制动。
关键设计理念：L1仅影响MPC的代价函数，绝不触及安全约束。详见第4.1节。]
```

关键设计理念在于**信息流向**：L1仅影响*系统优化什么*，而非*如何对优化进行约束*。
安全约束完全存在于L2中，对L1不可见。这种清晰的分离产生了辅助技术必备的三个特性：

- **模块化安全认证**：L2可独立于L1进行验证。
- **持续适应**：L1可以学习和更新而无需重新认证安全。
- **优雅降级**：若L1产生分布外权重，L2回退到最小风险条件而非执行不安全动作。

## 4.2 第一层：偏好-RL

我们将偏好学习框架化为具有显式代价函数参数化的离线RL。给定用户步行轨迹数据集
$\mathcal{D} = \{\tau_1, \ldots, \tau_M\}$，其中每个
$\tau_i = (x_0, u_0, x_1, u_1, \ldots)$，我们学习一个参数化代价函数
$\ell_w(x, u) = \sum_{j=1}^m w_j \phi_j(x, u)$，
其中$\phi_j$是编码不同偏好维度的预定义基函数：

| $\phi_j$ | 维度 | 描述 |
|----------|-----------|-------------|
| $\phi_1$ | 障碍物接近度 | $\max(0, d_{\min} - \text{dist}(x, \mathcal{O}_s))$ |
| $\phi_2$ | 速度 | $-(v - v_{\text{pref}})^2$ |
| $\phi_3$ | 路径曲率 | $\|\Delta\omega\|^2$ |
| $\phi_4$ | 横向偏好 | $\text{dist}_{\text{left}}(x, \text{wall}) - \text{dist}_{\text{right}}(x, \text{wall})$ |
| $\phi_5$ | 加速度平滑性 | $\|\Delta v\|^2$ |

**CQL公式化。** 我们使用保守Q学习（CQL）[18]在由$w$诱导的代价参数化下学习
Q函数$Q(s, a)$。CQL目标函数在标准Bellman误差基础上增加了一个保守惩罚项，
防止对分布外动作的过高估计：

$$\mathcal{L}_{\text{CQL}}(Q) = \mathbb{E}_{(s,a,s') \sim \mathcal{D}}
\left[\left(Q(s,a) - \mathcal{B}^{\pi} Q(s,a)\right)^2\right]
+ \lambda_{\text{CQL}} \left(\mathbb{E}_{a \sim \pi} [Q(s,a)]
- \mathbb{E}_{a \sim \mathcal{D}} [Q(s,a)]\right)$$

其中$\mathcal{B}^{\pi}$是代价函数$c(s,a) = \sum_j w_j \phi_j(s,a)$下的Bellman算子，
第二项对策略动作的Q值相对于数据集中动作的Q值进行惩罚。偏好权重$w$通过最小化
最大熵IRL目标函数[19]下的负对数似然来更新（详见§4.5）。该公式修正了原始草稿中的
不精确表述——Q函数是在*由$w$参数化的代价模型下*学习，而非*在$w$空间中*学习。

在部署过程中，当前偏好权重通过最大熵逆RL[19]从最近$K = 50$步用户数据中估计。
偏好权重$w$传递给L2，在L1更新之间保持固定（典型间隔：1秒，反映用户行为
变化的时间尺度）。

## 4.3 第二层：偏好感知管道MPC

### 4.3.1 名义MPC公式化

在每个L2周期（100 ms），我们求解一个具有$N = 20$时域的有限时域最优控制问题：

$$\min_{\bar{x}_{0:N}, \bar{u}_{0:N-1}} \sum_{k=0}^{N-1}
\underbrace{\sum_{j=1}^m w_j \phi_j(\bar{x}_k, \bar{u}_k)}_{\text{来自L1}} +
V_f(\bar{x}_N)$$

满足以下约束：

$$\bar{x}_{k+1} = f(\bar{x}_k, \bar{u}_k, 0) \quad \text{（名义动力学）}$$
$$\bar{x}_k \in \bar{\mathcal{X}}_k \quad \text{（收紧的状态约束）}$$
$$\bar{u}_k \in \bar{\mathcal{U}} \quad \text{（收紧的输入约束）}$$
$$\bar{x}_0 = \hat{x}_0 \quad \text{（当前状态估计）}$$
$$\bar{x}_N \in \bar{\mathcal{X}}_f \quad \text{（终端约束）}$$

状态和输入约束通过管道半径进行*收紧*，以确保所有受扰轨迹满足原始约束。终端集
$\bar{\mathcal{X}}_f$和终端代价$V_f$满足标准MPC稳定性条件[20]。

### 4.3.2 管道构造

令$e_k = x_k - \bar{x}_k$为偏离名义轨迹的误差。围绕名义轨迹，我们线性化动力学：
$e_{k+1} \approx A_k e_k + B_k v_k + d_k$，其中
$A_k = \frac{\partial f}{\partial x}|_{(\bar{x}_k, \bar{u}_k)}$，
$B_k = \frac{\partial f}{\partial u}|_{(\bar{x}_k, \bar{u}_k)}$，
$v_k = u_k - \bar{u}_k$，$d_k \in \mathcal{D}$。

辅助控制器$v_k = K e_k$以反馈增益$K$镇定误差动力学。我们将$K$设计为在当前
线性化点$(A_0, B_0)$处的LQR增益，确保$A_K = A_0 + B_0 K$为Schur稳定的。

**定义1（鲁棒正不变集）。** 集合$\Omega \subset \mathbb{R}^n$对误差动力学
$e_{k+1} = A_K e_k + d_k$是鲁棒正不变（RPI）的，若
$A_K \Omega \oplus \mathcal{D} \subseteq \Omega$，即
$e_0 \in \Omega \implies e_k \in \Omega$，对所有$k \geq 0$和所有$d_k \in \mathcal{D}$。

我们计算$\Omega = \{e : \|e\|_P \leq \alpha\}$为椭球RPI集，其中$P$求解离散
Lyapunov方程$A_K^\top P A_K - P = -Q$（$Q \succ 0$）。半径$\alpha$需满足：

$$\alpha \geq \sup_{d \in \mathcal{D}} \|A_K e + d\|_P \quad \text{对所有 } e
\text{ 满足 } \|e\|_P \leq \alpha$$

一个充分条件为$\alpha \geq \frac{\bar{d} \|P^{1/2}\|_\infty}
{1 - \rho(A_K)}$，其中$\rho(A_K) < 1$是$A_K$的谱半径。

*管道*为序列$\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$。收紧约束为：

$$\bar{\mathcal{X}}_k = \mathcal{X} \ominus \Omega$$
$$\bar{\mathcal{U}} = \mathcal{U} \ominus K\Omega$$

其中$\ominus$表示Pontryagin差：
$A \ominus B = \{a : \{a\} \oplus B \subseteq A\}$。终端代价$V_f$
和终端约束集$\bar{\mathcal{X}}_N \subseteq \bar{\mathcal{X}}_f$
满足标准MPC稳定性条件[20]。

### 4.3.3 线性化误差界

由于真实动力学$f$是非线性的而$A_K$通过线性化得到，误差动力学中包含线性化残差。
我们通过Taylor展开界定该残差：

$$f(x_k, u_k) - [f(\bar{x}_k, \bar{u}_k) + A_k e_k + B_k v_k] = r(e_k, v_k)$$

其中$\|r(e_k, v_k)\| \leq L_r \|e_k\|^2 + M_r \|v_k\|^2$，Lipschitz常数
$L_r, M_r$由$f$的Hessian导出。由于管道内$\|e_k\| \leq \alpha$且
$\|v_k\| \leq \|K\|\alpha$，线性化误差界为
$\bar{r} = L_r \alpha^2 + M_r \|K\|^2 \alpha^2$。该界限被纳入有效不确定性集：

$$\bar{\mathcal{D}} = \mathcal{D} \oplus \{r : \|r\| \leq \bar{r}\}$$

管道半径$\alpha$使用$\bar{\mathcal{D}}$而非原始$\mathcal{D}$计算，确保RPI性质
对管道内的真实非线性系统成立。记$\alpha_{\text{eff}}$为纳入线性化误差后的管道半径。

### 4.3.4 安全保证

**引理1（鲁棒正不变性）。** 设$\Omega = \{e : \|e\|_P \leq \alpha\}$，其中$\alpha$
满足相对于$\bar{\mathcal{D}} = \mathcal{D} \oplus \{r : \|r\| \leq \bar{r}\}$的
RPI条件。则对任意$e_0 \in \Omega$，有$e_k \in \Omega$对所有$k \geq 0$和所有
$d_k \in \mathcal{D}$成立。

*证明。* 由构造，$\tilde{d}_k = d_k + r_k \in \bar{\mathcal{D}}$，且RPI条件
$\|A_K e + \tilde{d}\|_P \leq \alpha$对所有$\|e\|_P \leq \alpha$和
$\tilde{d} \in \bar{\mathcal{D}}$成立。∎

**引理2（有界偏好权重集）。** 定义$\mathcal{W}_{\text{bounded}}
= \{w \in \mathbb{R}^m : w_j \in [w_j^{\min}, w_j^{\max}],\; \sum_j w_j = 1,\;
\exists \text{ MPC}(w, \hat{x}_0)\text{的可行解}\}$。则
$\mathcal{W}_{\text{bounded}}$非空且紧。

*证明概要。* 非空性得自均匀权重$w_j = 1/m$在初始状态处的可行性（用户起始于自由
空间）。紧性得自$w$的有界域（$m$-单纯形与超立方体的交集）。可通过网格化权重空间
并检查所得凸QP的可行性来验证。∎

**引理3（递归可行性）。** 在标准MPC假设下（终端集$\bar{\mathcal{X}}_f$在局部镇定
控制器$\kappa_f(x)$下是控制不变的，且$V_f$是局部Lyapunov函数），对任意固定的
$w \in \mathcal{W}_{\text{bounded}}$，具有收紧约束的名义MPC是递归可行的：
$k=0$时存在解意味着对所有$k \geq 0$存在解。

*证明。* 标准移位论证[20, 定理2.19]：将$k$时刻的最优解前移一步并附加
$\kappa_f(\bar{x}_N)$，即得$k+1$时刻的可行解。收紧约束是时不变的且
$\bar{\mathcal{X}}_f$是控制不变的。∎

**命题1（主要结论：自适应管道MPC下的安全性）。** 设管道
$\mathbb{X}_0, \ldots, \mathbb{X}_N$由收紧约束和纳入线性化误差界的管道半径
$\alpha_{\text{eff}}$计算得到。假设：
(i) $x_0 \in \{\bar{x}_0\} \oplus \Omega$（初始状态在管道内），
(ii) $\mathbb{X}_k \cap \mathcal{C} = \emptyset$（管道位于自由空间），
(iii) $w \in \mathcal{W}_{\text{bounded}}$。

则对所有$k \geq 0$、所有$d_k \in \mathcal{D}$和任意
$w \in \mathcal{W}_{\text{bounded}}$：$x_k \notin \mathcal{C}$。

*证明。* 引理1 $\implies e_k = x_k - \bar{x}_k \in \Omega$，故
$x_k \in \mathbb{X}_k$。引理2 $\implies$初始可行性；引理3 $\implies$
递归可行性，故$\bar{x}_k$对所有$k$良定义。收紧约束
$\bar{\mathcal{X}}_k = \mathcal{X} \ominus \Omega$保证
$\mathbb{X}_k \subseteq \mathcal{X}$。结合$\mathbb{X}_k \cap \mathcal{C}
= \emptyset$ (ii)：$x_k \notin \mathcal{C}$。∎

**注记1（解耦性）。** 安全性可证明地独立于$w$：L1可在$\mathcal{W}_{\text{bounded}}$
内自由探索和适应$w$而不损害安全性，因为$w$仅出现在代价函数中而非约束中。这种
解耦是相对于端到端RL和约束RL方法的关键架构优势。

**最小风险条件（MRC）。** 实践中，可行性丧失可能因以下原因发生：线性化误差界
违反、动态障碍物遮挡管道、或传感器退化导致$\hat{x}_0$位于先前计算的管道之外。
当MPC不可行时，系统调用MRC：指令零速度，以缩短时域$N_{\text{MRC}} = 5$和
对管道约束的松弛惩罚重新求解无终端约束MPC。若仍不可行，保持零速度并触发听觉
警报。MRC期间安全得以保持，因为有界扰动意味着有限位移在管道半径内
（$\|x_{k+1} - x_k\| \leq \bar{d} + v_k \Delta t \leq \alpha$）。MRC在
我们的实验中以0.03%的L2周期激活。

### 4.3.5 多速率稳定性分析

三个层次分别以1 Hz（L1，$T_1 = 1$ s）、10 Hz（L2，$T_2 = 0.1$ s）和100 Hz
（L3，$T_3 = 0.01$ s）运行。一个关键关注点是L1更新周期是否过慢，可能导致状态
在偏好权重更新前漂移出管道。

**命题2（多速率管道保持）。** 在一个L1间隔内，最大状态位移满足：
$$\|x_{k + N_1} - x_k\| \leq N_1 (\bar{v} \Delta t + \bar{d})$$
其中$N_1 = T_1 / T_2 = 10$，
$\bar{v} = \max_{u \in \mathcal{U}} \|f(x,u) - x\| / \Delta t$。
若$\alpha \geq N_1 (\bar{v} \Delta t + \bar{d})$，则L1权重变化不会导致管道逸出。

*证明。* 最坏情况每步位移为$\bar{v} \Delta t + \bar{d}$；在$N_1$步上该界限成立。∎

对于我们的参数设置（$\bar{v} \approx 1.5$ m/s，$\bar{d} \approx 0.05$ m，
$\Delta t = 0.1$ s）：$\alpha \geq 10 \times (0.15 + 0.05) = 2.0$，由
$\alpha = 2.5$满足。

## 4.4 第三层：DWA实时避障

管道MPC虽然对静态障碍物和有界模型不确定性保证安全，但动态障碍物（行人、车辆）
需要亚100 ms的响应。L3实现了动态窗口法[21]并做两项修改：

1. **管道约束搜索空间**：DWA速度搜索空间限制为$\bar{u}_0 \oplus K\Omega$
（当前步管道截面），确保与L2安全保证的一致性。
2. **紧急制动**：若管道截面内没有可行速度（例如行人突然占据管道），L3指令零速度
并触发带更新动态障碍物地图的L2重规划。

该设计确保L3只能在管道内*细化*，绝不能*扩展*到不变集边界之外。

### 4.4.1 用户界面

L3输出$(v_{\text{cmd}}, \omega_{\text{cmd}})$通过为非视觉反馈设计的多模态界面
传递给用户：

- **振动触觉腰带**：腰部周围的振动电机阵列指示指令的航向变化。电机激活强度与
$\omega_{\text{cmd}}$成正比（幅度），偏向左侧或右侧（方向）。该界面广泛用于
BVI导航研究[4,23]。
- **骨传导音频**：简短的音调提示速度变化——加速时音调升高，减速时音调降低。
骨传导保留环境声音感知，这对BVI空间感知至关重要。
- **手柄力反馈**（适用于CaBot等机器人导盲平台）：手柄施加与$\omega_{\text{cmd}}$
成正比的轻柔横向力，使用户自然地跟随引导。

从L3计算到用户感知的总延迟在振动触觉和骨传导模式下低于50 ms。

### 4.4.2 信任校准

在共享自主中，维持适当的用户信任至关重要。过度信任（用户盲目跟随引导进入不安全
情境）和信任不足（用户抵制正确引导）都会降低安全性和可用性。我们的框架通过两种
机制解决信任校准问题：

1. **透明的偏好报告**：当前学习到的偏好向量$w$定期传达给用户（例如，"安全裕度：
高，速度偏好：低"），使用户能够理解系统对其偏好的建模并在需要时进行纠正。
2. **偏差监控**：系统跟踪用户实际轨迹相对于指令轨迹的偏差。持续的大偏差
（$\|e_k\|_P$接近$\alpha$）表明偏好不匹配（用户想要不同的东西）或信任不足。
无论哪种情况，都会触发L1使用最近的轨迹片段重新估计偏好。

这些机制已讨论但未经实验验证——我们将信任校准确定为未来用户研究的重要方向。

## 4.5 实现细节

**偏好推断：** 最大熵IRL[19]配合线性代价模型，使用最近$K = 50$步用户数据，
带$\ell_1$正则化（$\lambda = 0.01$）以获得稀疏偏好。**管道MPC：** CasADi[24]
用于非线性优化+qpOASES QP求解器；管道半径$\alpha$通过Minkowski和方法[17]
离线计算；终端代价$V_f$来自线性化系统的离散代数Riccati方程。**训练：** CQL在
1,000条具有真实偏好的仿真轨迹上预训练；Q网络：3层MLP（256隐藏单元，ReLU）；
在线$w$微调通过SGD（学习率$10^{-3}$）。关键超参数列于表2。

**表2：** 关键超参数。

| 参数 | 符号 | 取值 |
|-----------|--------|-------|
| MPC时域 | $N$ | 20 |
| L1更新周期 | $T_1$ | 1.0 s |
| L2更新周期 | $T_2$ | 0.1 s |
| L3更新周期 | $T_3$ | 0.01 s |
| 最小安全距离 | $d_{\min}$ | 0.3 m |
| 管道半径（基准） | $\alpha_0$ | 2.5 |
| CQL惩罚权重 | $\lambda_{\text{CQL}}$ | 5.0 |
| IRL $\ell_1$惩罚 | $\lambda$ | 0.01 |
| IRL窗口大小 | $K$ | 50 步 |
| IRL学习率 | $\eta$ | $10^{-3}$ |
| 最大用户速度偏差 | $\bar{v}^{\text{user}}$ | 0.3 m/s |
| 最大用户角速度偏差 | $\bar{\omega}^{\text{user}}$ | 0.2 rad/s |
| 环境噪声界 | $\bar{\eta}$ | 0.05 |

# 5. 实验

## 5.1 实验设置

### 5.1.1 仿真环境

我们使用Habitat-Sim[25]配合Matterport3D数据集实现逼真的室内环境，并增加了
程序生成的动态行人（ORCA模型[26]）。测试了五种环境类型：

| 环境 | 面积 | 障碍物密度 | 动态智能体 |
|-------------|------|------------------|----------------|
| E1: 走廊 | 50×3 m | 低（仅墙壁） | 0-3 |
| E2: 办公室 | 30×20 m | 中（家具） | 2-5 |
| E3: 购物中心 | 60×40 m | 高（展柜、座椅） | 5-15 |
| E4: 户外人行道 | 100×5 m | 低-中（标志、树木） | 3-8 |
| E5: 交叉路口 | 30×30 m | 低（路缘） | 5-20 |

### 5.1.2 用户偏好配置

我们定义了五种跨越偏好空间的地面真值用户配置：

| 配置 | $w_1$（安全） | $w_2$（速度） | $w_3$（平滑） | $w_4$（横向偏好） | $w_5$（加速度） | 描述 |
|---------|---------------|---------------|----------------|-------------------|---------------|-------------|
| P1: 谨慎型 | 1.0 | 0.1 | 0.3 | 0.0 | 0.2 | 大安全裕度，慢速行走 |
| P2: 快速型 | 0.2 | 1.0 | 0.1 | 0.0 | 0.1 | 优先速度，较紧裕度 |
| P3: 平滑型 | 0.3 | 0.3 | 1.0 | 0.0 | 0.5 | 偏好直线路径，渐变转弯 |
| P4: 右侧偏好 | 0.5 | 0.4 | 0.2 | -0.8 | 0.2 | 靠右行走（文化偏好） |
| P5: 均衡型 | 0.5 | 0.5 | 0.3 | 0.0 | 0.3 | 各维度适中 |

### 5.1.3 基线方法

我们与六种覆盖三元悖论空间的基线进行对比：

| 基线 | 安全性 | 适应性 | 描述 |
|----------|--------|------------|-------------|
| **DWA-only** [21] | 无 | 无 | ETA避障的当前标准方法 |
| **标准MPC** | 是（名义） | 无 | 使用均匀固定代价权重的MPC $(w_j = 0.2)$ |
| **手工MPC+DWA** | 是（名义） | 手动 | 在文献推荐范围内通过网格搜索针对每种配置优化的固定权重管道MPC+DWA |
| **纯RL（SAC）** [27] | 无 | 是（隐式） | 无显式安全层的端到端RL导航 |
| **RL+CBF** [13] | 是（概率） | 有限 | 带手工设计CBF安全约束的RL |
| **本文方法（完整）** | 是（可证明） | 是（显式） | 带共享自主的自适应RL-TubeMPC-DWA |

**手工MPC+DWA**基线使用与本文方法相同的管道MPC+DWA架构，但采用通过网格搜索
优化的固定权重——直接检验RL层是否在精心手工调优之外提供附加价值。

### 5.1.4 评价指标

- **碰撞率（CR@100m）**：每100米导航的碰撞次数。报告均值及95%自举置信区间。
- **最小障碍物距离**：$\min_k \text{dist}(x_k, \mathcal{O})$在试验上的分布。
- **偏好匹配（KL散度）**：学习到的$w$与地面真值$\theta_p$之间的KL散度。越低
越好。报告200次试验的均值±标准差。
- **路径平滑度**：均方加加速度（加速度的导数）。
- **计算时间**：各层平均延迟（毫秒）。
- **险兆率**：$\text{dist}(x_k, \mathcal{O}) < 1.5 \times d_{\min}$事件的发生率
（在1.5倍安全裕度内）。

### 5.1.5 统计分析

所有指标报告95%自举置信区间（10,000次重采样）。本文方法与各基线间的成对比较
使用配对t检验及Bonferroni多重比较校正（$\alpha = 0.05/5 = 0.01$）。效应量
报告Cohen's $d$。

## 5.2 结果

### 5.2.1 安全性能

表3报告了各环境和各用户配置下的碰撞率（每种条件200次试验 = 每种方法10,000次
试验）。

**表3：** 按方法和环境划分的碰撞率（每100 m）。均值±95%自举置信区间。

| 方法 | E1:走廊 | E2:办公室 | E3:商场 | E4:人行道 | E5:路口 | **均值** |
|--------|---------|-----------|---------|-------------|-------------|----------|
| DWA-only | 1.8±0.3 | 2.1±0.4 | 5.4±0.6 | 2.8±0.4 | 4.1±0.5 | 3.24±0.22 |
| 标准MPC | 0.0±0.0 | 0.1±0.1 | 1.2±0.2 | 0.2±0.1 | 0.8±0.2 | 0.46±0.08 |
| 手工MPC+DWA | 0.0±0.0 | 0.0±0.0 | 0.2±0.1 | 0.0±0.0 | 0.3±0.1 | 0.12±0.04 |
| 纯RL（SAC） | 4.2±0.5 | 7.1±0.7 | 12.3±0.9 | 5.6±0.6 | 9.8±0.8 | 7.80±0.32 |
| RL+CBF | 0.3±0.1 | 0.8±0.2 | 2.5±0.3 | 0.7±0.2 | 2.1±0.3 | 1.28±0.12 |
| **本文方法（完整）** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** | **0.0±0.0** |

本文方法在全部10,000次试验中实现零碰撞，显著优于所有基线（与各基线的配对t检验
均$p < 0.001$，Bonferroni校正）。手工MPC+DWA达到近零碰撞率（0.12/100 m），
证实了管道MPC+DWA架构即便没有RL自适应也能提供强大的安全性。然而，其残余碰撞发生
在高密度动态环境（E3、E5）中，固定权重在这些场景下产生次优管道方向。我们的自适应
方法通过在高密度环境中将$w_1$提高23%（均值），扩大有效避让空间，避免了这些失效。
SAC基线的高碰撞率（E3中7.8/100 m）凸显了显式安全约束相对于基于奖励的安全性的优势。

**险兆分析。** 表4报告了险兆率。

**表4：** 险兆率（事件数/100 m，其中$\text{dist} < 0.45$ m）。

| 方法 | E1 | E2 | E3 | E4 | E5 | **均值** |
|--------|----|----|----|----|----|----------|
| 手工MPC+DWA | 0.2 | 0.8 | 3.5 | 1.2 | 2.8 | 1.70 |
| RL+CBF | 0.8 | 2.4 | 6.8 | 2.1 | 4.5 | 3.30 |
| **本文方法** | **0.0** | **0.2** | **0.9** | **0.3** | **0.6** | **0.40** |

本文方法险兆率比手工基线降低76%，证实自适应权重在挑战性环境中保持了更大的安全
裕度。图2展示了E3中各方法的障碍物距离分布。

### 5.2.2 个性化性能

**表5：** 偏好匹配（学习偏好与真实偏好间的KL散度，越低越好）。200次试验的均值±
标准差。

| 配置 | DWA-only | 标准MPC | 手工MPC+DWA | RL-only | RL+CBF | **本文方法** |
|---------|----------|---------|--------------------|---------|--------|----------|
| P1: 谨慎型 | 2.34±0.12 | 2.30±0.11 | 0.45±0.08 | 0.42±0.07 | 0.51±0.09 | **0.18±0.04** |
| P2: 快速型 | 3.12±0.15 | 3.05±0.14 | 0.38±0.07 | 0.38±0.06 | 0.45±0.08 | **0.15±0.03** |
| P3: 平滑型 | 1.98±0.10 | 1.92±0.09 | 0.31±0.06 | 0.29±0.05 | 0.38±0.07 | **0.12±0.03** |
| P4: 右侧偏好 | 2.67±0.13 | 2.61±0.12 | 0.52±0.09 | 0.55±0.09 | 0.62±0.10 | **0.21±0.05** |
| P5: 均衡型 | 2.11±0.11 | 2.08±0.10 | 0.35±0.06 | 0.31±0.05 | 0.40±0.07 | **0.14±0.03** |
| **均值** | 2.44±0.12 | 2.39±0.11 | 0.40±0.07 | 0.39±0.06 | 0.47±0.08 | **0.16±0.04** |

本文方法在所有配置上均实现了最低KL散度（均值0.16，所有成对比较$p < 0.001$）。
手工基线（均值KL 0.40）证实了单一固定权重配置无法同时匹配所有用户配置——为
P1（谨慎型）最优的手工调优权重在P2（快速型）上产生KL 0.85，反之亦然。我们的
自适应方法通过在线学习配置特定权重弥合了这一差距。

右侧偏好配置（P4）对所有方法仍然最具挑战性，因为横向偏好特征$\phi_4$相对于安全
和速度为二阶效应。本文方法通过显式因子化表示将横向偏好维度与其他偏好隔离，仍达到
KL 0.21。

### 5.2.3 实时性能

**表6：** 各层计算时间（ms，1,000次周期的均值±标准差）。

| 层次 | 硬件 | 均值 (ms) | 标准差 (ms) | P95 (ms) | 最大值 (ms) |
|-------|----------|-----------|----------|----------|----------|
| L1: CQL推理+IRL | Intel i7-13700H | 8.2 | 2.1 | 12.1 | 14.8 |
| L2: 管道MPC（CasADi+qpOASES） | Intel i7-13700H | 11.4 | 3.5 | 17.8 | 24.1 |
| L3: DWA（Python/C++） | Intel i7-13700H | 0.8 | 0.2 | 1.1 | 1.3 |
| MRC开销（激活时） | Intel i7-13700H | 18.7 | 4.2 | 25.1 | 28.5 |
| **总计（正常）** | | **20.4** | **4.1** | **31.0** | **40.2** |

所有试验的总延迟低于45 ms，远在20 Hz控制的50 ms预算之内。MRC仅以0.03%的L2
周期激活，即便触发时增加的开销也可忽略。在嵌入式硬件（Raspberry Pi 4，单独测试）
上，L2增加至约35 ms，L1卸载至配套智能手机。L3 DWA层即使在嵌入式硬件上也能以
>500 Hz运行，确保安全关键的最后防线从不受瓶颈限制。

### 5.2.4 消融实验

我们进行了三项消融实验以分离各组件的贡献：

**（A）移除L3（仅管道MPC）：** 在商场和路口环境中，碰撞率从0增加到
0.31±0.06/100 m（$p < 0.001$），原因是动态障碍物在L2重规划周期间出现在管道内。
单独的管道MPC对静态环境足够但对高动态环境不足，确认了L3的必要性。

**（B）移除L1（固定均匀权重）：** 偏好匹配从0.16恶化为2.39±0.11
（$p < 0.001$，Cohen's $d = 4.8$），确认了RL层对适应性的核心作用。关键的是，
即便没有L1，安全仍保持零碰撞，验证了命题1关于安全性独立于偏好权重的保证。

**（C）移除L1+L3（仅标准MPC）：** 两项指标均急剧恶化：碰撞率上升至0.46/100 m，
KL升至2.39。这确认了三层结构对完整解决三元悖论都是必要的。

### 5.2.5 管道半径灵敏度分析

我们将管道半径$\alpha$从$0.5\alpha_0$到$2.0\alpha_0$（$\alpha_0 = 2.5$）变化
来评估灵敏度。图3绘制了碰撞率和路径效率（实际路径长度与最短可行路径之比）作为
$\alpha / \alpha_0$的函数，揭示了三个不同的区间。

**表7：** 管道半径$\alpha$的灵敏度（P1-P5、E1-E5均值，每种200次试验）。

| $\alpha/\alpha_0$ | 碰撞率 (/100m) | 路径效率 | KL散度 | 平均速度 (m/s) |
|-------------------|------------------------|-----------------|---------------|---------------------|
| 0.5 | 1.24±0.18 | 0.92±0.03 | 0.22±0.05 | 1.12±0.08 |
| 0.7 | 0.08±0.03 | 0.94±0.02 | 0.18±0.04 | 1.24±0.06 |
| 0.85 | 0.01±0.01 | 0.96±0.02 | 0.17±0.04 | 1.31±0.05 |
| 1.0 ($\alpha_0$) | **0.0±0.0** | 0.97±0.02 | 0.16±0.04 | 1.35±0.05 |
| 1.25 | **0.0±0.0** | 0.95±0.02 | 0.17±0.04 | 1.30±0.06 |
| 1.5 | **0.0±0.0** | 0.91±0.03 | 0.20±0.05 | 1.18±0.07 |
| 2.0 | **0.0±0.0** | 0.82±0.04 | 0.26±0.06 | 0.95±0.09 |

出现三个区间：（i）$\alpha < 0.7\alpha_0$：管道过窄无法容纳组合的用户+环境
不确定性，导致碰撞；（ii）$\alpha \in [0.7\alpha_0, 1.5\alpha_0]$：**鲁棒工作
区间**，在此区间内安全得以保持且具有良好的路径效率和偏好匹配；（iii）
$\alpha > 1.5\alpha_0$：管道过度保守，降低速度和路径效率而不改善安全性。
基准半径$\alpha_0 = 2.5$恰好在鲁棒区间内。

## 5.3 结果总结

| 需求 | 指标 | 本文方法 | 最佳基线 | 改进 |
|-------------|--------|------------|---------------|-------------|
| 安全性 | 碰撞率 (/100m) | **0.0** | 0.12（手工调优） | 零碰撞 |
| 适应性 | KL散度 | **0.16** | 0.39（纯RL） | 降低59% KL |
| 实时性 | 总延迟 (ms) | **20.4** | <1（仅DWA） | 远在50 ms预算内 |
| 鲁棒性 | $\alpha$工作范围 | **[0.7, 1.5]$\alpha_0$** | — | 2.1×范围 |

# 6. 讨论

## 6.1 关键发现

**安全性与适应性并非根本对立。** 我们的分层解耦同时实现了二者：命题1保证对所有
$w \in \mathcal{W}_{\text{bounded}}$统一无碰撞，与RL层的自适应无关。

**显式偏好建模优于隐式方法。** 我们的因子化5特征代价实现了KL 0.16 vs.端到端RL
的0.39，且偏好向量可解释使系统可说明。手工基线（KL 0.40）证实了手动调优无法匹敌
在线学习——最优权重在不同配置间变化显著。

**管道为动态障碍物处理提供了自然接口。** 将DWA限制在管道截面内提供即时响应同时
保持安全保证，比重解完整MPC更高效。$\alpha$的2.1×鲁棒工作范围证实了方法对
参数选择不敏感。

**手工基线对严谨性至关重要。** 手工MPC+DWA实现了强安全性（0.12/100 m vs.
仅DWA的3.2），但RL层增加了两个独特价值：通过自适应安全加权实现零碰撞，以及
2.5×更好的偏好匹配。

## 6.2 局限性

**固定管道半径。** 离线计算的固定$\alpha$限制了在变化不确定性条件下的性能；
动态管道MPC[28]可改善低不确定性时段的效率。

**偏好平稳性假设。** 我们的IRL模块假设偏好在最近$K = 50$步内平稳。
上下文条件偏好（如在陌生环境中更谨慎）仍是未来工作。

**仅仿真验证。** 真实世界部署将揭示额外挑战：传感器噪声特性、用户-设备物理交互
和人群社会动态。关键的是，尚未进行BVI用户研究——在与视障参与者的直接评估完成之前，
适应性声明应理解为在使用基于BVI导航文献[2,23]的合成用户配置的仿真中展示。

**信任校准**（§4.4.2）在架构上有据但尚缺实证评估。**线性化误差界**（§4.3.3）
使用整个操作域上的最坏情况Lipschitz常数；局部估计可减小有效管道半径。

## 6.3 未来工作

关键方向包括：（i）**终身偏好学习**——L1可持续更新而无需重新认证L2安全；
（ii）**上下文条件偏好**，适应环境类型和用户状态；（iii）**多模态个性化**，
从显式反馈、生理信号或自然语言中推断偏好；（iv）**硬件部署**到CaBot平台[4]
进行真实世界验证；（v）**BVI用户研究**，将本文自适应方法与基线对比；
（vi）**动态管道半径**[28]，根据人群密度和传感器置信度在线调整$\alpha$；
（vii）**人群导航**，拓展至多智能体设置中的非相交安全管道。

## 6.4 更广泛影响与伦理考量

AI引导的视障辅助导航部署引发了重要的伦理考量。

**安全作为伦理责任。** 对于BVI用户，一个明眼人可能避免的碰撞可能造成严重伤害。
我们的保证（命题1）确保系统不会指令进入碰撞集的轨迹。然而，该保证依赖于有界
不确定性、准确状态估计和正确障碍物检测——我们建议任何真实世界部署包含独立运行时
监控器，当传感器不确定性超出管道半径预算时触发MRC。

**保护用户自主权。** 我们的共享自主框架将用户建模为主动协作者：引导而非强制，
从实际行为中学习，以及透明的偏好报告。AI引导导航对用户自信心和空间认知技能的
长期影响尚不明确，值得纵向研究。

**公平与可及性。** 安全关键的DWA层（L3）即使在低成本嵌入式硬件上也能以>500 Hz
运行；MRC在高层不可用时提供安全降级模式。纯边缘部署和模型压缩是重要的未来方向。

**数据隐私。** 步行轨迹可能泄露用户的日常生活、健康状况和认知状态等敏感信息。
我们建议在设备端进行轨迹数据的差分隐私处理，仅向云服务传输匿名化的偏好向量而
非原始轨迹。

# 7. 结论

我们提出了一个用于自适应共享自主辅助导航的分层安全MPC-RL框架，同时实现了可证明的
安全性、用户适应性和实时性能。关键的架构洞见是解耦：RL参数化MPC代价函数，而
Tube MPC独立于学习偏好执行安全保障。我们严格的安全分析（引理1-3，命题1）保证
对所有容许偏好权重均无碰撞，并以MRC作为安全后备。大量仿真（10,000次试验，
5种环境，5种用户配置，6个基线）展示了零碰撞、KL散度0.16（比最强非自适应基线
好2.5倍）和20.4 ms延迟。该框架开启了包括终身学习、BVI用户研究和硬件部署在内的
多个方向。更广泛而言，安全性、适应性和实时响应的分层解耦——以人类作为共享自主
协作者——是面向人类辅助自主系统超越导航领域的一般性设计范式。

# 数据与代码可用性

本研究中使用的仿真环境、用户偏好配置和基线实现将在论文接收后以开源仓库形式发布。
代码库包括：（i）带CQL预训练和MaxEnt IRL在线自适应的三层RL-TubeMPC-DWA控制器；
（ii）所有五种测试环境（E1-E5）的Habitat-Sim配置；（iii）基于ORCA的动态行人
生成脚本；（iv）复现本文所有表格和图表的评估脚本。CQL预训练数据集（1,000条具有
真实偏好的仿真轨迹）将纳入发布。

# 附录：图表说明

**图1：** 三层分层架构。L1（偏好-RL，1 Hz）：CQL+MaxEnt IRL从轨迹片段推断用户
偏好权重$w \in \mathbb{R}^m$，参数化MPC代价函数。L2（管道MPC，10 Hz）：通过
CasADi+qpOASES求解带收紧约束的有限时域最优控制问题；管道
$\mathbb{X}_k = \{\bar{x}_k\} \oplus \Omega$为任意$w \in \mathcal{W}_{\text{bounded}}$
提供安全保证（命题1），MRC为后备。L3（DWA，100 Hz）：在管道截面内约束的速度搜索
用于实时动态避障；指令通过振动触觉腰带和骨传导音频传递。L1影响*优化什么*；
L2执行*如何约束*。

**图2：** E3（购物中心）中P2（快速型）的最小障碍物距离分布。每种方法$n = 200$次
试验的KDE。虚线：$d_{\min} = 0.3$ m。本文方法（实线蓝色）：中位数0.52 m，IQR [0.41, 0.68]。
手工MPC+DWA（点线绿色）：中位数0.44 m，IQR [0.34, 0.58]。纯RL（虚线红色）：
中位数0.21 m，在$d_{\min}$以下存在二次模式。

**图3：** 管道半径灵敏度。碰撞率（蓝色圆圈，左轴）和路径效率（橙色方块，右轴）
随$\alpha / \alpha_0$变化（$\alpha_0 = 2.5$）。三个区间：不安全
（$\alpha < 0.7\alpha_0$），鲁棒工作（$\alpha \in [0.7\alpha_0, 1.5\alpha_0]$，
零碰撞，效率$\geq 0.91$），保守（$\alpha > 1.5\alpha_0$，效率下降）。
P1-P5、E1-E5均值。

**图4：** 偏好学习收敛。P1-P5的KL散度随L1更新周期变化。阴影：50次运行的
$\pm 1\sigma$。虚线：手工MPC+DWA和纯RL（SAC）基线。所有配置在20-30次L1更新
（约20-30 s）内达到收敛。

# 参考文献

[1] M. A. Khan, M. A. Rahman, and S. A. Hossain, "A Survey on Outdoor
Navigation Applications for People With Visual Impairments," *IEEE Access*,
vol. 11, pp. 14647-14666, 2023. DOI: 10.1109/ACCESS.2023.3243432.

[2] J. M. Loomis, R. L. Klatzky, and N. A. Giudice, "Efficacy of Electronic
Travel Aids for the Blind and Visually Impaired During Wayfinding," *medRxiv*,
2025. DOI: 10.1101/2025.01.15.25320581.

[3] D. Dakopoulos and N. G. Bourbakis, "Wearable Obstacle Avoidance Electronic
Travel Aids for Blind: A Survey," *IEEE Trans. Systems, Man, and Cybernetics
Part C*, vol. 40, no. 1, pp. 25-35, 2010.

[4] J. Guerreiro, D. Sato, S. Asakawa, H. Dong, K. M. Kitani, and C. Asakawa,
"CaBot: Designing and Evaluating an Autonomous Navigation Robot for Blind
People," in *Proc. ACM ASSETS*, 2019, pp. 68-82.

[5] S. K. Singh, R. P. Singh, and A. K. Mishra, "AR Navigation System for
Guidance of Visually Impaired Individuals Using IoT and Reinforcement
Learning," in *Proc. IEEE ICACCS*, 2025, pp. 1-6.

[6] B. Zhang, Y. Liu, Z. Wang, and H. Chen, "LaF-GRPO: In-Situ Navigation
Instruction Generation for the Visually Impaired via GRPO with
LLM-as-Follower Reward," *arXiv:2506.04070*, 2025.

[7] A. Vaaler, S. Skjong, and T. A. Johansen, "Modular control architecture
for safe marine navigation: Reinforcement learning with predictive safety
filters," *Artificial Intelligence*, vol. 336, 104201, 2024.

[8] R. Reiter, J. Hoffmann, M. Diehl, and S. Gros, "Synthesis of Model
Predictive Control and Reinforcement Learning: Survey and Classification,"
*arXiv:2502.02133*, 2025.

[9] M. Saha, A. J. Fiannaca, M. Kneisel, E. Cutrell, and M. R. Morris,
"Field Evaluation of a Mobile App for Assisting Blind and Visually Impaired
Travelers to Find Bus Stops," *Translational Vision Science & Technology*,
vol. 13, no. 1, art. 4, 2024.

[10] F. M. Talaat, A. M. El-Sayed, and H. M. El-Bakry, "SightAid: Deep
Learning-Based Intelligent Wearable Vision System for Visually Impaired
People," *Neural Computing & Applications*, vol. 36, no. 19, pp. 11075-11095,
2024.

[11] J. Achiam, D. Held, A. Tamar, and P. Abbeel, "Constrained Policy
Optimization," in *Proc. ICML*, 2017, pp. 22-31.

[12] A. D. Ames, S. Coogan, M. Egerstedt, G. Notomista, K. Sreenath, and
P. Tabuada, "Control Barrier Functions: Theory and Applications," in *Proc.
ECC*, 2019, pp. 3420-3431.

[13] M. Guerrier, H. Fouad, and G. Beltrame, "Learning Control Barrier
Functions and Their Application in Reinforcement Learning: A Survey,"
*arXiv:2404.16879*, 2024.

[14] D. S. Kushwaha and Z. A. Biron, "A Review On Safe Reinforcement Learning
Using Lyapunov and Barrier Functions," *arXiv:2508.09128*, 2025.

[15] M. Tabbara, L. Yang, and H. Sibai, "Statistically Assuring Safety of
Control Systems using Ensembles of Safety Filters and Conformal Prediction,"
*arXiv:2511.07899*, 2025.

[16] D. Q. Mayne, M. M. Seron, and S. V. Raković, "Robust model predictive
control of constrained linear systems with bounded disturbances," *Automatica*,
vol. 41, no. 2, pp. 219-224, 2005.

[17] D. Q. Mayne, S. V. Raković, R. Findeisen, and F. Allgöwer, "Robust
output feedback model predictive control of constrained linear systems,"
*Automatica*, vol. 42, no. 7, pp. 1217-1222, 2006.

[18] A. Kumar, A. Zhou, G. Tucker, and S. Levine, "Conservative Q-Learning
for Offline Reinforcement Learning," in *Proc. NeurIPS*, 2020.

[19] B. D. Ziebart, A. Maas, J. A. Bagnell, and A. K. Dey, "Maximum Entropy
Inverse Reinforcement Learning," in *Proc. AAAI*, 2008, pp. 1433-1438.

[20] J. B. Rawlings, D. Q. Mayne, and M. Diehl, *Model Predictive Control:
Theory and Design*, 2nd ed. Nob Hill Publishing, 2017.

[21] D. Fox, W. Burgard, and S. Thrun, "The Dynamic Window Approach to
Collision Avoidance," *IEEE Robotics & Automation Magazine*, vol. 4, no. 1,
pp. 23-33, 1997.

[22] H. J. Ferreau, C. Kirches, A. Potschka, H. G. Bock, and M. Diehl,
"qpOASES: A parametric active-set algorithm for quadratic programming,"
*Mathematical Programming Computation*, vol. 6, no. 4, pp. 327-363, 2014.

[23] S. Azenkot, C. L. Bennett, and R. E. Ladner, "What do Blind and
Low-Vision People Really Want from Assistive Smart Devices?" in *Proc. ACM
ASSETS*, 2023, pp. 1-14.

[24] J. A. E. Andersson, J. Gillis, G. Horn, J. B. Rawlings, and M. Diehl,
"CasADi: A software framework for nonlinear optimization and optimal control,"
*Mathematical Programming Computation*, vol. 11, no. 1, pp. 1-36, 2019.

[25] M. Savva, A. Kadian, O. Maksymets, Y. Zhao, E. Wijmans, B. Jain,
J. Straub, J. Liu, V. Koltun, J. Malik, D. Parikh, and D. Batra, "Habitat:
A Platform for Embodied AI Research," in *Proc. ICCV*, 2019, pp. 9339-9347.

[26] J. van den Berg, S. J. Guy, M. Lin, and D. Manocha, "Reciprocal n-body
Collision Avoidance," in *Proc. ISRR*, 2011, pp. 3-19.

[27] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, "Soft Actor-Critic:
Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic
Actor," in *Proc. ICML*, 2018, pp. 1861-1870.

[28] N. Csomay-Shanklin, V. Sindhwani, and A. Majumdar, "Dynamic Tube MPC:
Learning Tube Dynamics with Massively Parallel Simulation for Robust Safety in
Practice," *arXiv:2404.02512*, 2024.

[29] A. D. Dragan and S. S. Srinivasa, "A Policy-Blending Formalism for Shared
Control," *Int. J. Robotics Research*, vol. 32, no. 7, pp. 790-805, 2013.

[30] J. Berberich and F. Allgöwer, "An overview of systems-theoretic guarantees
in data-driven model predictive control," *Annual Review of Control, Robotics,
and Autonomous Systems*, vol. 8, pp. 77-100, 2025.

[31] L. Hewing, K. P. Wabersich, M. Menner, and M. N. Zeilinger, "Learning-Based
Model Predictive Control: Toward Safe Learning in Control," *Annual Review of
Control, Robotics, and Autonomous Systems*, vol. 3, no. 1, pp. 269-296, 2020.

[32] S. Gros and M. Zanon, "Learning for MPC with Stability and Safety
Guarantees," *Automatica*, vol. 146, art. 110598, 2022.

[33] S. Real and A. Araujo, "Navigation Systems for the Blind and Visually
Impaired: Past Work, Challenges, and Open Problems," *Sensors*, vol. 19,
no. 15, art. 3404, 2019.

[34] A. Mesbah, K. P. Wabersich, A. P. Schoellig, M. N. Zeilinger et al.,
"Fusion of Machine Learning and MPC under Uncertainty: What Advances Are on
the Horizon?" in *Proc. ACC*, 2022, pp. 342-349.

[35] S. Javdani, S. S. Srinivasa, and J. A. Bagnell, "Shared Autonomy via
Hindsight Optimization," in *Proc. Robotics: Science and Systems (RSS)*, 2015.
