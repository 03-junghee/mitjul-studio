from django.contrib import admin
from django.urls import path, include # 'include'를 임포트해야 합니다.

urlpatterns = [
    path('admin/', admin.site.urls),

    # 프로젝트의 루트 URL ('')로 들어오는 모든 요청을 core 앱의 urls.py로 전달합니다.
    path('', include('core.urls')), # <-- 이 줄을 추가합니다.
]