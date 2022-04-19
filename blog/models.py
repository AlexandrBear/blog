from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child_comment', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    level_nesting = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '{} на пост {}'.format(self.name, self.post)

    def save(self):
        if self.parent:
            self.level_nesting = int(self.parent.level_nesting) + 1
        super().save()
