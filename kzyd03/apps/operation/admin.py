from django.contrib import admin
from operation.models import userFavBook, userCommentBook, userCommentChapter, userFellback

# Register your models here.
admin.site.register(userFavBook)
admin.site.register(userCommentBook)
admin.site.register(userCommentChapter)
admin.site.register(userFellback)