// static/scripts.js

// 페이지 로딩 후 실행될 함수
document.addEventListener('DOMContentLoaded', function () {
    // 필터 적용 버튼 클릭 이벤트
    document.getElementById('apply_filters').addEventListener('click', function () {
        // 선택한 카테고리 값을 가져옴
        const selectedCategory = document.getElementById('filter_category').value;

        // 모든 이미지 게시물 요소를 가져옴
        const imageElements = document.getElementsByClassName('image-item');

        // 각 이미지 게시물 요소를 반복하며 필터링 적용
        for (const element of imageElements) {
            // data-category 속성에 저장된 카테고리 값을 가져옴
            const itemCategory = element.getAttribute('data-category');

            // 선택한 카테고리가 '전체'이거나 선택한 카테고리와 이미지 게시물의 카테고리가 일치하면 보여줌
            if (selectedCategory === '' || selectedCategory === itemCategory) {
                element.style.display = 'block'; // 보이기
            } else {
                element.style.display = 'none';  // 숨기기
            }



        }
    });
});