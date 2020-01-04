
from django.db import models
from django.contrib.auth.models import User
from .fields import TransactionTypeField


class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name



class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    type = TransactionTypeField()
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')

    def __str__(self):
        return f"{self.user.username} {self.id}"

    class Meta:
        verbose_name_plural = 'Transactions'
