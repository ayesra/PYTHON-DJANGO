from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY=(
        (1,"High"),
        (2,"Medium"),
        (3,"Low")
    )
    task=models.CharField(max_length=20)
    description=models.TextField(null=True)
    priority=models.IntegerField(choices=PRIORITY,default=2)
    created_date=models.DateTimeField(auto_now_add=True,null=True)
    updated_date=models.DateTimeField(auto_now=True,null=True)
    is_done=models.BooleanField(default=False,null=True)

    def __str__(self):
        return  f"{self.priority} - {self.task} -{self.created_date}"
    
    class Meta:
        ordering=["priority"]









