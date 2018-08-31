class Song(object):

# 下面的方法是__init__，不是__int__，请看清楚（第一次就写错了）
# 这是因为Python在创建对象是，分为两个阶段：
# 第一个阶段，对象是通过调用new方法来创建的，这个方法的细节我们基本上不用关心。
# new方法并不会立即返回一个对象实例，new方法之后，会调用init方法来给对象增加新的属性
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
