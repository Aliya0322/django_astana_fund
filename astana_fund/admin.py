from django.contrib import admin
from django import forms

from .models import Event, EventImage, MediaPublication, Project, Video, Music, Article



class EventImageInlineForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields = ['image', 'caption']



class EventImageInlineFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.extra = max(12 - len(self.initial_forms), 1)
        if len(self.initial_forms) + self.extra > 12:
            self.extra = 12 - len(self.initial_forms)

    def clean(self):
        super().clean()
        total_photos = len([
            form for form in self.forms
            if form.cleaned_data.get('image') and not form.cleaned_data.get('DELETE', False)
        ])
        if total_photos > 12:
            raise forms.ValidationError("Максимальное количество фотографий — 12.")



class EventImageInline(admin.TabularInline):
    model = EventImage
    form = EventImageInlineForm
    formset = EventImageInlineFormSet
    extra = 1
    max_num = 12
    fields = ('image', 'caption')  # Убрано 'DELETE'
    verbose_name = 'Фотография'
    verbose_name_plural = 'Фотографии мероприятия'
    can_delete = True  # Добавлено для возможности удаления

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.min_num = 1
        return formset



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]
    list_display = ('title', 'start_date', 'status_display', 'location', 'is_active')
    list_filter = ('is_active', 'start_date')
    search_fields = ('title', 'location')

    def status_display(self, obj):
        return obj.status_display

    status_display.short_description = 'Статус'
    status_display.admin_order_field = 'start_date'  # Для сортировки по статусу



admin.site.register(MediaPublication)
admin.site.register(Project)
admin.site.register(Video)
admin.site.register(Music)
admin.site.register(Article)
