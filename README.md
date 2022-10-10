# pybites-code-clinic
Sample Django Project (work-in-progress) for the [Pybites](https://pybit.es/) Code Clinic sessions. 

## Instructions
1. Generate a Github personal access token at https://github.com/settings/tokens inclduing the `repo` and `user` scopes.
2. Add the token to the `GITHUB_TOKEN` environment variable or to the `GITHUB_TOKEN` setting in `settings.py`
3. Install requirements with `pip install requirements.txt`
4. Execute database migrations with `python manage.py migrate`
5. To access the administration site create a superuser with `python manage.py createsuperuser`
6. Run the project on your local machine with the command `python manage.py runserver`
7. Access http://127.0.0.1:8000/ for the web application and http://127.0.0.1:8000/admin/ for the administration site


## Additional Resources
- Django models – https://docs.djangoproject.com/en/4.1/topics/db/models/
- Many-to-one relationships – https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
- Django forms – https://docs.djangoproject.com/en/4.1/topics/forms/
- Django form field validation – https://docs.djangoproject.com/en/4.1/ref/forms/validation/
- Creating forms from models – https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
- Making queries with the Django ORM – https://docs.djangoproject.com/en/4.1/topics/db/queries/
- Using `annotate()` to generate aggregates for each item in a QuerySet – https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#generating-aggregates-for-each-item-in-a-queryset
- Django `F()` query expressions – https://docs.djangoproject.com/en/4.1/ref/models/expressions/
- Serving static files during development – https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-static-files-during-development
- PyGithub docs – https://pygithub.readthedocs.io/
- Github API docs – https://docs.github.com/en/rest
- Django Debug Toolbar – https://django-debug-toolbar.readthedocs.io/en/latest/

## Book
[<img src="https://djangobyexample.com/static/v4/img/django_by_example_4_cover.png" style="width:140px;"  align="left">](https://djangobyexample.com/)
Learn more with [Django 4 by Example](https://djangobyexample.com/). This book will walk you through the creation of four real-world applications, solving common problems, and implementing best practices, using a step-by-step approach that is easy to follow. After reading this book, you will have a good understanding of how Django works and how to build practical, advanced web applications.
