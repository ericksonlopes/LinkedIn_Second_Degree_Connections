import chromedriver_autoinstaller
from selenium import webdriver

# instala o driver do Chrome
chromedriver_autoinstaller.install()

# instancia o obj do webdriver chrome
driver = webdriver.Chrome()

# abre a página do linkedin
driver.get('https://www.linkedin.com')

input()
# fecha o chrome
driver.close()
