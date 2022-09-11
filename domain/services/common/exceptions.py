from domain.services.common.entities import E


class CustomException(Exception):
    msg = None

    def __init__(self, entity: type(E)):
        msg = f"[{entity.entity_name}] " + self.msg
        super().__init__(msg)


class DoesNotExistException(CustomException):
    msg = "Entity does not exist"


class IntegrityErrorException(CustomException):
    msg = "Entity could not be stored because of an integrity error"
