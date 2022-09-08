from django.conf import settings
from email.mime import image
from django.db import models, migrations


class User(models.Model):
    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user',
    )

    def get_username(self):
        return self.user.get_username()

    def get_full_name(self):
        return self.user.get_full_name()

    @property
    def username(self):
        return self.user.username

    @username.setter
    def username(self, value):
        self.user.username = value

    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, value):
        self.user.first_name = value

    @property
    def last_name(self):
        return self.user.last_name

    @last_name.setter
    def last_name(self, value):
        self.user.last_name = value

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, value):
        self.user.email = value

    @property
    def date_joined(self):
        return self.user.date_joined

    @property
    def last_login(self):
        return self.user.last_login

    @property
    def groups(self):
        return self.user.groups

    def __str__(self):
        return self.get_username()

class Post(models.Model):
    title = models.CharField(max_length=100 ),
    text = models.TextField(),
    image = models.ImageField()
# Create your models here.
