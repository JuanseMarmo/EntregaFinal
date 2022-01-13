from django.db.models import fields
from django.shortcuts import render
from django.http import HttpResponse




from AppCoder.models import Vender, Busqueda , Moto , Auto , Camion 

from AppCoder.forms import VenderFormulario , MotoFormulario , CamionFormulario , UserRegisterForm , UserEditForm




#PARA LOGIN
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout , authenticate

from django.contrib.auth.password_validation import password_changed
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView













# Create your views here.

#Vistas

def inicio(request):

    # return HttpResponse("Inicio del proyecto")
    return render(request, 'AppCoder/inicio.html')


def vehiculos(request):
    
    return render(request, 'AppCoder/vehiculos.html')


def inmaculados(request):

    return render(request, 'AppCoder/inmaculados.html')

def ofertas(request):

    return render(request, 'AppCoder/ofertas.html')

def aboutme(request):

    return render(request, 'AppCoder/aboutme.html')

@login_required   
def vender(request):

    if request.method == "POST":

        VFormulario = VenderFormulario(request.POST)

        if VFormulario.is_valid():

            informacion =VFormulario.cleaned_data

            venderalgo = Vender(marca=informacion["marca"] , modelo=informacion["modelo"], anio=informacion["anio"]) #VA EN MAYUSCULA LPM
        

            venderalgo.save()  #Se guarda en la base de datos

            return render(request, 'AppCoder/inicio.html') 

    else:

        VFormulario = VenderFormulario()



    return render(request, 'AppCoder/vender.html' , {"VFormulario" : VFormulario})

#Boton de busqueda

def busquedaAuto(request):

    return render(request, 'AppCoder/busquedaAuto.html')

def buscar(request):

    if request.GET["marca"]:

        marca = request.GET["marca"]

        autos = Auto.objects.filter(marca__icontains=marca)


        return render(request, "AppCoder/resultadosBusqueda.html", {"autos": autos, "marca": marca})


    else: 

        respuesta = "No enviaste datos"

        
# respueta = f"Estamos buscando : { request.GET ['marca'] }"

    return HttpResponse(request)


@login_required
def motoFormulario(request):

    if request.method == "POST":

        miMoto = MotoFormulario(request.POST)

        if miMoto.is_valid():

            informacion = miMoto.cleaned_data

            Mot = Moto(marca=informacion["marca"] , modelo=informacion["modelo"], anio=informacion["anio"]) 
        

            Mot.save()  #Se guarda en la base de datos

            return render(request, 'AppCoder/inicio.html')

    else:

        miMoto = MotoFormulario()

    return render(request , 'AppCoder/motoFormulario.html' , {"miMoto" : miMoto} )
    
    # render(request, 'AppCoder/motoFormulario.html' , {"miMoto" = miMoto} )

#FUNCIONES DE CAMIONES
@login_required
def leerCamiones(request):
    
    camiones = Camion.objects.all()
    
    dir = {"camiones": camiones}  #Contexto

    return render(request, "AppCoder/leerCamiones.html" , dir)

@login_required
def camionFormulario(request):

    if request.method == "POST":

        miCamion = CamionFormulario(request.POST)

        if miCamion.is_valid():

            informacion = miCamion.cleaned_data

            Cam = Camion(marca=informacion["marca"] , modelo=informacion["modelo"], anio=informacion["anio"]) 
        

            Cam.save()  #Se guarda en la base de datos

            return render(request, 'AppCoder/inicio.html')

    else:

        miCamion = CamionFormulario()

    return render(request , 'AppCoder/camionFormulario.html' , {"miCamion" : miCamion} )



def eliminarCamion(request, modelo_para_borrar):

    camionABorrar = Camion.objects.get(modelo = modelo_para_borrar)
    camionABorrar.delete()

    camiones = Camion.objects.all()

    return render(request, "AppCoder/leerCamiones.html", {"camiones" : camiones} )


def editarCamion(request, modelo_para_editar):  #recibe por parametro un numero para editar

    camion = Camion.objects.get(modelo=modelo_para_editar)  #modelo_para_editar tiene que coicidir con la url de editar

    if request.method == "POST":

        miCamion = CamionFormulario(request.POST)

        if miCamion.is_valid():

            informacion = miCamion.cleaned_data

            
            
            #ID
            camion.marca=informacion["marca"]
            camion.modelo=informacion["modelo"]
            camion.anio=informacion["anio"]

            
        
            camion.save()  #Se guarda en la base de datos

            return render(request, 'AppCoder/inicio.html' )

    else:

        miCamion = CamionFormulario(initial={"marca":camion.marca,"modelo":camion.modelo,"anio" :camion.anio})

    return render(request,'AppCoder/editarCamion.html',{"miCamion":miCamion,"modelo_para_editar":modelo_para_editar})





#Leer
class MotoList(ListView):

    model = Moto
    template_name = "AppCoder/moto_list.html"

#Detalle
class MotoDetalle(DetailView):

    model = Moto
    template_name = "AppCoder/moto_detalle.html"


#Crear
class MotoCreacion(CreateView):

    model = Moto
    success_url = "../moto/list"
    fields = ["marca" , "modelo" , "anio"]

#Modificar
class MotoUpdate(UpdateView):

    model = Moto
    success_url = "../moto/list"
    fields = ["marca" , "modelo" , "anio"]

#Borrar
class MotoDelete(DeleteView ):

    model = Moto
    success_url = "../moto/list"

# class Meta:
#     model = User
#     fields = [ 'email', 'password1', ' password2'] 
        





#LOGIN

def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido estimado, {usuario}!"})
                
            else:
                
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Datos erroneos:(!"})
                
            
        else:
            
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Formulario Invalido"})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppCoder/login.html", {"form":form} )


def register(request):

        if request.method == 'POST':

            # form = UserCreationForm(request.POST)
            
            form = UserRegisterForm(request.POST)
            
            if form.is_valid():

                    username = form.cleaned_data['username']

                    form.save()

                    return render(request,"AppCoder/inicio.html" ,  {"mensaje":f"{username} Usuario creado satisfactoriamente"})


        else:
            # form = UserCreationForm()     
            
        
            form = UserRegisterForm()     

        return render(request,"AppCoder/register.html" ,  {"form":form})

@login_required
def editarPerfil(request):
    
    
    usuario = request.user
    
    if request.method == 'POST':
        
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']
            usuario.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
        
    return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})







