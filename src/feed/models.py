from django.db import models

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    DEVELOPMENT = 'dv'
    PERSONAL = 'ps'
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal")
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices = CATEGORY_CHOICES,
        default= DEVELOPMENT,
    )

    #hashtagf를 사용하려면 hashtag class가 위에 있어야 한다.
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:200]


class Comment(models.Model):
    article= models.ForeignKey(Article,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return '{}의 대한 댓글:{}'.format(self.article.title, self.content)
