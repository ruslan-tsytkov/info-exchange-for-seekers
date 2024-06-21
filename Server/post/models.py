from django.db import models

from user.models import Employer


class Vacancy(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='vacancies')
    title = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    content = models.TextField()

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=100)
    content = models.TextField()