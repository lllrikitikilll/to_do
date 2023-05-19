from django.urls import path, include
from . import views
app_name = 'task'

urlpatterns = [
    path('', views.TsList.as_view(), name='index'),
    path('add/<str:date_str>', views.AddTask.as_view(), name='add'),
    path('<int:pk>/', views.TaskDetail.as_view(), name='detail')
]
