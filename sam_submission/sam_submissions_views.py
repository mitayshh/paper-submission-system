from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from sam_submission.models import Submission,Paper, Notification
from sam_main.models import UserProfile
from .forms import NewSubmissionForm, ReviseSubmissionForm


def author_new_submission(request):
    print('new submission')
    if request.method == 'POST':
        form = NewSubmissionForm(request.POST)

        new_sub = Submission.objects.create(submitter=request.user,
                                            topic=form.data['topic'],
                                            author_list=form.data['author_list'],
                                            contact=form.data['contact'],
                                            paper_format=form.data['paper_format'],
                                            )
        new_sub.save()

        new_paper = Paper.objects.create(submission_id=new_sub,
                                         revision=0,
                                         is_revised=False,
                                         paper=request.FILES['paper']
                                         )
        new_paper.save()

        #Notify PCC
        list_of_pcc = UserProfile.objects.filter(is_pcc=True)

        for p in list_of_pcc:
            msg = p.user.first_name + " has submitted a paper on " + new_sub.topic
            Notification.createNotification(sender=request.user,
                                recipient=p.user,
                                message=msg,
                                url='/sam2017/authorHome/')

        print(request.user.profile.getNotificationCount())

        return HttpResponseRedirect('/authorViewSubmission')
    else:
        print('new submission initial')
        form = NewSubmissionForm()
        args = {}
        args['form'] = form
        return render(request, "author_submission_new.html", args)


def author_revise_submission(request, paperid):
    curr_paper = Paper.objects.get(id=paperid)
    curr_revision = curr_paper.revision
    curr_submission = curr_paper.submission_id
    print('authReviseSubmission')
    if request.method == "POST":
        form = ReviseSubmissionForm(request.POST)

        new_paper = Paper.objects.create(submission_id=curr_submission,
                                         revision=curr_revision+1,
                                         is_revised=False,
                                         paper=request.FILES['paper']
                                         )
        new_paper.save()

        curr_paper.is_revised = True
        curr_paper.save()
        return HttpResponseRedirect('/authorViewSubmission')
    else:
        form = ReviseSubmissionForm()

        args={}
        args['form'] = form
        args['curr_paper'] = curr_paper
        return render(request, "author_submissions_revise.html", args)
