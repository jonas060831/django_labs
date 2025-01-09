from django.db import models

# Create your models here.
import uuid
from django.db import models

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #example 4f1a601d-0db5-4fbb-9e99-6d1c48a0d6f7
    name = models.CharField(max_length=32)
    industry = models.CharField(max_length=50)
