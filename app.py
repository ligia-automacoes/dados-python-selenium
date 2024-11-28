from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Configurar o ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1 - Entrar no site
driver.get('https://suap.ifsuldeminas.edu.br/')

# 2 - Localizar e preencher o campo de usuário
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys("XXXXX")  # suap aqui

# 3 - Localizar e preencher o campo de senha
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys("XXXXXX")  # senha aqui

# 4 - Clicar no botão "Acessar"
login_button = driver.find_element(
    By.CSS_SELECTOR, 'input[type="submit"][value="Acessar"]')
login_button.click()

# Aguardar alguns segundos para carregamento da página
time.sleep(10)

# 5 - Navegar no menu "Ensino"
menu_ensino = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, '//li[contains(@class, "menu-ensino")]/a[@title="Ensino"]'))
)
ActionChains(driver).move_to_element(menu_ensino).click().perform()

# 6 - Aguardar visibilidade do submenu "Relatórios" e clicar
try:
    submenu_relatorios = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@title="Relatórios"]'))
    )
    submenu_relatorios.click()
    print("Cliquei em Relatórios com sucesso!")
except Exception as e:
    print(f"Erro ao tentar clicar em Relatórios: {e}")

# 7 - Clicar em "Listagem de Alunos"
try:
    submenu_listagemAlunos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[@title="Listagem de Alunos"]'))
    )
    submenu_listagemAlunos.click()
    print("Cliquei em Listagem de Alunos com sucesso!")
except Exception as e:
    print(f"Erro ao tentar clicar em Relatórios: {e}")

# Manter o navegador aberto
print("Navegador aberto. Pressione Ctrl+C para encerrar manualmente.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o script...")
    driver.quit()
