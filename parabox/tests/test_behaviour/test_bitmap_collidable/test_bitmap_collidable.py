import os

import testscenarios

from parabox.behaviour import BitmapCollidable


class TestBitmapCollidable(testscenarios.TestWithScenarios):
    def setUp(self):
        filename = 'temp_bitmap.csv'
        with open(filename, 'w+') as file:
            file.write(''.join([
                "     0,    0,    0,    0,    1\n",
                "     0,    0,    0,    1,    1\n",
                "     0,    0,    1,    1,    1\n",
                "     0,    1,    1,    1,    1\n",
                "     1,    1,    1,    1,    1\n"]))
        self.bitmap = BitmapCollidable(
            bitmap=filename, size=(5, 5), pos=(100, 100))
        os.remove(filename)

    scenarios = [
        ('Full out', dict(new_bitmap_pos=(200, 200), collission=False)),
        ('No collission', dict(new_bitmap_pos=(98, 103), collission=False)),
        ('Collission', dict(new_bitmap_pos=(98, 102), collission=True)),
    ]

    def test_collission(self):
        another_one = BitmapCollidable(
            pos=self.new_bitmap_pos, size=(5, 5))
        self.assertEqual(
            self.bitmap.collide_widget(another_one), self.collission)
