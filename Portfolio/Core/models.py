from django.db import models


class Post(models.Model):
    class ProjectFlow(models.TextChoices):
        in_process = "process", "Process"
        completed = "completed", "Complete"

    class ProjectType(models.TextChoices):
        in_process = "web", "Web"
        completed = "mobile", "Mobile"

    project = models.CharField(max_length=50, unique=True)
    project_overview = models.CharField(max_length=1000)
    research_and_inspiration = models.CharField(max_length=1000)
    problem_statement = models.CharField(max_length=1000)
    concept_and_design_principles = models.CharField(max_length=1000)
    challenges_and_solutions = models.CharField(max_length=1000)
    conclusion_and_next_steps = models.CharField(max_length=1000)
    project_flow = models.CharField(max_length=50, choices=ProjectFlow.choices)
    project_type = models.CharField(max_length=50, choices=ProjectType.choices)
    project_cover = models.ImageField(
        upload_to="Design/Covers", max_length=100)
    project_logo = models.ImageField(
        upload_to="Design/Logos", max_length=100)
    project_date_created = models.DateField()
    github_link = models.CharField(max_length=1000, blank=True, null=True)
    figma_link = models.CharField(max_length=1000, blank=True, null=True)
    linkdin_link = models.CharField(max_length=1000, blank=True, null=True)
    show_advertise = models.BooleanField(default=False)


class Design(models.Model):
    image = models.ImageField(upload_to="Design", max_length=100)

    def upload_to_path(instance, filename):
        # Use the name of the associated post to create the directory structure
        return f"Design/{instance.design.project}/{filename}"

    design = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name='post_design')
    upload_to = upload_to_path  # Set the upload_to parameter to the function


class Gallery(models.Model):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name='post_gallery')
    gallery = models.ImageField(upload_to="Design/Gallery", max_length=100)

    def upload_to_path(instance, filename):
        # Use the name of the associated post to create the directory structure
        return f"Design/{instance.post.project}/{filename}"

    upload_to = upload_to_path


class Contact(models.Model):
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)
