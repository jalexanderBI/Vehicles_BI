import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st


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

st.markdown(page_bg_style, unsafe_allow_html=True)
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
            unsafe_allow_html=True)

def texto_titulo(texto):
    st.markdown(f'<h1 style="font-size: 28px; border: 2px solid #4CAF50; padding: 10px; border-radius: 8px;">{texto}</h1>', 
                unsafe_allow_html=True)
    
texto_titulo("Filtro de búsqueda de vehículo")
#st.header('Filtro de búsqueda de vehículo')

#build_histogram = st.checkbox('Generar listado de vehículos para la venta')

#if build_histogram:

#hist_button = st.button('Muestra de listado de vehículos para la venta')

#if hist_button:
    # Escribir un mensaje en la aplicación
#    st.write('A continuación primeros 100 datos del listado de vehículos en venta')
#    st.dataframe(car_data.head(100))

all_types = ['Todos'] + sorted(car_data['type'].dropna().unique().tolist())
selected_type = st.selectbox('Selecciona el Tipo de Vehículo', all_types)

# Aplicar el primer filtro al DataFrame
if selected_type != 'Todos':
    data_filtered_by_type = car_data[car_data['type'] == selected_type]
else:
    # Si elige "Todos", no se aplica filtro
    data_filtered_by_type = car_data.copy()

# 2. Segundo Filtro (en cascada): Modelo del Vehículo
# Las opciones del modelo DEPENDEN del tipo seleccionado
available_models = ['Todos'] + sorted(data_filtered_by_type['model'].dropna().unique().tolist())
selected_model = st.selectbox('Selecciona el Modelo', available_models)

# Aplicar el segundo filtro al DataFrame ya filtrado por tipo
if selected_model != 'Todos':
    filtered_data = data_filtered_by_type[data_filtered_by_type['model'] == selected_model]
else:
    filtered_data = data_filtered_by_type


condition_models = ['Todos'] + sorted(filtered_data['condition'].dropna().unique().tolist())
selected_condition = st.selectbox('Selecciona la condición', condition_models)

# Aplicar el segundo filtro al DataFrame ya filtrado por tipo
if selected_condition != 'Todos':
    filtered_condition = filtered_data[filtered_data['condition'] == selected_condition]
else:
    filtered_condition = filtered_data


min_value=int(filtered_condition['price'].min())
max_value=int(filtered_condition['price'].max())

# 2. Verificar y ajustar los valores si min_value >= max_value
if min_value > max_value:
    # Esta situación no debería ocurrir, pero es un resguardo
    min_value, max_value = 0, 1
elif min_value == max_value:
    # Si son iguales, ajusta max_value para que sea mayor
    max_value = min_value + 1  # O cualquier otra lógica que prefieras



# 3. Solo mostrar el slider si hay un rango válido para seleccionar
if min_value < max_value:
    price_range = st.slider(
        'Selecciona el rango de precio',
        min_value=min_value,
        max_value=max_value,
        value=(min_value, max_value)
        )

# 2. ¡ESTE ES EL FILTRO FALTANTE!
# Aplicar el rango de precios seleccionado al DataFrame
    final_filtered_data = filtered_condition[
        (filtered_condition['price'] >= price_range[0]) & 
        (filtered_condition['price'] <= price_range[1])
    ]
else:
    
    st.info("No hay un rango de precios disponible para filtrar con los criterios seleccionados.")
    final_filtered_data = filtered_condition



# Mostrar resultados
st.write(f'Mostrando {len(final_filtered_data)} vehículos de {len(car_data)} totales')
st.dataframe(final_filtered_data)

def texto_titulo2(texto):
    st.markdown(f'<h1 style="font-size: 28px; border: 2px solid #4CAF50; padding: 10px; border-radius: 8px;">{texto}</h1>', 
                unsafe_allow_html=True)
    
texto_titulo2("Distribución de stock por marca")

build_histogram1 = st.checkbox('Construir un histograma')

if build_histogram1:
# Crear un botón en la aplicación Streamlit
#hist_button1 = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
#if hist_button1:
    # Escribir un mensaje en la aplicación
    st.write('Histograma de distribución para el conjunto de datos de anuncios de venta de coches, odómetro')
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución cantidad de autos según Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)



build_histogram2 = st.checkbox('Construir gráfico de dispersión')
if build_histogram2:

#hist_button2 = st.button('Construir gráfico de dispersión')

#if hist_button2:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    #Crear un scatter plot utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig2 = go.Figure(data=[go.Scatter(x=car_data['model_year'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Relación entre Año de Modelo y Precio')

    st.plotly_chart(fig2, use_container_width=True)

    # Mostrar el gráfico Plotly
    #fig.show()
