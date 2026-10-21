# CDDA for Switch

[简体中文](README.zh-CN.md) | English

An unofficial native Nintendo Switch homebrew port of
[Cataclysm: Dark Days Ahead](https://github.com/CleverRaven/Cataclysm-DDA),
based on the 0.I (Ito) stable source. It runs as an AArch64 Horizon `.nro` and
does not emulate the Android or Linux version.

The port adds Switch-oriented defaults, controller mappings, a touch shortcut
bar, a compact full keyboard, native text input, and automatic English or
Simplified Chinese language selection.

> This is an unofficial community port. It is not affiliated with or endorsed
> by Nintendo or the upstream Cataclysm: DDA project.

## Download and install

1. Download `CDDAforSwitch-v0.1.0.zip` from the GitHub Releases page.
2. Extract the `CDDAforSwitch` folder to `sdmc:/switch/`.
3. Confirm that the resulting layout includes:

   ```text
   sdmc:/switch/CDDAforSwitch/CDDAforSwitch.nro
   sdmc:/switch/CDDAforSwitch/data/
   sdmc:/switch/CDDAforSwitch/gfx/
   sdmc:/switch/CDDAforSwitch/lang/
   ```

4. Launch Homebrew Menu with full RAM access: hold **R** while opening an
   installed game, then start **CDDA for Switch**. Album/applet mode is not
   recommended.

Saves, settings, and logs are stored in
`sdmc:/switch/CDDAforSwitch/user/`. Preserve that directory when upgrading.

## Switch controls

| Switch control | Game input |
| --- | --- |
| Left stick | Eight-direction movement |
| D-pad | Menu navigation / arrow keys |
| A | Enter / confirm |
| B | Escape / cancel |
| X | `I` |
| L | Tab |
| R | Shift+Tab |
| ZL | `x` |
| ZR | Space |
| Minus (`-`) | Open the full virtual keyboard immediately |
| Right-stick click | Inventory compatibility binding |

CDDA uses many context-sensitive single-key commands. A translucent shortcut
bar at the bottom of the screen shows useful actions for the current menu.
Every shortcut is touchable; tap **Kbd** to open the full keyboard.

## Virtual keyboard

The compact keyboard occupies the lower part of the display and has `ABC`,
`123`, and `NAV` pages. It includes letters, numbers, punctuation, Tab,
Shift+Tab, Esc, Backspace, Delete, Enter, Space, arrows, Home/End,
Page Up/Down, F1-F12, Shift, Ctrl, and Alt.

- Touch a key directly, or use the D-pad/left stick to select it.
- A activates the selected key; B closes the keyboard.
- Y toggles Shift, X changes page, R toggles Ctrl, and L toggles Alt.
- **Text** opens the Switch system input method for names and other continuous
  English or Chinese text.

## Language

Simplified and Traditional Chinese system languages default to Simplified
Chinese. Other system languages default to English. The language can also be
changed from the in-game interface options.

## Port-specific changes

- Native libnx touch polling for the shortcut bar and full keyboard.
- Switch controller mappings for keyboard-heavy CDDA commands.
- Compact UI defaults targeting the 1280x720 handheld display.
- First-run migration to a lightweight tileset to reduce memory use.
- Writable per-install `user/` directory for saves, configuration, and logs.
- Early configuration-directory creation and Switch locale detection.
- Static AArch64 Horizon build with SDL2 Tiles; sound is currently disabled.

## Known limitations

- This is an experimental homebrew port and has not been tested across every
  CDDA feature or mod.
- CDDA has more commands than a controller can expose. Use the shortcut bar,
  full virtual keyboard, or a USB keyboard for uncommon combinations.
- Sound is not enabled in v0.1.0.
- The included Simplified Chinese catalog may leave some strings in English.
- If the application exits during startup, verify that `data/`, `gfx/`, and
  the `.nro` are together and that Homebrew Menu is running with full RAM.
  Diagnostic output is written to `user/config/debug.log`.

## Building

The port uses CMake with the devkitPro Switch toolchain. Install devkitA64,
libnx, switch-pkg-config, switch-SDL2, switch-SDL2_image, switch-SDL2_ttf,
switch-freetype, switch-libpng, switch-libjpeg-turbo, switch-libwebp,
switch-zlib, and Python 3 with Babel.

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

The resulting executable is `build-switch/CDDAforSwitch.nro`.

## Upstream, license, and credits

CDDA for Switch is derived from
[CleverRaven/Cataclysm-DDA](https://github.com/CleverRaven/Cataclysm-DDA).
Cataclysm: DDA code and content are distributed under the
[Creative Commons Attribution-ShareAlike 3.0 Unported License](LICENSE.txt).
Bundled fonts and third-party components retain their own license notices.

All upstream contributors retain credit for their work. Switch-specific
changes are distributed under the same CC BY-SA 3.0 terms.
