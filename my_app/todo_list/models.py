from django.db import models

# Create your models here.

class ListItem(models.Model):
    item = models.CharField(max_length=150)
    complete = models.BooleanField(default=False)
    of_list = models.CharField(max_length=50)


    def __str__(self):
        return self.item

# end
