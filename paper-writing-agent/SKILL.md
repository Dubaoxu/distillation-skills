---
name: paper-writing-agent
description: |
  通用学术论文写作协调代理。
  加载用户提供的材料（论文草稿、研究笔记、参考文献等），提取观点与创新点，
  搜索并构建引用图谱，识别研究缺口，生成写作简报。
  撰写阶段委托给 academic-paper（12-agent 写作管线），
  评审阶段委托给 academic-paper-reviewer（7-agent 多角色评审），
  迭代修订至达标。旧版归档至 older/，缺失数据标注至 need/。
  最终输出终稿与期刊推荐策略。
  适用任何学科领域——从工程、计算机到人文社科。
---

# Academic Paper Writing Agent

## 定位

本 Skill 是**通用协调层**，连接三个组件：

| 组件 | 角色 |
|------|------|
| **用户材料** | 用户上传的全部文档：草稿、笔记、数据、参考文献、领域知识等 |
| **academic-paper** (v3.1.2) | 12-agent 论文写作管线（10 模式、IMRaD/综述/理论等 6 种结构、APA/Chicago/IEEE 等 5 种引用格式） |
| **academic-paper-reviewer** (v1.9.1) | 7-agent 多角色评审（EIC + 3 位同行评审 + Devil's Advocate，0-100 评分量表） |

本 Skill 的价值在于：**系统化协调** — 在启动通用写作管线之前，自动完成材料分析、文献匹配、引用图谱构建和研究缺口分析，让 academic-paper 和 academic-paper-reviewer 产生更精准、更有深度的输出。无论什么学科，流程统一，质量一致。

---

## 核心原则

1. **证据驱动**：每个主张必须有文献或数据支撑。不能提供证据时，标注至 `need/` 而非编造。
2. **用户材料优先**：所有分析从用户上传的材料起步，补充缺口时再联网搜索。
3. **委托专长**：写作委托给 `academic-paper`，评审委托给 `academic-paper-reviewer`，本 Skill 不做重复造轮子。
4. **版本可追溯**：每次修订产生新版本号，旧版完整保留在 `older/`。
5. **迭代有界**：最多 3 轮 external review。第 3 轮仍未达标时汇总未解决问题并交用户决策。
6. **学科无关**：流程设计不依赖特定领域知识。Phase 0 自动识别领域并从用户材料中提取领域上下文。

---

## 运行流程

### Phase 0：领域识别与材料加载

0.1 **领域识别**：从用户上传的材料中自动识别：
  - 学科领域（如计算机科学、控制工程、生物学、经济学等）
  - 子领域/研究方向
  - 方法论类型（理论分析 / 实验 / 仿真 / 实证 / 综述）
  - 核心术语和关键词

0.2 **材料扫描**：读取用户上传的全部文档，按类型归类：
  - **草稿**：已有论文文本（完整或片段）
  - **数据**：实验数据、调查结果、仿真结果
  - **笔记**：研究笔记、会议记录、idea 碎片
  - **参考文献**：用户已收集的论文、BibTeX、文献列表
  - **领域知识**：用户提供的领域调研、知识框架

0.3 **生成领域摘要**：基于以上分析，输出 3-5 句话的领域画像，确认理解正确，写入 `material_analysis.md` 开头。

0.4 将本地材料作为第一信源；仅在覆盖不足时发起联网检索。

### Phase 1：材料分析

1.1 深度阅读 Phase 0 中归类的全部材料
1.2 提取以下结构化信息，写入 `material_analysis.md`：
  - **核心观点**：论文的中心主张（1-3 句话）
  - **创新点**：与现有工作的本质区别（逐条列出）
  - **研究问题**：要解决的具体问题（主问题 + 子问题）
  - **方法框架**：采用的方法论、算法、实验设计
  - **数据来源**：使用的数据集、实验平台、调查对象
  - **关键假设**：方法成立的前提条件
  - **领域定位**：映射到学科的知识结构中的位置
1.3 **质量标注**：对每项信息标注置信度：
  - `[明确]` — 材料中直接陈述
  - `[推断]` — 从材料中间接推断
  - `[待确认]` — 需要用户澄清

### Phase 2：文献检索

2.1 **本地检索**：从用户提供的参考文献和材料中匹配相关论文，按相关性排序
2.2 **联网检索**（在本地覆盖不足时启动，逐步推进）：
  - **学术搜索引擎**：Google Scholar / Semantic Scholar — 按引用量和相关性取 top 20-30
  - **预印本**：arXiv / bioRxiv / SSRN — 搜索近 5 年 preprint
  - **中文文献**：CNKI / 万方 — 当论文涉及中文语境时启用
  - **专利检索**：Google Patents — 仅在涉及工程技术方案时检索
2.3 每条检索记录必须包含：`检索词 | 数据库 | 日期 | 命中数 | 纳入数`
2.4 文献汇总输出为 `literature_map.md`，按以下分组：
  - **核心引用**（直接支撑论文主张，5-10 篇）
  - **对比基准**（用于实验对比的 SOTA 方法，3-8 篇）
  - **背景文献**（提供领域背景，不限数量）

