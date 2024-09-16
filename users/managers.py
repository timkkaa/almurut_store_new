from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def crsate_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_active'] = True
        return self.crsate_user(email, password, **extra_fields)