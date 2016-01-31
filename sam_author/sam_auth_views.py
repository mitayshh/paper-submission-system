from django.shortcuts import render
from sam_submission.models import Submission,Paper,PCM_Requests,ReviewAssignments
# Create your views here.

def author_home(request):
    print('@ Author home')
    args = {}
    args['msg'] = 'Your are an Author'
    return render(request, "author_home.html", args)

def author_view_submission(request):
    print('@author view papers')
    auth_subs = Submission.objects.filter(submitter=request.user.id)
    auth_papers =[]

    for i in auth_subs:
        print('auth',i)
        paper = i.sub_paper.get(is_revised=0)
        auth_papers.append(paper)
        print('auth',paper)
    args={}
    args['auth_papers'] = auth_papers
    return render(request, "author_submissions.html", args)
