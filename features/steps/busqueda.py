from behave import given, then, when
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

paginas = {
    'Principal':'https://www.google.com'
}

@given('Un usuario que se encuentra en la pagina {pagina}')
def step_impl(context,pagina):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(paginas[pagina])


@given(u'Un usuario no registrado')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//span[contains(text(),'Iniciar sesión')]")

@when(u'Realiza la busqueda de {texto}')
def step_impl(context,texto):
    barra_busqueda = context.driver.find_element(By.XPATH,'//textarea[@id="APjFqb"]')
    barra_busqueda.send_keys(texto)
    barra_busqueda.send_keys(Keys.RETURN)
    sleep(2)


@then(u'Encuentra resultados que contengan {texto}')
def step_impl(context,texto):

    html = context.driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    h3_tags = soup.find_all('h3', text=lambda text: text and texto in text)

    assert h3_tags != []

