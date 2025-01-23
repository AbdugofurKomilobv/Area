from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)



class ContactMe(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    text = models.TextField()


    def __str__(self):
        return self.name