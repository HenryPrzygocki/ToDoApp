from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class ToDoList(models.Model):
    titulo = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('list', args=[self.id])

    def __str__(self):
        return self.titulo

class ToDoItem(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    feita = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('item-update', args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        if self.feita:
            return f"{self.titulo} (Completa)"
        return f"{self.titulo} (Adicionada em: {self.data_criacao})"

    class Meta:
        ordering = ['data_criacao']

