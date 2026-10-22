# CDDA for Switch v0.1.1

## English

Save reliability patch for the native Nintendo Switch port, based on
Cataclysm: DDA 0.I (Ito).

Fixes:

- Safely replaces existing save files on Horizon, where rename cannot
  overwrite a destination directly.
- Explicitly commits completed save operations to the SD-card filesystem.
- Stores UTF-8 world names in reversible ASCII-safe directories while keeping
  the original name in the game interface.
- Stores achievement files for UTF-8 character names under ASCII-safe names;
  the original character name remains inside the JSON data.
- Preserves and continues loading existing legacy world directories.
- Adds detailed Switch save-stage diagnostics to `user/config/debug.log`.

Install by extracting `CDDAforSwitch` to `sdmc:/switch/` and launch it from a
full-memory Homebrew Menu session. Sound is not enabled in this release.

## 简体中文

这是基于 Cataclysm: DDA 0.I（Ito）的 Nintendo Switch 原生移植版存档可靠性
补丁版本。

修复内容：

- 修复 Horizon 文件重命名无法直接覆盖旧存档的问题，安全替换正式存档。
- 保存完成后显式提交 SD 卡文件系统，防止重启后存档丢失。
- 中文等 UTF-8 世界名使用可逆的 ASCII 安全目录，游戏界面仍显示原名称。
- 中文等 UTF-8 角色名的成就文件使用 ASCII 安全名称，JSON 中仍保留原名称。
- 保留并继续读取旧版世界目录，不自动删除或迁移用户存档。
- 在 `user/config/debug.log` 中增加 Switch 保存阶段诊断信息。

安装时将 `CDDAforSwitch` 解压到 `sdmc:/switch/`，并从完整内存模式的
Homebrew Menu 启动。本版本尚未启用声音。
