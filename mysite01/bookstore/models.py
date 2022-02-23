from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField('书名', max_length=50, unique=True)
    pub = models.CharField('出版社', max_length=100, default='')
    price = models.DecimalField('图书定价', max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField('图书零售价', default=0.0, max_digits=7, decimal_places=2)

    # info = models.CharField('描述信息', max_length=100, default='')

    class Meta:
        db_table = 'book'


class Author(models.Model):
    name = models.CharField('姓名', max_length=11, null=False)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField(null=True)

    class Meta:
        db_table = 'author'
