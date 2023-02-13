import os
import dearpygui.dearpygui as dpg


class AssetLoader:
    @staticmethod
    def load():
        asset_folder = "assets"
        with dpg.texture_registry():
            for file in os.listdir(asset_folder):
                if file.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                    f = os.path.join(asset_folder, file)
                    width, height, channels, data = dpg.load_image(f)
                    dpg.add_static_texture(width, height, data, tag=file.lower())
