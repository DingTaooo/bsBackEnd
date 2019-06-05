"""kzyd03 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from django.conf.urls import url, include
from kzyd03.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from books.views import BooksListViewset, ChaptersListViewset, BookCommentsListViewset, ExpandListViewset, AuthorViewset, TimelineViewset, CharactersViewset
from circles.views import CirclesListViewset, AllCirclesViewset, CircleCommentViewset, AllCircleCommentViewset
from operation.views import UsersBooksListViewset, UsersBookDetailListViewset, UserCommentBooksListViewset, UserAddCommentBooksListViewset, UserCommentChapterListViewset, AddUserCommentChapterListViewset, UserFellbackViewset, UserLikeCircleViewset, UserLikeCircleDetailViewset

router = DefaultRouter()
router.register(r'books', BooksListViewset)
router.register(r'chapters', ChaptersListViewset, base_name="chapters")
router.register(r'chaptersexpand', ExpandListViewset)
router.register(r'bookcomments', BookCommentsListViewset)
router.register(r'usersbooks', UsersBooksListViewset, base_name="userdbooks")
router.register(r'usersbookdetail', UsersBookDetailListViewset, base_name="usersbookdetail")
router.register(r'usersfellback', UserFellbackViewset, base_name="usersfellback")
router.register(r'timeline', TimelineViewset, base_name="timeline")
router.register(r'characters', CharactersViewset, base_name="characters")
router.register(r'usercommentbook', UserCommentBooksListViewset, base_name="usercommentbook")
router.register(r'useraddcommentbook', UserAddCommentBooksListViewset, base_name="useraddcommentbook")
router.register(r'usercommentchapter', UserCommentChapterListViewset, base_name="usercommentchapter")
router.register(r'addusercommentchapter', AddUserCommentChapterListViewset, base_name="addusercommentchapter")
router.register(r'addcircles', CirclesListViewset, base_name="addcircles")
router.register(r'allcircles', AllCirclesViewset, base_name="allcircles")
router.register(r'likecircles', UserLikeCircleViewset, base_name="likecircles")
router.register(r'likecirclesdetail', UserLikeCircleDetailViewset, base_name="likecirclesdetail")
router.register(r'circlescomment', CircleCommentViewset, base_name="circlescomment")
router.register(r'allcirclescomment', AllCircleCommentViewset, base_name="allcirclescomment")

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
  url(r'^', include(router.urls)),
  url(r'desc/', include_docs_urls(title="扩展阅读系统")),
  url(r'^api-auth/', include('rest_framework.urls'))
]
