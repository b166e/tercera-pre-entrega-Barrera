from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cursos/', views.cursos, name="Cursos"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),
    path('buscar/', views.buscar),
    path('leerProfesores/', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<str:profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<str:profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
    path('curso/list/', views.CursoList.as_view(), name='List'),
    path('curso/<int:pk>/', views.CursoDetalle.as_view(), name='Detail'),
    path('curso/nuevo/', views.CursoCreacion.as_view(), name='New'),
    path('curso/editar/<int:pk>/', views.CursoUpdate.as_view(), name='Edit'),
    path('curso/borrar/<int:pk>/', views.CursoDelete.as_view(), name='Delete'),
    
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('agregarAvatar/', views.agregarAvatar, name="AgregarAvatar"),
]
