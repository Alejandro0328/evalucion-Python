import Archivos
import Prestamos
from Reportes import prestamos_vencidos
import menus
Prestamos_vencidos= Archivos.cargar_datos("PrestamosVencidos.csv")
prestamos=Archivos.cargar_datos("prestamos.json")
def menu():
    while True:
        menus.limpiar_pantalla()
        menus.imprimir_encabezado(" BIENVENIDO AL MODULO DE EXAMEN")
        print(" 1. Ingrese la fecha actual")
        print(" 2. Ver prestamos vencidos")
        print(" 0. salir")
        print("─" * 50)
        
        op = input("\n  Seleccione una opción: ")
        
        if op == "1":
            

            print(" REPORTE: PRÉSTAMOS VENCIDOS ".center(40))
            print("─"*40)
            
            # Pedir la fecha actual para comparar
            hoy_str = input("-> Ingrese la fecha de hoy (DD-MM-AAAA): ").strip()
            
            if not Prestamos.validar_fecha(hoy_str):
                print("Fecha inválida.")
                return

            hoy_num = Prestamos.fecha_a_numero(hoy_str)
            encontrado = False
            prestamo_vencido={}

            for id_p, info in prestamos.items():
                # Solo verificamos préstamos que aún están "Activos"
                if info['estado'] == "Activo":
                    fecha_vence_num = Prestamos.fecha_a_numero(info['fecha_entrega'])
                    usuario=info['usuario']
                    herramienta= info['herramienta']
                    cantidad = info['cantidad']
                    fecha_i= info['fecha_inicio']
                    fecha_es = info['fecha_entrega']
                    dias_atraso = 1
                    
                    # Si la fecha de entrega es menor a hoy, está vencido
                    if fecha_vence_num < hoy_num:
                        prestamo_vencido[id_p]= {
                            id_p,
                            usuario,
                            herramienta,
                            cantidad,
                            fecha_i,
                            fecha_es,




                        }
                        Archivos.guardar_datos_Prestamos_vencidos(prestamo_vencido,"PrestamosVencidos.csv")
                        

                    
            if not encontrado:
                print(" No hay préstamos vencidos a la fecha.")
        elif op == "2":
            pass
        elif op == "0":
            Archivos.guardar_datos(Prestamos_vencidos,"PrestamosVencidos.csv")
            Archivos.guardar_datos(prestamos,"prestamos.json")
            break
        else:
            print(" Opción no válida.")
            input("Presione Enter...")
menu()