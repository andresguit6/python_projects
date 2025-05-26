import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# para ver las voces disponibles
# engine = pyttsx3.init()
# for voz in engine.getProperty("voices"):
#    print(voz)

# opciones de voz / idioma
id1 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
id2 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3 = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar el reconocedor en una variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que e4scucho como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-col")


            # prueba de que pudo ingresar
            print("dijiste : " + pedido)

            # devolver pedido
            return pedido

        # en caso de qye no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso no de resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("ups, algo salio mal")

            # devolver error
            return "sigo en espera"

# funcion apra que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    engine.say(mensaje)
    engine.runAndWait()

# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miércoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sábado",
                  6:"Domingo"}

    # decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")

# informar que hora es
def pedir_hora():

    # crear unavariable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"Andrés, en este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora)

# funcion saludo inicial
def saludo_inicial():

    # crear variables con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 12:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"
    #decir el saludo
    hablar(f"{momento}, soy helena, tu asistente personal. Por favor, dime en que te puedo ayudar")

#funcion central del asistente
def pedir_cosas():

    #activar saludo inicial
    saludo_inicial()

    #variable de corte
    comenzar = True

    #loop central
    while comenzar:

        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("con gusto, estoy abriendo youtube")
            webbrowser.open("https://www.youtube.com ")
            continue
        elif "abrir google" in pedido:
            hablar("Claro, estoy en eso")
            webbrowser.open("https://www.google.com")
            continue
        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue
        elif "qué hora es" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("buscando eso en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("wikipedia dice lo siguiente")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "chiste" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera =  {"apple": "APPL",
                        "amazon": "AMZN",
                        "google":"GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"la encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("perdon pero no la he econtrado")
                continue
        elif "adiós" in pedido:
            hablar("me voy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()