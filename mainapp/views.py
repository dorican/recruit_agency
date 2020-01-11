from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import *
from .models import *


def index(request):
	context = {
		'page_title': 'Рекрутинговое агентство Ордена Ситхов',
	}
	return render(request, 'mainapp/index.html', context)


def recruit_create(request):
	if request.method == 'POST':
		form = RecruitsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('mainapp:recruit_questions'))
	else:
		form = RecruitsForm()
	context = {
		'page_title': 'Создание рекрута',
		'form': form,
	}
	return render(request, 'mainapp/recruit_form.html', context)


def recruit_questions(request):
	recruit = Recruit.objects.all().order_by('-id')[0]
	questions = Question.objects.all().exclude(choice__answer__recruit=recruit)
	context = {
		'page_title': 'Список вопросов',
		'questions': questions,
		'recruit': recruit,
	}
	return render(request, 'mainapp/list_questions.html', context)


def choice_sitkh(request):
	if request.method == 'GET':
		sitkhs = Sitkh.objects.all()
		context = {
			'page_title': 'Выбор ситха',
			'sitkhs': sitkhs,
		}
		return render(request, 'mainapp/sitkh_form.html', context)
	if request.method == 'POST':
		recruits = Recruit.objects.exclude(in_order=True)
		context = {
			'page_title': 'Выбор падавана',
			'recruits': recruits,
			'sitkh': request.POST.get('sitkh'),
		}
		return render(request, 'mainapp/list_recruits.html', context)


def recruit_answers(request, pk, sitkh):
	recruit = Recruit.objects.get(id=pk)
	sitkh = Sitkh.objects.get(id=sitkh)
	questions = Question.objects.filter(choice__answer__recruit_id=pk)
	context = {
		'page_title': 'Данные падавана',
		'recruit': recruit,
		'sitkh': sitkh,
		'questions': questions,
	}
	return render(request, 'mainapp/answer_recruit_detail.html', context)


def question_detail(request, pk):
	if request.method == 'GET':
		question = Question.objects.get(id=pk)
		context = {
			'page_title': 'Список вопросов',
			'question': question,
		}
		return render(request, 'mainapp/question_detail.html', context)
	if request.method == 'POST':
		user = Recruit.objects.all().order_by('-id')[0]
		choice_obj = Choice.objects.get(id=request.POST.get('choice'))
		Answer.objects.create(recruit=user, choice=choice_obj)
		return HttpResponseRedirect(reverse('mainapp:recruit_questions'))


def add_recruit(request, pk, sitkh):
	if request.method == 'POST':
		id_sitkh = sitkh
		sitkh_obj = Sitkh.objects.get(id=sitkh)
		count_pupils = sitkh_obj.number_pupils
		if count_pupils < 3:
			recruit = Recruit.objects.get(id=pk)
			recruit.in_order = True
			recruit.save()
			group = HandOfShadow.objects.create(recruit_id=pk, sitkh_id=sitkh)
			group.save()
			messages.success(request, 'Вы успешно добавили себе ученика')
			subject = 'Зачисление в орден'
			message = f'Поздравляем, {recruit.name}! Вы зачислены в Орден Ситхов.'
			send_mail(subject, message, settings.EMAIL_HOST_USER, [recruit.email], fail_silently=False)
			count_pupils += 1
			sitkh_obj.number_pupils = count_pupils
			sitkh_obj.save()
			return redirect(f'/recruits/for/sitkh/{pk}/{id_sitkh}/')
		else:
			messages.error(request, 'Вы не можете иметь более трех учеников!')
			return redirect(f'/recruits/for/sitkh/{pk}/{id_sitkh}/')


def recruits_for_sitkh(request, pk, sitkh):
	recruits = Recruit.objects.exclude(in_order=True)
	context = {
		'page_title': 'Выбор падавана',
		'recruits': recruits,
		'sitkh': sitkh
	}
	return render(request, 'mainapp/list_recruits.html', context)


def list_of_sitkhs(request):
	all_sitkhs = Sitkh.objects.all()
	sitkhs_more_hands = Sitkh.objects.filter(number_pupils__gt=1)
	context = {
		'page_title': 'Список всех ситхов ордена',
		'all_sitkhs': all_sitkhs,
		'sitkhs_more_hands': sitkhs_more_hands,
	}
	return render(request, 'mainapp/list_sitkhs.html', context)