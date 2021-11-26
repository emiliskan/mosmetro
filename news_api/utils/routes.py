from functools import wraps
import json
from datetime import datetime
from uuid import UUID


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (UUID, datetime)):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


def response_json_list(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        return json.dumps(func(*args, **kwargs), cls=CustomEncoder)

    return wrapper
