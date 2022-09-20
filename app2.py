
import pyautogui as pg # Biblioteca para automação, preciso instalar ela uma única vez com o comando "pip install pyautogui" no terminal
import time # Biblioteca para tempo, ela já vem no python nativamente

print(pg.KEYBOARD_KEYS) # Comando pra listar as teclas que você pode usar para sua automação quando for pressionar alguma tecla

contatos=['vinicius programador','estudos eduardo'] 


# Abrir o chrome
pg.alert('Não mexa em nada antes que o código se acabe!') # Alert trás uma caixa de diálogo antes de começar o código

pg.press('winleft') # Comando "press" serve para pressionar algum tecla, no caso eu quero apertar a tecla esquerda do windows no meu teclado. E sempre passamos a tecla em aspas.

time.sleep(1) # Com o time usamos "sleep" pra dizer pro código dar uma "dormida" antes de executar o resto, no caso eu coloquei (1 segundo)

pg.write('chrome') # Comando "write" serve para escrever alguma coisa, sempre passado em aspas. Também é possível passar uma variável

time.sleep(1)
pg.press('enter') # Pressionando ENTER

time.sleep(1)

# Entrar no gmail
pg.write('youtube.com.br')

time.sleep(5)

pg.press('enter')
time.sleep(10)


pg.press('f3')
time.sleep(2)
pg.write('visualizacoes')
time.sleep(2)
pg.hotkey('ctrl','enter')
pg.press('tab')
pg.press('enter')
time.sleep(2)

pg.press(['down','down','down'])
pg.press('enter')
time.sleep(1)
pg.hotkey('shift','tab')
pg.hotkey('shift','tab')
pg.hotkey('shift','tab')
pg.press('enter')
time.sleep(1)
pg.hotkey('ctrl','l')
pg.write('https://web.whatsapp.com/')
pg.press('enter')
time.sleep(10)



for item in contatos:
    pg.hotkey('ctrl','alt','n')
    time.sleep(1)
    pg.write(item)
    time.sleep(2)
    pg.press('enter')
    time.sleep(2)
    pg.hotkey('ctrl','v')
    time.sleep(2)
    pg.press('enter')
    time.sleep(3)
pg.hotkey('ctrl','w')

