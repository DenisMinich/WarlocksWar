import os.path

from kivy.lang import Builder

from warlocks_war.objects.behaviour_mixins.movable.movable import Movable

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'movable.kv'))
