# CDDA for Switch

简体中文 | [English](README.md)

这是
[Cataclysm: Dark Days Ahead](https://github.com/CleverRaven/Cataclysm-DDA)
的非官方 Nintendo Switch 原生 Homebrew 移植版，基于 0.I（Ito）稳定版源码。
程序以 AArch64 Horizon `.nro` 运行，并非 Android 或 Linux 模拟版本。

移植版加入了适合 Switch 的默认显示设置、手柄映射、触摸快捷栏、紧凑全键盘、
系统文字输入，以及根据系统语言自动选择英文或简体中文的功能。

> Nintendo Switch 是任天堂的商标。本项目是独立的非官方社区移植，与任天堂
> 不存在隶属关系，也未获得任天堂的认可、赞助或支持。本项目不包含任天堂的
> 源代码、SDK、固件、加密密钥、ROM、游戏内容或技术措施规避工具。

## 下载与安装

1. 从 GitHub Releases 下载 `CDDAforSwitch-v0.1.0.zip`。
2. 将压缩包内的 `CDDAforSwitch` 文件夹解压到 SD 卡的 `switch` 目录。
3. 最终目录结构应包含：

   ```text
   sdmc:/switch/CDDAforSwitch/CDDAforSwitch.nro
   sdmc:/switch/CDDAforSwitch/data/
   sdmc:/switch/CDDAforSwitch/gfx/
   sdmc:/switch/CDDAforSwitch/lang/
   ```

4. 建议以完整内存模式进入 Homebrew Menu：按住 **R** 打开一款已安装游戏，
   然后启动 **CDDA for Switch**。不建议使用相册 Applet 模式。

存档、设置和日志位于 `sdmc:/switch/CDDAforSwitch/user/`。升级时请保留此目录。

## Switch 按键

| Switch 操作 | 游戏输入 |
| --- | --- |
| 左摇杆 | 八方向移动 |
| 方向键 | 菜单导航／方向键 |
| A | Enter／确认 |
| B | Esc／取消 |
| X | `I` |
| L | Tab |
| R | Shift+Tab |
| ZL | `x` |
| ZR | 空格 |
| Minus（`-`） | 立即打开完整虚拟键盘 |
| 按下右摇杆 | 物品栏兼容绑定 |

CDDA 有大量随界面变化的单键命令。屏幕底部的半透明快捷栏会按照当前菜单
显示常用操作；所有按钮都可以触摸，点击 **Kbd** 可打开完整键盘。

## 虚拟键盘

紧凑键盘显示在画面下半部，包含 `ABC`、`123` 和 `NAV` 三页，提供字母、
数字、标点、Tab、Shift+Tab、Esc、Backspace、Delete、Enter、Space、方向键、
Home/End、Page Up/Down、F1-F12、Shift、Ctrl 和 Alt。

- 可以直接触摸按键，也可以用方向键或左摇杆选择。
- A 输入当前按键，B 关闭键盘。
- Y 切换 Shift，X 切换页面，R 切换 Ctrl，L 切换 Alt。
- **Text** 会打开 Switch 系统输入法，适合连续输入人物名、世界名及中英文文本。

## 语言

系统语言为简体中文或繁体中文时，游戏默认使用简体中文；其他系统语言默认
使用英文。也可以在游戏的界面设置中手动更改语言。

## Switch 专用改动

- 使用 libnx 原生触摸轮询，支持快捷栏和完整键盘。
- 为按键数量较多的 CDDA 设置 Switch 手柄映射。
- 针对 1280×720 掌机屏幕设置紧凑界面默认值。
- 首次启动自动迁移到轻量图块集，降低内存占用。
- 使用程序目录下可写的 `user/` 保存存档、配置和日志。
- 提前创建配置目录，并检测 Switch 系统语言。
- 使用 SDL2 Tiles 静态交叉编译为 AArch64 Horizon 程序；当前关闭声音。

## 已知限制

- 这是实验性 Homebrew 移植版，尚未覆盖测试 CDDA 的全部功能和模组。
- CDDA 的命令数量远多于手柄按键。罕见组合键请使用触摸快捷栏、完整虚拟
  键盘或 USB 键盘。
- v0.1.0 尚未启用声音。
- 简体中文翻译来自上游 0.I 语言目录，少量文本仍可能显示英文。
- 如果启动时立即退出，请确认 `.nro`、`data/` 和 `gfx/` 位于同一目录，且
  Homebrew Menu 使用完整内存模式。诊断日志位于 `user/config/debug.log`。

## 编译

本项目使用 CMake 和 devkitPro Switch 工具链。需要安装 devkitA64、libnx、
switch-pkg-config、switch-SDL2、switch-SDL2_image、switch-SDL2_ttf、
switch-freetype、switch-libpng、switch-libjpeg-turbo、switch-libwebp、
switch-zlib，以及带 Babel 的 Python 3。

```sh
export DEVKITPRO=/opt/devkitpro
export DEVKITA64="$DEVKITPRO/devkitA64"
cmake -S . -B build-switch \
  -DCMAKE_TOOLCHAIN_FILE="$DEVKITPRO/cmake/Switch.cmake" \
  -DCMAKE_BUILD_TYPE=Release \
  -DTILES=ON -DSOUND=OFF -DLOCALIZE=ON -DTESTS=OFF \
  -DGETTEXT_MSGFMT_BINARY="$PWD/tools/switch-msgfmt"
cmake --build build-switch --target CDDAforSwitch-nro -j"$(nproc)"
```

生成文件为 `build-switch/CDDAforSwitch.nro`。

## 上游、许可证与致谢

CDDA for Switch 基于
[CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA)。
Cataclysm: DDA 的代码和内容依照
[知识共享 署名—相同方式共享 3.0 未本地化版本许可证](LICENSE.txt)发布。
随附字体和第三方组件继续使用各自的许可证。

所有上游贡献者保留其作品署名；Switch 专用修改以相同的 CC BY-SA 3.0
条款发布。
