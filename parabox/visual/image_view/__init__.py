import os.path

from kivy.lang import Builder

from parabox.visual.image_view.image_view import ImageView

dirrectory_path = os.path.dirname(os.path.realpath(__file__))

Builder.load_file(os.path.join(dirrectory_path, 'image_view.kv'))
