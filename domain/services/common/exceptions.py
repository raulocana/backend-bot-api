from domain.services.common.entities import E


class CustomException(Exception):
    msg = None
    status_code = None

    def __init__(self, entity: type(E) = None):
        msg = self.msg
        if entity is not None:
            msg = f"[{entity.entity_name}] " + msg
        super().__init__(msg)


class DoesNotExistException(CustomException):
    msg = "Entity does not exist"
    status_code = 400


class IntegrityErrorException(CustomException):
    msg = "Entity could not be stored because of an integrity error"
    status_code = 500


class UncontrolledTopicException(CustomException):
    msg = "Topic received is not controlled"
    status_code = 500


class UncontrolledIntegrationServiceException(CustomException):
    msg = "Integration service received is not controlled"
    status_code = 500
