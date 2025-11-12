from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 프로젝트의 루트 URL ('/')로 들어오는 모든 요청을 core 앱의 urls.py로 전달합니다.
    path('', include('core.urls')), 
]

# DEBUG=False인 프로덕션 환경에서 정적 파일과 미디어 파일을 서빙하기 위한 설정 추가 (WhiteNoise와 함께 작동)
# Render 환경에서는 WhiteNoise가 처리하지만, 이 설정을 유지하는 것이 Django 표준에 가깝습니다.
if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 미디어 파일이 있다면 이 라인도 추가합니다.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)