from django.db import models

class UserName(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-created_at']