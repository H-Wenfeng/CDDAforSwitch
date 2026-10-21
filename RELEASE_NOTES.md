# CDDA for Switch v0.1.0

## English

First public experimental release of the native Nintendo Switch port, based
on Cataclysm: DDA 0.I (Ito).

Highlights:

- Native AArch64 Horizon `.nro` with SDL2 Tiles.
- Touch-enabled, context-sensitive shortcut bar.
- Compact full virtual keyboard plus Switch system text input.
- Corrected physical mappings: A=Enter, B=Esc, X=`I`, L=Tab,
  R=Shift+Tab, ZL=`x`, ZR=Space, Minus=keyboard.
- Automatic English/Simplified Chinese selection and bundled Chinese catalog.
- 1280x720-friendly UI defaults and lightweight tileset migration.
- Fixes for writable configuration paths and boolean migration options.

Install by extracting `CDDAforSwitch` to `sdmc:/switch/` and launch it from a
full-memory Homebrew Menu session. Sound is not enabled in this release.

## 简体中文

这是基于 Cataclysm: DDA 0.I（Ito）的 Nintendo Switch 原生移植版首个公开
实验版本。

主要功能：

- 使用 SDL2 Tiles 的 AArch64 Horizon 原生 `.nro`。
- 支持触摸、随当前菜单变化的半透明快捷栏。
- 紧凑完整虚拟键盘，并可调用 Switch 系统输入法。
- 修正实体按键映射：A=Enter、B=Esc、X=`I`、L=Tab、R=Shift+Tab、
  ZL=`x`、ZR=空格、Minus=键盘。
- 自动选择英文／简体中文，并包含中文翻译文件。
- 适配 1280×720 的界面默认值和轻量图块集迁移。
- 修复配置目录写入和布尔迁移选项错误。

安装时将 `CDDAforSwitch` 解压到 `sdmc:/switch/`，并从完整内存模式的
Homebrew Menu 启动。本版本尚未启用声音。
