from django.contrib import admin
from .models import *


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
	list_display = ('name',)
	list_display_links = ('name',)


@admin.register(Sitkh)
class PlanetAdmin(admin.ModelAdmin):
	list_display = ('name', 'teaching_planet',)
	list_display_links = ('name',)


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'living_planet', 'email',)
	list_display_links = ('name',)


class ChoiqceInline(admin.TabularInline):
	model = Choice
	extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('id', 'title',)
	list_display_links = ('title',)
	inlines = [ChoiqceInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ('recruit', 'choice',)
	list_display_links = ('recruit',)


@admin.register(HandOfShadow)
class HandOfShadowAdmin(admin.ModelAdmin):
	list_display = ('recruit', 'sitkh',)
	list_display_links = ('recruit', 'sitkh',)