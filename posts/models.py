from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    dob = models.DateField()
    idNo = models.IntegerField(blank=True, null=True)
    phone_number = models.IntegerField()
    joined_at = models.DateTimeField(auto_now_add=True)    

    class Meta:
        ordering = ['-joined_at']

    def __str__(self):
        return str(self.first_name)