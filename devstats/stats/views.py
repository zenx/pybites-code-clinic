# django imports
from django.shortcuts import render, get_object_or_404
# project imports
from stats.models import Developer


def developer_list(request):
    developers = Developer.objects.all()

    return render(request,
                  'developer/list.html',
                  {'developers': developers})


def developer_detail(request, username):
    developer = get_object_or_404(Developer, username=username)
    top_repos = developer.repos.all()

    return render(request,
                  'developer/detail.html',
                  {'developer': developer})
