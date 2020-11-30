from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appone.models import UserProfi, Student, Teacher, Subject
# Register your models here.

# Register your models here.
admin.site.register(UserProfi)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Subject)

