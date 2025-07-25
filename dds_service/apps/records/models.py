from django.db import models
from apps.categories.models import Category


class RecordManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related("category", "status", "type")
        return qs


class Record(models.Model):
    # date
    created_at = models.DateField(auto_now_add=True)

    # data
    amount = models.DecimalField(max_digits=20, decimal_places=2, help_text='Amount in RUB')
    comment = models.TextField(max_length=200, null=True, blank=True)
    # relations
    status = models.ForeignKey("records.RecordStatus", on_delete=models.CASCADE, related_name='status')
    type = models.ForeignKey("records.RecordType", on_delete=models.CASCADE, related_name='type')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user')
    objects = RecordManager()

    def __str__(self):
        return f"Record#{self.id}(amount={self.amount}, status={self.status}, type={self.type})"



class RecordStatus(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class RecordType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
