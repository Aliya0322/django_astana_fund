from django.http import HttpRequest, JsonResponse
from .models import Event, MediaPublication, Project, Article, Video, Music
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone


def main_page(request):
    now = timezone.now()
    current_events = Event.objects.filter(start_date__gte=now, is_active=True).order_by('start_date')[:3]
    past_events = Event.objects.filter(start_date__lt=now, is_active=True).order_by('-start_date')[:3]

    return render(request, 'main_page.html', {
        'current_events': current_events,
        'past_events': past_events,
    })


def event(request):
    now = timezone.now()
    upcoming = Event.objects.filter(start_date__gt=now).order_by('start_date')
    past = Event.objects.filter(start_date__lte=now).order_by('-start_date')

    return render(request, 'event.html', {
        'upcoming_events': upcoming,
        'past_events': past,
        'now': now,
    })


def event_detail_future(request, event_id):
    now = timezone.now()
    event = get_object_or_404(
        Event.objects.filter(start_date__gt=now),
        pk=event_id,
        is_active=True
    )
    return render(request, 'event_detail_future.html', {'event': event})


def event_detail_past(request, event_id):
    now = timezone.now()
    event = get_object_or_404(
        Event.objects.filter(
            Q(end_date__lt=now) | Q(end_date__isnull=True, start_date__lt=now)  # Убрано models.
        ),
        pk=event_id,
        is_active=True
    )
    return render(request, 'event_detail_past.html', {'event': event})


def about(request:HttpRequest):
    return render(request, 'about.html')

def media(request):
    publications = MediaPublication.objects.filter(is_published=True).order_by('-publication_date')
    context = {
        'publications': publications
    }
    return render(request, 'media.html', context)

def media_detail(request, slug):
    publication = get_object_or_404(MediaPublication, slug=slug, is_published=True)
    return render(request, 'media_detail.html', {'publication': publication})

# Страница "Проекты"
def projects(request):
    return render(request, 'projects.html')

# Страница "Помощь фонду"
def help(request):
    return render(request, 'help.html')

# Страница "Интересное"
def interesting(request):
    videos = Video.objects.all()
    music_list = Music.objects.all()
    articles = Article.objects.all()

    return render(request, 'interesting.html', {
        'videos': videos,
        'music_list': music_list,
        'articles': articles
    })

#Отправка письма
def feedback_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f'Новое обращение от {first_name} {last_name}'
        email_message = f'''
        Имя: {first_name}
        Фамилия: {last_name}
        Email: {email}

        Сообщение:
        {message}
        '''

        try:
            # Отправляем письмо администратору (используем CONTACT_EMAIL из settings)
            send_mail(
                subject=subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],  # почта администратора
                fail_silently=False,
            )

            # Отправляем подтверждение пользователю
            send_mail(
                subject='Ваше обращение в Фонд "Астана"',
                message=f'Благодарим за ваше обращение! Мы получили ваше сообщение:\n\n{message}\n\nСкоро с вами свяжемся.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],  # почта пользователя из формы
                fail_silently=False,
            )

            messages.success(request, 'Ваше сообщение успешно отправлено!')
            return redirect('feedback')

        except Exception as e:
            messages.error(request, f'Произошла ошибка при отправке: {e}')

    return render(request, 'feedback.html')


def global_search(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        # Поиск по Event
        event_qs = Event.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(short_description__icontains=query)
        ).filter(is_active=True)[:5]

        for item in event_qs:
            results.append({
                'type': 'event',
                'title': item.title,
                'url': item.get_absolute_url(),
            })

        # Поиск по MediaPublication
        media_qs = MediaPublication.objects.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(full_content__icontains=query)
        ).filter(is_published=True)[:5]

        for item in media_qs:
            results.append({
                'type': 'media',
                'title': item.title,
                'url': item.get_absolute_url(),
            })

        # Поиск по Project
        project_qs = Project.objects.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query) |
            Q(full_description__icontains=query)
        )[:5]

        for item in project_qs:
            results.append({
                'type': 'project',
                'title': item.title,
                'url': item.get_absolute_url(),
            })

        # Поиск по Article
        article_qs = Article.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query)
        ).filter(is_published=True)[:5]

        for item in article_qs:
            results.append({
                'type': 'article',
                'title': item.title,
                'url': item.get_absolute_url(),
            })

    return JsonResponse({'results': results})


