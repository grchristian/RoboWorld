from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from json import loads, dumps
from . models import Reto
from . models import * 
from random import randrange
import psycopg2
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

#------------------------------------------------------- FINALES FUNCIONANDO -------------------------------------------------------#
#------------------------ ENVÍA A INDEX ------------------------#
def inicio(request):
    return render(request, "roboworld_app/index.html")

#----------------------- ENVÍA AL JUEGO -----------------------#
def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")

#-------------- ENVÍA A MI CUENTA / INCIAR SESIÓN --------------#
@login_required
def cuenta_usuario(request):
    usuario = request.user # asigna a "usuario" el usuario loggeado
    resultados = Reto.objects.filter(id_de_usuario_id=usuario)
    minutos_info = resultados[0].minutos_jugados
    veces_info = resultados[0].repeticion_niveles
    engranes_info = resultados[0].engranes
    return render(request, 'roboworld_app/cuenta_usuario.html', {"engranes_info":engranes_info,"veces_info":veces_info,"minutos_info":minutos_info})

#------------------ REGISTRAR NUEVO USUARIO ------------------#
def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            messages.success(request, 'done')
            new_user = f.save()

            #para que se loggee automaticamente despues de crear cuenta
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
            #Crea un registro en RETO con el usuario creado
            Reto.objects.create(id_de_usuario_id=request.user.id,minutos_jugados="0",minimo="0",maximo="0",repeticion_niveles="0",engranes="0",duracion_promedio="0",success_promedio="0",a_que_nivel_llego="0",sesion_iniciada_dia="0",sesion_iniciada_mes="0")


            '''
            Perfil.objects.create(id_de_usuario_id=request.user.id,genero="i",birth_date="13/04/2000")
            '''


            return render(request, "roboworld_app/index.html")
    else:
        f = CustomUserCreationForm()
        fp = PerfilForm()
    return render(request, 'roboworld_app/register.html', {'form':f,'formdatos':fp})

#------------------------------------------------------- FINALES FUNCIONANDO -------------------------------------------------------#



