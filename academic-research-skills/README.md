# Academic Research Skills

**一个 skill，完成调研、写作、评审与迭代修订。**

本仓库改版版本：**v4.0.0**。面向 Claude Code 和 Codex，保留上游研究协议、角色与模板，并将原四个独立入口合并为一个 `academic-research-skills`。

## v4.0.0 更新

- **四合一入口**：调研、写作、评审、编排融合为 `academic-research-skills`，按任务选择内部模式。
- **两种论文方向**：支持综述与实验／方法类论文；综述可选叙述性、系统性或范围综述。
- **Zotero 文献接入**：使用当前环境已有的实时工具，或导入 Better BibTeX JSON；修复导出对象的 `items` 数组兼容问题。
- **Obsidian 协作**：导入选定目录的文献笔记，保留引用键、个人注释和材料来源。
- **Claude Code / Codex**：提供跨平台项目级安装脚本，每个工具只生成一个同名 skill 入口。
- **项目续接**：配置文件记录论文类型与材料路径，现有 Material Passport 保留阶段状态。

## 支持的工具与接入方式

| 工具 / 环境 | 本 skill 的用途 | 接入条件与范围 |
|---|---|---|
| Codex（本地客户端 / CLI / IDE） | 运行统一研究、写作、评审流程 | 安装项目级 skill；需要能读取本地文件，运行脚本时需 Python |
| Claude Code | 同一套流程与项目材料 | 使用 `--target claude` 安装；可与 Codex 共用项目 |
| Zotero | 提供文献条目、引用键、摘要及已授权读取的材料 | 实时读取依赖另行配置的 Zotero MCP / 连接工具；也可使用离线导出 |
| Better BibTeX for Zotero | 导出带引用键的文献记录 | 离线适配器读取 **Better BibTeX JSON**，不是 Better CSL JSON |
| Obsidian | 导入选定目录的文献笔记，记录研究决策和草稿 | 普通 Markdown / YAML 文件即可；无需 Obsidian 社区插件，不自动同步整个 vault |
| Semantic Scholar / OpenAlex / Crossref | 文献元数据查询与交叉核验 | 仓库含客户端；需要网络，鉴权、配额和限流依服务而定；元数据核验不等于原文支持核验 |
| Markdown / BibTeX | 保存草稿、研究笔记与参考文献信息 | 根据现有文件和引用键工作；不自动将 Zotero 条目键当作 BibTeX 键 |
| Pandoc / LaTeX 工具链（可选） | 按任务转换 DOCX、LaTeX 或 PDF | 需额外安装相应工具；未安装时提供 Markdown 和转换说明 |

安装 skill 只添加工作流程，不会同时安装 Zotero、Better BibTeX、MCP 服务、Pandoc 或 LaTeX，也不会自动获取这些服务的账号权限。

## 多平台兼容：DeepSeek Harness 等

统一 skill 使用 `SKILL.md` 与本地参考文件组织工作流，可接入具备相应 Skills 加载、文件访问和脚本执行能力的宿主。

| 平台 | 安装与接入方式 | 当前验证状态 |
|---|---|---|
| Codex | 使用 `--target codex` 生成 `.agents/skills/academic-research-skills/SKILL.md` | 安装入口和脚本测试通过；完整论文流程待实测 |
| Claude Code | 使用 `--target claude` 生成 `.claude/skills/academic-research-skills/SKILL.md` | 安装入口和脚本测试通过；完整论文流程待实测 |
| DeepSeek Harness | 默认文件系统 Skills 提供器支持项目 `.agents/skills`，可复用 `--target codex` 生成的共享目录入口；也可将完整 skill 目录放入 `.dsh/skills` | 按官方目录规范接入，尚未在 Harness 中实测 |
| 其他支持 Agent Skills 的软件 | 将完整 skill 目录放到该软件规定的技能目录，保留内部协议、脚本与参考文件 | 需核对该宿主的加载规则、工具权限和运行时能力；未逐一验证 |

### DeepSeek Harness 接入

在源码的 `academic-research-skills` 目录执行（参数名称 `codex` 代表现有安装器使用的共享 `.agents/skills` 目标，不限制模型厂商）：

```sh
python scripts/setup_research.py install --project "/path/to/project" --target codex
```

