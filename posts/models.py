from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
import misaka
from goups.models import Group
from django.conf import settings


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='post')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = medels.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='post', null=True, blank=True)


    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)


    def get_absolute_url(self):
        return reverse('posr:single', kwargs={'username':self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']



# Create your models here.