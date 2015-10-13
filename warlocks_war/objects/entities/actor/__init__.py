import os.path

from kivy.lang import Builder

from warlocks_war.objects.entities.actor.actor import Actor

Builder.load_file(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'actor.kv'))
