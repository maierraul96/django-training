from django.db import models

# Create your models here.


class Counter(models.Model):
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