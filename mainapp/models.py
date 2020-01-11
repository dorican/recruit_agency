from django.db import models


class Planet(models.Model):
	name = models.CharField(verbose_name='Имя', max_length=32, blank=False, unique=True)
	
	def __str__(self):
		return f'{self.name}'
	
	class Meta:
		verbose_name = 'Планета'
		verbose_name_plural = 'Планеты'


class Sitkh(models.Model):
	name = models.CharField(verbose_name='Имя', max_length=32, blank=False, unique=True)
	teaching_planet = models.ForeignKey(Planet, on_delete=models.PROTECT, blank=True, null=True)
	number_pupils = models.PositiveSmallIntegerField(verbose_name='Количество учеников', default=0)
	
	def __str__(self):
		return f'{self.name}'
	
	class Meta:
		verbose_name = 'Ситх'
		verbose_name_plural = 'Ситхи'
	

class Recruit(models.Model):
	name = models.CharField(verbose_name='Имя', max_length=32, blank=False, unique=False)
	living_planet = models.ForeignKey(Planet, verbose_name='Планета обитания', on_delete=models.PROTECT)
	age = models.PositiveSmallIntegerField(verbose_name='Возраст', blank=False)
	email = models.EmailField(verbose_name='Email', max_length=254, blank=False)
	in_order = models.BooleanField(verbose_name='Состоит в ордене', default=False)
	
	def __str__(self):
		return f'{self.name}'
	
	class Meta:
		verbose_name = 'Рекрут'
		verbose_name_plural = 'Рекруты'
	
	@property
	def answers(self):
		return self.answer_set.all
	

class Question(models.Model):
	title = models.TextField(blank=True, null=True)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'

	@property
	def choices(self):
		return self.choice_set.all


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.CharField(blank=True, null=True, max_length=512)

	def __str__(self):
		return f'{self.text}'

	class Meta:
		verbose_name = 'Вариант ответа'
		verbose_name_plural = 'Варианты ответов'


class Answer(models.Model):
	recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
	choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.recruit.name}'

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'


class HandOfShadow(models.Model):
	recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, blank=True, null=True)
	sitkh = models.ForeignKey(Sitkh, on_delete=models.CASCADE)
