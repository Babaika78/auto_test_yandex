from Base_app import BasePage
from selenium.webdriver.common.by import By

class YandexSearchLocators:
    LOCATOR_YANDEX_BUTTON_MENU = (By.CSS_SELECTOR,'li[class*="services-suggest__list-item-more"]')
    LOCATOR_YANDEX_IMG_BUTTON_MENU = (By.CSS_SELECTOR,'a[aria-label*="Картинки"]')
    LOCATOR_YANDEX_ING_POPULAR = (By.CSS_SELECTOR,'div[class*="PopularRequestList-Item_pos_0"]')
    LOCATOR_YANDEX_SEARCH_LINE = (By.CSS_SELECTOR,'input[class*="mini-suggest__input"]')
    LOCATOR_YANDEX_IMG_ONE = (By.CSS_SELECTOR, 'div[class*="serp-item_pos_0"]')
    LOCATOR_YANDEX_IMG_INFO = (By.CSS_SELECTOR, 'img[class*="MMImage-Origin"]')
    LOCATOR_YANDEX_BUTTON_NEXT = (By.CSS_SELECTOR,'div[class*="CircleButton_type_next"]')
    LOCATOR_YANDEX_BUTTON_BACK = (By.CSS_SELECTOR,'div[class*="CircleButton_type_prev"]')

class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINE,time=2)
        search_field.send_keys(word)
        return search_field
    
    def menu_service(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_MENU,time=2)

    def click_on_the_menu_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_MENU,time=2).click()
    
    def click_on_the_img_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMG_BUTTON_MENU,time=2).click()
    
    def click_on_the_img_popular(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_ING_POPULAR,time=2).click()
    
    def check_the_img_popular(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_ING_POPULAR,time=2).text
    
    def check_search_line_text(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_LINE,time=2).get_attribute('value')
    
    def click_on_the_img_one(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMG_ONE,time=2).click()
    
    def check_img_one(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMG_ONE,time=2)
    
    def check_img_info(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMG_INFO,time=2).get_attribute('src')
    
    def click_on_the_button_next(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_NEXT,time=2).click()
    
    def click_on_the_button_back(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_BUTTON_BACK,time=2).click()
        

    

        
 