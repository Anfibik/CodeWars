

def make_class(*keys_class):
    class Animal:
        def __init__(self, *volume):
            for i in range(len(keys_class)):
                self.__dict__[keys_class[i]] = volume[i]

    return Animal
