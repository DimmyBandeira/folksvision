'''
Camera Example
==============

Este exemplo demonstra um uso simples da câmera. Ele mostra uma janela 
com um botão rotulado 'play' para ligar e desligar a câmera. Observe que não encontrar uma câmera, 
talvez porque o gstreamer não esteja instalado, lançará uma exceção durante o processamento da linguagem kv.

'''

# Descomente estas linhas para ver todas as mensagens
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (1280, 720)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Função para capturar as imagens e dar-lhes os nomes de acordo com a hora e data de captura.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()