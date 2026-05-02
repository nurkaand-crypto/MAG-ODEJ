#!/bin/bash

# МАГ-ОДЕЖ - Скрипт запуска для Linux/Mac

echo ""
echo "╔══════════════════════════════════════╗"
echo "║        МАГ-ОДЕЖ МАГАЗИН             ║"
echo "║   Интернет-магазин одежды и обуви   ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Проверяем наличие Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python не установлен"
    echo "Установите Python с https://www.python.org/"
    exit 1
fi

echo "✅ Python найден"

# Проверяем наличие pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip не установлен"
    exit 1
fi

echo "✅ pip найден"
echo ""
echo "📦 Установка зависимостей..."

pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Ошибка при установке зависимостей"
    exit 1
fi

echo ""
echo "✅ Зависимости установлены"
echo ""
echo "🚀 Запуск сервера МАГ-ОДЕЖ..."
echo ""
echo "📌 ПОЖАЛУЙСТА, ОБРАТИТЕ ВНИМАНИЕ:"
echo "   1. Откройте main.py в текстовом редакторе"
echo "   2. Найдите строки с YOUR_TELEGRAM_BOT_TOKEN и YOUR_CHAT_ID"
echo "   3. Замените на ваши данные из Telegram"
echo "   4. Найдите EMAIL_SENDER и EMAIL_PASSWORD"
echo "   5. Замените на ваши данные Gmail"
echo ""
echo "📍 После запуска откройте: http://localhost:5000"
echo ""

python3 main.py
