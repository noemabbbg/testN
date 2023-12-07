from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Rating(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    user_id = models.IntegerField()  # предполагается, что user_id - это целое число
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.comic} - {self.value}"
