# AI MV Director

**一套可复用、可审阅、可跨项目使用的 AI 音乐 MV 导演 Skill。**

它把音乐分析、创意策划、分镜预演、AI 素材制作、剪辑质检和项目归档组织成四阶段工作流。核心原则是：**技术流程可以复用，创意表达不能流水线化。**

## 能做什么

- 分析源音频、源视频、专辑封面、歌词时间和音乐节拍。
- 检查倒放、电话音、口白、合唱、现场欢呼等特殊音频线索。
- 提出三个有实质差异的故事方案，并评估与近期作品的创意距离。
- 建立项目专属视觉圣经、角色/道具连续性和节拍分镜。
- 规划歌词字幕、联系表、动态预演和分段验收。
- 检查最终成片并更新创意指纹档案。

## 设计原则

1. 不默认像素风、水彩、写实或任何固定媒介。
2. 不默认 HUD、游戏机制、雨夜、红色道具、冷暖回忆或桥段反转。
3. 不默认镜头数量；镜头密度由音乐和叙事决定。
4. 先分析真实素材，再提出创意。
5. 四个阶段逐一确认，不擅自跳过。
6. 模型、脚本和工程结构可以复用，故事和视觉表达必须为歌曲重新设计。
7. 不虚构工具执行、素材检查、歌词、时间码或成片指标。

## 目录

- `SKILL.md`：Agent 入口指令。
- `agents/openai.yaml`：Codex / ChatGPT 桌面端的可选 UI 元数据。
- `references/`：详细工作规范。
- `prompts/`：每个阶段可直接复制的调用文案。
- `templates/`：项目简报、分析报告、分镜、创意指纹和交付报告模板。
- `scripts/`：项目初始化与 Skill 结构检查脚本。
- `docs/GITHUB_RELEASE.md`：GitHub 仓库文案、发布说明和发布步骤。

## 安装

正式版本：[v1.0.0 Release](https://github.com/Water-N/ai-mv-director-skill/releases/tag/v1.0.0)。

下载 [ai-mv-director-skill-v1.0.0.zip](https://github.com/Water-N/ai-mv-director-skill/releases/download/v1.0.0/ai-mv-director-skill-v1.0.0.zip)，解压后得到 `ai-mv-director/` 文件夹。Release 同时提供 `SHA256SUMS.txt`，可用于核对 ZIP 的 SHA-256。

### Codex（用户级）

将整个 Skill 文件夹放到：

- Windows：`%USERPROFILE%\.agents\skills\ai-mv-director\`
- macOS / Linux：`~/.agents/skills/ai-mv-director/`

确认入口文件位于 `ai-mv-director/SKILL.md`。

也可以在当前代码仓库中使用项目级路径：

`<repo-root>/.agents/skills/ai-mv-director/`

Codex 会扫描支持的 Skill 目录。若没有出现，重启 Codex 或重新加载 Skill 列表。

### Claude Code 或其他 Agent

Agent Skills 是开放文件夹格式，但每个产品的发现目录和调用方式可能不同。将此文件夹放入目标 Agent 支持的 Skills 目录，再按该产品文档加载。不要假设不同客户端的目录完全相同。

## 使用

显式调用示例：

`$ai-mv-director`

项目启动文案：

```text
启动新 MV 项目。

歌曲：[歌名]
歌手：[歌手]
源素材：[歌曲文件夹或文件路径]
指定模型：[可选]
参考素材：[可选]

读取 AI MV Director Skill。
先执行阶段一：素材调查。
只检查源素材并提交分析报告，不生成画面。
等待我确认后再进入阶段二。
```

更多调用文案见 `prompts/`。

## 四阶段工作流

| 阶段 | 目标 | 主要交付 | 是否需要确认 |
|---|---|---|---|
| 01 素材调查 | 事实、音频、歌词、节拍 | 分析报告与段落表 | 是 |
| 02 创意导演 | 独立故事与机制 | 三个提案与推荐 | 是 |
| 03 分镜预演 | 视觉系统与时间线 | 视觉圣经、分镜、联系表 | 是 |
| 04 工程制作 | 生成、剪辑、质检、归档 | 成片与交付报告 | 分段确认 |

## 工具与脚本

Skill 不假设用户的环境一定存在 `beats.py`、`grid.py`、`beatmap.py`、`scan.js`、`kicks.json`、FFmpeg 或特定 AI 模型。

执行前必须检查：
- 文件是否存在；
- 运行环境是否支持；
- 参数和输出格式是否明确；
- 是否会覆盖源文件。

缺失时说明受阻原因，并提出真实可执行的替代方案。

## 本地检查

辅助脚本要求 Python 3.9 或更高版本，仅使用标准库。规划和编写分镜无需安装特定生成模型；生成与剪辑需另行配置用户选择的工具。

```bash
python scripts/validate_skill.py .
```

初始化项目目录：

```bash
python scripts/init_project.py "/path/to/song-folder/制作"
```

初始化脚本只创建缺失的目录和模板副本，不覆盖已存在文件。

维护者可运行 `python scripts/package_release.py . --output-dir dist` 生成完整 ZIP 和校验和。脚本先验证包结构，并按固定文件类型打包；不会收集 Git 历史、缓存或用户媒体。

## 创意指纹

每个完成的项目保存一份 `creative-fingerprint.yaml`。下一部作品先读取最近三份记录，再评估叙事机制、道具、视角、结构、场景、媒介、色彩、剪辑、开场和结尾的差异。

没有历史档案时必须明确说明，不得假装读取过历史作品。

## 隐私与数据处理

本 Skill 不包含遥测、跟踪代码、凭据或自动上传素材的功能。它会指导宿主 AI Agent 检查项目文件或调用用户选择的工具；实际数据处理遵循对应 AI 客户端和外部工具的隐私政策。未经授权，不要将私人素材发送给外部服务。详见 `docs/PRIVACY.md`。

## GitHub

仓库发布文案、Topics、Release Notes 和发布检查清单见 `docs/GITHUB_RELEASE.md`。

## License

MIT。详见 `LICENSE`。
