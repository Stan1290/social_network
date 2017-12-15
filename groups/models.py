from django.db import models
from django.utils.text import slugify
import misaka
from django import template
from django.contrib.auth import get_user_model



User = get_user_model

register = template.Library()

# Create your models here.
