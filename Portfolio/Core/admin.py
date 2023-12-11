from django.contrib import admin
from .models import *
from .forms import PostForm, ContactForm


# Register your models here.
class DesignInline(admin.TabularInline):
    model = Design
    extra = 4  # Number of empty forms to display
    

class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 4  # Number of empty forms to display


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ("id", "project", "project_date_created", "github_link")
    list_filter = ("project_date_created", "github_link", 'project_type')
    search_fields = ("project_overview",)
    inlines = [DesignInline, GalleryInline]
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ("subject",)
    search_fields = ("email",)
    
