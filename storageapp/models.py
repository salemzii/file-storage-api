from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid
from django.contrib.auth.models import User



class file_uploader(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                    primary_key=True,
                    editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=18)
    file = models.FileField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self) -> str:
        return self.name



class image(models.Model):

    id = models.UUIDField(default=uuid.uuid4,
                    primary_key=True,
                    editable=False)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=18)
    img = models.ImageField(upload_to="images")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name


"""class videos(models.Model):
    id = models.UUIDField(
        default= uuid.uuid4, 
        primary_key=True,
        editable=False
    )
    name = models.CharField(max_length=18)
    video = models.f"""        