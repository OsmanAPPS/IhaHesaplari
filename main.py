
import matplotlib.pyplot as plt
import numpy as np
import uav_formulas as formulas

def get_float_input(prompt):
    """Sayısal bir girdi almak için yardımcı fonksiyon."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Hatalı giriş. Lütfen sayısal bir değer girin.")

def plot_lift_vs_velocity(rho, wing_area, cl, min_velocity, max_velocity):
    """Kaldırma Kuvveti vs. Hız grafiğini çizer."""
    velocities = np.linspace(min_velocity, max_velocity, 100)
    lifts = [formulas.calculate_lift(rho, v, wing_area, cl) for v in velocities]
    plt.figure(figsize=(10, 6))
    plt.plot(velocities, lifts)
    plt.title('Kaldırma Kuvveti vs. Hız')
    plt.xlabel('Hız (m/s)')
    plt.ylabel('Kaldırma Kuvveti (N)')
    plt.grid(True)
    plt.savefig('lift_vs_velocity.png')
    print("Grafik 'lift_vs_velocity.png' olarak kaydedildi.")
    plt.show()

def plot_drag_vs_velocity(rho, wing_area, cd, min_velocity, max_velocity):
    """Sürükleme Kuvveti vs. Hız grafiğini çizer."""
    velocities = np.linspace(min_velocity, max_velocity, 100)
    drags = [formulas.calculate_drag(rho, v, wing_area, cd) for v in velocities]
    plt.figure(figsize=(10, 6))
    plt.plot(velocities, drags)
    plt.title('Sürükleme Kuvveti vs. Hız')
    plt.xlabel('Hız (m/s)')
    plt.ylabel('Sürükleme Kuvveti (N)')
    plt.grid(True)
    plt.savefig('drag_vs_velocity.png')
    print("Grafik 'drag_vs_velocity.png' olarak kaydedildi.")
    plt.show()

def main_menu():
    """Ana menüyü gösterir ve kullanıcı seçimini yönetir."""
    while True:
        print("\n--- İHA Hesaplama ve Grafik Aracı ---")
        print("1. Kaldırma Kuvveti Hesapla (Tek Değer)")
        print("2. Sürükleme Kuvveti Hesapla (Tek Değer)")
        print("3. Gerekli İtki Hesapla")
        print("4. Gerekli Güç Hesapla")
        print("5. Perdövites Hızı Hesapla")
        print("6. Kanat Yüklemesi Hesapla")
        print("7. Kanat Açıklık Oranı Hesapla")
        print("8. Reynolds Sayısı Hesapla")
        print("9. Kaldırma Kuvveti vs. Hız Grafiği")
        print("10. Sürükleme Kuvveti vs. Hız Grafiği")
        print("0. Çıkış")

        choice = input("Lütfen yapmak istediğiniz işlemi seçin: ")

        if choice == '1':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            v = get_float_input("Hız (m/s): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cl = get_float_input("Kaldırma katsayısı: ")
            lift = formulas.calculate_lift(rho, v, a, cl)
            print(f"-> Hesaplanan Kaldırma Kuvveti: {lift:.2f} N")

        elif choice == '2':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            v = get_float_input("Hız (m/s): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cd = get_float_input("Sürükleme katsayısı: ")
            drag = formulas.calculate_drag(rho, v, a, cd)
            print(f"-> Hesaplanan Sürükleme Kuvveti: {drag:.2f} N")

        elif choice == '3':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            v = get_float_input("Hız (m/s): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cd = get_float_input("Sürükleme katsayısı: ")
            thrust = formulas.calculate_thrust_required(rho, v, a, cd)
            print(f"-> Hesaplanan Gerekli İtki: {thrust:.2f} N")

        elif choice == '4':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            v = get_float_input("Hız (m/s): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cd = get_float_input("Sürükleme katsayısı: ")
            power = formulas.calculate_power_required(rho, v, a, cd)
            print(f"-> Hesaplanan Gerekli Güç: {power:.2f} Watt")

        elif choice == '5':
            weight = get_float_input("Uçak ağırlığı (N): ")
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cl_max = get_float_input("Maksimum kaldırma katsayısı (CL_max): ")
            stall_speed = formulas.calculate_stall_speed(weight, rho, a, cl_max)
            print(f"-> Hesaplanan Perdövites Hızı: {stall_speed:.2f} m/s")

        elif choice == '6':
            weight = get_float_input("Uçak ağırlığı (N): ")
            a = get_float_input("Kanat alanı (m^2): ")
            wing_loading = formulas.calculate_wing_loading(weight, a)
            print(f"-> Hesaplanan Kanat Yüklemesi: {wing_loading:.2f} N/m^2")

        elif choice == '7':
            span = get_float_input("Kanat açıklığı (m): ")
            a = get_float_input("Kanat alanı (m^2): ")
            ar = formulas.calculate_aspect_ratio(span, a)
            print(f"-> Hesaplanan Kanat Açıklık Oranı: {ar:.2f}")

        elif choice == '8':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            v = get_float_input("Hız (m/s): ")
            chord = get_float_input("Ortalama veter uzunluğu (m): ")
            viscosity = get_float_input("Dinamik viskozite (Pa.s, deniz seviyesinde ~1.81e-5): ")
            re = formulas.calculate_reynolds_number(rho, v, chord, viscosity)
            print(f"-> Hesaplanan Reynolds Sayısı: {re:.2f}")

        elif choice == '9':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cl = get_float_input("Kaldırma katsayısı: ")
            min_v = get_float_input("Minimum hız (m/s): ")
            max_v = get_float_input("Maksimum hız (m/s): ")
            plot_lift_vs_velocity(rho, a, cl, min_v, max_v)

        elif choice == '10':
            rho = get_float_input("Hava yoğunluğu (kg/m^3): ")
            a = get_float_input("Kanat alanı (m^2): ")
            cd = get_float_input("Sürükleme katsayısı: ")
            min_v = get_float_input("Minimum hız (m/s): ")
            max_v = get_float_input("Maksimum hız (m/s): ")
            plot_drag_vs_velocity(rho, a, cd, min_v, max_v)

        elif choice == '0':
            print("Uygulamadan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim. Lütfen menüden bir numara girin.")

if __name__ == '__main__':
    main_menu()
