from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'', include('question.urls')),
    url(r'', include('record.urls')),
    url(r'', include('subject.urls')),
    url(r'', include('comment.urls')),
    url(r'', include('manager.urls')),
]
