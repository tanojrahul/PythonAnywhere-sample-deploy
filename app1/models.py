from django.db import models

# class Student(models.Model):
#     student_id = models.CharField(max_length=10, unique=True)
#     name = models.CharField(max_length=100)
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=10)
#
#     def str(self):
#         return self.name


select_branch = [('cse', 'Computer Science and Engineering'), ('ece', 'Electronics and Communication Engineering'),('aids','Artificial Intelligence & Data Science')]
select_subject = [('pfsd', 'Professional Software Development'), ('mswd', 'Mobile Software Development')]
gender=[('male', 'Male'), ('female', 'Female')]


class Student(models.Model):
    sid = models.IntegerField()
    branch = models.CharField(max_length=10, choices=select_branch)
    subject = models.CharField(max_length=4, choices=select_subject)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=gender)

    def str(self):
        return f"Student ID: {self.sid}, Branch: {self.branch}, Subject: {self.subject}"