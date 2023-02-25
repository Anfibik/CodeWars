def hashtag(string):
    return '#' + "".join([i.capitalize() for i in string.split()]) if 0 < len(string) < 140 else False



s = ""
print(hashtag(s))