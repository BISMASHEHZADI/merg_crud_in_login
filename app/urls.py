from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('send/',views.send,name='send'),
    path('add/',views.add,name='add'),
    path('<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]
