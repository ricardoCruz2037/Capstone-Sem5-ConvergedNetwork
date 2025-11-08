import customtkinter as ctk  # Importamos la biblioteca para la GUI
import matplotlib.pyplot as plt
import tkinter  # para conversión de colores si se usa en el futuro
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- CLASE DE LÓGICA (La misma de antes) ---

class CalculadoraAmbiental:
    """
    Esta clase maneja la lógica para calcular el consumo de energía
    y las emisiones de CO2 de un conjunto de dispositivos.
    """
    
    def __init__(self):
        # Factores de emisión (kg CO2 / kWh)
        self.factores_emision = {
            "Promedio Global (Carbón)": 1.0,
            "Promedio Global (Gas Natural)": 0.5,
            "Promedio Red (México)": 0.45,
            "Promedio Red (España)": 0.25,
            "Renovable (Solar/Eólica)": 0.03
        }
        self.dispositivos = []

    def obtener_nombres_fuentes(self):
        """Devuelve la lista de nombres de fuentes de energía."""
        return list(self.factores_emision.keys())

    def agregar_dispositivo(self, nombre, potencia_watts, horas_uso_diarias):
        """
        Añade un dispositivo y sus datos de uso a la lista.
        Devuelve True si fue exitoso, False si hay error.
        """
        try:
            # Convertimos a números para validar
            potencia_w_num = float(potencia_watts)
            horas_num = float(horas_uso_diarias)

            if potencia_w_num <= 0 or horas_num <= 0:
                print("Error: Los valores deben ser positivos.")
                return False

            dispositivo = {
                "nombre": nombre,
                "potencia_w": potencia_w_num,
                "horas_diarias": horas_num
            }
            self.dispositivos.append(dispositivo)
            print(f"Dispositivo añadido: {nombre}")
            return True
        except ValueError:
            print("Error: Potencia y horas deben ser números.")
            return False

    def calcular_impacto(self, tipo_fuente_energia, dias_calculo=30):
        """
        Calcula el impacto total (kWh y CO2) para todos los dispositivos.
        """
        if tipo_fuente_energia not in self.factores_emision:
            return None
        
        factor_co2 = self.factores_emision[tipo_fuente_energia]
        
        resultados = {
            "total_kwh": 0,
            "total_co2_kg": 0,
            "detalle_dispositivos": []
        }
        
        if not self.dispositivos:
            print("No hay dispositivos para calcular.")
            return resultados # Devolver resultados vacíos

        for disp in self.dispositivos:
            kwh_disp = (disp["potencia_w"] * disp["horas_diarias"] * dias_calculo) / 1000
            co2_disp = kwh_disp * factor_co2
            
            resultados["detalle_dispositivos"].append({
                "nombre": disp["nombre"],
                "kwh": kwh_disp,
                "co2_kg": co2_disp
            })
            
            resultados["total_kwh"] += kwh_disp
            resultados["total_co2_kg"] += co2_disp
            
        return resultados

    def limpiar_dispositivos(self):
        """Limpia la lista de dispositivos."""
        self.dispositivos = []
        print("Lista de dispositivos limpiada.")


# --- CLASE DE LA INTERFAZ GRÁFICA (GUI) ---

