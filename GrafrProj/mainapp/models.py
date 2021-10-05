from django.db import models


class TelegrafModel(models.Model):
    uri = models.CharField(primary_key=True, max_length=6, verbose_name='Ссылка')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='uploads/', verbose_name='Файл', blank=True)
    content = models.TextField(db_index=True, verbose_name='Содержание')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('pub', kwargs={'uri': self.uri})

    def __str__(self):
        return self.uri

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created', 'uri']
