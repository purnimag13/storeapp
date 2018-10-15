# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.item_name