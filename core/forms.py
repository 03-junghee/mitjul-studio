from django import forms

# 1. 다음 밑줄 제안 폼 (Next Mitjul Suggestion Form)
class SuggestionForm(forms.Form):
    # '888.png' 이미지를 참고하여 필드를 구성합니다.
    name = forms.CharField(label='이름 / 닉네임 *', max_length=100)
    email = forms.EmailField(label='연락 가능한 이메일 *')
    
    quote_text = forms.CharField(
        label='밑줄 문장 (가장 중요한 한 줄) *',
        widget=forms.Textarea(attrs={'rows': 4}), # 텍스트 영역을 넓게 설정
        help_text='예: "우리의 영광이 운명을 경멸한다." (마르셀 프루스트)'
    )
    source = forms.CharField(
        label='출처 (책 이름, 저자, 페이지 등) *',
        max_length=255
    )
    idea = forms.CharField(
        label='굿즈 아이디어 (어떤 제품으로 만들까요?)',
        required=False, # 필수가 아님
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='예: "천연 가죽 커버 노트" 등 자유롭게 제안해주세요.'
    )


# 2. 일반 문의 및 제휴 폼 (General Contact Form)
class ContactForm(forms.Form):
    # '999.png' 이미지를 참고하여 필드를 구성합니다.
    name = forms.CharField(label='이름 *', max_length=100)
    email = forms.EmailField(label='이메일 *')
    subject = forms.CharField(label='제목 *', max_length=255)
    message = forms.CharField(
        label='문의 내용 *',
        widget=forms.Textarea(attrs={'rows': 6})
    )