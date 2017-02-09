from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


class Tag(models.Model):
    text = models.CharField(max_length=255,)

    def __unicode__(self):
        return self.text


class Question(models.Model):
    choices = (
        (1, 2),
        (3, 4)
    )

    text = models.CharField(max_length=255)
    rating = models.FloatField(default=1)
    a_var = models.CharField(max_length=255)
    b_var = models.CharField(max_length=255)
    c_var = models.CharField(max_length=255)
    d_var = models.CharField(max_length=255)
    correct_var = models.CharField(max_length=1)
    total_correct = models.FloatField(default=0)
    total_incorrect = models.FloatField(default=0)
    appear_counter = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    tag = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return '\n\t'.join([
            self.text,	    
            self.a_var,
            self.b_var,
            self.c_var,
            self.d_var,  
        ])

    def is_correct(self, answer):
        return answer.lower() == self.correct_var.lower()


class Answer(models.Model):
    answered_user = models.ForeignKey(User)
    asked_question = models.ForeignKey(Question)
    answer_choice = models.CharField(max_length=1)


class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    years_in_dota = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    photo_url = models.URLField(null=True, blank=True)
    photo = models.ImageField(upload_to=settings.PHOTO_DIR, default='{}/question.jpg'.format(settings.PHOTO_DIR))
    questions_answered = models.IntegerField(default=0)
    questions_proposed = models.IntegerField(default=0)

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username