from django.urls import path
from . import views

# 이 앱의 URL 이름공간을 정의합니다.
app_name = 'core'

urlpatterns = [
    # http://127.0.0.1:8000/ 에 접속하면 views.index 함수가 실행됩니다.
    path('', views.index, name='index'),

    # http://127.0.0.1:8000/story/ 에 접속하면 views.story 함수가 실행됩니다.
    path('story/', views.story, name='story'),
    
    path('suggestion/', views.suggestion_view, name='suggestion'), # 다음 밑줄 제안
    path('contact/', views.contact_view, name='contact'),         # 문의 및 제휴
    path('about/', views.about_us_view, name='about_us'), # 회사 소개
    path('projects/', views.projects_view, name='projects'), # 프로젝트 현황
]