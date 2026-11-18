#!/usr/bin/env python3
# /main y /logout (punto 8). Apache lo ejecuta como CGI.
#   GET /main    con la sesión iniciada (cookie), muestra el mensaje de login correcto.
#                Sin sesión, redirige a /login.
#   GET /logout  borra la cookie de la sesión y redirige a /login.
import os


def redirigir(destino, texto, cookie=None):
    print("Status: 303 See Other")
    if cookie:
        print("Set-Cookie: " + cookie)
    print("Location: " + destino)
    print("Content-Type: text/plain; charset=utf-8")
    print()
    print(texto)


def cookies():
    salida = {}
    for par in os.environ.get("HTTP_COOKIE", "").split(";"):
        if "=" in par:
            clave, valor = par.strip().split("=", 1)
            salida[clave] = valor
    return salida


if os.environ.get("SCRIPT_NAME") == "/logout":
    redirigir("/login", "Sesión cerrada. El servidor te redirige a /login.", "sesion=; Path=/; Max-Age=0")
elif cookies().get("sesion") == "admin":
    print("Status: 200 OK")
    print("Content-Type: text/html; charset=utf-8")
    print()
    print("<!DOCTYPE html>")
    print('<html><head><meta charset="utf-8"><title>Sinergia</title></head><body>')
    print("<h1>Login correcto</h1>")
    print("<p>Bienvenido, admin.</p>")
    print('<p><a href="/logout">Cerrar sesión</a></p>')
    print("</body></html>")
else:
    redirigir("/login", "No iniciaste sesión. El servidor te redirige a /login.")
