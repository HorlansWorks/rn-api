from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.utils.translation import ugettext_lazy as _
import uuid
# Create your models here.

# STACKS = (
#     ('REACT', 'react'),
#     ('REACT NATIVE', 'react native'),
#     ('PYTHON', 'python'),
#     ('SOFTWARE ENGINEER', 'software engineer'),
#     ('BACKEND DEVELOPER', 'backend developer'),
#     ('DEVOPS', 'devops'),
#     ('FRONTEND DEVELOPER', 'frontend developer'),
#     ('SOLUTION ARCHITECT', 'solution architect'),
#     ('ROBOTICS ENGINEER', 'robotics engineer'),
#     ('MACHINE LEARNING', 'machine learning'),

# )


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("enter a valid email")
        if not username:
            raise ValueError("enter a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                           editable=False)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, )
    last_name = models.CharField(max_length=255,)
    email = models.EmailField(max_length=100, unique=True)
    # phone = models.IntegerField(null=True, blank=True)
    role = models.CharField(max_length=255, unique=True, blank=True, null=True)
    profileImage = models.ImageField(blank=True, null=True)
    resume = models.FileField(blank=True, null=True)
    connects = models.IntegerField(blank=True, null=True)
    # address = models.TextField(max_length=500, null=True, blank=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class UserStack(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='stack')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
