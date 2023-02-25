"""https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/python"""


class VersionManager:
    def __init__(self, version=None):
        version = self.__correct_version(version)
        self.__check_version(version)

        self.ma = int(version[0])
        self.mi = int(version[1])
        self.pa = int(version[2])
        self.history = [self.get_current_version()]

    @staticmethod
    def __correct_version(version: str) -> list:
        if version is None or version == '':
            return ['0', '0', '1']
        version = version.split('.')
        if version[-1] == "":
            version.pop()
        while len(version) < 3:
            version.append('0')

        return version[0:3]

    @staticmethod
    def __check_version(version: list):
        for vol in version:
            if not vol.isdigit():
                raise ValueError("Error occured while parsing version!")

    def add_version_history(self, version):
        self.history.append(self.get_current_version())

    def major(self):
        self.ma += 1
        self.mi = 0
        self.pa = 0
        self.add_version_history(self.get_current_version())
        return self

    def minor(self):
        self.mi += 1
        self.pa = 0
        self.add_version_history(self.get_current_version())
        return self

    def patch(self):
        self.pa += 1
        self.add_version_history(self.get_current_version())
        return self

    def rollback(self):
        if len(self.history) == 1 and self.history[0] == '0.0.1':
            raise BaseException("Cannot rollback!")
        if len(self.history) == 1 and self.history[0] != '0.0.1':
            self.history[0] = '0.0.1'
            return self
        self.history.pop()
        current_version = self.__correct_version(self.history[-1])
        self.ma = int(current_version[0])
        self.mi = int(current_version[1])
        self.pa = int(current_version[2])
        return self

    def get_current_version(self):
        version = [str(self.ma), str(self.mi), str(self.pa)]
        return '.'.join(version)

    def release(self):
        if len(self.history) == 1:
            return self.history[0]
        return self.history[-1]


#
vm = VersionManager()
vm.rollback()
