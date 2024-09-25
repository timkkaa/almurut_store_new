from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


from users.models import CustomUser


class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Котегория товара'
        verbose_name_plural = 'Котегория товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField(verbose_name='цена без скидки', help_text=' сомах')
    sales_percent = models.PositiveSmallIntegerField(
        verbose_name='скидка в процентах',
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ],
    )

    description = models.TextField()
    preview_imag = models.ImageField()

    new_expiry_date = models.DateField()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_price_with_sales(self):
        if self.sales_percent == 0:
            return self.price
        else:
            return int((self.price / 100) * (100-self.sales_percent))

    def __str__(self):
        return self.name


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='product_gallery/')

    class Meta:
        verbose_name = 'Галерея товара'
        verbose_name_plural = 'Галерея товаров'

class ProductUserRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'product'], name='unique_user_product')
        ]

class ProductRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'product',)


