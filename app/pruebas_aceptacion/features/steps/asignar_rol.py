import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que ingreso al sistema "{url}"')
def step_impl(context, url):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    time.sleep(2)

@given(u'presiono la opcion para loguearme LOGIN')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/nav/div/div/form/a").click()
    time.sleep(2)

@given(u'escribo mi usuario "{usuario}" y mi contraseña "{contra}"')
def step_impl(context, usuario, contra):
    context.driver.find_element(By.NAME,"username").send_keys(usuario)
    context.driver.find_element(By.NAME,"password").send_keys(contra)
    time.sleep(2)


@given(u'presiono el boton Login')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div/div/div/form/button").click()
    time.sleep(2)

@given(u'selecciono la opción de Tutores')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/nav/div/ul/li[3]/a").click()
    time.sleep(2)


@given(u'selecciono la opcion editar del usuario')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/ul/li[2]/div/a[1]").click()
    time.sleep(2)


@given(u'selecciono tutor en tipo user')
def step_impl(context):
    context.driver.find_element(By.NAME, "tipo_user").send_keys("Tutor")
    time.sleep(2)

@given(u'selecciono Estudiante en tipo user')
def step_impl(context):
    context.driver.find_element(By.NAME, "tipo_user").send_keys("Estudiante")
    time.sleep(2)


@when(u'presiono el botón Registrarse')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div/div/div/div/div[2]/form/button").click()
    time.sleep(2)

@then(u'puedo ver la lista de Usuarios')
def step_impl(context):
    div =context.driver.find_element(By.XPATH, "/html/body/div/h2")
    time.sleep(2)
    assert "Lista de usuarios" in div.text, f'El texto no se encuentra en {div.text}'