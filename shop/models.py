from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200,
                              db_index=True),
        slug=models.SlugField(max_length=200,
                              db_index=True,
                              unique=True))

    class Meta:
        verbose_name_plural = "Categories"


    def get_absolute_url(self):
        return reverse("shop:product_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True),
        description=models.TextField(blank=True)
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products")
    image = models.ImageField(
        upload_to="products/%Y/%m/%d", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ["name"]
    #     index_together = (("id", "slug"),)

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name
