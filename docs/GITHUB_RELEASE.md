# GitHub 仓库与发布文案

## 推荐仓库

- Repository: `ai-mv-director-skill`
- Visibility: Public（公开发布前由仓库所有者确认）
- Description: `A reusable Agent Skill for distinctive, end-to-end AI music video direction.`
- Website: 留空，或在项目正式发布后填写文档页
- Topics:
  - `agent-skills`
  - `ai-video`
  - `music-video`
  - `storyboarding`
  - `creative-workflow`
  - `codex`
  - `claude-code`
  - `video-production`

## GitHub About 文案

一套可复用的 AI 音乐 MV 总导演 Skill：从源素材调查、音乐分析、独立创意、节拍分镜，到 AI 视频制作、分段验收、最终质检和创意去重归档。

## 首次发布标题

`v1.0.0 — AI MV Director Skill`

## 首次发布说明

### Features
- Four approval-gated phases: source analysis, creative direction, storyboard/previsualization, and production/QC.
- Song-led creative direction with a persistent creative-fingerprint archive.
- Beat-aware storyboard and lyric-subtitle workflow.
- Visual-bible and continuity templates.
- Contact-sheet review gates and delivery reporting.
- Optional Codex UI metadata and portable Agent Skills structure.

### Design principles
- Reuse technical infrastructure, not creative formulas.
- No default art style, HUD, prop, plot twist, or shot count.
- Report only verified tool execution and media properties.
- Preserve original source assets.

### Compatibility
Designed for Agent Skills-compatible clients. Product-specific skill discovery paths and invocation methods may differ.

## 自动创建 GitHub Release

仓库提交完成后，可在 GitHub 的 **Actions → Publish v1.0.0 Release → Run workflow** 手动触发发布。首次上传发布工作流时，提交信息包含 `release: publish v1.0.0` 也会触发。工作流先验证结构并生成完整 ZIP 和 SHA-256，再使用仓库自动提供的 `GITHUB_TOKEN` 创建 `v1.0.0` 标签、正式 Release 和两个下载附件，不需要个人访问令牌。

工作流检查当前分支的提交身份。存在非 GitHub noreply 邮箱时会停止发布；只有仓库所有者明确授权后，维护者才能将 `REBUILD_HISTORY` 设为 `true`。这会在必要时保留完整文件树，用 GitHub Actions 机器人身份重建为一个根提交，并通过精确旧 SHA 的 force-with-lease 更新 `main`。提交 SHA 会改变；GitHub 缓存或其他副本中的旧提交可能仍需另行清除。不得把重建默认分支描述为全站清除历史隐私。

如果 Actions 尚未启用，先进入仓库的 Actions 页面并允许工作流运行。发布前确认 `main` 分支已有完整 Skill 文件。

## 账号隐私提醒

公开仓库会显示仓库所有者的 GitHub 登录名和公开个人资料。项目文件不应包含真实姓名、私人邮箱、个人设备路径或账号凭据。建议在 GitHub Settings → Emails 中开启 **Keep my email addresses private**，并使用 GitHub 提供的 noreply 邮箱进行本地 Git 提交。

## 发布前检查

- [ ] `SKILL.md` frontmatter 有效
- [ ] `name` 与安装目录名称一致
- [ ] `agents/openai.yaml` 的 display name、description 和 default prompt 正确
- [ ] README 安装步骤已验证
- [ ] 无个人隐私、密钥、源音频或受版权保护的素材
- [ ] 示例明确标注为虚构
- [ ] MIT License 已包含
- [ ] `python scripts/validate_skill.py .` 通过
- [ ] 仓库可见性由所有者确认
- [ ] Release tag 为 `v1.0.0`

## 本地发布命令

在已创建并配置好 GitHub 远程仓库后：

```bash
git init
git config user.name "Water-N"
git config user.email "YOUR_GITHUB_NOREPLY_ADDRESS"
git add .
git commit -m "feat: publish AI MV Director Agent Skill v1.0.0"
git branch -M main
git remote add origin https://github.com/Water-N/ai-mv-director-skill.git
git push -u origin main
git tag -a v1.0.0 -m "AI MV Director Skill v1.0.0"
git push origin v1.0.0
```

先将 `YOUR_GITHUB_NOREPLY_ADDRESS` 替换为 GitHub Settings → Emails 显示的 noreply 地址。以上命令用于维护者首次初始化本地副本；已有仓库应先拉取并核对远程，勿重复初始化或覆盖他人变更。发布工作流会完成标签、Release 和附件；若改用手动方式，须执行打包脚本并另行上传 ZIP 与校验和。

## 社区发布文案（中文）

**标题：开源一个 AI MV 总导演 Skill：让每首歌都有自己的故事**

我整理了一套 Agent Skill，把 AI 音乐 MV 的制作流程拆成四个阶段：

1. 源素材调查：音频、歌词、节拍、封面和特殊声音；
2. 创意导演：三个差异化故事方案、叙事机制和创意指纹；
3. 分镜预演：视觉圣经、节拍分镜、字幕和联系表；
4. 工程制作：分段生成、验收、质检和归档。

它最重要的原则是：技术流程可以复用，创意表达不能流水线化。

不会默认每首歌都用像素风、HUD、雨夜或同一类道具。每个项目先分析歌曲，再决定故事和视觉语言。

适用于支持 Agent Skills 的 AI 工作流。欢迎试用、提 Issue 和 PR。

## Community post (English)

**AI MV Director — an open Agent Skill for song-specific music video production**

This skill organizes music-video work into four approval-gated phases: source investigation, creative direction, storyboard/previsualization, and production/QC.

It emphasizes song-led concepts, beat-aware storyboards, visual continuity, staged contact-sheet reviews, and a creative-fingerprint archive to reduce repetition across projects.

Technical workflows can be reused; creative formulas should not be copied from one song to the next.
