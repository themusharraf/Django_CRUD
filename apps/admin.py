from django.contrib import admin
from django.utils.html import format_html

from apps.models import Person, Job


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'address', 'phone', 'job','image_tag')
    fields = ('fullname', 'email', 'address', 'phone', 'job', 'image')

    def image_tag(self, obj):
        return format_html(f'''<a href="{obj.image.url}" target="_blank"><img src="{obj.image.url}"
         alt="image" width="100 height="100" style="object-fit : cover;"/></a>''')


@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)
