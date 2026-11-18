# TP Final – Redes y Comunicaciones 2026

· Instituto Zona Oeste 
· Docente: Ing. Ricardo Brisighelli 
· Alumno: Uriel Germán Godoy

Laboratorio en Kathara de la red de la empresa **Sinergia** (`sinergia.izo`): 20 routers con OSPF, 22 LAN, salida a Internet por RC con NAT, DNS en HC1, DHCP en RUV para la LAN LV y un servidor HTTP con login en HD1.

## Estructura

- `Kathara/`: el laboratorio (`lab.conf` y la configuración de cada equipo). En `Kathara/shared/` están las capturas de tráfico (ARP, DHCP, DNS y HTTP).
- `Documentacion/`: esquema de conectividad y documentos del TP.

## Uso

Requiere Kathara con Docker.

```bash
git clone https://github.com/German2242/redes2026_tpfinal_godoy.git
cd redes2026_tpfinal_godoy/Kathara
kathara lstart
```

Para detenerlo: `kathara lclean`.

Login de prueba (usuario `admin`, clave `sinergia`), desde cualquier host del laboratorio:

```bash
curl -d "usuario=admin&clave=sinergia" http://www.sinergia.izo/login
```

Desde afuera del laboratorio (en la terminal de la máquina donde corre Kathara, sin entrar a ningún equipo), el servidor responde en el puerto 8080. Esa máquina necesita `curl` (en Debian: `apt install curl`):

```bash
curl http://localhost:8080/login
```

Sin instalar nada, con `wget`, que Debian suele traer:

```bash
wget -qO- http://localhost:8080/login
```
