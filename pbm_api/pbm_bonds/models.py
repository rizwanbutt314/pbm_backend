import datetime
from django.db import models


class BondCategory(models.Model):
    category = models.CharField(
        max_length=255,
        unique=True,
        help_text="Name of Bond e.g. 750 or 200 etc")
    first_prize = models.CharField(
        max_length=255,
        help_text="First prize in Rs.")
    second_prize = models.CharField(
        max_length=255,
        help_text="Second prize in Rs.")
    third_prize = models.CharField(
        max_length=255,
        help_text="Third prize in Rs.")


class Bond100(models.Model):
    BOND_LEVEL_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
    )

    year = models.IntegerField(
        default=0,
        help_text="Year of prize bond announced"
    )
    date = models.DateField(default=datetime.date.today)
    bond_number = models.IntegerField(
        default=0,
        help_text="Prize bond number"
    )
    bond_level = models.IntegerField(choices=BOND_LEVEL_CHOICES)
    bond_category = models.ForeignKey(
        BondCategory,
        null=True,
        on_delete=models.CASCADE)
