from django.contrib import admin
from books.models import Books, BookComments, ChapterComments, Chapters, Expand,  Authors, Timeline, Characters

# Register your models here.
admin.site.register(Books)
admin.site.register(BookComments)
admin.site.register(ChapterComments)
admin.site.register(Chapters)
admin.site.register(Expand)
admin.site.register(Authors)
admin.site.register(Timeline)
admin.site.register(Characters)