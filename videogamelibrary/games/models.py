from django.db import models
from django.core.validators import MaxLengthValidator
from ckeditor.fields import RichTextField
# Create your models here.



class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Developer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=200) # Suppose it's possible to have a WorldEnd situation but eh.
    pub_date = models.DateTimeField("date released")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)
    description = RichTextField(max_length=3000, blank=True, validators=[MaxLengthValidator(3000)])
    cover = models.ImageField("cover", upload_to='covers/%Y/%m/%d')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name + " (" + str(self.pub_date.year) + ")"


