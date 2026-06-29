# Paper Writing Agent（论文写作代理）

[English](README.md)

**通用型** Claude Code 学术论文写作协调技能——从原始研究材料到可投稿终稿，附期刊推荐策略。适用于任何学科领域。

## 概述

`paper-writing-agent` 是一个**通用协调层**，连接三个组件形成统一写作管线：

| 组件 | 角色 |
|------|------|
| **用户材料** | 用户上传的全部文档——草稿、笔记、数据、参考文献、领域知识 |
| **academic-paper**（v3.1.2） | 12-agent 论文写作管线 — 10 种模式、6 种论文结构（IMRaD/综述/理论/案例研究/政策简报/会议论文）、5 种引用格式（APA/Chicago/IEEE/MLA/GB/T 7714） |
| **academic-paper-reviewer**（v1.9.1） | 7-agent 多角色评审 — 主编 + 3 位同行评审 + 魔鬼代言人，0–100 分量表 |

本代理的核心价值在于**系统化协调**：在调用通用写作/评审管线之前，先完成材料分析、文献匹配、引用图谱构建和研究缺口分析，在任何学科领域都能产生更精准、更有深度的输出。

## 运行流程（8 阶段）

```
Phase 0：领域识别   →  从用户材料自动识别学科、子领域、方法论类型
Phase 1：材料分析   →  提取核心观点、创新点、方法框架、关键假设
Phase 2：文献检索   →  本地优先 → Google Scholar / arXiv / Semantic Scholar
Phase 3：引用图谱   →  构建引用关系图（延续/对比/泛化/分歧）
Phase 4：研究缺口   →  已解决 / 部分解决 / 未解决问题分类
Phase 5：写作简报   →  汇总简报 → 委托 academic-paper 撰写初稿
Phase 6：评审       →  委托 academic-paper-reviewer（5 份独立评审）
Phase 7：迭代修订   →  修订循环（最多 3 轮，有界迭代）
Phase 8：终稿与推荐 →  格式化输出（LaTeX/DOCX/PDF）+ 期刊推荐
```

**终止条件**：评分 ≥80（接收）/ 达到 3 轮评审上限 / 连续 2 轮评分改善 < 5 分 / 用户手动终止。

## 目录结构

```
paper-writing-agent/
├── SKILL.md                     # 技能定义（8 阶段完整流程）
├── README.zh-CN.md              # 本文件（中文）
├── README.md                    # English version
├── references/                  # 研究材料
│   ├── citation_graph.md        # 引用关系图
│   ├── journal_recommendations.md # 期刊推荐
│   ├── literature_map.md        # 文献覆盖地图
│   ├── material_analysis.md     # 原始材料分析
│   ├── research_gaps.md         # 识别的研究缺口
│   ├── writing_brief.md         # 写作简报（供 academic-paper 使用）
│   └── review_round2.md         # 第二轮评审报告
├── need/                        # 缺失数据标注
└── older/                       # 历史版本归档（v0.1, v0.2, ...）
```

> **注意：** 本技能依赖 [academic-research-skills](../academic-research-skills/)（v3.9.2），需安装在同一父目录下。

## 适用场景

- 从多个文档、草稿、笔记中系统化撰写学术论文
- 管理写作—评审—修订的完整生命周期
- 需要精准的文献对齐和引用图谱构建
- 需要版本管理和可追溯的迭代流程
- 在投稿前获得模拟同行评审
- 基于论文内容匹配最适合的期刊

## 不适用场景

- 仅需深度调研而不写论文 → 直接使用 `deep-research`
- 仅需评审已有论文 → 直接使用 `academic-paper-reviewer`
- 需要含完整性检查的全自动端到端管线 → 使用 `academic-pipeline`
- 快速写短文/博客 → 直接使用 `academic-paper`

## 委托模型

```
paper-writing-agent（协调层）
    │
    ├── Phase 0–4：本地分析（用户材料驱动）
    ├── Phase 5：   ──委托──→ academic-paper（12-agent 写作）
    ├── Phase 6：   ──委托──→ academic-paper-reviewer（7-agent 评审）
    ├── Phase 7：   ──委托──→ academic-paper（修订模式）
    └── Phase 8：   ──委托──→ academic-paper（格式转换）+ 期刊推荐
```

## 核心原则

1. **证据驱动** — 每个主张必须有文献或数据支撑。缺乏证据时标注至 `need/`，绝不编造。
2. **用户材料优先** — 所有分析从用户上传的材料起步，联网搜索仅补缺口。
3. **委托专长** — 写作委托给 `academic-paper`，评审委托给 `academic-paper-reviewer`，不做重复造轮子。
4. **版本可追溯** — 每次修订产生新版本号，旧版完整保留在 `older/`，绝不覆盖。
5. **迭代有界** — 最多 3 轮 external review。3 轮后仍未达标时，汇总未解决问题交用户决策。
6. **学科自适应** — Phase 0 从用户材料中自动识别领域，不预设任何特定学科的知识结构。

## 期刊推荐框架

基于五个维度推荐目标期刊：

| 维度 | 评估标准 |
|------|---------|
| 主题匹配 | 论文主题是否在期刊 scope 内？ |
| 方法偏好 | 期刊偏好理论深度还是实证结果？ |
| 创新层级 | 增量改进 → 三区；显著突破 → 二区；领域定义 → 一区 |
| 引用来源 | 论文的核心引用发表于哪些期刊？→ 优先投这些 |
| 领域惯例 | 该领域公认的顶刊/顶会是什么？ |

## 安装

1. 克隆完整的 `distillation-skills` 仓库：
   ```bash
   git clone <仓库地址> ~/.claude/skills/distillation-skills
   ```

2. Claude Code 检测到技能目录时自动加载。确保 `paper-writing-agent/` 和 `academic-research-skills/` 在同一父目录下。

3. 将你的领域参考文献放在工作目录中——代理会在 Phase 0 自动检测和使用它们。

## 依赖

本技能需要 [academic-research-skills v3.9.2](../academic-research-skills/)（安装于父目录），提供：

- `deep-research`（v2.9.4）— 13-agent 深度研究团队
- `academic-paper`（v3.1.2）— 12-agent 论文写作管线
- `academic-paper-reviewer`（v1.9.1）— 多角色论文评审
- `academic-pipeline`（v3.9.2）— 全流程编排器

## 许可证

参见 [SKILL.md](SKILL.md) 头部声明。继承自父项目。

## 作者

吳政毅（Cheng-I Wu）— [@Imbad0202](https://github.com/Imbad0202)
