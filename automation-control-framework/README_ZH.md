# 自动化与控制 · 知识蒸馏框架

[English](README.md)

面向**自动化与控制工程**领域的 Claude Code 知识蒸馏技能——将 6 个子领域、300+ 篇论文的核心知识提炼为可导航的框架：7 个方法论共识、6 条学派分歧与融合趋势、5 层技术栈模型。

---

## 这是什么

这是自动化与控制领域的**研究导航与知识索引**。它不生成新内容——而是帮你快速定位核心论文、理解方法论格局、识别你的工作在学术谱系中的位置。

## 领域覆盖（六维调研）

```
  强化学习控制 (RL)  ← 策略层
  鲁棒控制 · 自适应控制 · MPC  ← 控制层
  导盲辅助 (BVI)  ← 应用层
  自主导航  ← 执行层
```

| 维度 | 核心主题 |
|------|---------|
| **导航** | SLAM、路径规划、传感器融合、学习导航 |
| **导盲辅助** | 计算机视觉、穿戴式传感器、人机交互反馈、室内定位 |
| **鲁棒控制** | H∞、μ 综合、滑模控制、LMI、小增益定理 |
| **自适应控制** | MRAC、反步法、ILC、L1、极值搜索 |
| **MPC** | 线性/NMPC、Tube MPC、数据驱动 MPC、RL+MPC 融合 |
| **RL 控制** | PPO、SAC、安全 RL、MBRL、Sim-to-Real |

## 提炼成果

### 7 个核心方法论共识
1. **反馈是控制的灵魂** — 跨域不变量
2. **模型不确定性决定性能上界** — 从鲁棒到 RL 的统一约束
3. **稳定性与最优性的权衡** — 根本性张力
4. **学习补充而非替代结构** — 混合方法胜出
5. **安全需要显式约束** — 不能只靠 Reward Shaping
6. **数据质量 > 数据数量** — 自适应/学习控制中尤为关键
7. **实机验证不可替代** — Sim-to-Real Gap 是真实的

### 6 条学派分歧与融合趋势
1. 基于模型 vs. 免模型 → 走向**模型知情 (model-informed)**
2. 鲁棒 vs. 自适应 → 走向**鲁棒自适应 (robust-adaptive)**
3. 集中式 vs. 分散式 → 任务依赖，无普适赢家
4. 线性 vs. 非线性 → **增益调度 + LPV** 作为务实桥梁
5. 最优性 vs. 可解性 → **MPC + 学习** 作为新兴解决方案
6. 理论优先 vs. 实验优先 → **仿真在环 (simulation-in-the-loop)** 硬化

### 5 层技术栈模型
| 层级 | 功能 | 核心方法 |
|------|------|---------|
| **策略层** | 高层决策与学习 | RL、博弈论、元学习 |
| **规划层** | 轨迹与路径生成 | MPC、优化、采样法 |
| **控制层** | 底层驱动与稳定 | 鲁棒、自适应、非线性 |
| **感知层** | 状态估计与传感 | SLAM、计算机视觉、传感器融合 |
| **执行层** | 物理具身与驱动 | 电机控制、触觉、运动学 |

---

## 适用场景

- 在自动化与控制研究中快速定位方法论方向
- 理解你的工作在方法论谱系中的位置
- 在 6 个子领域中查找核心论文
- 在共识/分歧边界处识别研究缺口
- 作为下游论文写作的知识库（配合 [paper-writing-agent](../paper-writing-agent/)）

## 不适用场景

- 直接写论文 → 使用 [academic-paper](../academic-research-skills/academic-paper/) 或 [paper-writing-agent](../paper-writing-agent/)
- 开展新的文献检索 → 使用 [deep-research](../academic-research-skills/deep-research/)
- 评审论文 → 使用 [academic-paper-reviewer](../academic-research-skills/academic-paper-reviewer/)

---

## 目录结构

```
automation-control-framework/
├── README_ZH.md                 # 本文件（中文）
├── README.md                    # English version
├── SKILL.md                     # 技能定义（中文，309行）
├── SKILL_EN.md                  # 技能定义（英文，315行）
└── references/
    └── research/
        ├── 01-navigation.md     # 自主导航调研
        ├── 02-blind-guidance.md # 导盲辅助调研
        ├── 03-robust-control.md # 鲁棒控制调研
        ├── 04-adaptive-control.md # 自适应控制调研
        ├── 05-rl-control.md     # 强化学习控制调研
        └── 06-mpc.md            # 模型预测控制调研
```

## 安装

```bash
# 克隆到 Claude Code skills 目录
git clone <本仓库地址> ~/.claude/skills/automation-control-framework

# 或创建符号链接
ln -s $(pwd)/automation-control-framework ~/.claude/skills/automation-control-framework
```

## 依赖

- Claude Code v3.7.0+
- 无需 Python 依赖
- 参考文献均为独立 Markdown 文件

## 相关技能

- [academic-research-skills](../academic-research-skills/) — 完整学术管线（调研→写作→评审）
- [paper-writing-agent](../paper-writing-agent/) — 领域特化论文写作协调
- [nuwa-skill](../nuwa-skill/) — 蒸馏任意人物的思维框架

## 许可证

参见 [SKILL.md](SKILL.md) 头部声明。
