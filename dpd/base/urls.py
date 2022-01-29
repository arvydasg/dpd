from django.urls import path
from . views import TaskaiList, TaskaiDetail, TaskaiCreate, TaskaiUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView # for logout is simply this and one url pattern as you can see above. no need to create another view class

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    
    path('', TaskaiList.as_view(), name='visi-taskai'),
    path('taskas/<int:pk>/', TaskaiDetail.as_view(), name='taskas'),
    path('taskas-pridek/', TaskaiCreate.as_view(), name='taskas-pridek'),
    path('taskas-update/<int:pk>/', TaskaiUpdate.as_view(), name='taskas-update'),
    path('taskas-delete/<int:pk>/', DeleteView.as_view(), name='taskas-delete'),
]
