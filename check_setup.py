#!/usr/bin/env python3
"""
МАГ-ОДЕЖ - Проверка конфигурации
Скрипт для проверки, что всё настроено правильно перед запуском
"""

import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

# Цвета для вывода
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    """Печать заголовка"""
    print(f"\n{BLUE}{'='*50}{RESET}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{BLUE}{'='*50}{RESET}\n")

def check_python_version():
    """Проверка версии Python"""
    print(f"{BLUE}🐍 Проверка версии Python...{RESET}")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"{GREEN}✅ Python {version.major}.{version.minor}.{version.micro} - OK{RESET}\n")
        return True
    else:
        print(f"{RED}❌ Требуется Python 3.8+, у вас {version.major}.{version.minor}{RESET}\n")
        return False

def check_required_files():
    """Проверка наличия необходимых файлов"""
    print(f"{BLUE}📁 Проверка файлов...{RESET}")
    required_files = [
        'main.py',
        'html.html',
        'basket.html',
        'script.js',
        'style.css',
        'requirements.txt',
        '.env.example'
    ]
    
    all_exist = True
    for file in required_files:
        if os.path.exists(file):
            print(f"{GREEN}✅ {file}{RESET}")
        else:
            print(f"{RED}❌ {file} - ОТСУТСТВУЕТ{RESET}")
            all_exist = False
    
    print()
    return all_exist

def check_dependencies():
    """Проверка установленных зависимостей"""
    print(f"{BLUE}📦 Проверка зависимостей...{RESET}")
    
    required_packages = {
        'Flask': 'Flask',
        'telegram': 'python-telegram-bot',
        'dotenv': 'python-dotenv',
        'aiohttp': 'aiohttp',
    }
    
    all_installed = True
    for package, pip_name in required_packages.items():
        try:
            __import__(package)
            print(f"{GREEN}✅ {pip_name}{RESET}")
        except ImportError:
            print(f"{RED}❌ {pip_name} - НЕ УСТАНОВЛЕН{RESET}")
            print(f"   {YELLOW}Установите: pip install {pip_name}{RESET}")
            all_installed = False
    
    print()
    return all_installed

def check_env_file():
    """Проверка .env файла"""
    print(f"{BLUE}🔐 Проверка конфигурации .env...{RESET}")
    
    if not os.path.exists('.env'):
        print(f"{YELLOW}⚠️  .env файл не найден{RESET}")
        print(f"   {BLUE}Команда для создания: cp .env.example .env{RESET}\n")
        return False
    
    load_dotenv('.env')
    
    required_vars = [
        'TELEGRAM_BOT_TOKEN',
        'TELEGRAM_BOT_USERNAME',
        'TELEGRAM_CHAT_ID'
    ]
    
    config_ok = True
    for var in required_vars:
        value = os.getenv(var, '')
        if value and value not in ['your_bot_token_here', 'YOUR_TELEGRAM_BOT_TOKEN', 'your_chat_id_here', 'YOUR_CHAT_ID']:
            print(f"{GREEN}✅ {var}: {value[:20]}...{RESET}")
        else:
            print(f"{RED}❌ {var}: НЕ ЗАПОЛНЕН или содержит значение по умолчанию{RESET}")
            config_ok = False
    
    print()
    return config_ok

def check_telegram_bot():
    """Проверка подключения к Telegram боту"""
    print(f"{BLUE}🤖 Проверка Telegram бота...{RESET}")
    
    load_dotenv('.env')
    token = os.getenv('TELEGRAM_BOT_TOKEN', '')
    
    if not token or len(token) < 10:
        print(f"{RED}❌ Токен бота не установлен или неверный формат{RESET}\n")
        return False
    
    try:
        import urllib.request
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = urllib.request.urlopen(url, timeout=5)
        data = json.loads(response.read())
        
        if data.get('ok'):
            bot_info = data.get('result', {})
            print(f"{GREEN}✅ Бот подключен: @{bot_info.get('username')}{RESET}")
            print(f"   Имя: {bot_info.get('first_name')}\n")
            return True
        else:
            print(f"{RED}❌ Ошибка Telegram: {data.get('description')}{RESET}\n")
            return False
    
    except urllib.error.URLError:
        print(f"{YELLOW}⚠️  Нет подключения к интернету{RESET}\n")
        return False
    except Exception as e:
        print(f"{RED}❌ Ошибка: {e}{RESET}\n")
        return False

def print_summary(checks):
    """Вывести итоговый отчёт"""
    print_header("📊 ИТОГОВЫЙ ОТЧЁТ")
    
    total = len(checks)
    passed = sum(1 for v in checks.values() if v)
    
    status_bar = ''.join([
        f"{GREEN}●{RESET}" if check else f"{RED}●{RESET}"
        for check in checks.values()
    ])
    
    print(f"Статус: {status_bar}")
    print(f"Результат: {passed}/{total} проверок пройдено\n")
    
    if passed == total:
        print(f"{GREEN}{'='*50}{RESET}")
        print(f"{GREEN}✅ ВСЁ ГОТОВО! Вы можете запустить приложение:{RESET}")
        print(f"{GREEN}   python main.py{RESET}")
        print(f"{GREEN}{'='*50}{RESET}\n")
        return True
    else:
        print(f"{RED}{'='*50}{RESET}")
        print(f"{RED}❌ ЕЩЕ ЧТО-ТО НЕ ГОТОВО{RESET}")
        print(f"{RED}Пожалуйста, исправьте ошибки выше перед запуском{RESET}")
        print(f"{RED}{'='*50}{RESET}\n")
        return False

def main():
    """Основная функция"""
    print_header("🛍️  МАГ-ОДЕЖ - Проверка конфигурации")
    
    checks = {
        'Python версия': check_python_version(),
        'Необходимые файлы': check_required_files(),
        'Зависимости Python': check_dependencies(),
        'Конфигурация .env': check_env_file(),
        'Telegram бот': check_telegram_bot(),
    }
    
    all_ok = print_summary(checks)
    
    return 0 if all_ok else 1

if __name__ == '__main__':
    sys.exit(main())
