#!/usr/bin/env python3
"""
Интерактивный конфигуратор МАГ-ОДЕЖ
Помогает легко настроить все необходимые параметры
"""

import os
import sys

def print_header():
    print("\n" + "="*50)
    print("  МАГ-ОДЕЖ - Конфигуратор")
    print("="*50 + "\n")

def print_section(title):
    print(f"\n{'='*50}")
    print(f"  {title}")
    print(f"{'='*50}\n")

def get_telegram_token():
    """Получить Telegram токен от пользователя"""
    print_section("🤖 НАСТРОЙКА TELEGRAM БОТ")
    
    print("Как получить Telegram Bot Token:")
    print("1. Откройте Telegram и найдите @BotFather")
    print("2. Отправьте команду: /newbot")
    print("3. Следуйте инструкциям")
    print("4. Скопируйте полученный токен\n")
    
    token = input("Введите Telegram Bot Token: ").strip()
    
    if not token or ":" not in token:
        print("⚠️  Токен выглядит неправильно. Проверьте формат: 123456:ABC-DEF...")
        return None
    
    return token

def get_telegram_chat_id():
    """Получить Chat ID от пользователя"""
    print("\nКак получить Chat ID:")
    print("1. Отправьте своему боту любое сообщение")
    print("2. Откройте в браузере:")
    print("   https://api.telegram.org/bot<ВАШ_ТОКЕН>/getUpdates")
    print("3. Найдите 'id' в ответе\n")
    
    chat_id = input("Введите Telegram Chat ID: ").strip()
    
    if not chat_id or not chat_id.isdigit():
        print("⚠️  Chat ID должен быть числом")
        return None
    
    return chat_id

def get_gmail_config():
    """Получить Gmail конфигурацию"""
    print_section("📧 НАСТРОЙКА EMAIL (GMAIL)")
    
    print("Требуется:")
    print("1. Gmail аккаунт")
    print("2. Включённая двухфакторная аутентификация")
    print("3. Пароль приложения (App Password)\n")
    
    print("Как получить пароль приложения:")
    print("1. Откройте https://myaccount.google.com/security")
    print("2. Включите двухфакторную аутентификацию")
    print("3. Найдите 'Пароли приложений'")
    print("4. Выберите Mail и текущее устройство")
    print("5. Скопируйте 16-символьный пароль\n")
    
    email = input("Введите ваш Gmail адрес: ").strip()
    
    if "@gmail.com" not in email:
        print("⚠️  Email должен быть Gmail аккаунтом (@gmail.com)")
        return None, None
    
    password = input("Введите пароль приложения (16 символов): ").strip()
    
    if len(password.replace(" ", "")) != 16:
        print("⚠️  Пароль должен содержать 16 символов (пробелы можно пропустить)")
        return None, None
    
    return email, password

def update_main_py(token, chat_id, email, password):
    """Обновить main.py с новыми значениями"""
    
    main_py_path = "main.py"
    
    if not os.path.exists(main_py_path):
        print("❌ Файл main.py не найден!")
        return False
    
    try:
        with open(main_py_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Заменяем значения
        if token:
            content = content.replace(
                'TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"',
                f'TELEGRAM_BOT_TOKEN = "{token}"'
            )
        
        if chat_id:
            content = content.replace(
                'TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"',
                f'TELEGRAM_CHAT_ID = "{chat_id}"'
            )
        
        if email:
            content = content.replace(
                'EMAIL_SENDER = "your_email@gmail.com"',
                f'EMAIL_SENDER = "{email}"'
            )
        
        if password:
            content = content.replace(
                'EMAIL_PASSWORD = "your_app_password"',
                f'EMAIL_PASSWORD = "{password}"'
            )
        
        # Сохраняем файл
        with open(main_py_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    except Exception as e:
        print(f"❌ Ошибка при обновлении main.py: {e}")
        return False

def print_summary(token, chat_id, email, password):
    """Вывести итоговую информацию"""
    print_section("✅ КОНФИГУРАЦИЯ ЗАВЕРШЕНА")
    
    print("Сохранённые данные:\n")
    
    if token:
        print(f"✅ Telegram Token: {token[:20]}...")
    else:
        print("❌ Telegram Token: НЕ НАСТРОЕН")
    
    if chat_id:
        print(f"✅ Telegram Chat ID: {chat_id}")
    else:
        print("❌ Telegram Chat ID: НЕ НАСТРОЕН")
    
    if email:
        print(f"✅ Email: {email}")
    else:
        print("❌ Email: НЕ НАСТРОЕН")
    
    if password:
        print(f"✅ Email пароль: {'*' * len(password)}")
    else:
        print("❌ Email пароль: НЕ НАСТРОЕН")
    
    print("\n" + "="*50)
    print("Теперь вы готовы к запуску!")
    print("\nДля запуска сервера используйте:")
    print("  python main.py")
    print("\nОткройте браузер: http://localhost:5000")
    print("="*50 + "\n")

def main():
    """Главная функция"""
    print_header()
    
    print("Этот скрипт поможет вам настроить МАГ-ОДЕЖ магазин\n")
    
    # Спрашиваем, хочет ли пользователь настраивать Telegram
    configure_telegram = input("Хотите настроить Telegram уведомления? (y/n): ").lower().strip()
    
    token = None
    chat_id = None
    
    if configure_telegram == 'y':
        token = get_telegram_token()
        if token:
            chat_id = get_telegram_chat_id()
    
    # Спрашиваем, хочет ли пользователь настраивать Email
    configure_email = input("\nХотите настроить Email уведомления? (y/n): ").lower().strip()
    
    email = None
    password = None
    
    if configure_email == 'y':
        email, password = get_gmail_config()
    
    # Обновляем main.py
    print("\n⏳ Сохранение конфигурации...")
    
    if update_main_py(token, chat_id, email, password):
        print("✅ Конфигурация сохранена!")
        print_summary(token, chat_id, email, password)
    else:
        print("❌ Ошибка при сохранении конфигурации")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Конфигурация отменена пользователем")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        sys.exit(1)
