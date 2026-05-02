#!/bin/bash
# МАГ-ОДЕЖ - Запуск приложения (Linux/Mac)

echo "🛍️  МАГ-ОДЕЖ - Запуск приложения"
echo "================================"

# Проверяем Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 не установлен"
    exit 1
fi

echo "✅ Python установлен"

# Создаём виртуальное окружение если его нет
if [ ! -d "venv" ]; then
    echo "📦 Создаём виртуальное окружение..."
    python3 -m venv venv
fi

# Активируем виртуальное окружение
echo "🔄 Активирую виртуальное окружение..."
source venv/bin/activate

# Устанавливаем зависимости
echo "📥 Устанавливаю зависимости..."
pip install -q -r requirements.txt

# Проверяем конфигурацию
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  Файл .env не найден!"
    echo "   Создаю .env из примера..."
    cp .env.example .env
    echo "   Пожалуйста, отредактируйте .env файл и добавьте:"
    echo "   - TELEGRAM_BOT_TOKEN (от @BotFather)"
    echo "   - TELEGRAM_BOT_USERNAME (имя вашего бота)"
    echo "   - TELEGRAM_CHAT_ID (ваш личный ID)"
    echo ""
    exit 1
fi

# Запускаем проверку конфигурации
echo ""
echo "🔍 Проверяю конфигурацию..."
python3 check_setup.py

if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  Пожалуйста, исправьте ошибки выше"
    exit 1
fi

echo ""
echo "🚀 Запускаю приложение..."
echo "📍 Открывите браузер на: http://localhost:5000"
echo ""
echo "Для остановки нажмите Ctrl+C"
echo ""

python3 main.py