class AppGUI(ctk.CTk):
    
    def __init__(self, motor_calculo):
        super().__init__()
        
        # --- 1. Configuración de la Ventana ---
        self.title("Calculadora de Huella Ambiental 🌳")
        self.geometry("800x600")
        
        # Le pasamos la instancia de la calculadora
        self.calc = motor_calculo
        
        # Configuramos el tema
        ctk.set_appearance_mode("System")  # Puede ser "Dark" o "Light"
        ctk.set_default_color_theme("blue")
        
        # --- 2. Crear Frames (Contenedores) ---
        # Frame izquierdo para añadir dispositivos
        self.frame_izquierda = ctk.CTkFrame(self, width=300)
        self.frame_izquierda.pack(side="left", fill="y", padx=10, pady=10)
        
        # Frame derecho para mostrar resultados y gráficos
        self.frame_derecha = ctk.CTkFrame(self)
        self.frame_derecha.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # --- 3. Llamar a los métodos para crear los widgets ---
        self.crear_widgets_izquierda()
        self.crear_widgets_derecha()
        
        # Variable para el gráfico
        self.canvas_grafico = None

    def crear_widgets_izquierda(self):
        """Crea los widgets del panel izquierdo (inputs)."""
        
        # Título
        lbl_titulo_inputs = ctk.CTkLabel(self.frame_izquierda, text="Añadir Dispositivo", font=ctk.CTkFont(size=16, weight="bold"))
        lbl_titulo_inputs.pack(pady=15, padx=10)
        
        # --- Nombre ---
        lbl_nombre = ctk.CTkLabel(self.frame_izquierda, text="Nombre del Dispositivo:")
        lbl_nombre.pack(padx=10, pady=(5,0), anchor="w")
        self.entry_nombre = ctk.CTkEntry(self.frame_izquierda, placeholder_text="Ej: Servidor BD")
        self.entry_nombre.pack(pady=5, padx=10, fill="x")
        
        # --- Potencia ---
        lbl_potencia = ctk.CTkLabel(self.frame_izquierda, text="Potencia (Watts):")
        lbl_potencia.pack(padx=10, pady=(5,0), anchor="w")
        self.entry_potencia = ctk.CTkEntry(self.frame_izquierda, placeholder_text="Ej: 150")
        self.entry_potencia.pack(pady=5, padx=10, fill="x")
        
        # --- Horas de Uso ---
        lbl_horas = ctk.CTkLabel(self.frame_izquierda, text="Horas de Uso (diarias):")
        lbl_horas.pack(padx=10, pady=(5,0), anchor="w")
        self.entry_horas = ctk.CTkEntry(self.frame_izquierda, placeholder_text="Ej: 12")
        self.entry_horas.pack(pady=5, padx=10, fill="x")
        
        # --- Botón Añadir ---
        btn_anadir = ctk.CTkButton(self.frame_izquierda, text="Añadir Dispositivo", command=self.on_agregar_dispositivo)
        btn_anadir.pack(pady=15, padx=10, fill="x")
        
        # --- Separador ---
        lbl_separador = ctk.CTkLabel(self.frame_izquierda, text="-"*50)
        lbl_separador.pack(pady=10)
        
        # --- Título Cálculo ---
        lbl_titulo_calc = ctk.CTkLabel(self.frame_izquierda, text="Calcular Impacto", font=ctk.CTkFont(size=16, weight="bold"))
        lbl_titulo_calc.pack(pady=10, padx=10)
        
        # --- Selección de Fuente de Energía ---
        lbl_fuente = ctk.CTkLabel(self.frame_izquierda, text="Tipo de Fuente de Energía:")
        lbl_fuente.pack(padx=10, pady=(5,0), anchor="w")
        
        fuentes_energia = self.calc.obtener_nombres_fuentes()
        self.opcion_fuente = ctk.CTkOptionMenu(self.frame_izquierda, values=fuentes_energia)
        self.opcion_fuente.pack(pady=5, padx=10, fill="x")
        
        # --- Botón Calcular ---
        btn_calcular = ctk.CTkButton(self.frame_izquierda, text="Calcular Impacto Total", command=self.on_calcular_impacto, fg_color="green", hover_color="darkgreen")
        btn_calcular.pack(pady=15, padx=10, fill="x")

        # --- Botón Limpiar ---
        btn_limpiar = ctk.CTkButton(self.frame_izquierda, text="Limpiar Todo", command=self.on_limpiar_todo, fg_color="gray")
        btn_limpiar.pack(pady=5, padx=10, fill="x")

        # --- Label de Estado ---
        self.lbl_estado = ctk.CTkLabel(self.frame_izquierda, text="", text_color="green")
        self.lbl_estado.pack(pady=10, padx=10)

    def crear_widgets_derecha(self):
        """Crea los widgets del panel derecho (resultados)."""
        
        # Título
        lbl_titulo_res = ctk.CTkLabel(self.frame_derecha, text="Resultados del Cálculo", font=ctk.CTkFont(size=16, weight="bold"))
        lbl_titulo_res.pack(pady=15, padx=10)
        
        # --- Frame para Totales ---
        frame_totales = ctk.CTkFrame(self.frame_derecha)
        frame_totales.pack(pady=10, padx=10, fill="x")
        
        self.lbl_total_kwh = ctk.CTkLabel(frame_totales, text="Total kWh: 0.00", font=ctk.CTkFont(size=14))
        self.lbl_total_kwh.pack(side="left", padx=20, pady=10)
        
        self.lbl_total_co2 = ctk.CTkLabel(frame_totales, text="Total CO₂: 0.00 kg", font=ctk.CTkFont(size=14))
        self.lbl_total_co2.pack(side="right", padx=20, pady=10)
        
        # --- Frame para el Gráfico ---
        self.frame_grafico = ctk.CTkFrame(self.frame_derecha)
        self.frame_grafico.pack(fill="both", expand=True, padx=10, pady=10)
        
        lbl_info_graf = ctk.CTkLabel(self.frame_grafico, text="El gráfico de impacto por dispositivo aparecerá aquí.")
        lbl_info_graf.pack(pady=20)


    # --- MÉTODOS DE ACCIÓN (CALLBACKS) ---

    def on_agregar_dispositivo(self):
        """Se llama al presionar el botón 'Añadir Dispositivo'."""
        nombre = self.entry_nombre.get()
        potencia = self.entry_potencia.get()
        horas = self.entry_horas.get()
        
        if not nombre or not potencia or not horas:
            self.lbl_estado.configure(text="Error: Todos los campos son requeridos.", text_color="red")
            return
            
        exito = self.calc.agregar_dispositivo(nombre, potencia, horas)
        
        if exito:
            self.lbl_estado.configure(text=f"Añadido: {nombre}", text_color="green")
            # Limpiar campos de entrada
            self.entry_nombre.delete(0, "end")
            self.entry_potencia.delete(0, "end")
            self.entry_horas.delete(0, "end")
        else:
            self.lbl_estado.configure(text="Error: Revisa los valores (deben ser > 0).", text_color="red")
            
    def on_calcular_impacto(self):
        """Se llama al presionar 'Calcular Impacto Total'."""
        tipo_fuente = self.opcion_fuente.get()
        
        resultados = self.calc.calcular_impacto(tipo_fuente, dias_calculo=30)
        
        if resultados is None:
            self.lbl_estado.configure(text="Error al calcular.", text_color="red")
            return

        if not resultados["detalle_dispositivos"]:
            self.lbl_estado.configure(text="Añade al menos un dispositivo.", text_color="yellow")
            return

        # --- 1. Actualizar Totales ---
        self.lbl_total_kwh.configure(text=f"Total kWh: {resultados['total_kwh']:.2f}")
        self.lbl_total_co2.configure(text=f"Total CO₂: {resultados['total_co2_kg']:.2f} kg")
        
        self.lbl_estado.configure(text="Cálculo realizado con éxito.", text_color="green")

        # --- 2. Generar Gráfico (¡Nuevo!) ---
        self.generar_grafico(resultados["detalle_dispositivos"])

    def generar_grafico(self, detalle_dispositivos):
    
    # Limpiar gráfico anterior si existe
        if self.canvas_grafico:
            self.canvas_grafico.get_tk_widget().pack_forget()
    
    # Extraer datos para el gráfico
        nombres = [d["nombre"] for d in detalle_dispositivos]
        emisiones_co2 = [d["co2_kg"] for d in detalle_dispositivos]
    
    # --- Determinar color de fondo del gráfico según el modo de la app ---
        color_tuple = self.frame_grafico.cget("fg_color")
        mode = ctk.get_appearance_mode()
    
    # Algunos temas devuelven tuplas (modo claro, oscuro), otros un solo valor
        if isinstance(color_tuple, tuple):
            bg_color = color_tuple[1] if mode == "Dark" else color_tuple[0]
        else:
            bg_color = color_tuple
    
    # En caso de que sea un color no reconocido por Matplotlib (ej. 'gray81'),
    # usamos valores hexadecimales seguros.
        if mode == "Dark":
            bg_color = "#2b2b2b"   # gris oscuro
            text_color = "#d0d0d0" # texto claro
        else:
            bg_color = "#f2f2f2"   # gris claro
            text_color = "#333333" # texto oscuro
    
    # --- Crear la figura ---
        fig, ax = plt.subplots(figsize=(6, 4), facecolor=bg_color)
    
    # Crear las barras con una paleta continua
        colores = plt.cm.viridis([i / len(nombres) for i in range(len(nombres))])
        # Guardamos las barras en una variable
        barras = ax.barh(nombres, emisiones_co2, color=colores) 
        # Usamos la variable para añadir las etiquetas
        ax.bar_label(barras, fmt='%.2f kg', padding=3, color=text_color, fontsize=9)
        # Esto añade la etiqueta de texto al final de cada barra
        ax.bar_label(barras, fmt='%.2f kg', padding=3, color=text_color, fontsize=9)
    
    # Estilizar el gráfico
        ax.set_xlabel("Emisiones (kg CO₂)", color=text_color)
        ax.set_title("Impacto de CO₂ por Dispositivo (30 días)", color=text_color)
        ax.tick_params(axis='x', colors=text_color)
        ax.tick_params(axis='y', colors=text_color)
        ax.set_facecolor(bg_color)
    
    # Quitar bordes innecesarios
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(text_color)
        ax.spines['bottom'].set_color(text_color)
    
        fig.tight_layout()  # Ajusta el gráfico al tamaño del contenedor
    
    # --- Integrar Matplotlib con CustomTkinter ---
        self.canvas_grafico = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        self.canvas_grafico.draw()
        self.canvas_grafico.get_tk_widget().pack(fill="both", expand=True)
    
    def on_limpiar_todo(self):
        """Limpia los dispositivos, resultados y el gráfico."""
        self.calc.limpiar_dispositivos()
        
        # Limpiar labels de totales
        self.lbl_total_kwh.configure(text="Total kWh: 0.00")
        self.lbl_total_co2.configure(text="Total CO₂: 0.00 kg")
        self.lbl_estado.configure(text="Datos reiniciados.", text_color="gray")
        
        # Limpiar gráfico
        if self.canvas_grafico:
            self.canvas_grafico.get_tk_widget().pack_forget()
            self.canvas_grafico = None
        
        print("Todo limpio.")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    
    # 1. Creamos la instancia del motor de cálculo
    mi_calculadora = CalculadoraAmbiental()
    
    # 2. Creamos la instancia de la App y le pasamos el motor
    app = AppGUI(motor_calculo=mi_calculadora)
    
    # 3. Iniciamos el bucle principal de la aplicación
    app.mainloop()
    