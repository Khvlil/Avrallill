from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
import random
from django.http import Http404
from django_htmx.http import HttpResponseClientRedirect
from django.core.cache import cache
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.


def home(request):
    try:
        projects = Post.objects.filter(project_type='web')
    except Post.DoesNotExist:
        projects = None

    # Paginate the projects
    paginator = Paginator(projects, 3)
    per_page = request.GET.get("page")
    recommendation = paginator.get_page(per_page)
    load_type = 'web'
    version = 'mobile'

    return render(request, "LandingPage/Home.html", context={"projects": recommendation, "load_type": load_type, 'version': version})


def show_project(request, project_name):
    # Check if the project's context is already in the cache
    cached_project_context = cache.get(f"project_{project_name}")

    if not cached_project_context:
        # If not in cache, compute the context
        works = [work for work in Post.objects.all()]

        try:
            project = Post.objects.get(project=project_name)
        except Post.DoesNotExist:
            raise Http404("Project not found")

        designs = [design for design in Design.objects.filter(
            design__project=project_name)]

        works_without_current_project = [
            work for work in works if work != project]

        paginator = Paginator(random.sample(
            works_without_current_project, k=3), 3)

        per_page = request.GET.get("page")
        recommendation = paginator.get_page(per_page)

        project_context = {
            "project": project,
            "works": works,
            "designs": designs,
            "recommendation": recommendation,
        }

        # Store the computed context in the cache for 1 hour (you can adjust the timeout)
        cache.set(f"project_{project_name}", project_context, timeout=3600)

        # Use the computed context
        context = project_context
        print('# Use the DB context')

    else:
        # Use the cached context
        context = cached_project_context
        print('# Use the cached context')

    return render(request, "Project.html", context)


def get_project_types(request, type_):
    # Try to get projects from cache
    cached_project_type_ = cache.get(f'project_type_{type_}')

    if cached_project_type_ is not None:
        # If cached data is available, use it
        projects = cached_project_type_
    else:
        # If not, fetch projects from the database
        try:
            projects = Post.objects.filter(project_type=type_)
        except Post.DoesNotExist:
            projects = None

        # Store fetched projects in the cache for future use
        cache.set(f'project_type_{type_}', projects)

    # Paginate the projects
    paginator = Paginator(projects, 3)
    per_page = request.GET.get("page")
    recommendation = paginator.get_page(per_page)

    context = {"projects": recommendation, "load_type": type_}

    return render(request, "Components/Works.html", context)


def get_version(request, version):
    # Check if the version is already in the cache
    cached_version = cache.get(f"version_{version}")

    if not cached_version:
        # If not in cache, compute the context
        version_context = {'version': version}

        # Store the computed context in the cache for 1 hour
        cache.set(f"version_{version}", version_context, timeout=3600)

        # Use the computed context
        context = version_context
    else:
        # Use the cached context
        context = cached_version

    # if the request I make is HTMX-Request
    return render(request, "Components/Version.html", context)


def contact_us(request):
    email_send = False
    if request.htmx:

        if request.method == 'POST':
            print('HTMX')
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                email = contact_form['email'].value()
                client_subject = contact_form['subject'].value()
                client_message = contact_form['message'].value()
                website = request.path
                print(email)

                email_content(email, client_subject, client_message, website)

                email_send = True
                print('Everything is correct')
                if email_send:
                    messages.success(
                        request, 'The post has been created successfully.')

                    return redirect('Home')
            return render(request, "Contact_Us.html", {'form': contact_form})
        else:
            messages.warning(
                request, 'Holly molly 😱, something goes wrong ... please re submit your GOGO.')
            contact_form = ContactForm()

            print('HTMX None')

            return render(request, "Contact_Us.html", {'form': contact_form})

    return render(request, "Base.html")


def email_content(email, client_subject, client_message, website):
    email_extract = email.split('@', 1)[0]
    subject = 'Thank You for Contacting Avrallill 🚀'

    context = {
        'email_extract': email_extract,
        'client_subject': client_subject,
        'client_message': client_message
    }

    html_message = render_to_string(
        'Components/Letter.html', context)

    plain_message = strip_tags(html_message)

    return mail.send_mail(
        subject,
        plain_message,
        f"Welcome <{settings.EMAIL_HOST_USER}>",
        [email],
        html_message=html_message
    )


def loader(request):
    return render(request,'Components/Loader.html')