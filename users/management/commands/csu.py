from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):

        User = get_user_model()
        user = User.objects.create(email="admin@admin.ru")
        user.set_password("123")
        user.is_staff = True
        user.is_superuser = True
        user.save()

        try:
            permission = Permission.objects.get(codename="can_block_user")
            user.user_permissions.add(permission)
            self.stdout.write(self.style.SUCCESS(f"Право 'can_block_user' добавлено"))
        except Permission.DoesNotExist:
            self.stdout.write(
                self.style.ERROR("Разрешение 'can_block_user' не найдено!")
            )
        self.stdout.write(
            self.style.SUCCESS(f"Успешно создан суперпользователь с email {user.email}")
        )
