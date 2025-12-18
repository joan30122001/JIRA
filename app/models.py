from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    STATUS_CHOICES = [
        ('not tested', 'Non testé'),
        ('correct', 'Correct'),
        ('incorrect', 'Incorrect'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not tested')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
