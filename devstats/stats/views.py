# django imports
from django.db.models import Count, F
from django.shortcuts import render, redirect, get_object_or_404
# project imports
from stats.models import Developer
from stats.forms import DeveloperCreateForm


def developer_list(request):
    #developers = Developer.objects.all()
    developers = Developer.objects.annotate(total_repos=Count('repos'))

    return render(request,
                  'developer/list.html',
                  {'developers': developers})


def developer_detail(request, username):
    developer = get_object_or_404(Developer, username=username)
    field_ops = F('stargazers_count') + F('watchers_count') + F('forks_count')
    top_repos = developer.repos.annotate(counts_sum=field_ops)\
                               .order_by('-counts_sum')[:5]

    return render(request,
                  'developer/detail.html',
                  {'developer': developer,
                   'top_repos': top_repos})


def developer_create(request):
    if request.method == 'POST':
    # if POST: create form POST data
        form = DeveloperCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            developer = Developer.objects.create(username=username)
            developer.update_profile_from_github()
            developer.update_repos_from_github()

            return redirect('developer_detail', username=username)
    else:
        form = DeveloperCreateForm()

    return render(request,
                  'developer/create.html',
                  {'form': form})
