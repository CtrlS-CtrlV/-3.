"""Модуль визначення доменних виключень застосунку."""

class AppError(Exception):
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.code = code

    def __str__(self):
        return f"[{self.code}] {self.args[0]}"

class ValidationError(AppError):
    def __init__(self, message: str, field: str):
        super().__init__(message, code=400)
        self.field = field

    def __str__(self):
        return f"{super().__str__()} (Поле: {self.field})"

class ResourceNotFoundError(AppError):
    def __init__(self, message: str, resource_id: str):
        super().__init__(message, code=404)
        self.resource_id = resource_id

class ProcessingError(AppError):
    def __init__(self, message: str, stage: str):
        super().__init__(message, code=500)
        self.stage = stage
