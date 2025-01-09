from django.db import models
from django.core.validators import MinValueValidator
import uuid

# Create your models here.
class Worker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #example 4f1a601d-0db5-4fbb-9e99-6d1c48a0d6f7
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[MinValueValidator(14)]) #minimum working age in california
    company = models.ForeignKey('companies_api.Company', on_delete=models.CASCADE, related_name="workers") #when the company is deleted all person will also be deleted
    registered_date = models.DateTimeField(auto_now_add=True)
