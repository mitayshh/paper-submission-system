from django.shortcuts import render
from sam_submission.models import Submission,Paper,PCM_Requests,ReviewAssignments
from django.template import RequestContext
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.

def pcm_home(request):
    print('@ PCM home')
    args = {}
    args['msg'] = 'You\'re are a PCM'
    current_pcm = request.user
    print(current_pcm)
    #papers = Paper.objects.all().filter(~Q(is_assigned_to = request.user))
    #for p in papers:
        #print(p.submission_id.topic)

    return render(request, "pcm_home.html")


def pcm_view_submissions(request):
    submission = Submission.objects.filter(isReviewed='0')
    paper = Paper.objects.filter(is_revised='0').exclude(submission_id__submitter=request.user.id).exclude(submission_id__reviewers_count__gte=3)
    requested_subs = PCM_Requests.objects.filter(pcm_id=request.user.id)
    assigned_subs = ReviewAssignments.objects.filter(pcm__id=request.user.id)
    paper1 = paper.exclude(submission_id__id__in=[i.submission.id for i in requested_subs])
    paper2 = paper1.exclude(submission_id__id__in=[j.submission.id for j in assigned_subs])
    args = {}
    args['submission'] = submission
    args['paper'] = paper2
    args['requestedpaper'] = requested_subs
    print("pcm_request_paper")

    return render(request, "pcm_request_paper.html", args)


def pcm_request_paper(request, submission_id):
    print('pcm_request_paper', submission_id)
    curr_sub = Submission.objects.get(id=submission_id)
    new_request = PCM_Requests.objects.create(submission=curr_sub, pcm=request.user)
    new_request.save()
    return HttpResponseRedirect('/pcmViewSubmissions')

def pcm_view_assigned_subs(request):
    print('pcm_view_assigned_papers')
    all_assignments = []
    assigned_subs = ReviewAssignments.objects.filter(pcm__id=request.user.id)

    for i in assigned_subs:
        print(i.submission)
        paper = i.submission.sub_paper.get(is_revised=0)
        all_assignments.append(paper)
        print(paper.is_assigned)
    args = {}
    args['all_assignments'] = all_assignments
    return render(request, "pcm_view_assignments.html", args)