### Phase 3：引用关系图谱

3.1 为 Phase 2 的核心引用构建关系图，标注关系类型：
  - `→` 直接引用 / 技术延续
  - `↔` 对比关系（不同方法解决同一问题）
  - `⊃` 包含/泛化关系
  - `≠` 观点分歧
3.2 图谱写入 `citation_graph.md`（Mermaid 或 ASCII 格式）
3.3 标注核心引用之间的流派/学派关系（如适用）

### Phase 4：研究缺口分析

4.1 基于 Phase 1-3 的产出，列出三类问题：
  - **已解决**：有充分文献支撑 → 作为论文背景 / Related Work
  - **部分解决**：有方案但存在已知局限 → 作为论文改进动机
  - **未解决**：无公开方案或所有方案存在根本缺陷 → 作为论文核心贡献点
4.2 对每个"未解决"问题，评估：
  - 为什么现有方法无法解决？（引用具体文献说明）
  - 解决该问题的可行方向是什么？
4.3 写入 `research_gaps.md`
4.4 **缺失数据标注**：若某个主张缺乏证据，生成 `need/<topic>.md`

### Phase 5：生成写作简报

5.1 将 Phase 1-4 的所有产出汇总为 **写作简报**（`writing_brief.md`），包含：
  - 材料分析摘要（来自 Phase 1）
  - 文献地图（来自 Phase 2）
  - 引用图谱（来自 Phase 3）
  - 研究缺口（来自 Phase 4）
  - 推荐论文结构类型（IMRaD / 理论分析 / 综述 / 案例研究 / 政策简报，基于论文性质判断）
  - 推荐引用格式（默认 APA 7.0；领域习惯不同可调整）
  - 目标期刊偏好（若用户已指定）

5.2 **将此写作简报作为输入，委托给 `academic-paper` 技能进行初稿撰写**：
  - 使用 `academic-paper` 的 `plan` 模式先确认结构（如用户需要引导）
  - 或使用 `academic-paper` 的 `full` 模式直接撰写（如简报已足够明确）
  - academic-paper 的 12-agent 管线自动处理：配置访谈 → 文献策略 → 结构设计 → 论证构建 → 全文起草 → 引用合规 + 双语摘要 → 同行评审 → 格式化输出

### Phase 6：评审

6.1 初稿完成后，**委托给 `academic-paper-reviewer` 技能进行独立多角色评审**：
  - `field_analyst_agent`：分析论文领域，配置评审人身份
  - `eic_agent`：期刊主编视角 — 期刊匹配度、原创性、整体质量
  - `methodology_reviewer_agent`：方法论评审 — 研究设计、统计有效性、可复现性
  - `domain_reviewer_agent`：领域评审 — 文献覆盖、理论框架、领域贡献
  - `perspective_reviewer_agent`：跨学科评审 — 跨领域连接、实际影响
  - `devils_advocate_reviewer_agent`：魔鬼代言人 — 核心论点挑战、逻辑谬误检测
  - `editorial_synthesizer_agent`：综合所有评审意见，生成编辑决策 + 修订路线图

6.2 评审结果保存为 `review_round{N}.md`
6.3 评审决策对应关系（来自 academic-paper-reviewer 的 0-100 评分量表）：
  - ≥80：Accept → 进入 Phase 8 终稿
  - 65-79：Minor Revision → 进入 Phase 7 修订
  - 50-64：Major Revision → 进入 Phase 7 修订
  - <50：Reject → 汇总评审意见交用户决策

### Phase 7：迭代修订

7.1 **委托给 `academic-paper` 的 `revision` 模式**，输入 academic-paper-reviewer 的 Revision Roadmap
7.2 修订流程：
  - 将当前完整论文复制到 `older/v0.{N}/`
  - academic-paper revision 模式处理修订
  - 修订完成后重新进入 Phase 6 评审
  - 新版本号递增

7.3 **终止条件**（满足任一即停止迭代）：
  - ✓ academic-paper-reviewer 综合评分 ≥80（Accept）
  - ✓ 达到最大 external review 轮数 3 轮
  - ✓ 连续 2 轮评分无实质性改善（综合分变化 < 5 分）
  - ✓ 用户手动终止

7.4 第 3 轮后仍未达标时：输出当前最佳版本 + academic-paper-reviewer 的残余问题清单 + `need/` 标注的未解决缺口，交由用户决策。

### Phase 8：终稿与期刊推荐

8.1 **委托给 `academic-paper` 的 `format-convert` 模式**生成最终格式化输出（LaTeX / DOCX / PDF / Markdown）
8.2 输出最终论文（文件名：`manuscript_final.md` 及格式化版本）
8.3 基于论文主题、方法类型和创新程度推荐期刊：

**期刊推荐框架**：

| 维度 | 评估标准 |
|------|---------|
| **主题匹配** | 论文主题是否在期刊 scope 内？ |
| **方法匹配** | 期刊偏好理论深度还是实证结果？ |
| **创新层级** | 增量改进 → 三区；显著突破 → 二区；领域定义 → 一区 |
| **引用来源** | 论文的核心引用发表于哪些期刊？→ 优先投这些 |
| **领域惯例** | 该领域公认的顶刊、顶会是什么？ |

