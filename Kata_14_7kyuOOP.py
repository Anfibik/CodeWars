"""https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python"""


class Dictionary:
    def __init__(self):
        self.dict_storage = {}

    def newentry(self, word, definition):
        self.dict_storage.update([(word, definition)])


    def look(self, key):
        if key in self.dict_storage:
            return f"{self.dict_storage[key]}"
        return f"Can't find entry for {key}"


d = Dictionary()

d.newentry("Apple", "A fruit")
print(d.look("Apple"))

d.newentry("Soccer", "A sport")
d.newentry("Soccer", "A sport")
d.newentry("Soccer", "A sport")
print(d.look("Soccer"))
print(d.look("Hi"))
print(d.look("Ball"))
print(d.look("Soccer"))

d.newentry("soccer", "a sport")
d.look("soccer")

