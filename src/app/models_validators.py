from uuid import UUID
from django.core.exceptions import ValidationError

class TopicValidators:

    @staticmethod
    def validate_uuid(value):
        try:
            UUID(value)
        except ValueError as e:
            raise ValidationError("It is not a valid UUID") from e