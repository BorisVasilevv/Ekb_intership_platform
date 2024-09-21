// logic method
document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('.subcategory-button');
    var companies = document.querySelectorAll('.companies-item');

    buttons.forEach(function (button) {
        button.addEventListener('click', function () {

            if(button.classList.contains('active')){
                button.classList.remove('active');
            }
            else {
                button.classList.add('active');
            }
            var selectedSubcategories = [];
            buttons.forEach(function(btn) {
                if (btn.classList.contains('active')) {
                    var selectedCategory = btn.getAttribute('data-category');
                    selectedSubcategories.push(selectedCategory)
                }
            });

            if (selectedSubcategories.length === 0) {
                companies.forEach(function (company) {
                    company.style.display = 'flex';
                });
            }
            else {
                // Перебираем компании и скрываем те, которые не соответствуют выбранной подкатегории
                companies.forEach(function (company) {
                    var companyCategory = company.getAttribute('data-category');
                    companyCategoryList = [];
                    if (companyCategory.includes(',')){
                        var regex = /<Subcategory:\s(.*?)>/g;
                        var subctgr;
                        while((subctgr = regex.exec(companyCategory)) !== null) {
                            subctgr[1].trim()
                            companyCategoryList.push(subctgr[1]);
                        }
                    }
                    else {
                        companyCategory = companyCategory.substring(companyCategory.indexOf(':')+1, companyCategory.indexOf('>')).trim();
                        companyCategoryList.push(companyCategory);
                    }

                    try {
                        companyCategoryList.forEach(function(companyctgr) {
                            if (selectedSubcategories.includes(companyctgr)) {
                                company.style.display = 'flex'; // Показываем компанию
                                throw 'StopIteration'; // Кидаем исключение, чтобы выйти из цикла и случайно не скрыть компанию, которая состоит в двух категориях
                            } else {
                                company.style.display = 'none'; // Скрываем компанию
                            }
                        });
                    } catch (e) {
                        if (e !== 'StopIteration') {
                            throw e;
                        }
                    }
                });
            }
        });
    });
});

// view change method
document.addEventListener('DOMContentLoaded', function () {
    var buttons = document.querySelectorAll('.subcategory-button');

    buttons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Toggle background color and border color
            var currentColor = button.style.backgroundColor;
            var newColor = button.style.borderColor;

            button.style.backgroundColor = newColor;
            button.style.borderColor = currentColor;
        });
    });
});