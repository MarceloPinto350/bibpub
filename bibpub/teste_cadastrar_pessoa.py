import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class CadastroPessoaPage:
    def __init__(self, driver):
        self.driver = driver

    def preencher_informacoes(self, nome, nascimento, cpf, email, cep, endereco, cidade, uf):
        self.driver.find_element(By.ID, "id_nome").send_keys(nome)
        self.driver.find_element(By.ID, "id_nascimento").send_keys(nascimento)
        self.driver.find_element(By.ID, "id_cpf").send_keys(cpf)
        self.driver.find_element(By.ID, "id_email").send_keys(email)
        self.driver.find_element(By.ID, "id_cep").send_keys(cep)
        self.driver.find_element(By.ID, "id_endereco").send_keys(endereco)
        self.driver.find_element(By.ID, "id_cidade").send_keys(cidade)

        uf_dropdown = self.driver.find_element(By.ID, "id_uf")
        uf_dropdown.find_element(By.XPATH, f"//option[. = '{uf}']").click()

    def clicar_cadastrar(self):
        cadastrar_button = self.driver.find_element(By.CSS_SELECTOR, "button")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button")))
        cadastrar_button.click()

    def verificar_sucesso(self):
        #print(self.driver.find_element(By.CSS_SELECTOR, ".success").text=='Cadastro realizado com sucesso. Aguarde a análise.')
        assert self.driver.find_element(By.CSS_SELECTOR, ".success").text=='Cadastro realizado com sucesso. Aguarde a análise.'


class TestCadastrarPessoa:
    def setup_method(self, method):
        chrome_path = '/Users/alikson/Downloads/chromedriver-mac-x64/chromedriver'
        service = ChromeService(executable_path=chrome_path)
        self.driver = webdriver.Chrome(service=service)
        self.cadastro_page = CadastroPessoaPage(self.driver)

    def teardown_method(self, method):
        self.driver.quit()

    def test_cadastrar_pessoa_sucesso(self):
        self.driver.get("http://localhost:8000/cadastrar_pessoa/")
        self.driver.set_window_size(1280, 696)

        self.cadastro_page.preencher_informacoes("Daniel", "20/01/1988", "983.392.331-09", "jose@gmail.com",
                                                 "59280-000", "rua teste 123", "Natal", "Rio Grande do Norte")

        self.cadastro_page.clicar_cadastrar()
        self.driver.implicitly_wait(1)

        self.cadastro_page.verificar_sucesso()

if __name__ == "__main__":
    pytest.main()
