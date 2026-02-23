import Archivos
import Prestamos
import menus
prestamos=Archivos.cargar_datos("prestamos.json")
def menu(prestamos):
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

                    
                    # Si la fecha de entrega es menor a hoy, está vencido
                    if fecha_vence_num < hoy_num:
                        encontrado=True
                        prestamo_vencido[id_p]= {
                            "usuario": info['usuario'],
                            "herramienta": info['herramienta'],
                            "cantidad": info['cantidad'],
                            "fecha_i": info['fecha_inicio'],
                            "fecha_es": info['fecha_entrega']
                        }
                        Archivos.guardar_datos_Prestamos_vencidos(prestamo_vencido,"PrestamosVencidos.csv")
                        

                    
            if not encontrado:
                print(" No hay préstamos vencidos a la fecha.")
        elif op == "2":
            pass
        elif op == "0":
            Archivos. guardar_datos_Prestamos_vencidos(Prestamos_vencidos,"PrestamosVencidos.csv")
            Archivos.guardar_datos(prestamos,"prestamos.json")
            break
        else:
            print(" Opción no válida.")
            input("Presione Enter...")
menu()