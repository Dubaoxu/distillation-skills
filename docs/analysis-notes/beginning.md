# 项目起始文档：控制与导航领域知识蒸馏与学术论文撰写

## 项目概述

本项目旨在系统性地收集、整理和蒸馏控制理论与辅助导航领域的权威学术文献，构建结构化的知识框架，并在此基础上撰写可发表的学术论文。项目结合了两种方法论工具——**nuwa-skill**（女娲·技能，用于将领域知识蒸馏为可运行的 AI 技能框架）和 **Academic Research Skills v3.9.2**（ARS，用于学术研究的全流程支持）。

---

## 1. 项目时间线

| 阶段 | 日期 | 内容 |
|------|------|------|
| 工具安装 | 2026-05-19 | 安装 nuwa-skill 和 ARS v3.9.2 |
| 文献收集 | 2026-05-19 | 六大领域权威论文系统性搜索与整理 |
| 知识蒸馏 | 2026-05-19 | 提取7项核心共识原则、6项关键分歧、5层技术栈 |
| 热点分析 | 2026-05-19 | 识别当前控制方向研究热点与可撰写论文方向 |
| 论文撰写 | 2026-05-19 | 完成完整7章节英文学术论文初稿 |
| 论文翻译 | 2026-05-19 | 完成中文学术论文翻译稿 |
| 同行评审 | 2026-05-19 | ARS 7-agent 全流程模拟评审，5/5 审稿人建议大修 |

---

## 2. 文献收集范围

项目涵盖六大核心领域的权威论文，共计约 430 篇文献：

### 2.1 导航领域（Navigation）
- 论文数量：约 100 篇
- 核心脉络：SLAM 谱系（Smith/Cheeseman 1990 → FastSLAM → MonoSLAM/PTAM → ORB-SLAM → NeRF/3DGS SLAM）
- 关键方法：A*、RRT、DWA、VINS-Mono、因子图优化
- 文献位置：`learning/references/research/01-navigation.md`

### 2.2 导盲领域（Blind Guidance）
- 论文数量：约 80 篇
- 核心脉络：17 篇综述、经典 ETA、商业系统（CaBot、NOA、All_Aboard、Envision、Seeing AI）
- 研究方向：可穿戴设备、计算机视觉、深度学习、传感器融合、HCI 反馈
- 文献位置：`learning/references/research/02-blind-guidance.md`

### 2.3 鲁棒控制（Robust Control）
- 论文数量：约 40 篇
- 核心脉络：H∞ 基础（Zames 1981、DGKF 1989）→ μ-synthesis → 滑模控制（Utkin、Edwards & Spurgeon）→ LMI 方法（Boyd et al. 1994）→ 鲁棒 MPC
- 文献位置：`learning/references/research/03-robust-control.md`

### 2.4 自适应控制（Adaptive Control）
- 论文数量：约 80 篇
- 核心脉络：MRAC、STR、Backstepping、NN/模糊自适应、ILC、L1 自适应、极值搜索
- 文献位置：`learning/references/research/04-adaptive-control.md`

### 2.5 强化学习控制（RL Control）
- 论文数量：约 80 篇
- 核心脉络：Model-free（PPO/SAC/TD3/DDPG）、Model-based（Dreamer v1-3、MBPO、PETS）、Safe RL、RL+MPC 融合、Offline RL、Sim-to-Real
- 文献位置：`learning/references/research/05-rl-control.md`

### 2.6 模型预测控制（MPC）
- 论文数量：约 50 篇
- 核心脉络：IDCOM/DMC/GPC → 线性 MPC 理论 → NMPC/RTI → Tube MPC（2005）→ 随机/经济/分布式 MPC → Koopman/DeePC（2019-2025）
- 文献位置：`learning/references/research/06-mpc.md`

---

## 3. 知识蒸馏成果

使用 nuwa-skill 的三重验证方法论（跨域复现性、生成能力、排他性），从 430+ 篇论文中蒸馏出：

