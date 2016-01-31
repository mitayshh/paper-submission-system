from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Submission(models.Model):

    PDF = 'PDF'
    WORD = 'WORD'

    paper_format_choice = (
        (PDF, 'PDF'),
        (WORD, 'WORD'),
    )
    submitter = models.ForeignKey(User)
    topic = models.TextField()
    author_list = models.TextField()
    contact = models.TextField()
    paper_format = models.CharField(max_length=4, choices=paper_format_choice)

    isReviewed = models.BooleanField(default=0)
    reviewers_count = models.IntegerField(default=0)
    review_count = models.IntegerField(default=0)



class Paper(models.Model):

    submission_id = models.ForeignKey(Submission, related_name='sub_paper')
    revision = models.IntegerField(default=0)
    is_revised = models.BooleanField(default=0)
    is_assigned = models.BooleanField(default=0)
    counter = models.IntegerField(default=0)
    #is_assigned_to = models.ManyToManyField(User)


    paper = models.FileField(upload_to='papers', blank=True, null=True)


class PCM_Review(models.Model):

    paper_id = models.ForeignKey(Paper)
    reviewer = models.ForeignKey(User)
    comments = models.TextField()
    review = models.FileField(upload_to='reviews', blank=True, null=True)
    reviewed_completed = models.BooleanField(default=0)

class PCM_Requests(models.Model):

    submission = models.ForeignKey(Submission)
    pcm = models.ForeignKey(User)

class ReviewAssignments(models.Model):
    submission = models.ForeignKey(Submission)
    pcm = models.ForeignKey(User)
    is_reviewed = models.BooleanField(default=0)

class Notification(models.Model):
    recipient = models.ForeignKey(User, related_name='%(class)s_recip')
    sender = models.ForeignKey(User, related_name='%(class)s_sender')
    date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User Notification'

        def __str__(self):
            return self.recipient.name + ' (' + self.date.isoformat() + ')'
    @classmethod
    def createNotification(self,recipient,sender,message,url):
        n = Notification.objects.create(sender=sender,recipient=recipient,message=message,url=url)
        n.save();
