import my_pics.hema_pics.art #subpackage,sub-subpackage,module
my_pics.hema_pics.art
from my_pics.hema_pics import art
art.display()
from my_pics.hema_pics import art,cooking_photos,photography
cooking_photos.display()
photography.display()

from my_pics.hema_pics.art import display,mandalaart,pencilart,painting

mandalaart()
painting()

from my_pics.hema_pics.art import *
pencilart()

