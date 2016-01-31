from django.db import models
from django.contrib.auth.models import User
from sam_submission.models import Notification

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='UserProfile')
    is_admin = models.BooleanField(default=0)
    is_pcc = models.BooleanField(default=0)
    is_pcm = models.BooleanField(default=0)
    is_author = models.BooleanField(default=1)

    def getNotification(self, notifyID):
        return Notification.objects.filter(id=notifyID)[0]

    def getNotifications(self):
        return Notification.objects.filter(recipient=self)

    def getNotificationCount(self):
        aVar = Notification.objects.filter(recipient=self).filter(read=False)
        print(Mitesh)
        return Notification.objects.filter(recipient=self).filter(read=False).count()

        def __str__(self):
            return self.user_id

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])