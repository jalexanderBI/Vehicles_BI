import pandas as pd # libreria para trabajar con dataset
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import plotly.express as px # importación de plotly.express
import streamlit as st # libreria para desplegar el proyecto en un explorador
from PIL import Image # importación de librerias para cargar imágenes


# Código para establecer color de background en gris gainsboro
page_bg_style = '''
<style>
.stApp {
    /* Para un color sólido */
    background-color:gainsboro;

    /* Para un gradiente lineal */
    /* background-image: linear-gradient(to right, red, blue); */
}
</style>
'''

st.markdown(page_bg_style, unsafe_allow_html=True) #MOstrar el txto en formato markdown y renderizar en HTML


# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')


#st.title('Reporte General Vehículos en Venta')


# Estilo CSS global para recuadros
st.markdown("""
<style>
.recuadro-header {
    border: 2px solid #4CAF50;
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    background-color: #f9f9f9;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.recuadro-texto {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 12px;
    margin: 10px 0;
    background-color: white;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Header con recuadro
st.markdown('<div class="recuadro-header"><h1>Reporte General Vehículos en Venta</h1></div>', 
            unsafe_allow_html=True) # Titulo general de proyecto


# Se muestra imagen desde archivo local ubicado en el mismo directorio razi del proyecto
image = Image.open("cars aisle.jpg") # Ruta de la imagen
st.image(image, use_container_width=True) # cargar imagen en streamlit, ajuste automático de ancho dela imagen


def texto_titulo(texto): # función para definir parámetros de foramto de texto para el texto_titulo
    st.markdown(f'<h1 style="font-size: 28px; border: 2px solid #4CAF50; padding: 10px; border-radius: 8px;">{texto}</h1>', 
                unsafe_allow_html=True)
    
texto_titulo("Filtro de búsqueda de vehículo") # nombre del texto_titulo


all_types = ['Todos'] + sorted(car_data['type'].dropna().unique().tolist()) # Se crea un filtro interactivo de streamlit con el texto " Todos" más un filtro de todos los valores únicos de la columna "type" pasándolos a una lista de python con .tolist()
selected_type = st.selectbox('Selecciona el Tipo de Vehículo', all_types) # Herramienta de caja de selección con la variable creada all types

# Aplicar el primer filtro al DataFrame
if selected_type != 'Todos': # Condición si no se elige " Todos"
    data_filtered_by_type = car_data[car_data['type'] == selected_type] #La variable resultante será el valor del filtro de dataset seleccionado como selected_type
else: 
    
    data_filtered_by_type = car_data.copy() # Si elige "Todos", no se aplica filtro

# Segundo Filtro (en cascada): Modelo del Vehículo
# Las opciones del modelo dependen del tipo seleccionado en el nuevo dataset filtrado resultante: data_filtered_by_type
available_models = ['Todos'] + sorted(data_filtered_by_type['model'].dropna().unique().tolist()) # Se crea un filtro interactivo de streamlit con el texto " Todos" más un filtro de todos los valores únicos de la columna "model" pasándolos a una lista de python con .tolist()
selected_model = st.selectbox('Selecciona el Modelo', available_models) # Herramienta de caja de selección con la variable creada available_models

# Aplicar el segundo filtro al DataFrame ya filtrado por tipo
if selected_model != 'Todos':# Condición si no se elige " Todos"
    filtered_data = data_filtered_by_type[data_filtered_by_type['model'] == selected_model]#La variable resultante será el valor del filtro de dataset seleccionado como selected_model
else: 
    filtered_data = data_filtered_by_type # Si elige "Todos", no se aplica filtro


condition_models = ['Todos'] + sorted(filtered_data['condition'].dropna().unique().tolist()) # Se crea un filtro interactivo de streamlit con el texto " Todos" más un filtro de todos los valores únicos de la columna "condition" pasándolos a una lista de python con .tolist()
selected_condition = st.selectbox('Selecciona la condición', condition_models) # Herramienta de caja de selección con la variable creada condition_models

# Aplicar el segundo filtro al DataFrame ya filtrado por tipo
if selected_condition != 'Todos': # Condición si no se elige " Todos"
    filtered_condition = filtered_data[filtered_data['condition'] == selected_condition] #La variable resultante será el valor del filtro de dataset seleccionado como selected_condition
    #filtered_condition = filtered_condition.reset_index()
    #filtered_condition.columns = ['item','price','model_year','model','condition','cylinders','fuel','odometer','transmission','type','paint_color','is_4wd','date_posted','days_listed']
    
else:
    filtered_condition = filtered_data # Si elige "Todos", no se aplica filtro
    #filtered_condition = filtered_condition.reset_index()
    #filtered_condition.columns = ['item','price','model_year','model','condition','cylinders','fuel','odometer','transmission','type','paint_color','is_4wd','date_posted','days_listed']

min_value=int(filtered_condition['price'].min()) # se crea variable para determinar valor mínimo de la columna precio del dataset filtrado
max_value=int(filtered_condition['price'].max()) # se crea variable para determinar valor máximo de la columna precio del dataset filtrado

# 2. Verificar y ajustar los valores si min_value >= max_value
if min_value > max_value:
    # COndición por si sucede, esta situación no debería ocurrir, pero por seguridad
    min_value, max_value = 0, 1
elif min_value == max_value:
    # Si son iguales, ajusta max_value para que sea mayor
    max_value = min_value + 1  # Max value sera mayor en +1 que min_value, porque si



# 3. Solo mostrar el slider si hay un rango válido para seleccionar
if min_value < max_value: # si valor minimo menor que máximo
    price_range = st.slider( # mostrar slider
        'Selecciona el rango de precio',
        min_value=min_value, # valor mínimo
        max_value=max_value, # valor máximo
        value=(min_value, max_value) # límites de valores
        )

# Aplicar el rango de precios seleccionado al DataFrame
    final_filtered_data = filtered_condition[
        (filtered_condition['price'] >= price_range[0]) & 
        (filtered_condition['price'] <= price_range[1])
    ]
else:
    
    st.info("No hay un rango de precios disponible para filtrar con los criterios seleccionados.")
    final_filtered_data = filtered_condition



# Mostrar resultados
st.write(f'Mostrando {len(final_filtered_data)} vehículos de {len(car_data)} totales') # texto cantidad de valores encontrados en el filtro
st.dataframe(final_filtered_data) #mostrar dataframe con el resultado del filtro

def texto_titulo2(texto): # función para formato de titulo 2
    st.markdown(f'<h1 style="font-size: 28px; border: 2px solid #4CAF50; padding: 10px; border-radius: 8px;">{texto}</h1>', 
                unsafe_allow_html=True)
    

texto_titulo2("Distribución por precio de vehículos filtrados") # Texto de título 2

build_histogram1 = st.checkbox('Construir histograma de distribución por precio') # Elemento de Checkbox de streamlit

if build_histogram1: # condicional en caso de activar el checkbox

# Contar la cantidad de vehículos por marca
    conteo_por_marca = car_data['transmission'].value_counts().reset_index() # filtro de dataset de valores unicos y con reseteo de encabezado de columnas 
    conteo_por_marca.columns = ['transmission', 'count']  # Renombrar columnas

# Crear el gráfico de histograma
    fig = px.histogram(
    final_filtered_data,  #DataFrame después de aplicar todos los filtros
    x='price', #eje x
    title=f'Distribución de Precios ({len(final_filtered_data)} vehículos)', #título del histograma
    nbins=20
    )
    
# Mejorar el formato del grafico, tamaño de texto, posición,etc.
    fig.update_traces(
        textfont_size=12,
        textangle=0,
        textposition="outside",
        cliponaxis=False
    )
    fig.update_layout(xaxis_tickangle=-45)  # Rota las etiquetas del eje X para mejor legibilidad

# Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


st.header("💰 Cotizador de Financiamiento Vehicular") # tercer encabezado

# Seleccionar un vehículo para cotizar
st.subheader("Vehículo más económico encontrado en tu búsqueda :") # subtitulo

# Mostrar algunos vehículos para seleccionar (puedes adaptar esto a tus filtros)


if 'final_filtered_data' in locals(): # locals: Función que devuelve un diccionario con todas las variables locales existentes en ese momento
    vehiculos_sample = final_filtered_data[['model', 'price']].sort_values('price', ascending = True).drop_duplicates(subset=['model']) # selección para filtrar dataset por las columnas model y price, evitar duplicados de la columna model
    selected_vehicle = st.selectbox( # caja de selección básado en el dataset filtrado vehiculos_sample
        "Elige un vehículo:",
        options=vehiculos_sample['model'].tolist(),
        format_func=lambda x: f"{x} - ${vehiculos_sample[vehiculos_sample['model']==x]['price'].tolist()}"
    )

    
    # Obtener el precio del vehículo seleccionado
    precio_vehiculo = vehiculos_sample[vehiculos_sample['model']==selected_vehicle]['price'].iloc[0]
else:
    # Si no tienes car_data, usar un valor por defecto
    precio_vehiculo = st.number_input("Ingresa el precio del vehículo ($):", min_value=1000, max_value=1000000, value=25000)




# Parámetros del crédito
st.subheader("Condiciones del Crédito")

tasa_interes_anual = 0.24  # 24% EA
st.info(f"Tasa de interés: {tasa_interes_anual*100}% EA")

# Barra deslizante para años de financiamiento
anos_financiamiento = st.slider(
    "Años de financiamiento:",
    min_value=5,
    max_value=10,
    value=7,
    step=1
)

# Cálculos financieros
def calcular_cuota_mensual(precio, tasa_anual, anos):
    """Calcula la cuota mensual usando la fórmula de anualidades"""
    tasa_mensual = tasa_anual / 12
    numero_pagos = anos * 12
    
    if tasa_mensual > 0:
        cuota = precio * (tasa_mensual * (1 + tasa_mensual)**numero_pagos) / ((1 + tasa_mensual)**numero_pagos - 1)
    else:
        cuota = precio / numero_pagos
    
    return cuota

def generar_tabla_amortizacion(precio, tasa_anual, anos):
    """Genera tabla de amortización"""
    tasa_mensual = tasa_anual / 12
    numero_pagos = anos * 12
    cuota = calcular_cuota_mensual(precio, tasa_anual, anos)
    
    saldo = precio
    tabla = []
    
    for mes in range(1, numero_pagos + 1):
        interes = saldo * tasa_mensual
        capital = cuota - interes
        saldo -= capital
        
        tabla.append({
            'Mes': mes,
            'Cuota': cuota,
            'Interés': interes,
            'Capital': capital,
            'Saldo': max(saldo, 0)
        })
    
    return pd.DataFrame(tabla)

# Calcular resultados
cuota_mensual = calcular_cuota_mensual(precio_vehiculo, tasa_interes_anual, anos_financiamiento)
total_pagado = cuota_mensual * (anos_financiamiento * 12)
interes_total = total_pagado - precio_vehiculo

# Mostrar resultados
st.subheader("📊 Resumen de la Cotización")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Cuota Mensual",
        f"${cuota_mensual:,.2f}",
        delta=None
    )

with col2:
    st.metric(
        "Total a Pagar",
        f"${total_pagado:,.2f}",
        delta=f"${interes_total:,.2f} de interés"
    )

with col3:
    st.metric(
        "Costo Financiero",
        f"${interes_total:,.2f}",
        delta=f"{((interes_total/precio_vehiculo)*100):.1f}% del valor"
    )

# Gráfico de distribución de pagos
st.subheader("📈 Distribución de Pagos")

import plotly.graph_objects as go

labels = ['Valor del Vehículo', 'Intereses']
values = [precio_vehiculo, interes_total]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.update_layout(title="Composición del Total a Pagar")
st.plotly_chart(fig, use_container_width=True)

# Tabla de amortización (opcional)
if st.checkbox("Mostrar tabla de amortización (primeros 12 meses)"):
    st.subheader("📋 Tabla de Amortización")
    tabla_amort = generar_tabla_amortizacion(precio_vehiculo, tasa_interes_anual, anos_financiamiento)
    st.dataframe(tabla_amort.head(12).style.format({
        'Cuota': '${:,.2f}',
        'Interés': '${:,.2f}',
        'Capital': '${:,.2f}',
        'Saldo': '${:,.2f}'
    }))

# Información adicional
st.subheader("💡 Información Importante")
st.write(f"""
- **Plazo:** {anos_financiamiento} años ({anos_financiamiento * 12} meses)
- **Tasa efectiva anual:** {tasa_interes_anual * 100}%
- **Tasa mensual:** {(tasa_interes_anual/12)*100:.2f}%
- **Valor financiado:** ${precio_vehiculo:,.2f}
- **Total intereses:** ${interes_total:,.2f}
""")

def texto_titulo3(texto):
    st.markdown(f'<h1 style="font-size: 28px; border: 2px solid #4CAF50; padding: 10px; border-radius: 8px;">{texto}</h1>', 
                unsafe_allow_html=True)
    



texto_titulo3("Distribución por Año de Fabricación del Vehículo")

build_histogram2 = st.checkbox('Construir Histograma por Año de Fabricación')
if build_histogram2:

    fig = px.histogram(
        car_data,
        x="model_year",        # Columna para el eje X (año del modelo)
        color="condition",     # Columna para diferenciar por color (condición)
        title="Distribución del Año de Fabricación por Condición del Vehículo",
        labels={"model_year": "Año del Vehículo", "condition": "Condición"}, # Etiquetas más claras
        category_orders={"condition": ["excellent", "good", "fair", "like new", "new", "salvage"]} # Orden opcional
    )

# Personalizar el diseño del gráfico
    fig.update_layout(
        bargap=0.1,  # Espacio entre grupos de barras
        xaxis_title="Año del Vehículo",
        yaxis_title="Cantidad de Vehículos"
    )

# Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)


