from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    named_url = models.CharField(max_length=200, blank=True, null=True)
    simple_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["menu", "parent_id", "id"]

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.simple_url or "#"
        else:
            return self.simple_url or "#"
