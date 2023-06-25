# pyautogui.clicl=k -> clicar
# pyautogui.write -> escrever
# pyautogui.press -> pressionar
# pyautogui.hotkey -> atalho

import pyautogui
import pyperclip
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write('chrome')
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=462, y=350, clicks=2)

time.sleep(5)

pyautogui.click(x=462, y=350, clicks=1)

time.sleep(5)

pyautogui.click(x=1665, y=201, clicks=1)

time.sleep(5)

pyautogui.click(x=1391, y=663, clicks=1)

time.sleep(8)

tabela = pandas.read_excel(r"C:\Users\gabri\Downloads\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(faturamento)
print(quantidade)



