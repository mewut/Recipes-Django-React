from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=55, null=True, blank=True)  # создаем категории блюд. Типа супы, гарниры, напитки...
    detail = models.TextField('Описания', max_length=2255, blank=True)         # описываем, если надо
    url = models.SlugField(max_length=255, unique=True, null=True, blank=True)        # захотим посмотреть все супы - вот ссылка на супы

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ManyToManyField(Category, related_name='category', verbose_name='Категория', default='default_category')  # относится к супу
    name = models.CharField('Название', max_length=55, unique=True)    # Уха
    calorie = models.CharField('КБЖУ', max_length=255, null=True, blank=True)       # кбжу
    ingredients = models.CharField('Ингридиенты',max_length=2255)    # рыбка, картоха, лук, морковка
    steps = models.CharField('Рецепт',max_length=5000, blank=True)    # описание, как готовить. Но можно это поле пропустить
    image = models.ImageField(upload_to='media/', null=True, blank=True)   # можно прикрепить фотку
    url = models.SlugField(max_length=255, unique=True, null=True, blank=True)        # ссылка на уху

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=55)  
    detail = models.TextField('Отзыв', max_length=2255)   
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name='блюдо')     # если удалим блюдо, то удалятся и все комменты к нему
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)   # коммент останутся в БД даже при удалении автора

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'    

    def __str__(self):
        return f'{self.name} - {self.dish}'
    