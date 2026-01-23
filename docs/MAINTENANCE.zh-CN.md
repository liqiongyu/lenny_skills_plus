# 维护指南（Maintenance）

> English version: `MAINTENANCE.md`

## 更新上游源材料

上游 Refound 内容可能会变化。本仓库默认不把 “raw sources” 提交进 git。

如果你想在本地刷新上游源材料：

```bash
python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw
```

（根据上游策略，你可能需要更像浏览器的 User-Agent。）

## 新增一个 skill pack

1) 创建 `skills/<new-skill>/`
2) 添加 `SKILL.md` + `README.md` + `references/`
3) 运行 lint：
   ```bash
   python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<new-skill>
   ```
4) 生成本地镜像用于使用：
   ```bash
   python3 scripts/mirror_skills.py --overwrite
   ```

## 重新生成 / 再次转换

如果你通过 Codex 重新跑转换，建议：

- 每次 Codex 只处理一个 skill（减少上下文漂移）
- 每个 skill 转换后都跑 lint
- 每个 category 先 smoke-test 1–2 个真实 prompt，再扩大批量

## 重新生成仓库文档

- Skills 目录：
  - `python3 scripts/generate_skills_catalog.py`
- 审计报告：
  - `python3 scripts/generate_audit_report.py`

