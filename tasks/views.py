from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages


from .forms import TaskForm
from .models import Task

# Create your views here.

# Funções relacionadas as URL's

def taskList(request):		#   order_by: ordena por data de criação do mais novo para mais antigo 
	tasks = Task.objects.all().order_by('-created_at') # Vou pegar todos os objetos de task do banco de dados
	return render(request, 'tasks/list.html', {'tasks':tasks})	# render: "renderiza"  a página


def taskView(request, id):
	task = get_object_or_404(Task, pk=id)
	return render(request, 'tasks/task.html', {'task':task})
											#		'-> Argumento enviado para p front-end		


def newTask(request):
	# Dispor e tratar formulário
	if request.method == 'POST': # Se for POST vai fazer inserção
		form = TaskForm(request.POST) # Passa request.POST para preencher o formulário

		if form.is_valid(): # Se o formulário for válido
			task = form.save(commit=False) # Com o commit=False ele vai parar o processo save e esperar até salvar
			task.done = 'fazendo'
			task.save()

			return redirect('/') # Volta para home, se não voltaria para msm url

	else: # Senão vai mostrar o formulário
		form = TaskForm()	# Chama o formulário. Lembrandoq em TaskForm temos Metadados
		return render(request, 'tasks/addtask.html', {'form':form})


def editTasks(request, id):
	# O id vem do parametro da url para poder achar a task
	task = get_object_or_404(Task, pk=id)
						#	(model, primary_key)
	form = TaskForm(instance=task) # Para puxar o formulário. No instance=task deixar o form prepopulado

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task) # instance=task para saber qual form está sendo alterado

		if form.is_valid(): # Se o formulário for válido	
			task.save()
			return redirect('/')
		else:
			return render(request, 'tasks/edittask.html', {'form':form, 'task':task})	# Volta para mesma página, em caso de erro
	else:
		return render(request, 'tasks/edittask.html', {'form':form, 'task':task})


def deleteTasks(request, id):
	task = get_object_or_404(Task, pk=id)
	task.delete()
	
	messages.info(request, 'Tarefa deletada com sucesso!')

	return redirect('/')



def helloWorld(request):
	return HttpResponse('Hello World')


def yourName(request, name):
	return render(request, 'tasks/yourname.html', {'name':name})

