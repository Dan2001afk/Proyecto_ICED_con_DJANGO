from django.http import HttpResponseBadRequest, JsonResponse
from .forms import *
from django.views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json
from .models import *
from django.shortcuts import *
from .formsUsuario import *
from django.contrib.auth.decorators import *
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login



def verificarS(request):
    if request.user.is_authenticated:
        # El usuario tiene una sesión iniciada
        print("se inicio la sesion")
        return JsonResponse({'mensaje': True})
    else:
        # El usuario no tiene una sesión iniciada
        print("no se inicio la sesion")
        return JsonResponse({'mensaje': False})




class RegistrarUsuarioView(View):
    template_name = 'formulario.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        form = UserForm()  # Definir form con un valor predeterminado
        if request.method == 'POST':
            print("en el metodod")
            #if request.headers.get('content-type') == 'application/json':
            if 'application/json' in request.headers.get('content-type', ''):
                print("en el json")
                self.handle_flutter_data(request)
            else:
                print("no json")
                print(form.is_valid())
                form = UserForm(request.POST)
                
                if form.is_valid():
                    print("iiiii")
                    if form.cleaned_data['imagen'] or form.cleaned_data['imagen'] is None:
                        print('eeeeeee')
                        form.save()
                        imagen_file = request.FILES['imagen']
                        user_instance = form.save(commit=False)
                        user_instance.imagen = imagen_file
                        user_instance.save()
                    
                    messages.success(request, 'Usuario registrado correctamente desde formulario HTML.')
                    return redirect('iniciar_sesion')
                else:
                    print('EEEEEEEEEEE',form.errors)
                    messages.error(request, 'Error al registrar el usuario desde formulario HTML.')
        else:
            print("no metodo")
            form = UserForm()
        return render(request, self.template_name, {'form': form})

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def handle_flutter_data(self, request):
        try:
            data = json.loads(request.body)
            print("Datos recibidos desde Flutter:")
            print(data)  # Imprime los datos recibidos desde Flutter
            form = UserForm(data)
            if form.is_valid():
                print("Datos válidos:")
                print(form.cleaned_data)  # Imprime los datos validados por el formulario
                form.save()
                messages.success(request, 'Usuario registrado correctamente desde Flutter.')
            else:
                print("Errores en el formulario:")
                print(form.errors)  # Imprime los errores de validación del formulario
        except json.JSONDecodeError:
            messages.error(request, 'Error en los datos enviados desde Flutter.')
    

class IniciarSesionView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'Inicio.html', {'form': form})

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "get":
            print("entro a la vista de iniciar sesion2")
            return self.get(request, *args, **kwargs)
        elif request.method.lower() == "post":
            print("entro a la vista de iniciar sesion3")
            return self.post(request, *args, **kwargs)

    def post(self, request):
        accept_header = request.META.get('HTTP_ACCEPT', '')
        if 'application/json' in accept_header:
            try:
                json_data = json.loads(request.body)
                username = json_data.get('username')
                password = json_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    print("json validacion")
                    login(request, user)
                    print("entro")
                    return JsonResponse({'mensaje': "inicio de sesion exitoso"})
                else:
                    return JsonResponse({'mensaje': "No se inicio la sesion "})
            except json.JSONDecodeError:
                return HttpResponseBadRequest('Invalid JSON data')

        else:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    if user.rol in ['Aprendiz', 'aprendiz', 'Instructor', 'instructor']:
                        print("entro al rol")
                        return redirect('perfil_usuario')
                    else:
                        print("no entra")
                        return redirect('Equipo')
                # Si la validación del formulario falla, el formulario con errores se pasará al contexto
                return render(request, 'Inicio.html', {'form': form})


@method_decorator(login_required(login_url='iniciar_sesion'), name='dispatch')
class PerfilClienteView(View):
    template_name = 'ActualizarUsuario.html'

    def get(self, request):
        try:
            
            #print("ssssssssssssssss",request.user.documento_id)
            usuario = Usuarios.objects.get(Usu_Documento=request.user.Documento_id)
            userr=request.user
            print(userr.imagen)
            #print("Datos del cliente:", cliente.documento, cliente.nombre, cliente.apellido, cliente.correo, cliente.celular)
        except Usuarios.DoesNotExist:
            messages.error(request, 'No se encontraron los datos del cliente.')
            return redirect('iniciar_sesion')

        form = UsuariosForm(instance=usuario)
       # print("aaaaaaaaaaa",form.nombre)
        return render(request, self.template_name, {'form': form, 'usuario': usuario,'user':userr})

    def post(self, request):
        try:
            usuario = Usuarios.objects.get(Usu_Documento=request.user.Documento_id)
        except Usuarios.DoesNotExist:
            messages.error(request, 'No se encontraron los datos del cliente.')
            return redirect('iniciar_sesion')

        form = UsuariosForm(request.POST, instance=usuario)

        if form.is_valid():
            form.save()

            messages.success(request, 'Cambios guardados correctamente.')
            return redirect('perfil_usuario')

        return render(request, self.template_name, {'form': form, 'usuario': usuario})

    
def frmcliente(request):
     return render(request,"ActualizarUsuario.html")


