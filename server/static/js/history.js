        // =========================== 스크롤 이벤트 부분 ===========================
        // 스크롤 옵저버 객체 생성
        const io = new IntersectionObserver(sections => {
            // 각 섹션을 옵저버 객체가 주시하다가 
            sections.forEach(s => {
                // 해당 섹션의 위치로 화면이 이동했음을 감지하면 섹션이 보이도록 설정
                if (s.intersectionRatio > 0) {
                    s.target.classList.add('section-active');
                }
                // 해당 섹션의 위치에서 화면이 벗어나면 섹션이 안 보이도록 설정
                else {
                    s.target.classList.remove('section-active');
                }
            })
        })

        // 모든 섹션에 대하여 옵저버 객체가 주시하도록 설정
        const sectionList = document.querySelectorAll('.category-content > div');
        sectionList.forEach((s) => {
            io.observe(s);
        })

        // =========================== 카테고리 출력 이벤트 부분 ===========================
        document.addEventListener('DOMContentLoaded', function () {
            const buttons = document.querySelectorAll('#button-wrapper .button');
            const categories = document.querySelectorAll('#body-wrapper > div');

            // 페이지 첫 로드 시 첫 번째 카테고리만 표시
            categories.forEach((cat, index) => {
                if (index === 0) {
                    cat.style.display = 'block';
                    buttons[index].classList.add('button-active');
                } else {
                    cat.style.display = 'none';
                }
            });
            
            // 각 버튼 별로 이벤트 리스너 적용
            buttons.forEach(button => {
                button.addEventListener('click', function () {
                    // 버튼에 해당하는 카테고리 번호('category(n)') 불러옴
                    const targetId = this.getAttribute('data-category');
                    
                    // 각 카테고리 중에서 현재 카테고리 번호('category(n)')와 일치하는 카테고리는 화면에 출력, 
                    // 일치하지 않는 카테고리 번호는 화면에 출력되지 않도록 설정
                    categories.forEach(category => {
                        category.style.display = (category.id === targetId) ? 'block' : 'none';
                    });

                    // 모든 버튼에서 .button-active 클래스(그라데이션 강조 효과)를 제거
                    buttons.forEach(btn => btn.classList.remove('button-active'));
                    // 클릭한 버튼에는 .button-active 클래스(그라데이션 강조 효과)를 적용
                    this.classList.add('button-active');
                });
            });
        });

        // =========================== 페이지 상단 이동 이벤트 부분 ===========================

        // 페이지 상단으로 부드럽게 이동하는 함수
        const scrollTop = () => {
            window.scrollTo({top: 0, left:0, behavior: 'smooth'});
        }

        // 화면 우하단 fixed 버튼과 페이지 하단 버튼에 이벤트리스너로 페이지 이동 함수 적용
        const topBtn = document.getElementById("top-button");
        const endTopBtn = document.getElementById("end-top-button")
        topBtn.addEventListener("click", scrollTop);
        endTopBtn.addEventListener("click", scrollTop);