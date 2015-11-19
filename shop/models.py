from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название категории', max_length = 250)
    location = models.CharField('Вложенность', max_length = 250)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField('Название товара', max_length = 250)
    category = models.ForeignKey(Category, verbose_name='Категория', default=False)
    desc = models.CharField('Описание товара', max_length = 500)
    price = models.IntegerField('Стоимость')

    def __str__(self):
        return self.name + ' ' + self.desc + ' ' + str(self.price)

class User(models.Model):
    login = models.CharField('Имя пользователя', max_length = 16)
    email = models.CharField('Электронная почта', max_length = 100)
    password = models.CharField('Пароль', max_length = 16)

    def __str__(self):
        return self.login + ' ' + self.email + ' ' + self.password

class Order(models.Model):
    first_name = models.CharField('Имя заказчика', max_length = 16)
    last_name = models.CharField('Фамилия заказчика', max_length = 16)
    email = models.CharField('Электронная почта', max_length = 100)
    address = models.CharField('Адрес доставки', max_length = 300)
    pay_method = models.CharField('Способ оплаты', max_length = 50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.address

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказ', default=False)
    item = models.ForeignKey(Item, verbose_name='Товар', default=False)
    count = models.IntegerField('Количество')

    def __str__(self):
        return str(self.count)

class Bug(models.Model):
    bug_url = models.CharField('Страница с ошибкой', max_length = 300)
    bug_desc = models.CharField('Описание ошибки', max_length = 1000)
    bug_rate = models.CharField('Критичность ошибки', max_length = 300)

    def __str__(self):
        return self.bug_url + ' ' + self.bug_desc + ' ' + self.bug_rate

class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', default=False)
    address = models.CharField('Адрес пользователя', max_length = 300)
    pay_method  = models.CharField('Способ оплаты', max_length = 50)

    def __str__(self):
        return self.address + ' ' + self.pay_method

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', default=False)
    item = models.ForeignKey(Item, verbose_name='Товар', default=False)
    comment = models.CharField('Комментарий', max_length = 500)
    rating  = models.IntegerField('Рейтинг', max_length = 1)

    def __str__(self):
        return self.comment + ' ' + str(self.rating)