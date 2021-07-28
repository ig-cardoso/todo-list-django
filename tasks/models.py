from django.db import models

# Create your models here.

class Task(models.Model):
	STATUS = (
		('fazendo', 'Fazendo'),
		('feiro', 'Feito')
	)

	# Campos
	title = models.CharField(max_length=255)
	description = models.TextField()
	done = models.CharField(
		max_length=7, # Tamanho da entrada
		choices=STATUS,
	)
	completion_date = models.DateField(auto_now_add=False)	# Eu criei
  
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	# Métodos
	def __str__(self):  # Para mostrar o nome das tarefas na área admin (Task Object)
		return self.title