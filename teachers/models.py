from django.db import models

class Students(models.Model):

    student_roll = models.AutoField(primary_key=True, unique=True, editable=False)
    student_name = models.CharField(max_length=70)
    Exp1 = models.IntegerField(default=0)
    Exp2 = models.IntegerField(default=0)
    Exp3 = models.IntegerField(default=0)
    Exp4 = models.IntegerField(default=0)
    Exp5 = models.IntegerField(default=0)
    Exp6 = models.IntegerField(default=0)
    Exp7 = models.IntegerField(default=0)
    Exp8 = models.IntegerField(default=0)
    Exp9 = models.IntegerField(default=0)
    Exp10 = models.IntegerField(default=0)
    exp_avg = models.IntegerField(default=0)
    T1q1 = models.IntegerField(default=0)
    T1q2 = models.IntegerField(default=0)
    T1q3 = models.IntegerField(default=0)
    T1q4 = models.IntegerField(default=0)
    T1_total = models.IntegerField(default=0)
    T2q1 = models.IntegerField(default=0)
    T2q2 = models.IntegerField(default=0)
    T2q3 = models.IntegerField(default=0)
    T2q4 = models.IntegerField(default=0)
    T2_total = models.IntegerField(default=0)
    TT_avg = models.IntegerField(default=0)
    A1 = models.IntegerField(default=0)
    A2 = models.IntegerField(default=0)
    Ass_avg = models.IntegerField(default=0)
    attendance = models.IntegerField(default=0)
    final_marks = models.IntegerField(default=0)
    def __str__(self):
        return str(self.student_roll)+". "+self.student_name


