# 对话总结：翻译任务与引文分析

**日期**：2026-05-19

---

## 一、完成的任务

### 1.1 SKILL.md 中译英

- **源文件**：`learning/SKILL.md`（自动化与控制领域知识蒸馏框架，~310 行）
- **输出文件**：`learning/SKILL_EN.md`
- **内容**：领域全景图、7 项核心方法论共识、6 条学派分歧、5 层技术栈模型、论文速查表、诚实边界、附录
- **关键处理**：ASCII 架构图中的中文标签 → 英文，所有表格表头与内容翻译，文献引用信息保留原文

### 1.2 paper_draft.md 英译中

- **源文件**：`paper/paper_draft.md`（英文学术论文初稿，725 行，30 篇参考文献）
- **输出文件**：`paper/paper_draft_zh.md`
- **内容**：完整 7 章节学术论文（引言 → 相关工作 → 问题建模 → 方法 → 实验 → 讨论 → 结论）
- **关键处理**：
  - 数学符号与公式**原样保留**
  - ASCII 架构图标签翻译，结构不动
  - 参考文献中 `et al.` → "等人"，`and` → "和"
  - 文献标题与期刊名保留原文

### 1.3 参考文献年份分析

- **引用总数**：30 篇
- **年份跨度**：1997（DWA 原始论文）至 2025（最新 arXiv preprint）
- **年代分布**：

| 年代 | 篇数 | 占比 |
|------|:----:|:----:|
| 1990s | 1 | 3.3% |
| 2000s | 3 | 10.0% |
| 2010s | 6 | 20.0% |
| 2020s | 20 | 66.7% |

- **2024-2025 两年合计**：15 篇（50%）
- **中位数年份**：≈ 2022

- **主要问题**：
  1. 引文过度集中于近两年，经典奠基文献不足
  2. 2025 年 8 篇中 3 篇为 arXiv preprint，缺少同行评议
  3. 缺失 Mayne et al. 2000（10000+ 引用）、Sutton & Barto、DQN 2015、DGKF 1989 等关键经典

---

## 二、术语翻译对照表

### 2.1 控制理论

| 英文 | 中文 |
|------|------|
| Tube MPC | 管道模型预测控制 |
| Robust positively invariant (RPI) set | 鲁棒正不变集 |
| Safety filter | 安全过滤器 |
| Control Barrier Function (CBF) | 控制屏障函数 |
| Constrained Policy Optimization (CPO) | 约束策略优化 |
| Receding horizon | 滚动时域 |
| Pontryagin difference | Pontryagin 差 |
| Ancillary controller | 辅助控制器 |
| Tightened constraints | 收紧约束 |
| Lyapunov equation | Lyapunov 方程 |
| Small gain theorem | 小增益定理 |
| Sliding Mode Control (SMC) | 滑模控制 |
| Backstepping | 反步法 |
| Model Reference Adaptive Control (MRAC) | 模型参考自适应控制 |
| Extremum Seeking Control (ESC) | 极值搜索控制 |
| Iterative Learning Control (ILC) | 迭代学习控制 |

### 2.2 导航与感知

| 英文 | 中文 |
|------|------|
| SLAM (Simultaneous Localization and Mapping) | 同时定位与建图 |
| Dynamic Window Approach (DWA) | 动态窗口法 |
| Electronic Travel Aid (ETA) | 电子出行辅助工具 |
| Loop closure | 回环检测 |
| Bundle Adjustment (BA) | 光束法平差 |
| Sensor fusion | 传感器融合 |
| Path planning | 路径规划 |
| Nonholonomic system | 非完整系统 |

### 2.3 强化学习与机器学习

| 英文 | 中文 |
|------|------|
| Conservative Q-Learning (CQL) | 保守 Q 学习 |
| Soft Actor-Critic (SAC) | 软 Actor-Critic |
| Maximum Entropy Inverse RL | 最大熵逆强化学习 |
| Offline RL / Offline Reinforcement Learning | 离线强化学习 |
| Sim-to-Real | 仿真到真实迁移 |
| Domain randomization | 领域随机化 |
| Preference learning | 偏好学习 |
| Safety-critical control | 安全关键控制 |

### 2.4 辅助技术

| 英文 | 中文 |
|------|------|
| Visually impaired | 视障人士 |
| Blind and Low-Vision | 盲人与低视力 |
| Assistive navigation | 辅助导航 |
| Personalized | 个性化的 |
| Wearable device | 可穿戴设备 |
| Human-robot interaction | 人机交互 |
| User preference profile | 用户偏好配置 |

### 2.5 论文常用短语

| 英文 | 中文 |
|------|------|
| Proof sketch | 证明概要 |
| Remark | 注 |
| Proposition | 命题 |
| Ablation study | 消融实验 |
| Baseline | 基线（方法） |
| Hard/soft constraint | 硬约束 / 软约束 |
| Ground truth | 地面真值 |
| Formal guarantees | 形式化保证 |
| Ad hoc | 临时性的 |
| Trilemma | 三难困境 |

### 2.6 方法论共识（来自 SKILL.md）

| 英文 | 中文 |
|------|------|
| Core consensus | 核心共识 |
| School divergence | 学派分歧 |
| Technology stack model | 技术栈模型 |
| Honest boundaries | 诚实边界 |
| Knowledge distillation | 知识蒸馏 |
| Cross-domain evidence | 跨域证据 |
| Core claim | 核心主张 |

---

## 三、生成/修改的文件清单

| 文件 | 操作 | 说明 |
|------|:--:|------|
| `learning/SKILL_EN.md` | 新建 | SKILL.md 的英文翻译 |
| `paper/paper_draft_zh.md` | 新建 | 英文学术论文的中文翻译 |
| `docx/translation_and_analysis_2026-05-19.md` | 新建 | 本文档 |

---

*文档生成日期：2026-05-19*
