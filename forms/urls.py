from django.urls import path
from .views import work_completion_form, work_completion_list, toolbox_talk_form, toolbox_talk_list

urlpatterns = [
    path('work_completion/', work_completion_form, name='work_completion_form'),
    path('work_completion/list/', work_completion_list, name='work_completion_list'),
    path('toolbox_talk/', toolbox_talk_form, name='toolbox_talk_form'),
    path('toolbox_talk/list/', toolbox_talk_list, name='toolbox_talk_list'),
]
