from django.db import models

class Reg(models.Model):
          Student_name=models.CharField(max_length=20)
          Student_roll=models.IntegerField()
          student_marks=models.FloatField()
