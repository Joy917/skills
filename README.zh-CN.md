# enjoy-skills

[English](README.md)

我在 AI 时代自己在用、且价值经过自己判断的技能合集。精挑细选，而非简单堆砌。

这些不是一句话 prompt。每个 skill 都是我反复回到的工作流——抽离、打包、发布，让别人能直接用，不必从零重建。

---

## 为什么是这些 skill？

大多数 skill 仓库都是上游仓库的镜像。这个仓库不一样：

- **以"用"筛选，不用"名声"筛选。** 一个 skill 只有在我真实工作里用了至少一个月之后才会进这里。躺在 skills 目录里没人用的，不发。
- **对来源坦诚。** 仓库里大部分 skill 是我自己做的——来自我反复回到的工作流。少数借鉴或改编自他人的开源作品——这种情况下，SKILL.md 头部会注明原作者。不会把借鉴的东西包装成"全部原创"。
- **不依赖作者本人就能跑。** 不带个人路径、私有 API key、不需要"找 Joy 拿那张表"。每个 skill 在干净机器上能直接跑。
- **有立场。** 通用建议没用。每个 skill 都有自己的观点，并告诉你什么时候可以推翻它。
- **脱敏优先**：个人路径、API key、token、身份信息在发布前都会被剥离。如果你发现任何敏感内容，请提 issue。

> **AI 是放大器，不是思考的替代品。** 这些 skill 设计的目的是磨炼你的判断力，不是替代它。最好的输出，依然来自一个清楚自己要什么、为什么的人。

---

## Skills

| Skill | 作用 | 何时使用 |
|---|---|---|
| [product-judgment](./skills/product-judgment) | 训练产品判断力——判断哪些功能值得做、哪些按钮是用户真正需要的、一个需求是真需求还是"锦上添花" | 当你作为 PM、创始人、设计师或开发者要做产品决策、需要思考伙伴时 |

更多 skill 在路上。只有在它们在我日常工作流里赢得一席之地后，才会被发到这里。

---

## 快速安装

**前置条件**

- 支持 skills 标准的 agent：Claude Code、Hermes Agent，或其他兼容 runtime。
- `~/.claude/skills/` 或 `~/.hermes/skills/` 目录。大部分 agent 在首次启动时自动创建。

**安装单个 skill**

```bash
# 克隆整个仓库
git clone https://github.com/Joy917/enjoy-skills.git
cd enjoy-skills

# 复制你想要的 skill
cp -r skills/product-judgment ~/.hermes/skills/
# 或
cp -r skills/product-judgment ~/.claude/skills/
```

**安装全部 skill**

```bash
cp -r skills/* ~/.hermes/skills/
```

大部分 agent 会自动发现 home 目录下 `skills/` 文件夹中的 skill。重启 agent 即可加载新 skill。

---

## 筛选哲学

一个 skill 要进这个仓库，必须同时满足以下四条：

1. **解决我自己真遇到的问题。** 我做了它，就是我需要它。拒绝"为了 skill 而 skill"。
2. **不是一句话 prompt。** 全部价值就是一个 prompt，那它不是 skill，是一句咒语。Skill 是那种需要框架、清单、参考资料才能跑好的工作流。
3. **不依赖作者本人就能跑。** 每个 skill 在干净机器上能跑。不带个人路径、私有 API key。
4. **有立场。** 通用建议无用。每个 skill 都有自己的观点。

任何一个不满足，就留在本地 skills 目录里，不发。

---

## 如何贡献

欢迎提 issue 和 PR。如果你想贡献一个自己做的 skill：

1. **先开 issue** — 描述这个 skill 解决的问题，以及为什么它应该是一个 skill（而不是一句 prompt）。
2. **保持结构** — `skills/<name>/SKILL.md` + 可选的 `references/`、`scripts/`、`assets/`。
3. **确保在干净机器上能跑** — 不带个人路径、私有凭证。

> 这是个人策展，不是市场。我会审阅每一个提交，不符合上面哲学的可能会被拒。这不是针对你，是拒绝稀释信号。

---

## 许可证

MIT. 见 [LICENSE](./LICENSE)。

使用、fork、学习都欢迎。如果你基于这些 skill 做出了什么，我想听听。
