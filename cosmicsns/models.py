from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Department(models.Model):
    """所属 兼任可"""

    name = models.CharField(_('所属'), max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('所属')
        verbose_name_plural = _('所属')
        
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    icon = models.ImageField(blank=True, null=True)
    introduction = models.CharField(max_length=75, blank=True, null=True)
    followers = models.ManyToManyField('self', blank=True, symmetrical=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    full_name = models.CharField(_('氏名'), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    departments = models.ManyToManyField(
        Department,
        verbose_name=_('所属'),
        blank=True,
        help_text=_('Specific Departments for this user.'),
        related_name="user_set",
        related_query_name="user",
    )
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

class Posts(models.Model):
    message = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    postedtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.message[:10]