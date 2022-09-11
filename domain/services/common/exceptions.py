from domain.services.common.entities import E


class CustomException(Exception):
    msg = None
    status_code = None

    def __init__(self, entity: type(E)):
        msg = f"[{entity.entity_name}] " + self.msg
        super().__init__(msg)


class DoesNotExistException(CustomException):
    msg = "Entity does not exist"
    status_code = 400


class IntegrityErrorException(CustomException):
    msg = "Entity could not be stored because of an integrity error"
    status_code = 500
