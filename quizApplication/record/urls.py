from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^panel/question/record/$', views.record_list, name = 'record_list'),
    url(r'^panel/record/del/(?P<pk>\d+)/$', views.record_delete, name ='record_delete'),
    url(r'^user/panel/record/list/$', views.record_list_user, name = 'record_list_user'),
    url(r'^user/panel/result/(?P<word>.*)/$', views.user_result, name='user_result'),
]
