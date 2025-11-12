from django.contrib import admin
from django_mongoengine import mongo_admin
from .models import Suggestion, Contact


# 1. Suggestion 모델의 Admin 클래스 정의
class SuggestionAdmin(mongo_admin.DocumentAdmin):
    # 관리자 목록에서 보여줄 필드
    list_display = ('name', 'email', 'source', 'submitted_at') 
    # 검색 필드
    search_fields = ('name', 'email', 'quote_text', 'source')
    # 제출 시간 기준으로 필터링
    list_filter = ('submitted_at',)
    # 상세 보기 페이지에서 필드 순서와 그룹화 지정
    fieldsets = (
        ('제안자 정보', {
            'fields': ('name', 'email')
        }),
        ('밑줄 및 아이디어', {
            'fields': ('quote_text', 'source', 'idea'),
            'description': '고객이 제안한 핵심 문장과 굿즈 아이디어입니다.'
        }),
        ('메타 정보', {
            'fields': ('submitted_at',)
        }),
    )
    # submitted_at은 사용자 입력이 아니므로 읽기 전용으로 설정
    readonly_fields = ('submitted_at',)


# 2. Contact 모델의 Admin 클래스 정의
class ContactAdmin(mongo_admin.DocumentAdmin):
    list_display = ('subject', 'name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('submitted_at',)
    # submitted_at은 읽기 전용으로 설정
    readonly_fields = ('submitted_at',)


# 관리자 페이지에 등록
mongo_admin.site.register(Suggestion, SuggestionAdmin)
mongo_admin.site.register(Contact, ContactAdmin)