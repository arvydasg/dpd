from django.urls import path
from . views import TaskaiList, TaskaiDetail, TaskaiCreate, TaskaiUpdate, DeleteView

urlpatterns = [
    path('', TaskaiList.as_view(), name='visi-taskai'),
    path('taskas/<int:pk>/', TaskaiDetail.as_view(), name='taskas'),
    path('taskas-pridek/', TaskaiCreate.as_view(), name='taskas-pridek'),
    path('taskas-update/<int:pk>/', TaskaiUpdate.as_view(), name='taskas-update'),
    path('taskas-delete/<int:pk>/', DeleteView.as_view(), name='taskas-delete'),
]
