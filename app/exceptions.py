from fastapi import HTTPException, status


class TaskException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(TaskException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User already exists'


class IncorrectEmailOrPasswordException(TaskException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect Email or Password'


class TokenExpiredException(TaskException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token has been expired'


class NoTokenException(TaskException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'No token'


class IncorrectFormatTokenException(TaskException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Incorrect token format'


class NoUserException(TaskException):
    status_code = status.HTTP_401_UNAUTHORIZED


class NoTaskForUserException(TaskException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No task for this user'


class NoTaskException(TaskException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'No such task'


class CanNotUploadException(TaskException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Can not upload file'
