from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.get("https://sguweb.unimedflorianopolis.com.br/sgu-web/index.php")
time.sleep(10)

usuario = browser.find_element(By.NAME,"login")
usuario = browser.find_element(By.NAME,"senha")

usuario.send_keys("Usuario")
usuario.send_keys("Senha")

login_attemp = browser.find_element(By.XPATH,"ui-button-text")
login_attemp.submit()










