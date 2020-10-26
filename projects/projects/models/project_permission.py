from django.db import models
# from .project import Project

class ProjectPermission(models.Model):
    write = models.BooleanField()
    create = models.BooleanField()
    delete = models.BooleanField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
