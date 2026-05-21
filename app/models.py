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



class AsanaProject(models.Model):
    gid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255, blank=True)
    permalink_url = models.URLField(blank=True)
    workspace_name = models.CharField(max_length=255, blank=True)
    team_name = models.CharField(max_length=255, blank=True)
    archived = models.BooleanField(default=False)
    privacy_setting = models.CharField(max_length=50, blank=True)
    synced_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-synced_at", "name"]

    def __str__(self):
        return f"{self.name} ({self.gid})"