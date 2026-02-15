class MusicalNote:
    def __init__(self, name,  pitch):
        self.__pitch = pitch
        self.__name = name

    @property
    def pitch(self):
        return self.__pitch

    @pitch.setter
    def pitch(self, value):
        raise AttributeError("can't set attribute")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        raise AttributeError("can't set attribute")
