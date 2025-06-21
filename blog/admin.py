from django.contrib.admin import AdminSite
from .models import BlogPost


class CustomAdminSite(AdminSite):
    site_header = "Admin 💖"
    site_title = "Admin"
    index_title = "Ready to write a new blog post?"

    def each_context(self, request):
        context = super().each_context(request)
        context["css_files"] = ["css/admin_custom.css"]
        return context


admin_site = CustomAdminSite(name='custom_admin')

admin_site.register(BlogPost)
