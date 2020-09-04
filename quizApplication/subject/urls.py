from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/subject/list/$', views.subject_list, name='subject_list'),
    url(r'^panel/subject/add/$', views.subject_add, name='subject_add'),
    url(r'^user/panel/quiz/(?P<word>.*)/$', views.user_quiz, name='user_quiz'),
]
