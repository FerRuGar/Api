from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render, redirect
# from django.contrib.auth import acceso
from django.views import *

class Acceso(APIView):
    template_name="acceso.html"
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return redirect('galeria')

class Inicio(APIView):
    template_name="Inicio.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Carrito(APIView):
    template_name="carrito.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Forms(APIView):
    template_name="forms.html"
    def get(self, request):
        return render(request, self.template_name)

class Ubicacion(APIView):
    template_name="ubicacion.html"
    def get(self, request):
        return render(request, self.template_name)

class Tables(APIView):
    template_name="tables.html"
    def get(self, request):
        return render(request, self.template_name)
    
class Galeria(APIView):
    template_name="galeria.html"
    def get(self, request):
        return render(request, self.template_name)

class Completo(APIView):
    template_name="complete.html"
    def get(self, request):
        return render(request, self.template_name)

# class Registro(HttpRequest):
#     def index(request):
#         Usuario = Registro_Form
#         return render(request, "registro.html", {"form":Usuario})
#     def procesar_formulario(request):
#         Usuario = Registro_Form(request.POST)
#         if Usuario.is_valid():
#             Usuario.save()
#             Usuario = Registro_Form()
#         return render(request, "acceso.html", {"form":Usuario, "mensaje":"OK"})

# def registro(request):
#     if request.method == 'POST':
#         form = registros(request.POST)
#         if form.is_valid():
#             form.save()
#             send_mail(
#             'Bienvenido',    # Asunto del correo
#             'Felicidades su registro ha sido exitoso',    # Cuerpo del correo
#             'f2417881@gmail.com',   # Dirección de correo remitente
#             [request.POST['email']],  # Lista de direcciones de correo de destinatarios
#             fail_silently=False,     # Si se establece en True, los errores en el envío de correo no generarán una excepción
#             )
            
#             return redirect('acceso')   
#     else: 
#         form = registros()
        
#     context = { 'form' : form}
#     return render(request, 'registro.html', context)