随后在 DeepSeek Harness 打开该项目，确认已启用本地 Skills 文件系统提供器和技能调用能力，查看技能目录是否出现 `academic-research-skills`，再请求它读取研究材料。若已经为 Codex 创建同一入口，可直接共用，无需重复安装。

DeepSeek Harness 默认也可扫描 `<projectRoot>/.dsh/skills`。手动安装时将整个 `academic-research-skills` 文件夹复制进去；不只复制入口文件，也不要把四份内部协议分别安装。项目根目录按其提供器规则识别；存在 Git 仓库时注意入口所在位置是否与它识别的项目根一致。关闭默认扫描或使用自定义目录的环境，需要按宿主配置调整。

以上目录与提供器要求依据 [DeepSeek Harness 官方 Skills 文档](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/skill/skill-filesystem/README.md)。支持的宿主不等于对应厂商的所有聊天产品：DeepSeek 网页聊天不因此自动获得本地技能、Zotero 或 Obsidian 访问能力。多角色隔离、原文读取、网络检索和格式转换仍取决于具体运行环境。

## GPT / Codex 的 Skills 安装流程

GPT 是模型；本地 skill 需要由支持 Skills 的客户端加载。本仓库优先提供 Codex 的本地项目级安装方式。

### 1. 准备源码与依赖

先安装并登录可用的 Codex 客户端或 CLI，准备 Git 和 Python 3.10+。下面的命令在系统终端执行：

```sh
git clone https://github.com/Dubaoxu/distillation-skills.git
cd distillation-skills/academic-research-skills
python -m pip install -r requirements-dev.txt
```

如果使用下载的 ZIP，解压后进入包含 `SKILL.md` 和 `scripts/` 的 `academic-research-skills` 目录。此 v4.0.0 改版在推送前仅存在于本地预览；上述 GitHub 克隆方式在改版推送后才会取得新版。

### 2. 安装到实际工作项目

Windows PowerShell 示例（替换为你自己的目录）：

```powershell
python scripts/setup_research.py install --project "E:/Research/my-paper" --target codex
Test-Path -LiteralPath "E:/Research/my-paper/.agents/skills/academic-research-skills/SKILL.md"
```

macOS / Linux 示例：

```sh
python scripts/setup_research.py install --project "$HOME/Research/my-paper" --target codex
test -f "$HOME/Research/my-paper/.agents/skills/academic-research-skills/SKILL.md"
```

需要 Claude Code 共用时，将 `--target codex` 改为 `--target both`。安装器输出创建的入口路径；每个工具只有一个 `academic-research-skills`。

### 3. 打开项目并调用

在 Codex 中打开第 2 步指定的工作目录并新建会话。CLI 用户可先切换到该目录，再运行 `codex`。通过技能选择器选择该 skill，或在提示中明确使用：

```text
$academic-research-skills
读取当前项目的研究材料，先列出已有证据和待补材料，再制定论文计划。
```

