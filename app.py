from selenium.webdriver.support.ui import Select
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
username_field.send_keys("xxxxxxx")  # suap aqui

# 3 - Localizar e preencher o campo de senha
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys("xxxxxxx")  # senha aqui

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

# 8 -  Clicar em "Marcar Tudo" no campo "Campus"
# Localizar e clicar no campo popup (abrir opções)
popup_campus = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "__uo__"))
)
popup_campus.click()

# Localizar e clicar no checkbox "Marcar Tudo"
checkbox_marcar_tudo = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//input[@type="checkbox" and @value="0"]'))
)
checkbox_marcar_tudo.click()
print("Marquei todos os campos em 'Campus'.")

# 9 - Selecionar o ano "2024" em "Ano Letivo"
# Localizar o dropdown de Ano Letivo
dropdown_ano_letivo = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "id_ano_letivo"))
)

# Selecionar o valor correspondente a 2024 (value="58")
select = Select(dropdown_ano_letivo)
select.select_by_value("58")
print("Ano Letivo '2024' selecionado.")

# 10 - Clicar no botão "Pesquisar"
# Localizar e clicar no botão "Pesquisar"
botao_pesquisar = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//input[@type="submit" and @value="Pesquisar"]'))
)
botao_pesquisar.click()
print("Cliquei no botão 'Pesquisar'.")

# Manter o navegador aberto
print("Navegador aberto. Pressione Ctrl+C para encerrar manualmente.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando o script...")
    driver.quit()
