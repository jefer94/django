from django.db import models
# from .code import Code
# from .project_permission import ProjectPermission

class Project(models.Model):
    # blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # codes = models.ManyToManyField('Code')
    # collaborators = models.ManyToManyField('ProjectPermission')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_readonly_fields(self, request):
    #     return ['created_at', 'updated_at']