Codex CLI / IDE 可通过 `/skills` 或输入 `$` 查看技能。客户端界面可能有所不同，详见 [OpenAI Skills 官方指南](https://learn.chatgpt.com/docs/build-skills)。先用一次范围明确的小任务检查加载情况，再进入完整论文流程。

### 4. 可选：所有项目共用

项目级入口更方便控制范围。如果希望手动安装到用户级，可以将**整个** `academic-research-skills` 目录复制到 `~/.agents/skills/academic-research-skills/`，保留 `shared/`、`scripts/` 和四个内部协议目录；不要只复制 `SKILL.md`。本仓库安装脚本本身只负责项目级入口。目录约定参考 [OpenAI 官方安装说明](https://developers.openai.com/api/reference/cli)。

### ChatGPT 桌面、网页与自定义 GPT

支持独立 Skills 的 ChatGPT 桌面环境可按其提供的技能管理能力使用；网页等环境的分发方式可能需要插件。本仓库当前交付的是本地 skill，尚未发布为 OpenAI 插件，也未验证在各 ChatGPT 界面中的直接导入流程。请以 [官方 Skills 指南](https://learn.chatgpt.com/docs/build-skills) 和账号实际可用入口为准。

把 ZIP 上传到普通聊天或自定义 GPT 知识库，不代表已经安装可运行的 skill；本地 Python、Zotero 和 Obsidian 访问还需要运行环境提供对应能力。

### 加载排查与更新

- 找不到 skill：核对打开的项目目录和入口文件路径，然后新建会话；确认目录没有被多嵌套一层。
- 找得到入口但读不到协议：项目入口引用固定源码位置；若移动或删除源码，需重新配置该入口。
- 报旧入口或文件已存在：检查并备份已有安装，再迁移旧四个入口；安装器不会覆盖用户文件。
- 报缺少模块：在运行脚本所用的同一个 Python 环境执行依赖安装命令。
- Zotero 不可用：先确认当前环境已配置相应实时工具；没有实时连接时，选择离线导出。
- 更新：在源码仓库执行 `git pull --ff-only`（存在本地修改时先处理修改），保持源码路径不变；完整复制安装需要同步更新整份目录。更新后新建会话。

## 通用安装（Claude Code / Codex）

需要 Python 3.10+。在终端运行：

```sh
git clone https://github.com/Dubaoxu/distillation-skills.git
cd distillation-skills/academic-research-skills
python -m pip install -r requirements-dev.txt
python scripts/setup_research.py install --project "/path/to/your/project" --target both
```

将 `/path/to/your/project` 换成实际项目目录。Windows 中文路径和含空格路径请加引号。仅安装一个工具时，使用 `--target claude` 或 `--target codex`。

安装结果：

```text
project/
├── .agents/skills/academic-research-skills/SKILL.md
└── .claude/skills/academic-research-skills/SKILL.md
```

每个工具发现的是同一个 skill。入口引用此源码目录，请保留源码位置。安装器不会覆盖已有入口；若检测到原四个 skill 的旧入口，会提示先迁移，避免出现五个并存的入口。当前改版使用本地脚本安装，不使用上游 marketplace 安装命令。

## 开始使用

直接告诉工具你要做什么：

```text
使用 academic-research-skills，结合我的 Zotero 文献和 Obsidian 笔记，
围绕研究问题进行文献梳理，然后制定论文大纲。
```

也可以只做一个阶段：

- “评审这篇实验论文，重点检查方法、数据与结论是否一致。”
- “根据这些材料写系统综述大纲，标出尚缺的检索与筛选记录。”
- “根据审稿意见修改论文，并整理逐条回复。”
- “读取项目配置和 passport.yaml，继续上次的论文流程。”

无需切换四个独立 skill；单阶段请求也不会强制启动完整流程。

## 初始化论文项目

系统综述：

```sh
python scripts/setup_research.py init --directory "/path/to/project/my-review" --paper-type review --review-kind systematic --title "论文题目"
```

实验／方法类论文：

```sh
python scripts/setup_research.py init --directory "/path/to/project/my-paper" --paper-type empirical --title "论文题目"
```

综述类型可选 `narrative`、`systematic`、`scoping`。可添加 `--vault "/path/to/vault"` 记录 Obsidian 位置；这不会自动扫描或修改整个笔记库。

## 能力与验证边界

- Zotero 实时接入依赖当前工具环境；离线适配器不提供自动双向同步。
- 文献元数据、摘要、个人笔记与原文证据分别处理，不把导入成功等同于引文核验通过。
- 不虚构实验、数据或系统综述筛选数量；缺失证据会保留为待完成项。
- 模拟评审不等于真实期刊评审；独立盲审所需的隔离调用必须由运行环境实际提供。
- 当前相关测试 **265 项通过**；1 项因 Windows 符号链接权限未运行。统一入口、内部引用和解压后安装已验证；尚未完成两种工具中的真实论文全流程与实时 Zotero 联调。

## 目录与进一步说明

- [统一入口](SKILL.md)：任务路由、证据要求、阶段衔接。
- [快速开始](QUICKSTART.md)：安装和项目初始化。
- [Zotero / Obsidian 与跨工具协议](shared/references/portable_research_workflow.md)。
- [版本记录](CHANGELOG.md)。

`deep-research/`、`academic-paper/`、`academic-paper-reviewer/`、`academic-pipeline/` 保存内部 `WORKFLOW.md`、角色和参考资料，不再包含独立的 `SKILL.md`。

## 来源与许可

基于 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) 的协议与实现进行整合，保留原作者 Cheng-I Wu 的贡献说明与相关文件。本目录沿用 [CC BY-NC 4.0](LICENSE)；使用、修改和分发须遵守该许可。v4.0.0 是本仓库的整合版编号，不代表上游发布版本。
