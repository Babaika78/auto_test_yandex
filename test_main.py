from YandexPages import SearchHelper

def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    
    yandex_main_page.enter_word("Тензор")

    menu = yandex_main_page.menu_service()
    assert menu.is_enabled() == True
    
    yandex_main_page.click_on_the_menu_button()
    yandex_main_page.click_on_the_img_button()

    url = yandex_main_page.get_url()
    assert url == 'https://ya.ru/images/'

    img_popular_text = yandex_main_page.check_the_img_popular()
    yandex_main_page.click_on_the_img_popular()
    search = yandex_main_page.check_search_line_text()
    assert img_popular_text in search

    yandex_main_page.click_on_the_img_one()

    img_one = yandex_main_page.check_img_one()
    img_one_info = yandex_main_page.check_img_info()
    assert img_one.is_enabled() == True

    yandex_main_page.click_on_the_button_next()

    img_two_info = yandex_main_page.check_img_info()
    assert img_one_info != img_two_info

    yandex_main_page.click_on_the_button_back()

    img_one_info_2 = yandex_main_page.check_img_info()
    assert img_one_info == img_one_info_2





    
