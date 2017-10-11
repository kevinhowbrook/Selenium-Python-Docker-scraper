from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




class ShopPurchase:
    def __init__(self):
        display = Display(visible=0, size=(1400, 2800))
        display.start()
        # now Firefox will run in a virtual display.
        # you will not see the browser.
        browser = webdriver.Firefox()
     #   browser.implicitly_wait(10) # seconds
        browser.get('http://donkeysanctuary.dev/')
        print(browser.title)
        browser.save_screenshot('/code/screenshots/front.png')
        browser.get('http://donkeysanctuary.dev/shop/designer/donkey-mug')
        browser.save_screenshot('/code/screenshots/product.png')
        browser.find_element_by_css_selector(".product-form__button").click()
        browser.save_screenshot('/code/screenshots/product_added.png')
        browser.get('http://donkeysanctuary.dev/cart/oneOffBasket')
        browser.save_screenshot('/code/screenshots/cart.png')
        element = browser.find_element_by_css_selector(".basket__action-btn")
        browser.execute_script("arguments[0].scrollIntoView();", element)
        browser.save_screenshot('/code/screenshots/checkoutclick.png')
        browser.find_element_by_css_selector(".basket__action-btn").click()
        browser.save_screenshot('/code/screenshots/order1.png')

        # Fill in the order
        browser.find_element_by_css_selector("select#edit-custom-contact-information-title > option[value='Mr']").click()

        inputElement = browser.find_element_by_id("edit-custom-contact-information-first-name")
        inputElement.send_keys('Kevin')
        inputElement = browser.find_element_by_id("edit-custom-contact-information-last-name")
        inputElement.send_keys('Howbrook')

        browser.save_screenshot('/code/screenshots/order2.png')



        browser.quit()
        display.stop()