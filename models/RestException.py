class RestException(Exception):
    def __init__(self, error_type: str, status_code: int, info: str = None):
        self._error_type = error_type
        self._status_code = status_code
        self._info = info

    @property
    def error_type(self) -> str:
        return self._error_type

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def info(self) -> str:
        return self._info
