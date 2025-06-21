from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    use_code_highlighting = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def preview(self, num_chars=200):
        return self.content[:num_chars] + '...'
