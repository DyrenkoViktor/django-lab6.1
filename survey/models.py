import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(u'Текст запитання', max_length=150, help_text=u'Максимум 150 символів')
    pub_date = models.DateTimeField('Дата створення')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Створено нещодавно?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(u'Текст варіанту', max_length=100, help_text=u'Максимум 100 символів')
    votes = models.IntegerField(u'Кількість голосів', default=0)

    def __str__(self):
        return self.choice_text
# Create your models here.
