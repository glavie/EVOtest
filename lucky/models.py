# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.db import models
from django.core.validators import RegexValidator

AlphabeticValidator = RegexValidator(
    r'^[a-z]*$',
    message='Only alphabetic chars allowed.',
    flags=re.IGNORECASE,
)


class Names(models.Model):
    name = models.CharField(max_length=30, verbose_name='Username',
                            validators=[AlphabeticValidator])