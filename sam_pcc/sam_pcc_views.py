from django.shortcuts import render
from sam_submission.models import Paper,PCM_Review,PCM_Requests,ReviewAssignments
from django.http import HttpResponseRedirect

# Create your views here.

def pcc_home(request):
    print('@ PCC home')
    args = {}
    args['msg'] = 'Your are a PCC'
    return render(request, "pcc_home.html", args)


def pcc_view_requests(request):
    requests = PCM_Requests.objects.all()
    args = {}
    args['requests'] = requests
    return render(request, "pcc_requested_paper.html", args)


def pcc_approve_request(request, request_id, sub_id):
    print('pcc_approve_request id ',request_id)
    current_pcc = request.user
    current_request = PCM_Requests.objects.get(id=request_id)
    print(current_request.submission.id)
    requested_sub = current_request.submission
    requester = current_request.pcm

    if requested_sub.reviewers_count < 3:
        # create new assignment
        # NOTIFY PCM ABOUT ACCEPTANCE

        assignment = ReviewAssignments.objects.create(submission=requested_sub, pcm=requester)
        assignment.save()
        requested_sub.reviewers_count += 1
        requested_sub.save()

    elif requested_sub.reviewers_count > 2:
        # create new assignment
        # NOTIFY PCM ABOUT REJECTION
        print('cant assign')
    current_request.delete()
    return HttpResponseRedirect("/pccViewRequests")

def pcc_reject_request(request, request_id, sub_id):
    print('pcc_reject_request', request_id)
    current_pcc = request.user
    current_request = PCM_Requests.objects.get(id=request_id)
    print(current_request.submission.id)
    current_request.delete()
    # create new assignment
    # NOTIFY PCM ABOUT REJECTION


    return HttpResponseRedirect("/pccViewRequests")
