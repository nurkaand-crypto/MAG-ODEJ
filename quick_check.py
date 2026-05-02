#!/usr/bin/env python3
"""
БЫСТРАЯ ПРОВЕРКА - убедитесь что всё готово!
Запустите: python quick_check.py
"""

import os
import sys

def check_file(path, name):
    """Проверить есть ли файл"""
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"  ✅ {name}: {size} bytes")
        return True
    else:
        print(f"  ❌ {name}: НЕ НАЙДЕН")
        return False

def check_telegram_config():
    """Проверить конфигурацию Telegram"""
    print("\n🤖 Проверка Telegram конфигурации:")
    
    with open("main.py", "r") as f:
        content = f.read()
        
        if "YOUR_TELEGRAM_BOT_TOKEN" in content:
            print("  ❌ Telegram Token не настроен")
            print("     Замените YOUR_TELEGRAM_BOT_TOKEN на ваш токен")
            return False
        elif "TELEGRAM_BOT_TOKEN = \"" in content:
            print("  ✅ Telegram Token настроен")
        
        if "YOUR_CHAT_ID" in content:
            print("  ❌ Telegram Chat ID не настроен")
            print("     Замените YOUR_CHAT_ID на ваш ID")
            return False
        elif "TELEGRAM_CHAT_ID = \"" in content:
            print("  ✅ Telegram Chat ID настроен")
    
    return True

def main():
    print("""
╔═══════════════════════════════════════╗
║    МАГ-ОДЕЖ - БЫСТРАЯ ПРОВЕРКА      ║
╚═══════════════════════════════════════╝
    """)
    
    print("📁 Проверка файлов:")
    
    files = [
        ("html.html", "Главная страница"),
        ("basket.html", "Корзина"),
        ("about.html", "О нас"),
        ("style.css", "Стили"),
        ("script.js", "JavaScript"),
        ("main.py", "Flask сервер"),
        ("requirements.txt", "Python зависимости"),
        ("setup_telegram_webhook.py", "Webhook скрипт"),
        ("TELEGRAM_GUIDE.md", "Telegram документация"),
        ("README.md", "Основная документация"),
    ]
    
    all_exist = True
    for file, name in files:
        if not check_file(file, name):
            all_exist = False
    
    print("\n" + "="*50)
    
    if not all_exist:
        print("\n❌ Некоторые файлы отсутствуют!")
        sys.exit(1)
    
    # Проверяем конфиг
    if not check_telegram_config():
        print("\n⚠️  Внимание: Telegram не полностью настроен!")
    
    print("\n" + "="*50)
    print("""
✅ ВСЁ ГОТОВО К ЗАПУСКУ!

🚀 Следующие шаги:

1. Установите зависимости:
   pip install -r requirements.txt

2. Получите Telegram токен:
   @BotFather → /newbot → скопируйте токен

3. Обновите main.py:
   TELEGRAM_BOT_TOKEN = "ВАШ_ТОКЕН"
   TELEGRAM_CHAT_ID = "ВАШ_ID"

4. Запустите сервер:
   python main.py

5. Откройте браузер:
   http://localhost:5000

📖 Подробнее: TELEGRAM_GUIDE.md
═════════════════════════════════════════
    """)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)
