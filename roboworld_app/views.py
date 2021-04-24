from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from json import loads, dumps
from . models import Reto
from random import randrange
import psycopg2

from django.contrib.auth.models import User

# FUNCIONES LISTAS Y FUNCIONANDO
#-----------------------------------------------------------------------------------------
#envia a index (listo)
def inicio(request):
    return render(request, "roboworld_app/index.html")

#envia al juego (LIST)
def juego_unity(request):
    return render(request, "roboworld_app/juego_unity/index_unity.html")

#envia inciar sesión (LISTO)
def iniciar_sesion(request):
    return render(request, "roboworld_app/iniciar_sesion.html")


#envia a cuenta de usuario (LISTO)
@login_required
def cuenta_usuario(request):
    usuario = request.user # asigna a "usuario" el usuario loggeado
    resultados = Reto.objects.filter(id_de_usuario_id=usuario)
    minutos_info = resultados[0].minutos_jugados
    veces_info = resultados[0].repeticion_niveles
    engranes_info = resultados[0].engranes
    return render(request, 'roboworld_app/cuenta_usuario.html', {"engranes_info":engranes_info,"veces_info":veces_info,"minutos_info":minutos_info}) 
#-----------------------------------------------------------------------------------------
'''
#envia a grafica 1º (working)
def grafica1(request):
    return render(request,'roboworld_app/graficas/grafica1.html')
'''

def grafica1(request):
    data = [['Nombre', 'Engranes recolectados']]

    resultados = Reto.objects.all(), User.objects.all()

    for i in resultados:
        x = i.get_username()
        y = i.engranes
        data.append([x,y])
    
    datos_formato = dumps(data)    
    titulo = 'Indicador STEM'
    subtitulo = 'Engranes recolectados'

    titulo_formato = dumps(titulo)
    subtitulo_formato = dumps(subtitulo)
    return render(request,'roboworld_app/graficas/grafica1.html', {'losDatos':datos_formato, 'titulo':titulo_formato, 'subtitulo':subtitulo_formato})




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
Level
'''
@csrf_exempt
def Level(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    level_number = body_json['level_number']
    #level_number = ""
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
            if row[1] == level_number:
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
    print(level_number, enemigo,dificultad,duracion_individual)      
    retorno = {"level_number":level_number,
         "enemigo":enemigo,
         "dificultad":dificultad,
         "duracion_individual": duracion_individual}
    return JsonResponse(retorno)


'''
Engranes
'''
@csrf_exempt
def engranes(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    sessionObtained = body_json['sessionObtained']
    sesionObtained= ""
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
            if row[1] == sessionObtained:
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
            print("PostgreSQL connection is now closed")
    retorno = {"sessionObtained":sessionObtained,
         "numero":numero}
    return JsonResponse(retorno)

'''
Sesion
'''
@csrf_exempt
def sesion(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    started = body_json['started']
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
            if row[1] == started:
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

'''
recomoensas
'''
@csrf_exempt
def recompensas(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    engranes_necesarios = body_json['engranes_necesarios']
   
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
            if row[1] == engranes_necesarios:
                engranes_necesarios = row[1]
                top_score_global = row[2]
                top_five = row[3]
                
            print(row)
    
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
'''
Prueba
'''
@csrf_exempt
def prueba(request):
    body_unicode = request.body.decode('utf-8')
    body_json = loads(body_unicode) #convertir de string a JSON
    sessionID = body_json['sessionID']
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
            if row[1] == sessionID:
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




def index2(request):
    return render(request,'roboworld_app/index2.html')

def proceso2(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request,'roboworld_app/proceso2.html',{'name':nombre})

