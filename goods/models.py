from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200,blank=True,unique=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'ctegory'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200,blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField( default=0.00, max_digits=7, decimal_places=2 ,verbose_name='Цена')
    dicount = models.DecimalField( default=0.00, max_digits=4, decimal_places=2 ,verbose_name='Скидка в %')
    quanity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')


    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self) -> str:
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"
    

    def skidka(self):
        if self.dicount:
            return round(self.price - self.price*self.dicount/100, 2)
        
        return self.price