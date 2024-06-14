import os
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'presiono el boton  Subir documento')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[3]/a[1]").click()
    time.sleep(2)


@given(u'escribo el nombre del archivo "{nombre}"')
def step_impl(context,nombre):
    context.driver.find_element(By.NAME,"nombre").send_keys(nombre)
    time.sleep(2)


@given(u'selecciono el archivo "{archivo}"')
def step_impl(context, archivo):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    nombre_doc = "test.txt"
    ruta_doc = os.path.join(BASE_DIR, 'doc_test', 'docs', nombre_doc)
    context.driver.find_element(By.NAME,"archivo").send_keys(ruta_doc)
    time.sleep(2)


@when(u'presiono el boton Subir')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div/div/div/form/button").click()
    time.sleep(2)


@then(u'puedo ver el mensaje de exito "{mensaje}"')
def step_impl(context,mensaje):
    div = context.driver.find_element(By.XPATH,"/html/body/div/div/div/h1")
    time.sleep(2)
    assert mensaje in div.text, f'el candidato {mensaje} no esta en {div.text}'