import pathlib
import uuid

from django.db import models
from django.utils.text import slugify


def upload_image(instance, filename) -> pathlib.Path:
    filename = (f"{slugify(instance.title)}-{uuid.uuid4()}" + pathlib.Path(filename).suffix)
    return pathlib.Path("upload/products/") / pathlib.Path(filename)


class Product(models.Model):
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to=upload_image, null=True)
