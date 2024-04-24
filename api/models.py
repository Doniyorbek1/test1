from django.db import models

# Create your models here.
class User(models.Model):
    Age_labe_choices = (
        ('12-15', '12-15'),
        ('16-19', '16-19'),
        ('20 va undan yuqori', '20 va undan yuqori'),
    )
    
    first_name =models.CharField(max_length=120, blank=False)
    last_name =models.CharField(max_length=120, blank=False)
    login = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    age_label = models.CharField(max_length=50, choices=Age_labe_choices)
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    
# create test model
class Test(models.Model):

    # quetion_type  choices 
    Question_choices = (
        ('Elementary', 'Elementary'),
        ('Arifmetik', 'Arifmetik'),
        ('Professional', 'Professional'),
    )

    # quetion_label equel user's age_label
    question_label = models.ManyToManyField(User)
    question_type = models.CharField(max_length=50, choices=Question_choices)

# create result class 
class Result(models.Model):
    result_label = models.ManyToManyField(User)
    result_value = models.IntegerField()
    start_time = models.DateTimeField(auto_now_add=True, null=False)
    end_time = models.DateTimeField(auto_now_add=True, null=False)
    
    
    
