from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_time__lte=now)  # Less_or_Equal_than now, means "before now"

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        return self.filter(lookup)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class Post(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=256)
    slug = models.SlugField(default="default-slug", unique=True)
    image = models.ImageField(upload_to='img/', null=True, default='img/default.png')
    content = models.TextField(null=True, blank=True)

    publish_time = models.DateTimeField(auto_now=True, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-updated', '-pk', '-timestamp'] # '-publish_time'

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_img_url(self):
        return self.image.url

    def get_edit_url(self):
        return f"/blog/{self.slug}/update"

    def get_delete_url(self):
        return f"/blog/{self.slug}/delete"

    def __str__(self):
        return f"({self.pk}) {self.title}"

    '''
    python manage.py shell

    from appBlog.models import Post

    Post.objects.all()
                .first()
                .last().title
                .last().content

    obj = Post(title="foo", content='bar')
    obj.save()

    '''
