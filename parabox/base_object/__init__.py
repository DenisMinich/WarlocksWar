import os.path

from kivy.lang import Builder

from parabox.base_object.base_object import BaseObject


current_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)))
Builder.load_file(current_directory, 'base_object.kv')
