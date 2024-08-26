import pyautogui as pyauto
import time
import scripts.listener as listener 

def definir_regiao_atuacao(bloco):
    
    pyauto.alert(text=f'Clique na posição inicial do botão do {bloco} e aperte ENTER', title='', button='OK')
    while True:
        teste = listener.leitor_de_enter()
        if teste:
            x_start, y_start = pyauto.position()
            print(x_start,  y_start)
            break   
    
    pyauto.alert(text=f'Clique na posição final do botão do {bloco} e aperte ENTER', title='', button='OK')
    while True:
        teste2 = listener.leitor_de_enter()
        if teste2:
            x_end, y_end = pyauto.position()
            print(x_end,  y_end)
            break   
    
    return (x_start, y_start, x_end - x_start, y_end - y_start)
        
def encontrar_elemento(imagem, posicao):        
    while True:
        try:
            print("Tentando encontrar a imagem...")
            time.sleep(1)
            elemento = pyauto.locateCenterOnScreen(image=f"image_confidence/{imagem}", grayscale=True, confidence=0.5, region=posicao)
            if elemento:
                break
        except:
            pass
    pyauto.center(elemento, 2)
    pyauto.click()
    
def main():
    posicao_vortex = definir_regiao_atuacao("Vortex")
    posicao_nexus = definir_regiao_atuacao("Nexus")
    while True:
        encontrar_elemento("download_vortex.png", posicao_vortex)
        encontrar_elemento("slow_download.png", posicao_nexus)