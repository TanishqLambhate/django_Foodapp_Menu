from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    def __str__(self):
        return self.item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://th.bing.com/th/id/R.59b8493ce8bc3e21038d9b85a44b6133?rik=VwcGq4PVCk2dvA&riu=http%3a%2f%2fwww.ukvisitorguide.cn%2fwp-content%2fuploads%2f2015%2f11%2fFood-placeholder.jpg&ehk=vLfv4oTMqt4NGoXjvXIWptKQZN3aCyg9btfYCj4%2b3Lc%3d&risl=&pid=ImgRaw&r=0&sres=1&sresct=1")

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})