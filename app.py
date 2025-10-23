
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import uav_formulas as formulas

# Streamlit sayfa yapılandırması
st.set_page_config(page_title="İHA Tasarım Hesaplayıcı", layout="wide")

st.title("Sabit Kanat İHA Tasarım Hesaplayıcı ve Grafik Aracı")
st.write("Bu uygulama, sabit kanatlı bir İHA'nın temel aerodinamik ve performans hesaplamalarını yapmanıza olanak tanır.")

# Kenar çubuğu (sidebar) menüsü
st.sidebar.title("Hesaplama Seçenekleri")
# Menüdeki "placeholder" seçenekleri kaldır
options = [
    "Kaldırma Kuvveti", "Sürükleme Kuvveti", "Gerekli İtki", "Gerekli Güç",
    "Perdövites Hızı", "Kanat Yüklemesi", "Kanat Açıklık Oranı", "Reynolds Sayısı",
    "Kaldırma Kuvveti vs. Hız Grafiği", "Sürükleme Kuvveti vs. Hız Grafiği"
]
calculation_choice = st.sidebar.selectbox("Lütfen bir hesaplama veya grafik seçin:", options)


# --- HESAPLAMA FONKSİYONLARI ---

if calculation_choice == "Kaldırma Kuvveti":
    st.header("Kaldırma Kuvveti Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    with col2:
        velocity = st.number_input("Hız (m/s)", value=20.0)
        cl = st.number_input("Kaldırma Katsayısı (CL)", value=0.8)
    if st.button("Hesapla"):
        lift = formulas.calculate_lift(rho, velocity, wing_area, cl)
        st.success(f"Hesaplanan Kaldırma Kuvveti: **{lift:.2f} N**")

elif calculation_choice == "Sürükleme Kuvveti":
    st.header("Sürükleme Kuvveti Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    with col2:
        velocity = st.number_input("Hız (m/s)", value=20.0)
        cd = st.number_input("Sürükleme Katsayısı (CD)", value=0.04)
    if st.button("Hesapla"):
        drag = formulas.calculate_drag(rho, velocity, wing_area, cd)
        st.success(f"Hesaplanan Sürükleme Kuvveti: **{drag:.2f} N**")

elif calculation_choice == "Gerekli İtki":
    st.header("Gerekli İtki Hesaplama")
    st.info("Bu hesaplama, düz ve sabit hızlı uçuş için sürükleme kuvvetine eşit olan gerekli itkiyi bulur.")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    with col2:
        velocity = st.number_input("Hız (m/s)", value=20.0)
        cd = st.number_input("Sürükleme Katsayısı (CD)", value=0.04)
    if st.button("Hesapla"):
        thrust = formulas.calculate_thrust_required(rho, velocity, wing_area, cd)
        st.success(f"Hesaplanan Gerekli İtki: **{thrust:.2f} N**")

elif calculation_choice == "Gerekli Güç":
    st.header("Gerekli Güç Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    with col2:
        velocity = st.number_input("Hız (m/s)", value=20.0)
        cd = st.number_input("Sürükleme Katsayısı (CD)", value=0.04)
    if st.button("Hesapla"):
        power = formulas.calculate_power_required(rho, velocity, wing_area, cd)
        st.success(f"Hesaplanan Gerekli Güç: **{power:.2f} Watt**")

elif calculation_choice == "Perdövites Hızı":
    st.header("Perdövites Hızı (Stall Speed) Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Uçak Ağırlığı (N)", value=50.0)
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    with col2:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        cl_max = st.number_input("Maksimum Kaldırma Katsayısı (CL_max)", value=1.2)
    if st.button("Hesapla"):
        stall_speed = formulas.calculate_stall_speed(weight, rho, wing_area, cl_max)
        st.success(f"Hesaplanan Perdövites Hızı: **{stall_speed:.2f} m/s**")

elif calculation_choice == "Kanat Yüklemesi":
    st.header("Kanat Yüklemesi Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Uçak Ağırlığı (N)", value=50.0)
    with col2:
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    if st.button("Hesapla"):
        wing_loading = formulas.calculate_wing_loading(weight, wing_area)
        st.success(f"Hesaplanan Kanat Yüklemesi: **{wing_loading:.2f} N/m²**")

elif calculation_choice == "Kanat Açıklık Oranı":
    st.header("Kanat Açıklık Oranı (Aspect Ratio) Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        wingspan = st.number_input("Kanat Açıklığı (m)", value=2.0)
    with col2:
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
    if st.button("Hesapla"):
        ar = formulas.calculate_aspect_ratio(wingspan, wing_area)
        st.success(f"Hesaplanan Kanat Açıklık Oranı: **{ar:.2f}**")

elif calculation_choice == "Reynolds Sayısı":
    st.header("Reynolds Sayısı Hesaplama")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        velocity = st.number_input("Hız (m/s)", value=20.0)
    with col2:
        chord_length = st.number_input("Ortalama Veter Uzunluğu (m)", value=0.25)
        viscosity = st.number_input("Dinamik Viskozite (Pa.s)", value=1.81e-5, format="%.8f")
    if st.button("Hesapla"):
        re = formulas.calculate_reynolds_number(rho, velocity, chord_length, viscosity)
        st.success(f"Hesaplanan Reynolds Sayısı: **{re:,.0f}**")

# --- GRAFİK FONKSİYONLARI ---

elif calculation_choice == "Kaldırma Kuvveti vs. Hız Grafiği":
    st.header("Kaldırma Kuvveti vs. Hız Grafiği")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
        cl = st.number_input("Kaldırma Katsayısı (CL)", value=0.8)
    with col2:
        min_v = st.number_input("Minimum Hız (m/s)", value=5.0)
        max_v = st.number_input("Maksimum Hız (m/s)", value=50.0)

    if st.button("Grafiği Çiz"):
        velocities = np.linspace(min_v, max_v, 100)
        lifts = [formulas.calculate_lift(rho, v, wing_area, cl) for v in velocities]

        fig, ax = plt.subplots()
        ax.plot(velocities, lifts)
        ax.set_title('Kaldırma Kuvveti vs. Hız')
        ax.set_xlabel('Hız (m/s)')
        ax.set_ylabel('Kaldırma Kuvveti (N)')
        ax.grid(True)
        st.pyplot(fig)

elif calculation_choice == "Sürükleme Kuvveti vs. Hız Grafiği":
    st.header("Sürükleme Kuvveti vs. Hız Grafiği")
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Hava Yoğunluğu (kg/m³)", value=1.225, format="%.4f")
        wing_area = st.number_input("Kanat Alanı (m²)", value=0.5)
        cd = st.number_input("Sürükleme Katsayısı (CD)", value=0.04)
    with col2:
        min_v = st.number_input("Minimum Hız (m/s)", value=5.0)
        max_v = st.number_input("Maksimum Hız (m/s)", value=50.0)

    if st.button("Grafiği Çiz"):
        velocities = np.linspace(min_v, max_v, 100)
        drags = [formulas.calculate_drag(rho, v, wing_area, cd) for v in velocities]

        fig, ax = plt.subplots()
        ax.plot(velocities, drags)
        ax.set_title('Sürükleme Kuvveti vs. Hız')
        ax.set_xlabel('Hız (m/s)')
        ax.set_ylabel('Sürükleme Kuvveti (N)')
        ax.grid(True)
        st.pyplot(fig)
