# 单一 Skill 安装与使用

本版本只提供一个 skill：`academic-research-skills`。调研、写作、评审和编排都在同一入口内完成。旧目录保留角色、模板与协议，`WORKFLOW.md` 是内部参考，不是独立 skill。

## 安装

将仓库保存在固定位置，在 `academic-research-skills` 目录运行：

```sh
python -m pip install -r requirements-dev.txt
python scripts/setup_research.py install --project /path/to/project --target both
```

`--target codex` 只安装 Codex，`--target claude` 只安装 Claude Code。`both` 在两个工具各创建一个同名入口：

```text
project/
├── .agents/skills/academic-research-skills/SKILL.md
└── .claude/skills/academic-research-skills/SKILL.md
```

入口指向本地源码，保留源码目录的位置。无需符号链接权限。已有入口不会被覆盖；先检查并自行迁移旧安装，安装器不会删除用户已有 skill。新安装不会创建旧四个入口。该改版尚未发布到上游 marketplace，请使用这里的本地安装方式。

## 创建论文项目

综述论文：

```sh
python scripts/setup_research.py init --directory /path/to/project/my-review --paper-type review --review-kind systematic --title "论文题目"
```

`--review-kind` 可选 `narrative`、`systematic`、`scoping`。实验／方法类论文：

```sh
python scripts/setup_research.py init --directory /path/to/project/my-paper --paper-type empirical --title "论文题目"
```

可添加 `--vault /path/to/vault` 记录 Obsidian 位置。参数含空格或中文时使用引号。初始化配置和起始文件不代表已经完成研究。

## 使用同一个入口

- “使用 academic-research-skills，围绕我的问题检索和梳理文献。”
- “使用 academic-research-skills，根据材料写系统综述的大纲。”
- “使用 academic-research-skills，评审这份实验论文，先检查方法和结果。”
- “使用 academic-research-skills，从 research-project.yaml 和 passport.yaml 继续整个论文流程。”

只要求一个阶段时执行该阶段；要求全流程时在内部衔接各阶段，无需切换 skill。原 `/ars-*` 文件是可选模式快捷方式，本地安装器不注册这些插件命令，直接使用自然语言即可。

Zotero 实时工具、离线导入、Obsidian 文献笔记以及跨工具恢复见 [材料与运行环境协议](shared/references/portable_research_workflow.md)。实时连接是否可用由当前环境决定；导入书目和笔记不等于完成原文核查。
