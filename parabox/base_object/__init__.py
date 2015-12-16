import os.path

from kivy.lang import Builder

from parabox.base_object.base_object import BaseObject

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'base_object.kv'))

