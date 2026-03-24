import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ── Configuración de la página ────────────────────────────
st.set_page_config(
    page_title="Bienestar Equino — Predictor Clínico",
    page_icon="🐴",
    layout="centered"
)

# ── Cargar modelos ────────────────────────────────────────
@st.cache_resource
def cargar_modelos():
    with open('modelo_equino.pkl', 'rb') as f:
        modelo = pickle.load(f)
    with open('scaler_equino.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('label_encoder.pkl', 'rb') as f:
        le = pickle.load(f)
    with open('features.pkl', 'rb') as f:
        features = pickle.load(f)
    return modelo, scaler, le, features

modelo, scaler, le, features = cargar_modelos()

# ── Encabezado ────────────────────────────────────────────
st.title("🐴 Predictor de Bienestar Equino")
st.subheader("Herramienta de apoyo clínico veterinario")
st.markdown("""
> *"Los datos clínicos cuentan una historia de sufrimiento
> o bienestar antes de que cualquier diagnóstico sea evidente."*
""")
st.divider()

# ── Aviso clínico ─────────────────────────────────────────
st.warning("""
⚠️ **Aviso importante:** Esta herramienta es un apoyo clínico
basado en Machine Learning. No reemplaza el diagnóstico
veterinario profesional.
""")

# ── Formulario de entrada ─────────────────────────────────
st.header("📋 Datos clínicos del caballo")

col1, col2 = st.columns(2)

with col1:
    age = st.selectbox("Edad",
        options=[0, 1],
        format_func=lambda x: "Adulto" if x == 0 else "Joven")

    pulse = st.slider("Pulso (ppm)",
        min_value=30, max_value=184, value=60,
        help="Rango normal: 28-44 ppm")

    rectal_temp = st.slider("Temperatura rectal (°C)",
        min_value=35.0, max_value=41.0, value=38.2,
        step=0.1, help="Rango normal: 37.5-38.5°C")

    respiratory_rate = st.slider("Frecuencia respiratoria",
        min_value=8, max_value=96, value=20,
        help="Rango normal: 8-16 rpm")

    surgery = st.selectbox("¿Requirió cirugía?",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Sí")

with col2:
    pain = st.selectbox("Nivel de dolor",
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: {
            0: "Sin dolor",
            1: "Deprimido",
            2: "Dolor leve",
            3: "Dolor severo",
            4: "Dolor extremo"
        }[x])

    peristalsis = st.selectbox("Peristalsis",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Ausente",
            1: "Hipomotil",
            2: "Normal",
            3: "Hipermotil"
        }[x])

    packed_cell_volume = st.slider("Volumen celular (%)",
        min_value=23, max_value=75, value=45)

    total_protein = st.slider("Proteína total (g/dl)",
        min_value=3.0, max_value=89.0, value=7.5,
        step=0.1)

    abdominal_distention = st.selectbox("Distensión abdominal",
        options=[0, 1, 2, 3],
        format_func=lambda x: {
            0: "Ninguna",
            1: "Leve",
            2: "Moderada",
            3: "Severa"
        }[x])

st.divider()

# ── Calcular índice de bienestar ──────────────────────────
def calcular_bienestar(pulse, rectal_temp, pain, peristalsis):
    score = 0
    if pulse <= 44:
        score += 3
    elif pulse <= 60:
        score += 2
    elif pulse <= 80:
        score += 1
    if 37.5 <= rectal_temp <= 38.5:
        score += 2
    elif 37.0 <= rectal_temp <= 39.0:
        score += 1
    if pain == 0:
        score += 3
    elif pain == 1:
        score += 2
    elif pain == 2:
        score += 1
    if peristalsis == 2:
        score += 2
    elif peristalsis == 1:
        score += 1
    return score

def nivel_bienestar(score):
    if score >= 8:
        return "Alto", "🟢"
    elif score >= 5:
        return "Moderado", "🟡"
    elif score >= 2:
        return "Bajo", "🟠"
    else:
        return "Crítico", "🔴"

# ── Botón de predicción ───────────────────────────────────
if st.button("🔍 Analizar caballo", type="primary",
             use_container_width=True):

    # Construir vector de entrada con todos los features
    entrada = {f: 0 for f in features}
    entrada['age']                  = age
    entrada['pulse']                = pulse
    entrada['rectal_temp']          = rectal_temp
    entrada['respiratory_rate']     = respiratory_rate
    entrada['surgery']              = surgery
    entrada['pain']                 = pain
    entrada['peristalsis']          = peristalsis
    entrada['packed_cell_volume']   = packed_cell_volume
    entrada['total_protein']        = total_protein
    entrada['abdominal_distention'] = abdominal_distention

    # Calcular índice de bienestar
    idx_bienestar = calcular_bienestar(
        pulse, rectal_temp, pain, peristalsis)
    entrada['indice_bienestar'] = idx_bienestar

    # Preparar y escalar
    X_entrada = pd.DataFrame([entrada])[features]
    X_scaled  = scaler.transform(X_entrada)

    # Predecir
    prediccion   = modelo.predict(X_scaled)
    probabilidad = modelo.predict_proba(X_scaled)[0]
    resultado    = le.inverse_transform(prediccion)[0]

    # Índice de bienestar
    nivel, emoji = nivel_bienestar(idx_bienestar)

    st.divider()
    st.header("📊 Resultado del análisis")

    # Resultado principal
    if resultado == 'lived':
        st.success("## ✅ PRONÓSTICO: SOBREVIVIRÁ")
    elif resultado == 'died':
        st.error("## ❌ PRONÓSTICO: ALTO RIESGO DE MUERTE")
    else:
        st.warning("## ⚠️ PRONÓSTICO: CONSIDERAR EUTANASIA")

    # Probabilidades
    st.subheader("📈 Probabilidades por resultado")
    col1, col2, col3 = st.columns(3)
    clases = le.classes_
    nombres = {
        'lived'     : '✅ Sobrevive',
        'died'      : '❌ Muere',
        'euthanized': '⚠️ Eutanasia'
    }
    for col, clase, prob in zip([col1, col2, col3],
                                 clases, probabilidad):
        col.metric(nombres[clase], f"{prob*100:.1f}%")

    # Índice de bienestar
    st.subheader("🏥 Índice de Bienestar Equino")
    col1, col2 = st.columns(2)
    col1.metric("Puntuación", f"{idx_bienestar}/9")
    col2.metric("Nivel", f"{emoji} {nivel}")

    st.progress(idx_bienestar / 9)

    # Alertas clínicas
    st.subheader("⚠️ Alertas clínicas")
    alertas = []
    if pulse > 80:
        alertas.append(
            "🔴 Pulso muy elevado — estrés cardiovascular severo")
    elif pulse > 60:
        alertas.append(
            "🟡 Pulso elevado — monitorear de cerca")
    if rectal_temp > 39.0:
        alertas.append(
            "🔴 Temperatura alta — posible infección")
    elif rectal_temp < 37.0:
        alertas.append(
            "🔴 Temperatura baja — hipotermia")
    if pain >= 3:
        alertas.append(
            "🔴 Dolor severo — requiere atención inmediata")
    if peristalsis == 0:
        alertas.append(
            "🔴 Peristalsis ausente — riesgo de cólico")
    if total_protein > 8.5:
        alertas.append(
            "🟡 Proteína elevada — posible deshidratación")

    if alertas:
        for alerta in alertas:
            st.warning(alerta)
    else:
        st.success("✅ Sin alertas clínicas críticas detectadas")

    st.divider()
    st.caption("""
    ⚠️ Este modelo es una herramienta de apoyo clínico con
    65% de accuracy. No reemplaza el diagnóstico veterinario
    profesional. Desarrollado por Jorge Ojeda — ONE Alura LATAM 2026.
    """)