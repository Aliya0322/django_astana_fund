from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from astana_fund import views
from astana_fund.views import main_page, global_search, media_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main_page'), # Главная страница
    path('event/', views.event, name='event'), # Страница Мероприятия
    path('events/upcoming/<int:event_id>/', views.event_detail_future, name='event_detail_future'), # Страница с деталями будущего мероприятия
    path('events/past/<int:event_id>/', views.event_detail_past, name='event_detail_past'), # Страница с деталями прошедшего мероприятия
    path('about/', views.about, name='about'), # Страница О нас
    path('media/', views.media, name='media'),  # Страница СМИ о нас
    path('media/<slug:slug>/', media_detail, name='media_detail'),
    path('projects/', views.projects, name='projects'),  # Страница Проекты
    path('help/', views.help, name='help'),  # Страница Помощь Фонду
    path('interesting/', views.interesting, name='interesting'),  # Страница Интересное
    path('feedback/', views.feedback_view, name='feedback'), # Страница Обратная связь
    path('search/', global_search, name='global_search'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
