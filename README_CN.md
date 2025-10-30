# mp3-to-ogg-py

一个用于在 MP3 和 OGG 音频格式之间相互转换的命令行工具

[English](README.md) | 简体中文

## 安装

### 快速开始（推荐）

**Windows 用户：**
1. 双击运行 `install.bat`（会自动安装所有依赖和工具）
2. 完成后即可在任何位置使用 `audio-converter` 命令

**其他系统：**
```bash
# 1. 进入项目目录
cd mp3-to-ogg-py

# 2. 安装依赖
pip install -r requirements.txt

# 3. 安装命令行工具
pip install -e .
```

### 详细安装方法

#### 方法 1：一键安装（Windows）
双击运行 `install.bat` 或在命令行中执行：
```bash
install.bat
```
这个脚本会自动：
- ✅ 安装所有 Python 依赖库
- ✅ 安装命令行工具
- ✅ 提示你安装 FFmpeg

#### 方法 2：手动安装依赖 + 安装工具
```bash
# 步骤 1: 安装依赖库
pip install -r requirements.txt

# 步骤 2: 安装为命令行工具（开发模式）
pip install -e .

# 或者正式安装
pip install .
```

#### 方法 3：只安装依赖，直接运行脚本
如果你不想安装命令行工具，只想直接运行脚本：

**Windows:**
```bash
# 双击运行或执行
install_dependencies.bat
```

**其他系统:**
```bash
# 安装依赖
pip install -r requirements.txt

# 直接运行脚本
python3 mp3_to_ogg.py
```

## 使用方法

运行程序后会显示以下菜单：
```
===============
Audio converter
===============
[1] Mp3 to Ogg
[2] Ogg to Mp3
[3] Exit
===============
Select an option -> 
```

### 选项 1：将 MP3 转换为 OGG
你可以指定目录路径（转换所有 MP3 文件）或单个文件路径：

**转换目录中的所有 MP3 文件：**
```
Select an option -> 1
Write the path where the mp3 files are for export them as ogg
MP3 Path -> /home/klairm/Music/
```
或在 Windows 上：
```
MP3 Path -> D:/Music/
```

**转换单个 MP3 文件：**
```
Select an option -> 1
Write the path where the mp3 files are for export them as ogg
MP3 Path -> D:/Music/song.mp3
```

转换后的文件将保存在 `export/` 子目录中。

### 选项 2：将 OGG 转换为 MP3
与选项 1 相同，但用于 OGG 文件 - 同样支持目录和单个文件路径。

### 选项 3：退出
退出程序。

## 功能特点

✅ **双向转换** - 支持 MP3 ↔ OGG 互转  
✅ **批量处理** - 可一次转换整个目录的所有文件  
✅ **单文件转换** - 也可以只转换指定的单个文件  
✅ **智能跳过** - 自动跳过已转换的文件  
✅ **跨平台** - 支持 Windows、Linux 和 macOS  
✅ **进度显示** - 转换过程中显示进度动画  
✅ **命令行工具** - 安装后可在任何位置调用  

## 系统要求

- Python 3.6+
- pydub
- progress
- ffmpeg（pydub 进行音频转换所需）

### 安装 FFmpeg

**Windows:**
1. 从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载
2. 解压并添加到系统 PATH 环境变量

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install ffmpeg
```

## 卸载

使用卸载脚本（Windows）：
```bash
uninstall.bat
```

或手动卸载：
```bash
pip uninstall audio-converter-cli
```

## 项目结构

```
mp3-to-ogg-py/
├── mp3_to_ogg.py              # 主程序文件
├── exporters.py               # 转换器模块
├── requirements.txt           # Python 依赖列表
├── setup.py                   # 安装配置（传统）
├── pyproject.toml             # 项目配置（现代）
├── install.bat                # Windows 一键安装脚本
├── install_dependencies.bat   # Windows 依赖安装脚本
├── uninstall.bat              # Windows 卸载脚本
├── README.md                  # 英文说明文档
├── README_CN.md               # 中文说明文档
├── .gitignore                 # Git 忽略文件配置
└── LICENSE                    # GPL v3 许可证
```

## 使用示例

### 示例 1：转换单个文件
```
===============
Audio converter
===============
[1] Mp3 to Ogg
[2] Ogg to Mp3
[3] Exit
===============
Select an option -> 1
===============
Write the path where the mp3 files are for export them as ogg
MP3 Path -> D:/Download/Ink and Circuitry.mp3
Ink and Circuitry Processing... ████████████████████
```

### 示例 2：批量转换目录
```
Select an option -> 1
===============
Write the path where the mp3 files are for export them as ogg
MP3 Path -> D:/Music/
song1 Processing... ████████████████████
song2 Processing... ████████████████████
song3 Processing... ████████████████████
Program finalized succesfully
Program finalized.
```

## 常见问题

**Q: 为什么提示找不到 ffmpeg？**  
A: 需要先安装 ffmpeg 并确保它在系统 PATH 中。

**Q: 转换后的文件在哪里？**  
A: 转换后的文件保存在源文件所在目录的 `export/` 子目录中。

**Q: 可以转换其他格式吗？**  
A: 目前只支持 MP3 和 OGG 格式的互转。

**Q: 如何在代码中使用这些函数？**  
A: 可以导入模块使用：
```python
from mp3_to_ogg import mp3_to_ogg, ogg_to_mp3

# 转换目录中的所有 MP3 文件
mp3_to_ogg("D:/Music/")

# 转换单个文件
mp3_to_ogg("D:/Music/song.mp3")
```

## 许可证

本项目采用 GNU General Public License v3.0 许可证 - 详见 [LICENSE](LICENSE) 文件

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

原作者：klairm  
改进版本：包含单文件转换、命令行工具等功能

