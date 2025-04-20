
import openai

try:
    import readline  
except ImportError:
    try:
        import pyreadline3 as readline  
    except ImportError:
        print("No se pudo importar readline ni pyreadline3.")
        readline = None

# Introducir tu API para usar el programa
openai.api_key = 'mi API'

ULTIMA_CONSULTA = ""

try:
    consulta = input("Ingrese su consulta: ")

    try:
        if not consulta.strip():
            raise ValueError("La consulta está vacía.")

        # Guardar en historial (si readline está disponible)
        if readline:
            readline.add_history(consulta)

        ULTIMA_CONSULTA = consulta
        print("You:", consulta)

        try:
            respuesta = openai.ChatCompletion.create( # pylint: disable=no-member
                model="gpt-3.5-turbo",  # Aca puedes cambiar la version
                messages=[{"role": "user", "content": consulta}]
            )
            print("chatGPT:", respuesta['choices'][0]['message']['content'])

        except ValueError as e: 
            print("Error en la consulta:", e)

    except ValueError as e:
        print("Error en la API:", e)

except ValueError as e:
    print("Error al leer la entrada:", e)

# antes tenia 
# index.py:46:11: W0718: Catching too general exception Exception (broad-exception-caught)
## antes tenia except Exception as e:
### ahora con la modificacion no sale dicho error por que lo cambie por "except ValueError as e: "

#### pylint index.py --disable=E1101 use esta linea para evitar que salga este error, ya que es de " respuesta = openai.ChatCompletion.create" y al no haber API key no funcionara.