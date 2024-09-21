// Находим тег html и сохраняем его
let html = document.documentElement;
//сохраним текущую прокрутку:
let scrollPosition;


document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.add-fav').forEach(function (button) {
        button.addEventListener('click', function () {
            const companyId = button.getAttribute('data-company-id');
            addToFavorites(companyId);
        });
    });

    function addToFavorites(companyId) {
        fetch(`add_to_favorites/${companyId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
            },
        })
        .then(response => {
            if (response.ok) {
                if(response.redirected){
                    addBlockingScroll();
                }
                else {
                    changeDisplayButton(companyId);
                }
            }
            else{
                addBlockingScroll();
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    document.querySelectorAll('.remove-fav').forEach(function (button) {
        button.addEventListener('click', function () {
            const companyId = button.getAttribute('data-company-id');
            removeFromFavorites(companyId);
        });
    });

    function removeFromFavorites(companyId) {
        // Отправить запрос на сервер для удаления компании из избранного
        fetch(`/accounts/remove_from_favorites/${companyId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // добавьте токен CSRF
            },
            body: JSON.stringify({
                company_id: companyId,
            })
        })
        .then(response => {
            if (response.ok) {
                add_container = document.getElementById('add-to-favorites-container-' + companyId);
                if (add_container === null){
                    company_card = document.getElementById('company-' + companyId);
                    company_card.classList.toggle("hidden");
                    company_card.classList.toggle("companies-item");
                }
                else{
                    changeDisplayButton(companyId);
                }
            }
        })
        .catch(error => console.error('Ошибка:', error));
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    function changeDisplayButton(companyId){
        add_container = document.getElementById('add-to-favorites-container-' + companyId)
        remove_container = document.getElementById('remove-to-favorites-container-' + companyId);

        remove_container.classList.toggle("hidden");
        add_container.classList.toggle("hidden");
    }
});


// Закрытие модального окна при клике на "крестик"
document.querySelectorAll('.register_modal__close-button').forEach(function (button) {
    button.addEventListener('click', function () {
        putAwayBlockingScroll();
    });
});


// Закрытие модального окна при клике вне его
window.addEventListener("click", function(event) {
    if (event.target == document.getElementById("register_modal")) {
        putAwayBlockingScroll();
    }
});


function putAwayBlockingScroll(){
    document.getElementById("register_modal").style.display = "none";
    html.classList.remove("register_modal__opened");
    //прокручиваем окно туда где оно было
    window.scrollTo(0, scrollPosition);
    html.style.top = "";
    //при закрытии окна без прыжка скроллбар
    html.style.marginRight = "";
}


function addBlockingScroll(){
    let marginSize = window.innerWidth - html.clientWidth;
    //ширина скроллбара равна разнице ширины окна и ширины документа (селектора html)
    if (marginSize) {
        html.style.marginRight = marginSize + "px";
    }
    document.getElementById("register_modal").style.display = "flex";
    //сохраним текущую прокрутку:
    scrollPosition = window.pageYOffset
    //установим свойство top у html равное прокрутке
    html.style.top = -scrollPosition + "px";
    html.classList.add("register_modal__opened");
    //при открытии окна без прыжка скроллбар

}



