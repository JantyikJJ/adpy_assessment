import dearpygui.dearpygui as dpg
from utils import Fps
from utils import Settings


settings = Settings()
settings.load()

dpg.create_context()
dpg.create_viewport(title='Jumpy Junkie',
                    width=settings.width,
                    height=settings.height,
                    x_pos=settings.x,
                    y_pos=settings.y)
dpg.setup_dearpygui()

with dpg.window(label="Example Window"):

    dpg.add_text("Hello, world")

dpg.show_viewport()


fps = Fps(lambda value: print(value))

while dpg.is_dearpygui_running():
    fps.update()
    dpg.render_dearpygui_frame()

dpg.destroy_context()
