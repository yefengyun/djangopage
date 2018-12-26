from django.db import models


# Create your models here.
class Student(models.Model):
    """学生表"""
    name = models.CharField(max_length=100)
    gender = models.SmallIntegerField()  # 性别

    class Meta:
        db_table = 'student'


class Course(models.Model):
    """课程表"""
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'course'


class Score(models.Model):
    """分数表"""
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    number = models.FloatField()

    class Meta:
        db_table = 'score'


class Teacher(models.Model):
    """老师表"""
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'


