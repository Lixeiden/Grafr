# auto-del = models.BooleanField(default=False)
# pass = models.PassField ? or CharField
# filefield = make multiple? as widget

from django.db import models


class TelegrafModel(models.Model):
    uri = models.CharField(primary_key=True, max_length=6, verbose_name='Ссылка')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    file = models.FileField(upload_to='uploads/', verbose_name='Файл', blank=True)
    content = models.TextField(db_index=True, verbose_name='Содержание')
    #category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория') # make this Table as Secondary via Foreign key "category_id"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('pub', kwargs={'uri': self.uri})

    def __str__(self):
        return self.uri

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created', 'uri']





# create new Table as Primary
# class Category(models.Model):
#     title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
#
#     def __str__(self):
#        return self.title
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#         ordering = ['title']