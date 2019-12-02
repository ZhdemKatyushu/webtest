from selenium import webdriver
import time
import math

def calc(x):return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

xx = browser.find_element_by_id("treasure")
x = xx.get_attribute("valuex")
y = calc(x)

try:

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    time.sleep(1)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    time.sleep(1)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()