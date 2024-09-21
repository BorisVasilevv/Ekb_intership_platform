from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
