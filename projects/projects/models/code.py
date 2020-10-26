from django.db import models
# from .project import Project

class Code(models.Model):
    title = models.CharField(max_length=50)
    code = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def get_readonly_fields(self, request):
    #     return ['created_at', 'updated_at']
