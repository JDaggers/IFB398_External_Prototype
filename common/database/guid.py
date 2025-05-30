import timeflake
from sqlalchemy.types import TypeDecorator, BINARY


class GUID(TypeDecorator):
    """
    MySQL GUID type. Expects BINARY(16).
    """

    impl = BINARY
    cache_ok = True

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(BINARY(16))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        else:
            if isinstance(value, timeflake.Timeflake):
                return value.bytes
            return timeflake.parse(from_hex=value).bytes

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return timeflake.parse(from_bytes=value).hex

    @property
    def python_type(self):
        return timeflake.Timeflake
