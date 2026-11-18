#!/usr/bin/env python3
# /login (punto 8). Apache lo ejecuta como CGI.
#   GET  /login  devuelve el formulario de login.
#   POST /login  recibe usuario y clave del formulario. Si son correctos, guarda la sesión
#                en una cookie y redirige a /main (303). Si no, responde "Login incorrecto" (401).
import os
import sys
from urllib.parse import parse_qs

USUARIO = "admin"
CLAVE = "sinergia"

FORMULARIO = """<form method="post" action="/login">
Usuario: <input name="usuario"><br>
Clave: <input name="clave" type="password"><br>
<button type="submit">Ingresar</button>
</form>"""


def pagina(estado, contenido):
    print("Status: " + estado)
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("<!DOCTYPE html>")
    print('<html><head><meta charset="utf-8"><title>Sinergia</title></head><body>')
    print(contenido)
    print("</body></html>")


if os.environ.get("REQUEST_METHOD") == "POST":
    largo = int(os.environ.get("CONTENT_LENGTH") or 0)
    datos = parse_qs(sys.stdin.read(largo))
    usuario = datos.get("usuario", [""])[0]
    clave = datos.get("clave", [""])[0]
    if usuario == USUARIO and clave == CLAVE:
        # Login correcto: guarda la sesión en una cookie y redirige a /main
        print("Status: 303 See Other")
        print("Set-Cookie: sesion=" + USUARIO + "; Path=/")
        print("Location: /main")
        print("Content-Type: text/plain; charset=utf-8")
        print()
        print("Login correcto. El servidor te redirige a /main.")
    else:
        pagina("401 Unauthorized",
               "<h1>Login incorrecto</h1>\n<p>Usuario o clave incorrectos.</p>\n" + FORMULARIO)
else:
    pagina("200 OK", "<h1>Sinergia - Iniciar sesión</h1>\n" + FORMULARIO)
