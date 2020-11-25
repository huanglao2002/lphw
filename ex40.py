class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_baby = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They raly around the family",
                        "With pockets full of shells"])

merry_Christmas = Song(["merry Christmas",
                    "Merry Christmas"])

best_wish = ["祝你生日快乐","祝你生日快乐"]
best_for_you = Song(best_wish)

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

merry_Christmas.sing_me_a_song()

best_for_you.sing_me_a_song()