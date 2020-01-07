from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    diary_title     =   models.CharField(max_length=60,null=True)
    diary_content   =   models.TextField(max_length=5000,null=True)
    diary_date      =   models.DateTimeField(auto_now_add=True)
    user            =   models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.diary_title