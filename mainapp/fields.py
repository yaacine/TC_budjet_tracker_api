from django.db import models
from .enums import TransactionTypes


class TransactionTypeField(models.CharField):
    description = "Transaction Type"

    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(tag.name, tag.value) for tag in TransactionTypes]
        kwargs['default'] = TransactionTypes.income.name
        kwargs['max_length'] = 30
        super().__init__(*args, **kwargs)
