import dearpygui.dearpygui as dpg
from utils.fps import Fps
from utils.settings import Settings


class Game:
    def __init__(self):
        self.settings = Settings()
        self.settings.load()

        dpg.create_context()
        dpg.create_viewport(title='Fly Junkie',
                            width=self.settings.width,
                            height=self.settings.height,
                            x_pos=int(self.settings.__x__),
                            y_pos=int(self.settings.__y__))
        dpg.setup_dearpygui()

        self.fps = Fps(lambda value: print(value))

    def show(self):
        dpg.show_viewport()
        while dpg.is_dearpygui_running():
            self.fps.update()
            dpg.render_dearpygui_frame()
        dpg.destroy_context()
