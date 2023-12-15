# imports do Python
#import pytest
#import time
#import json
from time import sleep

# imports do Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCadastroAutor():
  
  def setup_method(self, method):
    global driver, vars 
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    vars = {}
      
  def teardown_method(self, method):
    driver.quit()
      
  def teste_CadastroAutor_sucesso(self):
    driver.get("http://localhost:8000/")
    driver.set_window_size(1395, 795)
    sleep(2)
    #driver.maximize_window()
    # primeiro acesso para entrar na app
    driver.find_element(By.NAME, "username").click()
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("@dm1n") 
    driver.find_element(By.CSS_SELECTOR, "button").click()    
    sleep(1)
    # selecionar o menu Autor
    driver.find_element(By.XPATH, "/html/body/div[3]/ul/li[4]/a").click()
    sleep(1)
    # clicar em adicionar autor
    driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()
    sleep(2)
    # preencher os campos
    driver.find_element(By.ID, "id_nome").send_keys("José de Oliveira")
    driver.find_element(By.ID, "id_nascimento").click()
    driver.find_element(By.ID, "id_nascimento").send_keys("07/02/1958")
    driver.find_element(By.ID, "id_biografia").click()
    driver.find_element(By.ID, "id_biografia").send_keys("Começou na dramaturgia no Teatro da Universidade Católica (TUCA), em São Paulo, com a peça Morte e Vida Severina, de João Cabral de Melo Neto e Chico Buarque, em 1967. Ao mesmo tempo, cursava Direito na Pontifícia Universidade Católica de São Paulo (PUC-SP). Um ano depois ele estava nos palcos e nas telas de cinema como profissional. Mas sua carreira teve que ser bruscamente interrompida por causa de sua militância política. Abreu foi preso em congresso da União Nacional dos Estudantes (UNE), pertenceu à Ação Popular e deu \"apoio logístico\" à VAR-Palmares (Vanguarda Armada Revolucionária), um grupo de esquerda que combatia com ações armadas o regime militar. Na mesma época, também participou do movimento hippie.")
    # clicar em salvar
    driver.find_element(By.NAME, "_save").click()  
    sleep(2)
    # verificando se o autor foi cadastrado com sucesso
    assert driver.find_element(By.CSS_SELECTOR, ".success").is_displayed() == True
    #assert driver.find_element(By.CSS_SELECTOR, ".success").text == "Autor adicionado com sucesso."
   