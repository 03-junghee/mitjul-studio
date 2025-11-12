from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import SuggestionForm, ContactForm
from .models import Suggestion, Contact
import datetime # MongoEngine의 DateTimeField에 timezone을 인식시키기 위해 필요
# 메인 페이지 (HOME)
def index(request):
    """
    메인 페이지를 렌더링합니다.
    슬로건: "당신의 밑줄, 우리의 예술이 되다."
    """
    # 나중에 데이터베이스에서 정보를 가져올 때 이 함수를 수정합니다.
    context = {
        'slogan': "당신의 밑줄, 우리의 예술이 되다.",
        'sub_text': "잊혀지지 않는 문장들을 위한, 밑줄 스튜디오의 기록.",
    }
    return render(request, 'core/index.html', context)

# 브랜드 스토리 페이지 (STORY)
def story(request):
    """
    브랜드 스토리 페이지를 렌더링합니다.
    """
    return render(request, 'core/story.html')

# 다음 밑줄 제안 페이지 (Suggestion)
def suggestion_view(request):
    # 요청이 POST 방식, 즉 폼 제출이라면
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            # 폼 데이터에서 필요한 값 가져오기
            data = form.cleaned_data
            
            # 1. MongoDB (MongoEngine)에 데이터 저장
            Suggestion.objects.create(
                name=data['name'],
                email=data['email'],
                quote_text=data['quote_text'],
                source=data['source'],
                idea=data['idea'],
                # 현재 시간을 UTC timezone으로 저장
                submitted_at=timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone())
            )
            
            # 2. 저장 후 성공 메시지와 함께 메인 페이지로 리디렉션
            # 실제로는 '제안 완료' 페이지로 리디렉션하는 것이 좋습니다.
            return redirect(reverse('core:index') + '?status=suggestion_success')

    # GET 방식이거나 폼 검증에 실패했다면
    else:
        form = SuggestionForm()

    context = {
        'form': form
    }
    return render(request, 'core/suggestion.html', context)


# 문의 및 제휴 페이지 (Contact)
def contact_view(request):
    # 요청이 POST 방식, 즉 폼 제출이라면
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # 1. MongoDB (MongoEngine)에 데이터 저장
            Contact.objects.create(
                name=data['name'],
                email=data['email'],
                subject=data['subject'],
                message=data['message'],
                submitted_at=timezone.make_aware(datetime.datetime.now(), timezone.get_current_timezone())
            )
            
            # 2. 저장 후 성공 메시지와 함께 메인 페이지로 리디렉션
            return redirect(reverse('core:index') + '?status=contact_success')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)

# 회사 소개 (About Us) 페이지
def about_us_view(request):
    # 555.png 이미지를 참고하여 문구를 정의합니다.
    context = {
        'quote': '“밑줄 스튜디오는 기록의 예술적 가치를 믿습니다. 우리가 선택한 한 줄의 문장, 그 작은 흔적이 우리의 삶을 비추는 가장 강력한 빛이 될 수 있습니다. 우아하고 진실된 물건을 통해 당신의 소중한 밑줄을 영원히 기억하겠습니다.”',
        'ceo': 'CEO. Anna Kim'
    }
    return render(request, 'core/about_us.html', context)

# 프로젝트 (Projects) 페이지
def projects_view(request):
    # 666.png, 777.png의 공모전 타임라인 데이터를 구성합니다.
    context = {
        'timeline': [
            {'date': '2025. 04. 01. ~ 05. 30.', 'event': '아이디어 제출'},
            {'date': '2025. 06. 01. ~ 06. 15.', 'event': '내부 심사 및 검토'},
            {'date': '2025. 06. 30.', 'event': '결과 발표'},
            {'date': '2025. 07. ~ 10.', 'event': '시제품 제작 및 출시'},
        ],
        'benefits': [
            {'title': '굿즈 출시', 'desc': '아이디어가 실제 제품으로 제작 및 출시됩니다.'},
            {'title': '로열티 지급', 'desc': '출시 후 발생하는 매출의 일정 비율이 지급됩니다.'},
            {'title': '디자인 참여', 'desc': '제품의 최종 디자인 과정에 참여 기회가 제공됩니다.'},
        ]
    }
    return render(request, 'core/projects.html', context)