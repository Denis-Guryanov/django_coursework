from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    """Модель пользователя"""

    username = None

    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    token = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Токен"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", null=True, blank=True, verbose_name="Аватар"
    )
    phone_number = PhoneNumberField(
        blank=True, null=True, verbose_name="Номер телефона"
    )
    country = CountryField(null=True, blank=True, verbose_name="Страна")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [("can_block_user", "Can block users")]
