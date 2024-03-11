class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for key, value in self.__dict__.items():
            object_attributes += f'{key}: {value},'
        return f"Создан объект со свойствами {object_attributes})"
