from django.urls import path
from AppCoder import views

#LOGOUT
from django.contrib.auth.views import LogoutView

urlpatterns = [



    path('inicio', views.inicio, name="Inicio"),
    path('vehiculos', views.vehiculos, name="Vehiculos"),
    path('inmaculados', views.inmaculados , name="Inmaculados" ),
    path('ofertas', views.ofertas , name="Ofertas"),
    path('vender', views.vender , name="Vender"),
    path('aboutme', views.aboutme , name="Aboutme"),
    
    
    path('busquedaAuto', views.busquedaAuto , name="BusquedaAuto"),
    path('buscar/', views.buscar , name="Buscar"),
    path('motoFormulario/' , views.motoFormulario , name="MotoFormulario" ),
    #CAMIONES
    path('leerCamiones' , views.leerCamiones, name = "LeerCamiones"),
    path('camionFormulario/' , views.camionFormulario , name="CamionFormulario" ),
    path('eliminarCamion/<modelo_para_borrar>/' , views.eliminarCamion , name="EliminarCamion" ),
    path('editarCamion/<modelo_para_editar>/' , views.editarCamion , name="EditarCamion" ),
    

    #Vistas en base a Django

    path('moto/list', views.MotoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.MotoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.MotoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.MotoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.MotoDelete.as_view(), name='Delete'),
    
    
    #LOGIN
    path('login', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name="Logout"),
    
    
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    
    # path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),


]