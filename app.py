from time import sleep
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from urls import dicas_python


def login(email, password, driverweb):
    # abre a página do linkedin
    driverweb.get('https://www.linkedin.com')

    xpath_email = '//*[@id="session_key"]'
    xpath_password = '//*[@id="session_password"]'

    # Procura o xpath do campo email, clica, e digita o email
    field_email = driverweb.find_element_by_xpath(xpath_email)
    field_email.click()
    field_email.send_keys(email)

    # Procura o xpath do campo password, clica, e digita o password
    field_passwod = driverweb.find_element_by_xpath(xpath_password)
    field_passwod.click()
    field_passwod.send_keys(password)

    xpath_btn = '/html/body/main/section[1]/div[2]/form/button'
    # clica no botão para entrar
    driverweb.find_element_by_xpath(xpath_btn).click()

    sleep(1)


if __name__ == '__main__':
    # instala o driver do Chrome
    chromedriver_autoinstaller.install()

    # instancia o obj do webdriver chrome
    driver = webdriver.Chrome()

    # Fazer login
    login(email='ofc.erickson@gmail.com', password='123', driverweb=driver)

    driver.get('https://www.linkedin.com/posts/ericksonlopesdev_dicapython-python-dica-activity-6773560821525082112-uQpq')

    sleep(1)
    reactions = driver.find_element_by_xpath('//*[@id="ember71"]/ul/li[1]/button')

    # printa quantidade de reações
    print(reactions.text)
    reactions.click()
    sleep(0.30)

    all_reaction = driver.find_element_by_id('ember545')

    for item in all_reaction.find_elements_by_class_name('mr1'):
        print(item)

    # print(all_reaction)

    # for url in dicas_python:
    #     print(url)

    input()
    # fecha o chrome
    driver.close()
