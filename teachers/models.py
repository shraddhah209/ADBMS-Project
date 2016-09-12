from django.db import models

class student_labs(models.Model):
    student_name = models.CharField(max_length=60)
    Exp1 = models.IntegerField(max_length=3)
    Exp2 = models.IntegerField(max_length=3)
    Exp3 = models.IntegerField(max_length=3)
    Exp4 = models.IntegerField(max_length=3)
    Exp5 = models.IntegerField(max_length=3)
    Exp6 = models.IntegerField(max_length=3)
    Exp7 = models.IntegerField(max_length=3)
    Exp8 = models.IntegerField(max_length=3)
    Exp9 = models.IntegerField(max_length=3)
    Exp10 = models.IntegerField(max_length=3)
    avg = models.IntegerField(max_length=3)

