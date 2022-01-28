from django.db import models
from django.utils import timezone


class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование производителя')
    email = models.CharField(max_length=50, verbose_name='Почта')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/suppliers'

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Stands(models.Model):
    price = models.IntegerField(default=1000, verbose_name='Цена')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='stand_supplier',
                                 verbose_name='Производитель')
    amount = models.IntegerField(verbose_name='Количество')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    square = models.IntegerField(default=10, verbose_name='Площадь м2')

    def __str__(self):
        return "№" + str(self.id) + " " + str(self.price) + "$"

    def get_absolute_url(self):
        return f'/stands'

    class Meta:
        verbose_name = 'Стенд'
        verbose_name_plural = 'Стенды'


class Media(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование сми')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/media'

    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'


class Application(models.Model):
    stand = models.ForeignKey(Stands, on_delete=models.CASCADE, related_name='stand_id', verbose_name='Cтенд')
    name = models.CharField("Имя клиента", max_length=50)
    phone = models.CharField("Телефон", max_length=50)
    date = models.DateTimeField(default=timezone.now, verbose_name="Дата",)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, related_name='media_id', verbose_name='сми')

    def __str__(self):
        return self.name + " " + str(self.date)

    def get_absolute_url(self):
        return f'/application/-date'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