### 3.1 七项核心共识原则
1. **反馈是控制的灵魂**：所有控制方法的共性基础
2. **模型精度与鲁棒性的权衡谱系**：从精确模型到无模型控制的连续谱
3. **约束处理为第一优先级**：安全关键系统中硬约束优先于性能优化
4. **不确定性量化**：确定性鲁棒与概率随机方法的统一视角
5. **数据与模型融合**：Learning-based 与 Model-based 的互补不可替代
6. **实时硬约束**：计算可行性与控制性能的工程折衷
7. **分层分解**：复杂控制问题按时间尺度和抽象层次分解

### 3.2 五层技术栈模型
```
Layer 5: 决策规划层（Decision & Planning）
Layer 4: 约束安全层（Constraint & Safety）
Layer 3: 控制综合层（Control Synthesis）
Layer 2: 感知与估计层（Perception & Estimation）
Layer 1: 物理建模层（Physical Modeling）
```

### 3.3 知识框架文件
- 完整蒸馏报告：`learning/SKILL.md`
- 包含：核心共识、关键分歧、技术栈、论文速查表、诚实边界

---

## 4. 研究热点与可撰写方向

基于对六大领域文献的综合分析，识别出以下当前控制方向研究热点：

### 4.1 热点主题
- **Koopman MPC**：数据驱动的非线性系统线性化表示（2019-2025 爆发期）
- **Safe RL + MPC 融合**：三原型分类（MPC as Expert/Actor/Critic），Reiter et al. 2025
- **DeePC（Data-enabled Predictive Control）**：完全数据驱动的预测控制，Berberich & Allgöwer 2025
- **NeRF/3DGS SLAM**：神经渲染替代传统几何建图
- **CBF + Learning**：从数据自动合成控制屏障函数
- **Foundation Models for Robotics**：大语言/视觉模型作为高层规划器

### 4.2 可撰写论文方向
1. **安全 MPC-RL 混合控制用于导盲导航**（本次选定的撰写方向）
2. Koopman 算子辅助的模型预测控制
3. 基于 CBF 的安全强化学习与形式化验证
4. 大模型驱动的自主导航决策系统
5. 多模态感知融合的鲁棒自适应控制

---

## 5. 论文撰写

### 5.1 选定方向
**方向 1：面向视障行人个性化辅助导航的分层安全 MPC-RL 框架**

### 5.2 核心架构
三层分层控制器：
- **L1（RL/CQL, 1 Hz）**：通过最大熵逆强化学习从行走轨迹中学习用户偏好特征权重
- **L2（Tube MPC, 10 Hz）**：通过鲁棒正不变集强制执行可证明安全性，约束收紧确保碰撞避免
- **L3（DWA, 100 Hz）**：在管道约束内处理动态障碍物，应急制动作为最后防线

### 5.3 关键理论洞察
RL 参数化 MPC 代价函数权重，而非直接控制输出——安全性可证明地独立于学习的偏好。

### 5.4 论文文件
- 英文原稿：`paper/paper_draft.md`（724 行，30 篇参考文献）
- 中文翻译：`paper/paper_draft_zh.md`（完整翻译）
- 7 个章节：引言 → 相关工作 → 问题形式化 → 方法 → 实验 → 讨论 → 结论

---

## 6. 同行评审结果

使用 ARS academic-paper-reviewer 的 **full mode**（7-agent 全流程）对论文初稿进行了模拟国际期刊评审：

### 6.1 审稿人配置
| 审稿人 | 角色 | 模拟身份 |
|--------|------|----------|
| Prof. Elena Vasconcelos | EIC（主编） | IEEE T-RO 资深编辑 |
| Prof. Kenji Taniguchi | 方法论审稿人 | 东京工业大学，Tube MPC 专家 |
| Dr. Sarah Okafor | 领域审稿人 | Smith-Kettlewell 眼科研究所，BVI 辅助技术专家 |
| Prof. Martin Lindqvist | 跨学科审稿人 | KTH 皇家理工学院，安全系统与自动驾驶专家 |
| Prof. David Rosenfeld | 魔鬼代言人 | CMU，以发现"致命缺陷"著称 |

### 6.2 评审决定
**Major Revision（大修）** — 5/5 审稿人一致

