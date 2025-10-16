import os
import django
from django.core.wsgi import get_wsgi_application

# Установка настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings_vercel')

# Инициализация Django
django.setup()

# Получение WSGI приложения
application = get_wsgi_application()

# Функция обработчик для Vercel
def handler(request):
    return application(request)

# Экспорт для совместимости
app = application
