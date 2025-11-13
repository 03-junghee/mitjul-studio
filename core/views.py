from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .forms import SuggestionForm, ContactForm
from .models import Suggestion, Contact
import datetime # MongoEngine의 DateTimeField에 timezone을 인식시키기 위해 필요

products_list = [
    {
        'slug': 'demian-bookmark',
        'name': '데미안 책갈피: 알을 깨고',
        'price': '18,000 KRW',
        'slogan': '새로운 세계로 나아가려는 모든 영혼을 위해',
        'image_name': 'product_1.png', # 'product_01.png' (데미안 관련 이미지) 사용
        # 상세 페이지에 보여줄 추가 정보
        'description': '헤르만 헤세의 《데미안》에서 영감을 받은 책갈피입니다. "새는 알을 깨고 나온다"는 구절처럼, 불안과 성장의 경계에 선 당신의 독서 여정에 동행합니다. 미려한 디자인과 고급스러운 마감은 책 속의 밑줄을 더욱 특별하게 만들어 줍니다.',
        'features': ['소재: 황동(Brass) 및 에나멜', '색상: 앤티크 골드', '특징: 섬세한 부조 표현, 얇고 가벼운 디자인', '원작: 헤르만 헤세, 《데미안》']
    },
    {
        'slug': 'brave-new-world-keyring-class',
        'name': '멋진 신세계 키링: 5계급',
        'price': '22,000 KRW',
        'slogan': '알파부터 앱실론까지, 정해진 운명을 상징하는 문장',
        'image_name': 'product_2.png', # 'product_02.png' (5계급 관련 이미지) 사용
        'description': '올더스 헉슬리의 《멋진 신세계》 속, 태어날 때부터 규정된 다섯 계급(Alpha, Beta, Gamma, Delta, Epsilon)을 모티프로 한 키링 세트입니다. 각 계급의 상징과 색상을 담아, 통제된 사회의 차가운 아름다움을 표현합니다.',
        'features': ['구성: 알파부터 엡실론까지 5개 세트', '재질: 아연 합금 및 유광 코팅', '특징: 각 계급 상징 디자인, 휴대폰 및 가방 장식용', '원작: 올더스 헉슬리, 《멋진 신세계》']
    },
    {
        'slug': 'brave-new-world-keyring-soma',
        'name': '멋진 신세계 키링: 소마 알약',
        'price': '35,000 KRW',
        'slogan': '고통 없는 행복, 통제된 사회의 만능 약물',
        'image_name': 'product_3.png', # 'product_03.png' (소마 얄약 관련 이미지) 사용
        'description': '《멋진 신세계》 속의 상징적인 물질, 소마(Soma) 알약을 형상화한 키링입니다. 현실의 불만과 고통을 잊게 해주는 환상의 약물처럼, 이 키링은 때로는 필요한 일탈과 평온을 시각적으로 상징합니다.',
        'features': ['재질: 투명 아크릴 수지 및 금속 체인', '색상: 스카이 블루 (소마 알약),', '특징: 영롱한 투명 재질, 독특한 캡슐 형태 디자인', '원작: 올더스 헉슬리, 《멋진 신세계》']
    },
]

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

def product(request):
    context = {
        'products': products_list
    }
    return render(request, 'core/product.html', context)


def product_detail(request, product_slug):
    # List를 순회하며 slug가 일치하는 상품을 찾습니다.
    product_data = next((p for p in products_list if p['slug'] == product_slug), None)

    if product_data is None:
        # 상품을 찾지 못하면 404 에러 대신 상품 목록으로 리다이렉트합니다.
        # 실제로는 return redirect('core:product') 를 사용하는 것이 더 사용자 친화적일 수 있습니다.
        raise Http404("상품을 찾을 수 없습니다.")
    
    # 찾은 상품 데이터 전체를 템플릿에 전달합니다.
    context = {
        'product': product_data,
    }
    return render(request, 'core/product_detail.html', context)

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