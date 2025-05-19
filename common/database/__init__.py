from .guid import GUID  # noqa: F401
from .connection import DBConnection  # noqa: F401


def uuid():
    import timeflake
    flake = timeflake.random()
    return flake.hex
