from mongoengine import Document, fields

# 1. 다음 밑줄 제안 (Next Mitjul Suggestion) 모델
class Suggestion(Document):
    """
    고객이 제안하는 다음 밑줄 문장과 굿즈 아이디어를 저장하는 모델입니다.
    """
    # 필드 정의
    name = fields.StringField(required=True, max_length=100)
    email = fields.EmailField(required=True)
    
    # 핵심 제안 내용
    quote_text = fields.StringField(required=True) # 밑줄 문장 (가장 중요한 한 줄)
    source = fields.StringField(required=True, max_length=255) # 출처 (책 이름, 저자 등)
    idea = fields.StringField() # 굿즈 아이디어 (예: 가죽 커버 노트)
    
    # 메타 데이터
    submitted_at = fields.DateTimeField() # 제안 제출 시간
    
    meta = {
        'collection': 'suggestions', # MongoDB 컬렉션 이름 지정
        'ordering': ['-submitted_at'] # 최근 제출된 순서로 정렬
    }


# 2. 일반 문의 및 제휴 (General Contact/Partnership) 모델
class Contact(Document):
    """
    일반 문의 및 제휴 요청을 저장하는 모델입니다.
    """
    # 필드 정의
    name = fields.StringField(required=True, max_length=100)
    email = fields.EmailField(required=True)
    subject = fields.StringField(required=True, max_length=255) # 제목
    message = fields.StringField(required=True) # 문의 내용
    
    # 메타 데이터
    submitted_at = fields.DateTimeField() # 문의 제출 시간
    
    meta = {
        'collection': 'contacts', # MongoDB 컬렉션 이름 지정
        'ordering': ['-submitted_at']
    }