# Distillation Skills — Claude Code 学术研究技能合集

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skills-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

一套完整的 **Claude Code 技能集合**，覆盖学术研究全流程：深度调研 → 论文写作 → 同行评审 → 迭代修订 → 发表就绪。同时包含人物思维方式蒸馏（女娲）和自动化控制领域知识框架。

---

## 📦 技能包概览

| 技能包 | 描述 | 许可 |
|--------|------|------|
| [academic-research-skills](./academic-research-skills/) | 学术研究全流程套件 v3.9.2（4技能：调研·写作·评审·编排） | CC BY-NC 4.0 |
| [nuwa-skill](./nuwa-skill/) | 女娲·人物思维方式蒸馏（17个人物视角示例） | MIT |
| [paper-writing-agent](./paper-writing-agent/) | 通用论文写作协调Agent（全学科·8阶段·自动领域识别） | 参见文件头部 |
| [automation-control-framework](./automation-control-framework/) | 自动化与控制领域知识蒸馏框架（6子领域·300+论文） | 参见文件头部 |

---

## 🔬 Academic Research Skills (ARS v3.9.2)

> 最完整的学术研究技能套件。一行命令安装。

```text
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

### 4 个核心技能

| 技能 | 版本 | Agents | 核心能力 |
|------|------|--------|---------|
| **deep-research** | v2.9.4 | 13 | 深度调研、事实核查、文献综述、Socratic对话 |
| **academic-paper** | v3.1.2 | 12 | 10种模式论文写作、双语摘要、格式转换、AI披露 |
| **academic-paper-reviewer** | v1.9.1 | 7 | 5审稿人+魔鬼代言人多角色评审、校准模式 |
| **academic-pipeline** | v3.9.2 | 5 | 全流程编排、完整性门禁、状态追踪 |

### 关键特性
- 🔗 **三级引文锚定** — quote/page/section/paragraph 级别定位
- 🔍 **三索引交叉验证** — Semantic Scholar + OpenAlex + Crossref 三重校验
- 📋 **Material Passport** — 跨会话恢复的研究状态
- 🛡️ **Sprint Contract** — 评审盲审硬门禁协议
- 🚫 **反泄露协议** — 会话材料优先于 LLM 记忆
- ✅ **完整性门禁** — Stage 2.5/4.5 的 7 模式 AI 失败检查

> 📖 详见 [academic-research-skills/README.md](./academic-research-skills/README.md)

---

## 🧙 女娲 · Skill 造人术 (Nuwa Skill)

> *「你想蒸馏的下一个员工，何必是同事」*

输入任何人名/主题 → 自动深度调研 → 思维框架提炼 → 生成可运行的**人物 Skill**。

### 蒸馏的不是语录，是思维操作系统

| 维度 | 蒸馏内容 |
|------|---------|
| 🧠 **心智模型** | 他用什么镜片看世界？ |
| ⚡ **决策启发式** | 他的直觉规则是什么？ |
| 🗣️ **表达 DNA** | 他怎么组织语言、构建叙事？ |
| 🚫 **反模式** | 他绝对不会做什么？ |
| 🎯 **诚实边界** | 这个 Skill 做不到什么？ |

### 已蒸馏人物（17个）

```
产品/商业    │ Steve Jobs · Elon Musk · 张一鸣
投资/思维    │ Charlie Munger · Naval Ravikant · Nassim Taleb
科学/技术    │ Richard Feynman · Ilya Sutskever · Andrej Karpathy
创业/教育    │ Paul Graham · MrBeast · 张雪峰
政治/商业    │ Donald Trump · 孙宇晨
社交媒体     │ X Mastery Mentor
```

> 📖 详见 [nuwa-skill/README.md](./nuwa-skill/README.md)（含 英/日/韩/西 多语言版本）

---

## 📝 Paper Writing Agent

**通用型**学术论文写作协调代理，适用于任何学科。加载用户提供的材料（草稿、笔记、数据、参考文献），自动识别领域 → 构建引用图谱 → 识别研究缺口 → 生成写作简报 — 然后委托给 academic-paper（12-agent）撰写、academic-paper-reviewer（7-agent）评审，迭代修订至达标。

### 8 阶段流程
```
Phase 0: 领域识别 → Phase 1-4: 材料分析+文献+图谱+缺口 → Phase 5: 委托写作 → Phase 6: 委托评审 → Phase 7: 迭代修订 → Phase 8: 终稿+期刊推荐
```

> 📖 详见 [paper-writing-agent/README.md](./paper-writing-agent/README.md)（中英双语）

---

## 🎛️ Automation Control Framework

自动化与控制领域的**知识蒸馏框架**。6 个子领域 × 300+ 篇论文 → 提炼为可导航的认知地图。

```
  强化学习控制 (RL)  ← 策略层
  鲁棒控制 · 自适应控制 · MPC  ← 控制层
  导盲辅助 (BVI)  ← 应用层
  自主导航  ← 执行层
