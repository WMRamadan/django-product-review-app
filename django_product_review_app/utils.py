import os
import uuid
from django.utils.deconstruct import deconstructible


@deconstructible
class GenerateUniqueName(object):

    def __init__(self, path):
        self.path = path
    def __call__(self, instance, filename):
        extension = "." + filename.split('.')[-1]
        filename = str(uuid.uuid4()) + extension
        return os.path.join(self.path, filename)

generate_unique_name = GenerateUniqueName('images/')
