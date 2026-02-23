import json
def cargar_datos(nom_archivo):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}

def guardar_datos(datos, nom_archivo):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch,indent=4)
            print(f"---Guardado exitoso en {nom_archivo} ---")
    except Exception as e:
        print(f"Error al guardar: {e}")

def guardar_datos_Prestamos_vencidos(datos, nom_archivo):
    try:
        with open(nom_archivo, "w",encoding="utf-8") as arch:
            arch.write("ID_Prestamo,Usuario.Herramiente,Cantidad_Prestada,fecha_inicio,fecha_estimada,dias_de_atrazo\n")
            for id_pv,info in datos.items():
                linea = f"{id_pv},{info['usuario']},{info['herramienta']},{info['cantidad']},{info['fecha_i']},{info['fecha_es']}\n"
            print(f"---Guardado exitoso en {nom_archivo} ---")

    except Exception as e:
        print(f"Error al guardar: {e}")
def cargar_prestamos_csv(nom_archivo):
    datos_vencidos = {}
    try:
        with open(nom_archivo, "r", encoding="utf-8") as arch:
            lineas = arch.readlines()
            
            # Si el archivo está vacío o solo tiene el encabezado, retornamos vacío
            if len(lineas) <= 1:
                return {}

            # Saltamos la primera línea (el encabezado)
            for linea in lineas[1:]:
                # Quitamos saltos de línea y separamos por comas
                partes = linea.strip().split(",")
                
                # Verificamos que la línea tenga todos los datos (6 columnas)
                if len(partes) == 6:
                    id_p = partes[0]
                    datos_vencidos[id_p] = {
                        "usuario": partes[1],
                        "herramienta": partes[2],
                        "cantidad": int(partes[3]),
                        "fecha_i": partes[4],
                        "fecha_es": partes[5]
                    }
        return datos_vencidos
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error al leer el reporte CSV: {e}")
        return {}