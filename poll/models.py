from django.db import models

class Poll(models.Model):
	title = models.CharField(max_length=100)
	option1 = models.CharField(max_length=20)
	option2 = models.CharField(max_length=20)
	option3 = models.CharField(max_length=20)
	count1 = models.PositiveSmallIntegerField(default='0')
	count2 = models.PositiveSmallIntegerField(default='0')
	count3 = models.PositiveSmallIntegerField(default='0')

	def save(self):
		super(Poll , self).save()

	def __str__(self):
		return self.title

