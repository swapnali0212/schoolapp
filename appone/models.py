from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfi(AbstractUser):
    user_type_data = ((1, "Student"), (2, "Teacher"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(UserProfi, on_delete = models.CASCADE)
    student_name = models.CharField('stud_name', max_length=100)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(UserProfi, on_delete = models.CASCADE)
    teacher_name = models.CharField('teacher_name', max_length=100)
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='teachers')

class Subject(models.Model):
    subject_name = models.CharField('subject_name', max_length=100)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='subjects')


@receiver(post_save, sender=UserProfi)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 1:
            Student.objects.create(admin=instance, student_name='' )
        if instance.user_type == 2:
            Teacher.objects.create(admin=instance, teacher_name='')


@receiver(post_save, sender=UserProfi)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.student.save()
    if instance.user_type == 2:
        instance.teacher.save()








