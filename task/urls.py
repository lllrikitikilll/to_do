from django.urls import path, include
from . import views
app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<str:date_str>', views.add_task, name='add'),
]
