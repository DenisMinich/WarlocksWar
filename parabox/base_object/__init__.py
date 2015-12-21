import os.path

from kivy.lang import Builder

from parabox.base_object.base_object import BaseObject


current_directory = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(os.path.join(current_directory, 'base_object.kv'))
