from django.urls import path
from . import views


#처음 로그인 메세지 호출
urlpatterns = [
    path('', views.index, name='index'),
]


#로그인
# app_name = 'fairecord'
# urlpatterns = [
    # 세션에 관한 Create
    #path('login/', views.login, name='login')
#]
