"""https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python"""


class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, listeners_today):
        listeners_today = [i.lower() for i in listeners_today]
        res = len(set(listeners_today) - set(self.listeners))
        self.listeners = list(set(self.listeners + listeners_today))
        return res


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']))
print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']))
print(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']))
print(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']))