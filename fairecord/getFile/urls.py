from django.urls import path

from . import views

#유알엘 패턴에 걸리게 되면 이 뷰를 호출하겠다. 
# question_id는 view에 있는 파라미터임
# view에서 처리하게 될 것임
#여기는 정말 url 의 경로에 따라서 어떤걸 실행시켜줄 지 나눠주는 곳

#URLconf에 namespace를 추가하여 앱(기능) 마다의 이름을 설정
#template html 파일에 polls이렇게 url이 변경되어도 괜찮음
app_name = 'getFile'

# path('url창에 들어갈 경로', views.함수 , name='함수' ) 
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:file_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    # path('<int:file_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    # path('<int:file_id>/vote/', views.vote, name='vote'),
]