8.4 对每个推荐期刊，给出：
  - 为什么适合（基于上述维度的具体分析）
  - 投稿时需强调哪些内容（如偏理论则强调推导；偏应用则强调实验结果）
8.5 输出 `journal_recommendations.md`

---

## 文件规范

### need/ 目录

当缺少证据时，生成 `need/<topic>.md`，格式：

```markdown
---
need_type: data | literature | experiment | theory | other
urgency: blocking | important | nice_to_have
source_expected: <期望的数据来源>
date_tagged: <YYYY-MM-DD>
---

# <缺失项标题>

## 缺失描述
<具体缺失什么，为什么需要它>

## 当前替代方案
<在没有该数据的情况下，论文做了什么保守处理>

## 获取途径
<建议的获取方式：搜索关键词 / 数据库 / 实验方案>
```

### older/ 目录

- 每次修订前，将当前完整论文复制到 `older/v0.{N}/`
- 目录结构：`older/v0.1/`, `older/v0.2/`, ...
- 每个版本目录内包含该轮的完整论文和对应的评审报告
- `v0.0` 保留给 Phase 1 产出的 `material_analysis.md`

### 工作文件清单

| 文件 | 产出阶段 | 说明 |
|------|---------|------|
| `material_analysis.md` | Phase 1 | 材料分析结果 |
| `literature_map.md` | Phase 2 | 文献检索汇总 |
| `citation_graph.md` | Phase 3 | 引用关系图谱 |
| `research_gaps.md` | Phase 4 | 研究缺口分析 |
| `writing_brief.md` | Phase 5 | 写作简报（委托给 academic-paper 的输入） |
| `review_round{N}.md` | Phase 6 | academic-paper-reviewer 评审报告 |
| `manuscript_v0.{N}.md` | Phase 5/7 | 论文草稿/修订版 |
| `need/*.md` | Phase 4+ | 缺失数据标注 |
| `older/v0.{N}/` | Phase 7 | 历史版本归档 |
| `manuscript_final.md` | Phase 8 | 终稿 |
| `journal_recommendations.md` | Phase 8 | 期刊推荐 |

---

## 委托接口

### 本 Skill → academic-paper

**触发条件**：Phase 5（生成写作简报后）

**传递材料**：`writing_brief.md`（包含材料分析、文献地图、引用图谱、研究缺口、推荐结构类型、引用格式偏好）

**调用方式**：使用 Skill 工具调用 `academic-paper`，将写作简报作为输入上下文。

**推荐模式**：
- 用户需要引导 → `plan` 模式（Socratic 逐章引导）
- 写作简报已足够明确 → `full` 模式（直接生成全文）
- 已有草稿需修订 → `revision` 模式（Phase 7 使用）

**接收产物**：完整论文草稿（Markdown）+ 可选 LaTeX/DOCX/PDF

### 本 Skill → academic-paper-reviewer

**触发条件**：Phase 6（初稿完成后）

**传递材料**：完整论文文本

**调用方式**：使用 Skill 工具调用 `academic-paper-reviewer`，传入论文全文。

**推荐模式**：
- 首次评审 → `full` 模式（5 位评审人完整评审）
- 修订后验证 → `re-review` 模式
- 仅关注方法 → `methodology-focus` 模式

**接收产物**：5 份独立评审报告 + Editorial Decision Letter + Revision Roadmap + 0-100 综合评分

---

## 约束

1. **不编造**：所有主张必须有文献或数据支撑。宁可标注 need/ 也不可虚构。遵循 academic-paper Anti-Pattern #5（IRON RULE: Fabricated citations）。
2. **可追溯**：每条检索记录和每项主张的来源必须可追溯到具体论文或数据。
3. **用户材料优先**：用户上传的材料是第一信源，联网检索仅用来补缺口。
4. **迭代有界**：最多 3 轮 external review。3 轮后输出当前最佳版本 + 未解决问题清单。
5. **版本清晰**：每次修订产生新版本号，旧版不得覆盖。
6. **学科自适应**：Phase 0 自动识别学科领域。不预设任何特定领域的知识结构，从用户材料中动态提取领域上下文。
7. **不修改评审结果**：academic-paper-reviewer 的评审报告是独立的，不可编辑或软化其批评意见。

---

## 适用场景

- 从多个文档、草稿、笔记中系统化撰写学术论文
- 需要统一流程管理写作—评审—修订全周期
- 需要精准的文献对齐和引用图谱构建
- 需要版本管理和可追溯的迭代流程
- 需要在投稿前获得模拟同行评审
- 需要基于论文内容匹配最合适的期刊

## 不适用场景

- 仅需深度调研而不写论文 → 使用 `deep-research`
- 仅需评审已有论文 → 使用 `academic-paper-reviewer`
- 需要全自动端到端管线（含 integrity check）→ 使用 `academic-pipeline`
- 快速写一篇短文章/博客 → 直接使用 `academic-paper`
