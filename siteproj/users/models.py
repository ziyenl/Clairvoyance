from django.db import models

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
		('B', 'Bisexual'),
		('G',  'Gay'),
		('L', 'Lesbian'),
    )
	
SMOKING = (
        ('N', 'Never'),
        ('O', 'Occasional'),
		('T', 'Trying to Quit'),
		('A',  'Always'),
    )

DRINKING = (
        ('N', 'Never'),
		('S', 'Social Drinker'),
		('T', 'Trying to Quit'),
		('A',  'Always'),
    )
	
class Login(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=20)

class Identification(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	nationality = models.CharField(max_length=30)
	ethnicity = models.CharField(max_length=30)
	spoken_language = models.CharField(max_length=30)
	residence = models.CharField(max_length=30)
	login = models.ForeignKey(Login, unique=True)
	
class Physical(models.Model):
	height = models.IntegerField()
	weight = models.IntegerField()
	login = models.ForeignKey(Login, unique=True)

class Hobby(models.Model): 
	description = models.CharField(max_length=30)

class Personality(models.Model): 
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	
class Test(models.Model):
	description =  models.CharField(max_length=30)
	
class Lifestyle(models.Model):
	smoking = models.CharField(max_length=1, choices=SMOKING)
	drinking = models.CharField(max_length=1, choices=DRINKING)
	night_owl = models.BooleanField()
	login = models.ForeignKey(Login, unique=True)
	hobby =  models.ManyToManyField(Hobby)
	personality = models.ManyToManyField(Personality)
	test = models.ForeignKey(Test)
	
