from django.contrib.auth.decorators import login_required
from questions.models import Question, Answer, Profile
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView, DetailView
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, render_to_response
from forms import *
from random import random
from users.views import loginza_login_required


def index(request):
    template = loader.get_template('home.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


class ListQuestionView(ListView):
    model = Question
    template_name = 'question_list.html'


class AskQuestionView(ListView):
    model = Question
    template_name = 'question_ask.html'


class QuestionDetails(DetailView):
    model = Question
    template_name = 'question_details.html'


@login_required(login_url='/users/login')
def ask_question_view(request, pk=None):
    user_answers = Answer.objects.filter(answered_user=request.user)
    questions_to_exclude = [user_answer.asked_question for user_answer in user_answers]
    if pk:
        question = get_object_or_404(Question, pk=pk)
    else:
        questions = Question.objects.all()
        for q in questions_to_exclude:
            questions = questions.exclude(text=q.text)
        try:
            question = questions.order_by('?')[0]
        except IndexError:
            return HttpResponseRedirect(reverse('index'))
    choices = [('a', question.a_var), ('b', question.b_var), ('c', question.c_var), ('d', question.d_var)]
    if request.method == 'GET':
        form = QuestionForm(choices)
        return render_to_response('question_ask.html', {'form': form, 'question': question}, RequestContext(request))
    else:
        form = QuestionForm(choices, data=request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user)
            user_answer = Answer()
            # answer
            selected_choice = form.cleaned_data['answer']
            user_answer.answer_choice = selected_choice
            user_answer.answered_user = request.user
            user_answer.asked_question = question
            user_answer.save()
            # question
            if question.is_correct(selected_choice):
                profile.rating += question.rating
                question.total_correct += 1
            else:
                question.total_incorrect += 1
                profile.rating -= question.rating
            question.rating = 1 + (question.total_incorrect/(question.total_correct+1))
            question.appear_counter += 1
            question.save()
            # profile
            profile.questions_answered += 1
            profile.save()
            return HttpResponseRedirect(reverse('questions-ask'))
        else:
            # error_message = form.errors['answer']
            question_id = question.id
            url = reverse('questions-ask', kwargs={'pk': question_id})
            return HttpResponseRedirect(url)
            # 'error_message': error_message })
