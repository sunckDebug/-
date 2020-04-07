from django.db import models

# Create your models here.


class userScore(models.Model):

    """角色"""

    name = models.CharField(max_length=10, verbose_name='用户名称', unique=True)
    score = models.IntegerField(verbose_name='最新分数')
    is_active = models.BooleanField(default=True, verbose_name='是否可用')

    def __str__(self):
        return self.name

    def to_dict(self):
        dict = {
            'name': self.name,
            'score': self.score,
        }
        return dict