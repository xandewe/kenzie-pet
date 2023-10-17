from django.db import models
from math import log as ln

class SexChoices(models.TextChoices):
    NA = "Não informado"
    MALE = "Macho"
    FEMALE = "Femea"


class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15, choices=SexChoices.choices, default=SexChoices.NA)

    group = models.ForeignKey("groups.Group", on_delete=models.CASCADE, related_name="animals")
    traits = models.ManyToManyField("traits.Trait", related_name="animals")

    def convert_in_human_years(self):
        return int(16 * ln(self.age) + 31)
