from django.urls import path

from . import views

urlpatterns = [
    path('helloWorld', views.helloWorld), # A função views.helloWorld foi importada de views
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newtask/', views.newTask, name='new-task'),
    path('edit/<int:id>', views.editTasks, name='edit-task'),
    path('delete/<int:id>', views.deleteTasks, name='delete-task'),
    path('changestatus/<int:id>', views.changestatus, name='change-status'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
    path('perfil/', views.perfil, name='perfil'),


    # Reset password
    path('password-reset/', views.PasswordResetView.as_view(
        template_name='registration/reset-password.html'), name='password-reset'),
    # path('password-reset/done', views.PasswordResetDoneView.as_view(
    #     template_name='registration/reset-password_done.html'), name='password-reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(
    #     template_name='registration/reset-password_confirm.html'), name='password-reset_confirm'),
    # path('password-reset-complete', views.PasswordResetCompleteView.as_view(
    #     template_name='registration/reset-password_complete.html'), name='password-reset_complete')
]
