from django.db import models


# Create your models here.
class Task(models.Model):

    template = "task.html"

    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return str(self.id) + "-" + self.title


class Department(models.Model):
    dept_name = models.CharField(max_length=50)

    def __str__(self):
        return self.dept_name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    join_year = models.IntegerField()
    department = models.ForeignKey(
        Department,
        related_name="employees",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
