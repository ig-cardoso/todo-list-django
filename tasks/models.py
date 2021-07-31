from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
	STATUS = (
		('fazendo', 'Fazendo'),
		('feiro', 'Feito')
	)

	# Campos
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	done = models.CharField(
		max_length=7, # Tamanho da entrada
		choices=STATUS,
	)
	#user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # Id do usuário
	# get_user_model() -> Atrela ao id do usuário
	# on_delete=models.CASCADE -> Quando o usuário for delato do sistema vai apagar todas as suas tarefas (atrelada ao seu id)

	completion_date = models.DateField(auto_now_add=False)  # Eu criei. blank=True permite que o campo fique em branco
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	# Métodos
	def __str__(self):  # Para mostrar o nome das tarefas na área admin (Task Object)
		return self.title
