import os.path

from kivy.lang import Builder

from warlocks_war.objects.entities.terra.terra import Terra

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'terra.kv'))
