from django.db import models

class NewsQuery(models.Model):
    country = models.CharField(max_length=2)
    category = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News Queries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.country} - {self.category}"