from django.urls import path
from . import views

app_name = 'Fairecord'

urlpatterns = [
    # 세션에 관한 Create, delete
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]