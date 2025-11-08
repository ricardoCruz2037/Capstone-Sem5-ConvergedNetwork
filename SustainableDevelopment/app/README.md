# Calculadora Ambiental — Environmental Impact Estimator

Esta aplicación forma parte del módulo de **Desarrollo Sustentable** dentro del proyecto *Capstone-Sem5-ConvergedNetwork*.  
Permite estimar el **consumo energético y la huella de carbono (CO₂)** generada por distintos dispositivos eléctricos empleados en el proyecto.

---

## Descripción General

La **Calculadora Ambiental** fue desarrollada en **Python** utilizando **CustomTkinter** y **Matplotlib** para ofrecer una interfaz moderna e interactiva.  
El usuario puede registrar dispositivos, definir su consumo diario y seleccionar la fuente de energía utilizada para estimar su impacto ambiental.

Los resultados se muestran tanto en formato numérico como gráfico, lo que permite **visualizar fácilmente las emisiones estimadas por dispositivo y el total del sistema**.

---

## Características Principales

- Interfaz gráfica intuitiva con CustomTkinter.  
- Cálculo del consumo energético (kWh) y emisiones de CO₂ (kg).  
- Selección de diferentes tipos de fuente de energía:
  - Promedio Global (Carbón)
  - Promedio Global (Gas Natural)
  - Promedio Red (México)
  - Promedio Red (España)
  - Renovable (Solar/Eólica)
- Visualización de resultados mediante gráficos de barras.
- Limpieza rápida de datos y reinicio de cálculos.

---

## Cálculos Realizados

Para cada dispositivo, el cálculo de consumo y emisiones se realiza con las siguientes fórmulas:

\[
\text{kWh}_{dispositivo} = \frac{Potencia\_W \times Horas\_diarias \times Días\_de\_uso}{1000}
\]

\[
\text{CO₂}_{dispositivo} = \text{kWh}_{dispositivo} \times \text{Factor\_de\_emisión}
\]

Donde el **factor de emisión (kg CO₂/kWh)** depende de la fuente de energía seleccionada.

El resultado total se obtiene sumando el consumo y las emisiones de todos los dispositivos registrados.

---

## Uso de la Aplicación

### Ejecución
Asegúrate de tener instaladas las dependencias necesarias:

```bash
pip install customtkinter matplotlib
```
Luego ejecute el programa desde la terminal:
```bash
python calculadoraAmbiental_legacy.py
```
### Flujo de Uso

1. Introduce el nombre del dispositivo, su potencia en watts y las horas de uso diario.
2. Pulsa “Añadir Dispositivo” para registrarlo.
3. Selecciona el tipo de fuente de energía desde el menú desplegable.
4. Presiona “Calcular Impacto Total” para obtener los resultados.
5. Observa los valores totales de kWh y CO₂, así como el gráfico comparativo por dispositivo.
6. Usa “Limpiar Todo” para reiniciar los cálculos.

### Resultados
El sistema genera automáticamente un gráfico de barras horizontal con las emisiones de CO₂ por dispositivo, adaptando los colores según el modo (claro u oscuro) del sistema operativo.
```
Ejemplo conceptual:
|---- Servidor BD        ████████  12.5 kg
|---- Router Core        ████      4.3 kg
|---- Laptop Operativa   ███       3.2 kg
```
