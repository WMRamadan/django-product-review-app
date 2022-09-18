import os
import uuid


def generate_unique_name(path):
    def wrapper(instance, filename):
        extension = "." + filename.split('.')[-1]
        filename = str(uuid.uuid4()) + extension
        return os.path.join(path, filename)

    return wrapper
