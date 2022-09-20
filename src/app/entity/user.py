


class User:
    def __init__(self) -> None:
        self.__user_uuid = None

    @property
    def user_uuid(self):
        if self.__user_uuid is None:
            return self.__user_uuid

    @property
    def user_uuid(self,value):
        return self.__user_uuid