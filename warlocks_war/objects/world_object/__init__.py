import os.path

from kivy.lang import Builder

from warlocks_war.objects.world_object.world_object import WorldObject

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'world_object.kv'))

