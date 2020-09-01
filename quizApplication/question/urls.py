from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/question/list/$', views.question_list, name = 'question_list'),
    url(r'^panel/question/add/$', views.question_add, name = 'question_add'),
    url(r'^panel/question/del/(?P<pk>\d+)/$', views.question_delete, name = 'question_delete'),
    url(r'^panel/question/edit/(?P<pk>\d+)/$', views.question_edit, name = 'question_edit'),
]