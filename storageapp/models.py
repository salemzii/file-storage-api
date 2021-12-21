from os import name
from django.db import models
from django.utils import timezone
import uuid


class file_uploader(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                    primary_key=True,
                    editable=False)

    name = models.CharField(max_length=18)
    file = models.FileField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name


