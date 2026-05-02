@echo off
REM МАГ-ОДЕЖ - Скрипт запуска для Windows

echo.
echo ╔══════════════════════════════════════╗
echo ║        МАГ-ОДЕЖ МАГАЗИН             ║
echo ║   Интернет-магазин одежды и обуви   ║
echo ╚══════════════════════════════════════╝
echo.

REM Проверяем наличие Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python не установлен или не в PATH
    echo Пожалуйста, установите Python с https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Python найден

REM Проверяем наличие pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip не установлен
    pause
    exit /b 1
)

echo ✅ pip найден
echo.
echo 📦 Установка зависимостей...
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo ❌ Ошибка при установке зависимостей
    pause
    exit /b 1
)

echo.
echo ✅ Зависимости установлены
echo.
echo � Проверка конфигурации...
python check_setup.py

if %errorlevel% neq 0 (
    echo.
    echo ❌ Конфигурация содержит ошибки
    echo Пожалуйста, исправьте их перед запуском
    pause
    exit /b 1
)

echo.
echo 🚀 Запуск сервера МАГ-ОДЕЖ...
echo.
echo 📍 Откройте в браузере: http://localhost:5000
echo.
echo Для остановки нажмите Ctrl+C
echo.
pause

python main.py

pause