### 6.3 核心问题共识
1. **缺乏真实世界验证**（5/5）："个性化"声称建立在合成数据上，形成循环验证
2. **命题 1 证明不充分**（4/5）：缺少递归可行性证明、线性化误差界、W_bounded 定义
3. **"人作为扰动"框架不当**（4/5）：对辅助技术而言伦理和技术上不恰当
4. **三难困境论证薄弱**（3/5）：缺少手动调参基线证明 RL 层的必要性
5. **"87% 准确率"未定义**（3/5）：摘要中的数字与结果表格无对应关系

### 6.4 修订路线图
- **Tier 1（必须修改，6 项）**：含添加手动调参基线、修正证明、重新框架化"人作为扰动"等
- **Tier 2（应当修改，6 项）**：含多速率稳定性分析、用户界面定义、灵敏度分析等
- **Tier 3（建议修改，8 项）**：含近距统计、代码发布、参考文献修正等

### 6.5 可行性评估
论文具有真正的学术价值，三层解耦架构被所有审稿人认可为"优雅且可能重要"的设计。修订预计需 4 个月，建议策略为收窄范围（移除标题中"Personalized"）、强化分析、修正框架化。

### 6.6 评审文件
- 完整评审报告：`paper/review_report.md`
- 包含：5 份独立审稿报告 + 编辑综合决策包 + 修订路线图

---

## 7. 方法论工具

### 7.1 nuwa-skill（女娲·技能）
- 来源：GitHub alchaincyf/nuwa-skill
- 核心方法：6 阶段蒸馏流程（入口路由 → 需求诊断 → 6-agent 并行搜索 → 三重验证框架提取 → 技能构建 → 双 agent 精炼）
- 三重验证：跨域复现性（≥2 个不同领域）、生成能力（推断新问题的立场）、排他性（非所有聪明人都这样想）
- 本项目贡献：生成 `learning/SKILL.md` 知识框架

### 7.2 Academic Research Skills (ARS) v3.9.2
- 来源：GitHub Imbad0202/academic-research-skills
- 许可：CC BY-NC 4.0
- 4 模块：deep-research（13 agent）、academic-paper（12 agent）、academic-paper-reviewer（7 agent）、academic-pipeline（10 阶段编排器）
- 25 种模式，覆盖 fidelity/balanced/originality 谱系
- v3.9.2 新增：三索引交叉验证引用检测（S2 + OpenAlex + Crossref）

---

## 8. 文件结构

```
e:/distillation/
├── paper/
│   ├── paper_draft.md          # 英文学术论文初稿（724 行）
│   ├── paper_draft_zh.md       # 中文学术论文翻译稿
│   └── review_report.md        # ARS 同行评审完整报告
├── learning/
│   ├── SKILL.md                # nuwa-skill 知识蒸馏综合框架
│   └── references/research/
│       ├── 01-navigation.md    # 导航领域文献（约 100 篇）
│       ├── 02-blind-guidance.md # 导盲领域文献（约 80 篇）
│       ├── 03-robust-control.md # 鲁棒控制文献（约 40 篇）
│       ├── 04-adaptive-control.md # 自适应控制文献（约 80 篇）
│       ├── 05-rl-control.md    # 强化学习控制文献（约 80 篇）
│       └── 06-mpc.md           # MPC 文献（约 50 篇）
├── docx/
│   └── beginning.md            # 本文档——项目起始与总览
├── nuwa-skill-main/            # nuwa-skill 工具包
├── academic-research-skills-3.9.2/ # ARS v3.9.2 工具包
└── .claude/skills/             # 已安装的 ARS 技能符号链接
    ├── deep-research
    ├── academic-paper
    ├── academic-paper-reviewer
    └── academic-pipeline
```

---

## 9. 后续工作

1. **论文修订**：根据 ARS 评审报告的 Tier 1-3 路线图修订论文
2. **LaTeX 排版**：将论文转换为 LaTeX 格式并生成 PDF
3. **实验实施**：构建仿真环境（Habitat-Sim + ORCA 行人）
4. **真实用户研究**：规划并实施 BVI 参与者评估（论文未来工作部分）
5. **硬件部署**：与 CaBot 平台集成（论文未来工作部分）

---

*文档生成日期：2026-05-19*
*工具：nuwa-skill + Academic Research Skills v3.9.2*
