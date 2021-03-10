import cocos
from cocos import collision_model
# from cocos.actions import *
# from cocos.collision_model import AARectShape


class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super(HelloWorld, self).__init__(64, 64, 224, 255)
        label = cocos.text.Label(
            'Hello, world`213',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center'
        )
        label.position = 320, 240
        self.add(label)
        sprite = cocos.sprite.Sprite('grossini.png')
        sprite.position = 320,20
        sprite.scale = 3
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
cocos.director.director.init()
collision_model.CollisionManagerGrid()
hello_layer = HelloWorld()
main_scene = cocos.scene.Scene(hello_layer)
cocos.director.director.run(main_scene)
