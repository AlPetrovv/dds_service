from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    record_type = models.ForeignKey("records.RecordType", on_delete=models.SET_NULL, null=True, related_name='category')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"

    def __str__(self):
        return self.name
