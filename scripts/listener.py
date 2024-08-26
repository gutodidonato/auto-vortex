import pynput as pt



def leitor_de_enter():
    valor = False
    
    def on_press(key):
        global valor
        if key == pt.keyboard.Key.enter:
            valor = True
            listener.stop()
            
    with pt.keyboard.Listener(on_press=on_press, on_release=None) as listener:
        listener.join()
    return True
    
    
    