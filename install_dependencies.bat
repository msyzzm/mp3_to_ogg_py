@echo off
echo =======================================
echo Audio Converter - 安装依赖
echo Installing Dependencies
echo =======================================
echo.
echo 正在安装 Python 依赖库...
echo Installing Python dependencies...
echo.

pip install -r requirements.txt

echo.
echo =======================================
echo 依赖安装完成！
echo Dependencies installed!
echo =======================================
echo.
echo 注意：你还需要安装 FFmpeg 才能进行音频转换
echo Note: You also need to install FFmpeg for audio conversion
echo.
echo FFmpeg 下载地址 / Download FFmpeg:
echo https://ffmpeg.org/download.html
echo.
pause

