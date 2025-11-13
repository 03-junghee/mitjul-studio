document.addEventListener('DOMContentLoaded', function() {
    const clickableImages = document.querySelectorAll('.clickable-image');
    const lightbox = document.getElementById('lightbox');
    const lightboxImage = document.querySelector('.lightbox-image');
    const lightboxCaption = document.querySelector('.lightbox-caption');
    const closeBtn = document.querySelector('.close-btn');

    clickableImages.forEach(image => {
        image.addEventListener('click', function() {
            lightbox.style.display = 'flex'; // 모달을 보이게 함
            lightboxImage.src = this.getAttribute('data-fullsize-src'); // 전체 샷 이미지 설정
            lightboxCaption.textContent = this.getAttribute('data-product-name'); // 캡션 설정
            document.body.style.overflow = 'hidden'; // 스크롤 방지
        });
    });

    // 닫기 버튼 클릭 시 모달 닫기
    closeBtn.addEventListener('click', function() {
        lightbox.style.display = 'none';
        document.body.style.overflow = 'auto'; // 스크롤 허용
    });

    // 모달 외부 클릭 시 모달 닫기
    lightbox.addEventListener('click', function(event) {
        if (event.target === lightbox) { // 라이트박스 배경 클릭 시
            lightbox.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });
});