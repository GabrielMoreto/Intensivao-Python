from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

navegador = webdriver.Chrome()


# Passo 1: Pegar a cotação do dólar

# Entrar no google

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_dolar)

# Pegar a cotação do euro

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_euro = navegador.find_element('xpath', '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(cotacao_euro)

# Pegar a cotação do ouro

navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element('xpath', '/html/body/div[5]/div[1]/div/div/input[2]').get_attribute('value')
cotacao_ouro = cotacao_ouro.replace(',', '.')

print(cotacao_ouro)

# Passo 4: Importar a base de dados e Atualizar a base

tabela = pd.read_excel(r"C:\Users\gabri\OneDrive\Área de Trabalho\Intensivão de Python\Produtos.xlsx")

print(tabela)