```

- ✅ 7 个核心方法论共识
- 🔀 6 条学派分歧与融合趋势
- 🏗️ 5 层技术栈模型

> 📖 详见 [automation-control-framework/README.md](./automation-control-framework/README.md)（中英双语）

---

## 📂 完整目录结构

```
distillation-skills/
├── README.md                              # 本文件
├── .gitignore
│
├── academic-research-skills/              # ARS v3.9.2（679 文件）
│   ├── README.md
│   ├── academic-paper/SKILL.md            # 12-agent 论文写作
│   ├── academic-paper-reviewer/SKILL.md   # 多角色评审
│   ├── academic-pipeline/SKILL.md         # 全流程编排
│   ├── deep-research/SKILL.md             # 深度调研
│   ├── shared/                            # 共享协议/模板/Schema
│   ├── docs/                              # 设计文档/迁移指南
│   ├── scripts/                           # CI检查/适配器/迁移
│   ├── tests/                             # 测试套件
│   ├── commands/                          # 10个 /ars-* 斜杠命令
│   └── hooks/                             # 插件生命周期钩子
│
├── nuwa-skill/                            # 女娲（125 文件）
│   ├── SKILL.md
│   ├── README.md (中/英/日/韩/西)
│   ├── LICENSE (MIT)
│   ├── examples/                          # 17个人物视角
│   ├── references/                        # 调研方法论
│   ├── scripts/                           # 辅助脚本
│   └── assets/                            # hero.gif, banner.svg
│
├── paper-writing-agent/                   # 通用论文写作Agent（13 文件）
│   ├── SKILL.md
│   ├── README.md / README.zh-CN.md
│   ├── references/                        # 引用图谱、写作简报、文献地图
│   ├── need/                              # 待补充数据
│   └── older/                             # 旧版归档
│
├── automation-control-framework/          # 控制领域知识（10 文件）
│   ├── SKILL.md / SKILL_EN.md
│   ├── README.md / README_ZH.md
│   └── references/research/               # 6个子领域调研
│
└── docs/                                  # 辅助文档（19 文件）
    ├── paper-samples/                     # 论文输出样本
    │   ├── paper_draft.md                 # 英文初稿
    │   ├── paper_draft_zh.md              # 中文初稿
    │   ├── paper_last.md / paper_last_ch.md  # 终稿
    │   ├── review_report.md               # 评审报告
    │   ├── generate_figures.py            # 图表生成脚本
    │   └── figures/                       # 4组论文图表 (PNG+PDF)
    └── analysis-notes/                    # 分析笔记
```

---

## 🚀 安装指南

### 方式一：整体安装（推荐）

```bash
# 1. 克隆整个仓库到 Claude Code skills 目录
git clone https://github.com/<你的用户名>/distillation-skills.git ~/.claude/skills/distillation-skills

# 2. 为每个技能创建符号链接（让 Claude Code 能自动发现）
ln -s ~/.claude/skills/distillation-skills/academic-research-skills ~/.claude/skills/academic-research-skills
ln -s ~/.claude/skills/distillation-skills/nuwa-skill ~/.claude/skills/nuwa-skill
ln -s ~/.claude/skills/distillation-skills/paper-writing-agent ~/.claude/skills/paper-writing-agent
ln -s ~/.claude/skills/distillation-skills/automation-control-framework ~/.claude/skills/automation-control-framework
```

### 方式二：通过 ARS 插件市场安装

```text
# 在 Claude Code 对话中运行：
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
```

> 注意：插件方式仅安装 ARS。女娲、paper-writing-agent、automation-control-framework 需手动安装。

### 方式三：仅安装单个技能包

```bash
# 只安装女娲
cp -r distillation-skills/nuwa-skill ~/.claude/skills/nuwa-skill

# 只安装自动化控制框架
cp -r distillation-skills/automation-control-framework ~/.claude/skills/automation-control-framework
```
创造：
首先，打开你的代理中的项目文件夹：目标是让AI指向你在上一步解压/克隆的目录。在IDE类工具中，使用“文件→打开文件夹”——AI聊天面板通常在侧边栏;先在CLI代理中启动，然后启动它。从这里开始的所有事情都在聊天里进行。

---

## 📄 许可证

| 技能包 | 许可证 | 备注 |
|--------|--------|------|
| academic-research-skills | [CC BY-NC 4.0](./academic-research-skills/LICENSE) | 非商业用途需署名 |
| nuwa-skill | [MIT](./nuwa-skill/LICENSE) | 可自由使用、修改、分发 |
| paper-writing-agent | CC BY-NC 4.0 | 继承自 ARS |
| automation-control-framework | 参见 SKILL.md 头部 | — |

---

## 🙏 致谢与引用

| 来源 | 贡献 |
|------|------|
| [PaperOrchestra](https://arxiv.org/abs/2604.05018) (Song et al., 2026) | ARS v3.3 多Agent协调架构 |
| [Zhao et al.](https://arxiv.org/abs/2605.07723) (2026) | ARS v3.7.3 引文忠实度三锚定系统 |
| Wang & Zhang (2026) IJETHE 23:11 | ARS v3.5 协作深度观测器 |
| [同事.skill](https://github.com/titanwings/colleague-skill) | 女娲 Skill 灵感来源 |
| Lu et al. (2026) *Nature* 651 | AI Scientist 失败模式清单 |
| arXiv / Semantic Scholar / OpenAlex / Crossref | 文献检索与验证基础设施 |

---

## 🌟 Star History

如果你觉得这个项目有用，请给一个 ⭐ Star！

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com)

---

## 📬 联系与贡献

- **ARS 原作者**: Cheng-I Wu ([@Imbad0202](https://github.com/Imbad0202))
- **女娲原作者**: [@alchaincyf](https://github.com/alchaincyf)
- **问题反馈**: 请在对应仓库提交 Issue
- **贡献**: 欢迎 PR！请先阅读各子项目的 CONTRIBUTING 指南

---

<p align="center">
  <sub>Made with ❤️ by the Claude Code community</sub>
</p>
