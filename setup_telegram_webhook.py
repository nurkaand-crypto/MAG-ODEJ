#!/usr/bin/env python3
"""
Скрипт для настройки Telegram Webhook для МАГ-ОДЕЖ бота
"""

import urllib.request
import urllib.error
import json
import sys

def setup_webhook(token, webhook_url):
    """Настроить webhook для Telegram бота"""
    
    print(f"\n⏳ Настройка Telegram webhook...")
    print(f"   URL: {webhook_url}")
    
    try:
        url = f"https://api.telegram.org/bot{token}/setWebhook"
        
        data = json.dumps({
            'url': webhook_url,
            'allowed_updates': ['message']
        }).encode('utf-8')
        
        req = urllib.request.Request(url, data=data)
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read())
            
            if result.get('ok'):
                print("✅ Webhook успешно настроен!")
                print(f"   Описание: {result.get('description', 'N/A')}")
                return True
            else:
                print(f"❌ Ошибка: {result.get('description', 'Unknown error')}")
                return False
    
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP ошибка: {e.code}")
        print(f"   {e.read().decode('utf-8')}")
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def get_webhook_info(token):
    """Получить информацию о текущем webhook"""
    
    print(f"\n📋 Информация о webhook...")
    
    try:
        url = f"https://api.telegram.org/bot{token}/getWebhookInfo"
        
        with urllib.request.urlopen(url, timeout=10) as response:
            result = json.loads(response.read())
            
            if result.get('ok'):
                info = result.get('result', {})
                print(f"✅ Webhook установлен:")
                print(f"   URL: {info.get('url', 'Не установлен')}")
                print(f"   Статус: {info.get('has_custom_certificate')}")
                print(f"   Обновлений получено: {info.get('pending_update_count', 0)}")
                return True
            else:
                print(f"❌ Ошибка: {result.get('description', 'Unknown error')}")
                return False
    
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    print("""
╔══════════════════════════════════════════════════════╗
║      МАГ-ОДЕЖ - Настройка Telegram Webhook         ║
╚══════════════════════════════════════════════════════╝
    """)
    
    # Получаем токен
    print("🔐 Введите данные:")
    token = input("   Telegram Bot Token: ").strip()
    
    if not token or ":" not in token:
        print("❌ Неверный формат токена!")
        sys.exit(1)
    
    # Получаем URL
    webhook_url = input("   Webhook URL (например: https://example.com/telegram_webhook): ").strip()
    
    if not webhook_url.startswith("https://"):
        print("❌ URL должен начинаться с https://")
        sys.exit(1)
    
    # Проверяем текущий webhook
    print("\n" + "="*50)
    get_webhook_info(token)
    
    # Настраиваем новый webhook
    print("\n" + "="*50)
    if setup_webhook(token, webhook_url):
        print("\n✅ Настройка завершена успешно!")
        print("""
📌 Информация:
   - Бот теперь будет получать сообщения через webhook
   - Все входящие сообщения будут обработаны
   - Убедитесь, что URL доступен из интернета
   - Для локального тестирования используйте ngrok:
     ngrok http 5000
   - И используйте URL из ngrok в качестве webhook
        """)
    else:
        print("\n❌ Ошибка при настройке webhook!")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Отменено пользователем")
        sys.exit(0)
