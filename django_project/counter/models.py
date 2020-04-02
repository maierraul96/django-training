from django.db import models


# Create your models here.
class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Counter(SingletonModel):
    """Counter model"""

    value = models.IntegerField(default=0)

    def increment(self):
        """Increment current value by 1"""
        self.value += 1

    def decrement(self):
        """Decrement current value by 1"""
        self.value -= 1

    def set_value(self, value):
        """Set current value"""
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return repr(self.value)