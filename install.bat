@echo off
echo =======================================
echo Audio Converter CLI - 安装程序
echo Audio Converter CLI - Installation
echo =======================================
echo.
echo 正在安装 audio-converter-cli...
echo Installing audio-converter-cli...
echo.
echo 步骤 1/2: 安装依赖库...
echo Step 1/2: Installing dependencies...
echo.

pip install -r requirements.txt

echo.
echo 步骤 2/2: 安装命令行工具...
echo Step 2/2: Installing CLI tool...
echo.

pip install -e .

echo.
echo =======================================
echo 安装完成！
echo Installation complete!
echo =======================================
echo.
echo 现在你可以在任何位置使用 'audio-converter' 命令
echo You can now use 'audio-converter' command from anywhere.
echo.
echo 使用方法 / Usage: audio-converter
echo.
echo =======================================
echo 重要提示 / IMPORTANT
echo =======================================
echo 请确保已安装 FFmpeg，否则无法进行音频转换
echo Please make sure FFmpeg is installed for audio conversion
echo.
echo FFmpeg 下载 / Download: https://ffmpeg.org/download.html
echo =======================================
echo.
pause

