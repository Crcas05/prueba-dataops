import pandas as pd
from datetime import datetime

def generar_reporte_comisiones():
    print("Iniciando proceso de cálculo de comisiones...")

    # Simulación de datos de ventas
    data = {
        "vendedor": ["Ana", "Luis", "Carlos", "Sofia", "Cristhian", "Jose", "Said", "Lucy","Teresa", "Fernando"],
        "ventas": [1000, 1500, 2000, 1800, 2500, 1500, 3500, 1250, 5000, 3200]
    }

    df = pd.DataFrame(data)

    # Cálculo de comisión (10%)
    df["comision"] = df["ventas"] * 0.10

    # Fecha de generación
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"reporte_comisiones_{fecha}.csv"

    # Guardar archivo CSV
    df.to_csv(nombre_archivo, index=False)

    print(f"Reporte generado correctamente: {nombre_archivo}")
    print("Proceso finalizado exitosamente.")

# Proyecto DataOps - Script de Comisiones

if __name__ == "__main__":
    generar_reporte_comisiones()


    