#funciona pero hay que darle mas formato
def grafica1(request):
    data = [['Nombre', 'Engranes recolectados']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.engranes
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Engranes recolectados'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/grafica1.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})


def grafica2(request):
    data = [['Nombre', 'Minutos jugados']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.minutos_jugados
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Minutos jugados'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/grafica2.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})


def graficaExito(request):
    data = [['Nombre', 'Promedio de exito']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.success_promedio
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Promedio de éxito de jugadores'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/graficaExito.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})


def graficaMinimo(request):
    data = [['Nombre', 'Minimo tiempo']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.minimo
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Minimo de tiempo por jugador'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/graficaMinimo.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})

def graficaMaximo(request):
    data = [['Nombre', 'Maximo tiempo']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.maximo
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Maximo de tiempo por jugador'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/graficaMaximo.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})

def graficaNiveLlego(request):
    data = [['Nombre', 'Nivel al que llegó']]

    resultados = Reto.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.a_que_nivel_llego
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Nivel al que llegó cada jugador'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/graficaNivelLlego.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})

def graficaGenero(request):
    data = [['Nombre', 'Genero de los jugadores']]

    resultados = Perfil.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.genero
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Genero de los jugadores'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/graficaGenero.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})
'''
def graficaTop5(request):
    data = [['Nombre', 'Maximo tiempo']]

    data.addColumn('string', 'Name');
        data.addColumn('number', 'Salary');
        data.addColumn('boolean', 'Full Time Employee');
        data.addRows([
          ['Mike',  {v: 10000, f: '$10,000'}, true],
          ['Jim',   {v:8000,   f: '$8,000'},  false],
          ['Alice', {v: 12500, f: '$12,500'}, true],
          ['Bob',   {v: 7000,  f: '$7,000'},  true]
        ]);
    
    resultados = recompensas.objects.all()

    for i in resultados:
        x = i.id_de_usuario_id
        y = i.maximo
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Maximo de tiempo por jugador'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    
    return render(request,'roboworld_app/graficas/graficaTop5.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})
'''
#-----------------------------------------------------------Conexiones----------------------------------#

def proceso(request):
    nombre = request.POST['nombre']
    nombre=nombre.upper()
    
    return render(request, "proceso.html", {"nombre":nombre}) 

@login_required
def datos(request):
    jugadores = Reto.objects.all() #select * from Reto;
    return render(request, 'datos.html', {'lista_jugadores':jugadores})

@login_required
def score(request):
    usuario = request.user
    resultados = Reto.objects.filter(nombre=usuario)
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
    return render(request, 'score.html', {"nombreUsuario":nombre,"score":score})

@csrf_exempt
def unity(request):
    nombre = "Martin"
    score = "1234"
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)


'''
@csrf_exempt

def micuenta(request):
    session={
    num_engranes = "43"
    min_jugados = "53"
    veces_jugadas = "5"
    }
    return JsonResponse(session)
'''
@csrf_exempt

def buscaJugadorBody(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    resultados = Reto.objects.filter(nombre=jugador_nombre)  #select * from Reto where nombre = jugador_nombre
    
    nombre = resultados[0].nombre
    score = resultados[0].minutos_jugados
   
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

@csrf_exempt
def ejemploSQL(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    jugador_nombre = body_json['usuario']
    nombre = ""
    score = ""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_reto;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == jugador_nombre:
                nombre = row[1]
                score = row[2]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"nombreUsuario":nombre,
        "score":score}
    return JsonResponse(retorno)

'''
@csrf_exempt
def Level(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    numero_nivel = body_json['nivel']
    level_number = numero_nivel
    enemigo = ""
    dificultad = ""
    duracion_individual=""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_level;")
        rows = cursor.fetchall()
        for row in rows:
            print("resulyados")
            if row[1] == numero_nivel:
                level_number = row[1]
                enemigo = row[2]
                dificultad = row[3]
                duracion_individual=row[4]
                print(row)
                print(level_number, enemigo,dificultad,duracion_individual) 
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
        
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    #print(level_number, enemigo,dificultad,duracion_individual)      
    retorno = {"level_number":level_number,
         "enemigo":enemigo,
         "dificultad":dificultad,
         "duracion_individual": duracion_individual}
    return JsonResponse(retorno)



@csrf_exempt
def engranes(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    sesionObtenida = body_json['sesion']
    sessionObtained= ""
    numero = ""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_engranes;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == sesionObtenida:
                sessionObtained = row[1]
                numero = row[2]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("Pihohbb")
    retorno = {"sessionObtained":sessionObtained,
         "numero":numero}
    return JsonResponse(retorno)


@csrf_exempt
def sesion(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    empezo = body_json['start']
    started = ""
    ended = ""
 

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_sesion;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == empezo:
                started = row[1]
                ended = row[2]
            print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
    retorno = {"started":started,
         "ended":ended}
    return JsonResponse(retorno)


@csrf_exempt
def recompensas(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    engranes_need= body_json['recompensas']
   
    engranes_necesarios = ""
    top_score_global = ""
    top_five=""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_recompensas;")
        rows = cursor.fetchall()
        for row in rows:
            #print ("resultados")
            print(row [1], engranes_need)
            if row[1] == engranes_need:
                engranes_necesarios = row[1]
                top_score_global = row[2]
                top_five = row[3]
              
            #print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
        retorno = {"engranes_necesarios":engranes_necesarios,
         "top_score_global":top_score_global,
         "top_five":top_five,
        }
    return JsonResponse(retorno)



@csrf_exempt
def prueba(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    sesion_id= body_json['sesion']
    sessionID = ""
    success = ""

    try:
        connection = psycopg2.connect(
            user = "admin",
            password = "adminpass",
            host = "localhost",
            port = "5432",
            database = "dataroboworld"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM roboworld_app_prueba;")
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == sesion_id:
                sessionID = row[1]
                success = row[2]
                print(row)
    
    except(Exception, psycopg2.Error) as error:
        print('Error connecting to PostgreSQL database', error)
        connection = None
    
    finally:
        if(connection != None):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is now closed")
        retorno = {"sessionID ":sessionID ,
        "success":success}
    return JsonResponse(retorno)
'''
#---------------------------------- Conexiones Finales------------------------------#

@csrf_exempt
def numero_de_level(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    Numero_nivel = body_json['nivel']
    resultados = Level.objects.filter(level_number=Numero_nivel)  #select * from Reto where nombre = jugador_nombre
    level_number = resultados[0].level_number
    enemigo = resultados[0].enemigo
    dificultad = resultados[0].dificultad
    duracion_indivudual = resultados[0].duracion_indivudual
    retorno = {"numero d enivel":level_number,
        "enemigo":enemigo,
        "dificultad": dificultad,
        "duracion individual": duracion_indivudual}
    return JsonResponse(retorno)

@csrf_exempt
def numero_de_engranes(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    engranes_num = body_json['engranes']
    resultados = Engranes.objects.filter(sessionObtained=engranes_num)
    sessionObtained= resultados[0].sessionObtained
    id_de_usuario= resultados[0].id_de_usuario
    number = resultados[0].number
    
    retorno = {"sesion Obtenida":sessionObtained,
        "id_de_usuario":id_de_usuario,
        "numero":number}
    return JsonResponse(retorno)


@csrf_exempt
def num_de_sesion(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    sesion_num = body_json['empezar']
    resultados = Sesion.objects.filter(started=sesion_num)  #select * from Reto where nombre = jugador_nombre
    started= resultados[0].started
    ended = resultados[0].ended
    
    retorno = {"started":started,
        "ended":ended}
    return JsonResponse(retorno)


@csrf_exempt
def num_de_recompensas(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    recompensas_num = body_json['recompensa']
    resultados = Recompensas.objects.filter(engranes_necesarios=recompensas_num)  #select * from Reto where nombre = jugador_nombre
    engranes_necesarios= resultados[0].engranes_necesarios
    top_score_global = resultados[0].top_score_global
    top_five = resultados[0].top_five
    
    retorno = {"engranes_necesarios":engranes_necesarios,
        "top_score_global":top_score_global,
        "top_five ":top_five}
    return JsonResponse(retorno)

@csrf_exempt
def num_de_pruebas(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    prueba_num = body_json['prueba']
    resultados = Prueba.objects.filter(SesionID=prueba_num)  #select * from Reto where nombre = jugador_nombre
    SesionID= resultados[0].SesionID
    success= resultados[0].success
    
    
    retorno = {"success":success,
        "SesionID":SesionID}
    return JsonResponse(retorno)






def index2(request):
    return render(request,'roboworld_app/index2.html')

def proceso2(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request,'roboworld_app/proceso2.html',{'name':nombre})

