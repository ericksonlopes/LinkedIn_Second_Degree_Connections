from time import sleep

import chromedriver_autoinstaller
from selenium import webdriver


def login(email, password, driverweb):
    # abre a página do linkedin
    driverweb.get('https://www.linkedin.com')

    xpath_email = '//*[@id="session_key"]'
    xpath_password = '//*[@id="session_password"]'

    # Procura o xpath do campo email, clica, e digita o email
    field_email = driverweb.find_element_by_xpath(xpath_email)
    field_email.click()
    field_email.send_keys(email)
    sleep(0.30)

    # Procura o xpath do campo password, clica, e digita o password
    field_passwod = driverweb.find_element_by_xpath(xpath_password)
    field_passwod.click()
    field_passwod.send_keys(password)

    xpath_btn = '/html/body/main/section[1]/div[2]/form/button'
    # clica no botão para entrar
    driverweb.find_element_by_xpath(xpath_btn).click()


if __name__ == '__main__':
    # instala o driver do Chrome
    chromedriver_autoinstaller.install()

    # instancia o obj do webdriver chrome
    driver = webdriver.Chrome()
    login(email='ofc.erickson@gmail.com', password='123', driverweb=driver)

    # fecha o chrome
    driver.close()
