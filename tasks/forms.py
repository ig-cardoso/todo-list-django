from django import forms

from .models import Task

'''
 Importa o model, pois vai ver o molde
 do formulário, assim é possível fazer com que 
 ele repeite todos os campos de models.
'''

class TaskForm(forms.ModelForm):

	# Metadados
	class Meta:
		model = Task
		fields = ('title', 'description', 'share', 'completion_date')
		# Campos que eu quero que apareca no front-end
