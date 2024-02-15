# Importamos el módulo time y el módulo colorama
import time
import colorama
from colorama import Fore, Back, Style

# Inicializamos el módulo colorama
colorama.init()

# Definimos el texto que queremos mostrar como una carta
texto = "Querida Fer\n\nSe que no hemos tenido los mejores momentos ultimamente sin embargo los sentimientos que tengo hacia ti siguen a flor de piel, no soy un romantico ni el consumista que te llena de regalos pero quiero brindarte algo mejor.\n\nQuiero decirte lo mucho que te aprecio y que pese a todo eres de las mejores cosas que me ha pasado en la vida. Gracias por estar siempre a mi lado, por apoyarme, por hacerme reír, por ser tan linda(amo esos ojos verdes) y tan inteligente(aunque aveces lo dudes).\nEres mi sueño hecho realidad.\n\nEspero que este no sea el ultimo y que las cosas mejoren para ambos, que sigamos creciendo y aprendiendo el uno del otro. Eres mi razón de sentir y experimentar una vision de la vida tan diferente.\n\nTe sigo esperando... ojala podamos reunirnos pronto.\n\nTe quiero mucho.\n\nBesito de Biznaguita."

# Usamos un ciclo for para recorrer cada carácter del texto
for caracter in texto:
  # Imprimimos el carácter sin salto de línea, con color rojo y fondo negro
  print(Fore.RED + Back.BLACK + caracter, end="")
  # Hacemos una pausa de 0.1 segundos entre cada carácter
  time.sleep(0.1)

# Imprimimos un salto de línea al final del texto
print()

# Restablecemos el color y el fondo por defecto
print(Style.RESET_ALL)

# Llamamos al programa corazon_fer.py usando la función exec
# Esta función ejecuta el código de otro archivo como si fuera parte del actual
exec(open("corazon_fer.py").read())
