from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Task(models.Model):
	STATUS = (
		('fazendo', 'Fazendo'),
		('feito', 'Feito')
	)

	# Campos
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	done = models.CharField(
		max_length=7, # Tamanho da entrada
		choices=STATUS,
	)
	
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # Id do usuário
	# get_user_model() -> Atrela ao id do usuário
	# on_delete=models.CASCADE -> Quando o usuário for delato do sistema vai apagar todas as suas tarefas (atrelada ao seu id)


	share = models.CharField(blank=True, max_length=25)
	# Eu criei. blank=True permite que o campo fique em branco
	completion_date = models.DateField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)

	# Métodos
	def __str__(self):  # Para mostrar o nome das tarefas na área admin (Task Object)
		return self.title


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     name = models.CharField(max_length=150)
#     email = models.EmailField()
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'
