from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"

    class Meta:
        verbose_name_plural = "people"


class Todo(models.Model):
    text = models.TextField()
    state = models.BooleanField(default=False)
    owner = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        null=True
    )
