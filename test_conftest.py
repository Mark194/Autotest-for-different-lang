import time


# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link = "https://vk.com/im?peers=148923312_-22142529&sel=92808306"

def test_should_see_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_xpath("(//button[@type='submit'])[2]")
    assert button is not None, "Кнопка не найдена!"
