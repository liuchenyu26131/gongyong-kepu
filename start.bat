@echo off
chcp 65001 >nul
echo ============================================
echo   功用科普 - 本地预览服务器
echo ============================================
echo.
echo 请选择一个方式启动：
echo.
echo 1 - Python 3 启动 (推荐)
echo 2 - Node.js 启动
echo 3 - 使用 VS Code Live Server
echo 4 - 直接退出
echo.
set /p choice="请输入数字 (1/2/3/4): "

if "%choice%"=="1" (
    echo.
    python --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo 启动 Python HTTP 服务器...
        echo 访问地址: http://localhost:8080
        echo 按 Ctrl+C 停止
        echo.
        python -m http.server 8080
    ) else (
        echo 未检测到 Python，尝试 Python 3...
        python3 --version >nul 2>&1 && (
            echo 访问地址: http://localhost:8080
            python3 -m http.server 8080
        ) || (
            echo 错误: 未安装 Python，请尝试其他选项
            pause
        )
    )
) else if "%choice%"=="2" (
    echo.
    npx --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo 启动 Node.js HTTP 服务器...
        echo 访问地址: http://localhost:3000
        echo 按 Ctrl+C 停止
        echo.
        npx http-server -p 3000 -c-1
    ) else (
        echo 错误: 未安装 Node.js/npx
        pause
    )
) else if "%choice%"=="3" (
    echo.
    echo 请在 VS Code 中打开当前文件夹，然后：
    echo 1. 按 Ctrl+Shift+P
    echo 2. 输入 "Live Server: Open with Live Server"
    echo 3. 或右键 index.html → Open with Live Server
    echo.
    pause
) else (
    exit /b
)
