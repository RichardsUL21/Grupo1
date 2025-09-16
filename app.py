import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="SO Libre y Privativo: Historia y Ejemplos",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1 class='main-header'>🖥️ Sistemas Operativos: Libre vs Privativo</h1>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/150px-Tux.svg.png", width=150)
    st.title("📚 Navegación")
    
    seccion = st.radio(
        "Selecciona una sección:",
        ["🏠 Inicio", "📖 Historia", "🔍 Comparación", "💡 Ejemplos", "📊 Estadísticas", "🎯 Quiz Interactivo"]
    )
    
    st.markdown("---")
    st.info("**Grupo #1**\nHistoria y Ejemplos de SO")
    st.markdown("---")
    st.caption(f"Última actualización: {datetime.now().strftime('%d/%m/%Y')}")

# Contenido principal basado en la selección
if seccion == "🏠 Inicio":
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("### 🔓 Software Libre")
        st.write("""
        El software libre es aquel que respeta la libertad de los usuarios sobre su producto adquirido y, 
        por tanto, una vez obtenido puede ser usado, copiado, estudiado, modificado y redistribuido libremente.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='info-box'>", unsafe_allow_html=True)
        st.markdown("### 🔒 Software Privativo")
        st.write("""
        El software privativo es aquel que no permite su libre acceso al código fuente, limitando las 
        posibilidades de modificación y redistribución por parte de los usuarios.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Métricas principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("SO Libres Populares", "15+", "↑ 3 nuevos")
    with col2:
        st.metric("SO Privativos", "5", "→ Estable")
    with col3:
        st.metric("Usuarios Linux", "2.8%", "↑ 0.3%")
    with col4:
        st.metric("Usuarios Windows", "73%", "↓ 1.2%")

elif seccion == "📖 Historia":
    st.markdown("## 📜 Historia de los Sistemas Operativos")
    
    # Timeline interactivo
    eventos = pd.DataFrame({
        'Año': [1969, 1983, 1985, 1991, 1993, 2001, 2004, 2008],
        'Evento': [
            'Creación de UNIX',
            'Richard Stallman inicia GNU',
            'Microsoft lanza Windows 1.0',
            'Linus Torvalds crea Linux',
            'Lanzamiento de Debian',
            'Mac OS X (basado en Unix)',
            'Ubuntu primera versión',
            'Android (basado en Linux)'
        ],
        'Tipo': ['Privativo', 'Libre', 'Privativo', 'Libre', 'Libre', 'Privativo', 'Libre', 'Libre']
    })
    
    fig = px.timeline(
        eventos,
        x_start='Año',
        x_end='Año',
        y='Evento',
        color='Tipo',
        title="Línea de Tiempo de Sistemas Operativos"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Tabs con información histórica
    tab1, tab2 = st.tabs(["🔓 Historia del Software Libre", "🔒 Historia del Software Privativo"])
    
    with tab1:
        st.write("""
        ### El Movimiento del Software Libre
        
        **1983 - Proyecto GNU**: Richard Stallman inicia el proyecto GNU con el objetivo de crear un sistema operativo completamente libre.
        
        **1989 - GPL**: Se publica la primera versión de la Licencia Pública General de GNU.
        
        **1991 - Linux**: Linus Torvalds libera el kernel Linux, completando el sistema GNU/Linux.
        
        **1998 - Open Source**: Se acuña el término "Open Source" como alternativa comercial al "Software Libre".
        """)
        
    with tab2:
        st.write("""
        ### Evolución del Software Privativo
        
        **1975 - Microsoft**: Bill Gates y Paul Allen fundan Microsoft.
        
        **1981 - MS-DOS**: Microsoft desarrolla MS-DOS para IBM PC.
        
        **1985 - Windows**: Lanzamiento de Windows 1.0.
        
        **2001 - Windows XP**: Uno de los SO privativos más exitosos de la historia.
        """)

elif seccion == "🔍 Comparación":
    st.markdown("## ⚖️ Comparación Detallada")
    
    # Tabla comparativa
    comparacion = pd.DataFrame({
        'Característica': [
            'Código Fuente',
            'Costo de Licencia',
            'Personalización',
            'Soporte Técnico',
            'Seguridad',
            'Compatibilidad',
            'Curva de Aprendizaje'
        ],
        'Software Libre': [
            '✅ Accesible',
            '✅ Gratuito (mayoría)',
            '✅ Total',
            '⚠️ Comunidad',
            '✅ Alta transparencia',
            '⚠️ Variable',
            '📈 Media-Alta'
        ],
        'Software Privativo': [
            '❌ Cerrado',
            '💰 Pago',
            '❌ Limitada',
            '✅ Empresarial',
            '⚠️ Opaca',
            '✅ Alta',
            '📉 Baja'
        ]
    })
    
    st.dataframe(comparacion, use_container_width=True, height=300)
    
    # Gráfico de radar
    categorias = ['Libertad', 'Costo', 'Seguridad', 'Soporte', 'Personalización']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=[5, 5, 4, 3, 5],
        theta=categorias,
        fill='toself',
        name='Software Libre'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[1, 2, 3, 5, 2],
        theta=categorias,
        fill='toself',
        name='Software Privativo'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5]
            )),
        showlegend=True,
        title="Comparación por Categorías"
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif seccion == "💡 Ejemplos":
    st.markdown("## 🖥️ Ejemplos de Sistemas Operativos")
    
    tab1, tab2 = st.tabs(["🐧 Sistemas Libres", "🪟 Sistemas Privativos"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### Ubuntu")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Logo-ubuntu_cof-orange-hex.svg/120px-Logo-ubuntu_cof-orange-hex.svg.png", width=100)
            st.write("""
            - **Basado en**: Debian
            - **Interfaz**: GNOME
            - **Uso**: Desktop/Server
            - **Actualización**: Cada 6 meses
            """)
            
        with col2:
            st.markdown("### Fedora")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Fedora_logo.svg/120px-Fedora_logo.svg.png", width=100)
            st.write("""
            - **Patrocinador**: Red Hat
            - **Interfaz**: GNOME
            - **Uso**: Desktop/Server
            - **Enfoque**: Innovación
            """)
            
        with col3:
            st.markdown("### Debian")
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Openlogo-debianV2.svg/120px-Openlogo-debianV2.svg.png", width=100)
            st.write("""
            - **Fundación**: 1993
            - **Interfaz**: Múltiples
            - **Uso**: Universal
            - **Estabilidad**: Muy alta
            """)
        
        st.markdown("---")
        
        # Más ejemplos
        with st.expander("Ver más distribuciones libres"):
            st.write("""
            - **Arch Linux**: Para usuarios avanzados
            - **openSUSE**: Enfoque empresarial
            - **Mint**: Amigable para principiantes
            - **Elementary OS**: Diseño elegante
            - **Manjaro**: Basado en Arch, más fácil
            - **CentOS**: Servidor empresarial
            - **Kali Linux**: Seguridad informática
            - **Zorin OS**: Similar a Windows
            """)
            
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Windows")
            st.write("""
            **Versiones actuales:**
            - Windows 11 (2021)
            - Windows 10 (2015)
            - Windows Server 2022
            
            **Características:**
            - Interfaz familiar
            - Gran compatibilidad
            - Soporte empresarial
            - Actualizaciones regulares
            """)
            
        with col2:
            st.markdown("### macOS")
            st.write("""
            **Versiones recientes:**
            - macOS Sonoma (2023)
            - macOS Ventura (2022)
            - macOS Monterey (2021)
            
            **Características:**
            - Integración con Apple
            - Diseño elegante
            - Basado en Unix
            - Ecosistema cerrado
            """)

elif seccion == "📊 Estadísticas":
    st.markdown("## 📈 Estadísticas de Uso")
    
    # Datos de uso de SO
    uso_so = pd.DataFrame({
        'Sistema Operativo': ['Windows', 'macOS', 'Linux', 'Chrome OS', 'Otros'],
        'Porcentaje': [73.48, 15.42, 2.88, 2.45, 5.77]
    })
    
    # Gráfico de pastel
    fig1 = px.pie(uso_so, values='Porcentaje', names='Sistema Operativo', 
                  title='Cuota de Mercado de Sistemas Operativos (Desktop 2024)')
    st.plotly_chart(fig1, use_container_width=True)
    
    # Tendencias históricas
    años = list(range(2010, 2025))
    windows_trend = [85, 84, 82, 80, 78, 77, 76, 75, 74, 73, 73, 73, 73, 73, 73]
    linux_trend = [1.5, 1.6, 1.8, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.8, 2.9, 2.9]
    macos_trend = [8, 8.5, 9, 10, 11, 12, 13, 14, 14.5, 15, 15.2, 15.3, 15.4, 15.4, 15.4]
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=años, y=windows_trend, mode='lines+markers', name='Windows'))
    fig2.add_trace(go.Scatter(x=años, y=linux_trend, mode='lines+markers', name='Linux'))
    fig2.add_trace(go.Scatter(x=años, y=macos_trend, mode='lines+markers', name='macOS'))
    
    fig2.update_layout(
        title='Tendencia de Uso de SO (2010-2024)',
        xaxis_title='Año',
        yaxis_title='Porcentaje de Uso (%)',
        hovermode='x unified'
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Estadísticas adicionales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🌍 Distribuciones Linux más populares")
        distros = pd.DataFrame({
            'Distribución': ['Ubuntu', 'Debian', 'Mint', 'Manjaro', 'Fedora'],
            'Popularidad': [33.9, 16.2, 11.8, 8.4, 6.5]
        })
        fig3 = px.bar(distros, x='Distribución', y='Popularidad', 
                     title='Top 5 Distribuciones Linux (%)')
        st.plotly_chart(fig3, use_container_width=True)
        
    with col2:
        st.markdown("### 💼 SO en Servidores")
        servidores = pd.DataFrame({
            'Sistema': ['Linux', 'Windows Server', 'Unix', 'Otros'],
            'Porcentaje': [68.2, 28.3, 2.1, 1.4]
        })
        fig4 = px.bar(servidores, x='Sistema', y='Porcentaje',
                     title='SO en Servidores Web (%)')
        st.plotly_chart(fig4, use_container_width=True)

elif seccion == "🎯 Quiz Interactivo":
    st.markdown("## 🎮 Quiz: ¿Cuánto sabes sobre SO Libre y Privativo?")
    
    score = 0
    total_preguntas = 5
    
    st.write("Responde las siguientes preguntas para evaluar tus conocimientos:")
    
    # Pregunta 1
    st.markdown("### Pregunta 1")
    p1 = st.radio(
        "¿Cuál de las siguientes es una característica fundamental del software libre?",
        ["Es siempre gratuito", "Permite acceso al código fuente", "Solo funciona en Linux", "No tiene licencia"],
        key="p1"
    )
    if p1 == "Permite acceso al código fuente":
        score += 1
        
    # Pregunta 2
    st.markdown("### Pregunta 2")
    p2 = st.radio(
        "¿Quién inició el movimiento del software libre?",
        ["Linus Torvalds", "Bill Gates", "Richard Stallman", "Steve Jobs"],
        key="p2"
    )
    if p2 == "Richard Stallman":
        score += 1
        
    # Pregunta 3
    st.markdown("### Pregunta 3")
    p3 = st.radio(
        "¿En qué año se lanzó el kernel Linux?",
        ["1983", "1991", "1995", "2000"],
        key="p3"
    )
    if p3 == "1991":
        score += 1
        
    # Pregunta 4
    st.markdown("### Pregunta 4")
    p4 = st.multiselect(
        "¿Cuáles de los siguientes son sistemas operativos libres? (Selecciona todos los que apliquen)",
        ["Ubuntu", "Windows", "Fedora", "macOS", "Debian", "Android"],
        key="p4"
    )
    respuestas_correctas = ["Ubuntu", "Fedora", "Debian", "Android"]
    if set(p4) == set(respuestas_correctas):
        score += 1
        
    # Pregunta 5
    st.markdown("### Pregunta 5")
    p5 = st.radio(
        "¿Cuál es la principal diferencia entre software libre y open source?",
        [
            "No hay diferencia, son lo mismo",
            "El software libre se enfoca en la libertad, open source en la metodología de desarrollo",
            "Open source es siempre gratuito, software libre no",
            "Software libre es para Linux, open source para todos los SO"
        ],
        key="p5"
    )
    if p5 == "El software libre se enfoca en la libertad, open source en la metodología de desarrollo":
        score += 1
    
    # Botón para mostrar resultados
    if st.button("📊 Ver Resultados", type="primary"):
        st.markdown("---")
        st.markdown(f"### 🏆 Tu puntuación: {score}/{total_preguntas}")
        
        porcentaje = (score/total_preguntas) * 100
        
        if porcentaje == 100:
            st.success("¡Excelente! Eres un experto en SO libre y privativo 🌟")
            st.balloons()
        elif porcentaje >= 80:
            st.success("¡Muy bien! Tienes buenos conocimientos sobre el tema 👏")
        elif porcentaje >= 60:
            st.info("Bien, pero puedes mejorar. Revisa las secciones anteriores 📚")
        else:
            st.warning("Necesitas estudiar más sobre el tema. Te recomendamos revisar toda la información 💪")
        
        # Respuestas correctas
        with st.expander("Ver respuestas correctas"):
            st.write("""
            1. **Permite acceso al código fuente** - Esta es la característica fundamental que define al software libre
            2. **Richard Stallman** - Fundador del movimiento del software libre y del proyecto GNU
            3. **1991** - Linus Torvalds liberó la primera versión del kernel Linux
            4. **Ubuntu, Fedora, Debian, Android** - Todos estos son sistemas operativos basados en software libre
            5. **El software libre se enfoca en la libertad, open source en la metodología de desarrollo** - Aunque comparten código, tienen filosofías diferentes
            """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Desarrollado por Grupo #1 | SO Libre y Privativo: Historia y Ejemplos</p>
    <p>© 2024 - Material educativo</p>
</div>
""", unsafe_allow_html=True)
