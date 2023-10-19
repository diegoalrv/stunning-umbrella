import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuración de la página de Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title="Dashboard con Streamlit",
    layout="wide"
)

# Título del dashboard
st.title("Dashboard con Radar Plot y Histogramas")

# Crear datos aleatorios para el radar plot
categorias = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D', 'Categoría E']
valores = np.random.randint(1, 10, len(categorias))

# Crear el radar plot
fig, ax = plt.subplots(figsize=(3, 3))
ax = plt.subplot(111, polar=True)
angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
# angulos += angulos[:1]
valores += valores[:1]
ax.fill(angulos, valores, 'b', alpha=0.1)
ax.set_thetagrids(np.degrees(angulos), categorias)
ax.set_title('Radar Plot')

ax.set_xticklabels([])
ax.set_yticklabels([])

# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
# ax.spines['left'].set_visible(False)
ax.tick_params(False)

st.pyplot(fig)

# Crear datos aleatorios para los histogramas
data = {
    'Histograma 1': np.random.randn(1000),
    'Histograma 2': np.random.randn(1000) + 2,
    # 'Histograma 3': np.random.randn(1000) - 2
}

# Crear un DataFrame con los datos
df = pd.DataFrame(data)

# Crear histogramas
# st.subheader('Histogramas')
# for col in df.columns:
#     st.write(f'**{col}**: ')
#     plt.hist(df[col], bins=20)
#     st.pyplot()

# Nota: Puedes personalizar aún más la apariencia y la disposición de los gráficos según tus necesidades.

# Código para ejecutar el dashboard
if __name__ == '__main__':
    st.sidebar.markdown("Configuraciones")
    st.sidebar.markdown("Personaliza las opciones del dashboard aquí.")
    st.sidebar.checkbox("Mostrar gráfico de radar", True)
    st.sidebar.checkbox("Mostrar histogramas", True)