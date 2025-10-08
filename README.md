# Vehicles_BI
Vehicles description , markets, trends and graphics

Resumen de la Aplicación: Sistema de Búsqueda y Cotización de Vehículos
Propósito General:

Esta es una aplicación web interactiva desarrollada con Streamlit que permite a los usuarios buscar, filtrar y cotizar financieramente vehículos usados a partir de un dataset completo. La aplicación combina análisis de datos con herramientas de simulación financiera.

Estructura y Secciones Principales:
1. Configuración Visual y Estilos
Fondo personalizado en color gainsboro con CSS
Diseño de recuadros para headers y contenido
Imagen de portada para mejorar la experiencia visual

2. Sistema de Filtros en Cascada
Sistema de filtrado donde cada selección afecta las opciones siguientes:
Filtro por Tipo (SUV, sedan, truck, etc.)
Filtro por Modelo (depende de los encontrados en el dataset)
Filtro por Condición (excellent, good, fair, etc.)
Filtro por Rango de Precio (con slider de streamlit dinámico)

3. Visualización de Resultados
DataFrame interactivo con los vehículos filtrados
Contador de resultados (vehículos mostrados vs. totales)
Histograma de precios de los vehículos filtrados

4. Cotizador Financiero Avanzado
Características principales:

Selección automática del vehículo más económico encontrado
Cálculo de cuota mensual usando fórmula de amortización francesa
Simulación con parámetros ajustables (3-7 años de plazo)
Tasa de interés del 24% EA (efectiva anual)
Desglose visual del total a pagar (capital vs. intereses)

Componentes del cotizador:
Métricas financieras en columnas (cuota, total, costo financiero)
Gráfico de pastel para composición de pagos
Tabla de amortización (primeros 12 meses)
Información detallada de condiciones del crédito

5. Análisis General del Dataset
Histograma adicional de distribución por año de fabricación
Filtrado por condición del vehículo
Visualización completa de todo el inventario

Tecnologías Utilizadas
Streamlit para la interfaz web
Pandas para manipulación de datos
Plotly para gráficos interactivos
PIL para manejo de imágenes


FUNCIONALIDAD:

Esta aplicación permite a potenciales compradores de vehículos:
Encontrar opciones que se ajusten a sus criterios específicos
Identificar el vehículo más económico dentro de sus preferencias
Simular escenarios financieros realistas antes de comprar
Entender claramente el costo total del financiamiento
Tomar decisiones informadas basadas en datos concretos
La aplicación transforma datos crudos de vehículos en información accionable y comprensible para el usuario final, facilitando el proceso de búsqueda y evaluación financiera de opciones vehiculares.


Enlace RENDER.COM : https://vehicles-bi.onrender.com

