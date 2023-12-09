# imports do Python
#import pytest
#import time
#import json

# imports do Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPesquisaGoogleflamengo():
  
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
      
  def teardown_method(self, method):
      self.driver.quit()
      
  def test_pesquisaGoogleflamengo(self):
      self.driver.get("http://localhost:8000/")
      self.driver.set_window_size(1395, 795)
      element = self.driver.find_element(By.LINK_TEXT, "Autor")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).click_and_hold().perform()
      actions.move_to_element(element).perform()
      element = self.driver.find_element(By.LINK_TEXT, "Autor")
      actions = ActionChains(self.driver)
      actions.move_to_element(element).release().perform()
      self.driver.find_element(By.LINK_TEXT, "Autor").click()
      self.driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()
      self.driver.find_element(By.ID, "id_nome").send_keys("José de Abreu")
      self.driver.find_element(By.ID, "id_nascimento").click()
      self.driver.find_element(By.ID, "id_nascimento").send_keys("07/02/1958")
      self.driver.find_element(By.ID, "id_biografia").click()
      self.driver.find_element(By.ID, "id_biografia").send_keys("Começou na dramaturgia no Teatro da Universidade Católica (TUCA), em São Paulo, com a peça Morte e Vida Severina, de João Cabral de Melo Neto e Chico Buarque, em 1967. Ao mesmo tempo, cursava Direito na Pontifícia Universidade Católica de São Paulo (PUC-SP). Um ano depois ele estava nos palcos e nas telas de cinema como profissional. Mas sua carreira teve que ser bruscamente interrompida por causa de sua militância política. Abreu foi preso em congresso da União Nacional dos Estudantes (UNE), pertenceu à Ação Popular e deu \"apoio logístico\" à VAR-Palmares (Vanguarda Armada Revolucionária), um grupo de esquerda que combatia com ações armadas o regime militar. Na mesma época, também participou do movimento hippie.")
      self.driver.find_element(By.NAME, "_save").click()
    
      