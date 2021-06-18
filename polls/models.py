from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Article(models.Model):
    article_title = models.CharField('Article_name', max_length = 200)
    article_text = models.TextField('Text')
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.article_title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'

class Info(models.Model):
    info_title = models.CharField('Info_name', max_length = 200)
    info_text = models.TextField('Text')
    pub_date = models.DateTimeField('Date published')

    def was_published_recently(self):
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.info_title

    class Meta:
        verbose_name = 'Інфо'
        verbose_name_plural = 'Інформація для учнів'

class Image(models.Model):
    title = models.CharField(max_length=50, default = "Image")
    image = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографіі класу'

class Subject(models.Model):
    subj = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(null = True, blank = True, upload_to='images')
    text = models.TextField('Text')
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'

class BestWorks(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Наші досягнення'