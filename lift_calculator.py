
import matplotlib.pyplot as plt
import numpy as np

def calculate_lift(rho, velocity, wing_area, cl):
    """
    Calculates the lift force.

    Args:
        rho (float): Air density (kg/m^3)
        velocity (float): Velocity (m/s)
        wing_area (float): Wing area (m^2)
        cl (float): Lift coefficient

    Returns:
        float: Lift force (N)
    """
    return 0.5 * rho * velocity**2 * wing_area * cl

def plot_lift_vs_velocity(rho, wing_area, cl, min_velocity, max_velocity):
    """
    Plots the lift force vs. velocity.

    Args:
        rho (float): Air density (kg/m^3)
        wing_area (float): Wing area (m^2)
        cl (float): Lift coefficient
        min_velocity (float): Minimum velocity for the plot (m/s)
        max_velocity (float): Maximum velocity for the plot (m/s)
    """
    velocities = np.linspace(min_velocity, max_velocity, 100)
    lifts = [calculate_lift(rho, v, wing_area, cl) for v in velocities]

    plt.figure(figsize=(10, 6))
    plt.plot(velocities, lifts)
    plt.title('Kaldırma Kuvveti vs. Hız')
    plt.xlabel('Hız (m/s)')
    plt.ylabel('Kaldırma Kuvveti (N)')
    plt.grid(True)
    plt.savefig('lift_vs_velocity.png')
    plt.show()

if __name__ == '__main__':
    # Kullanıcıdan girdileri al
    try:
        rho = float(input("Hava yoğunluğunu girin (kg/m^3, deniz seviyesi için ~1.225): "))
        wing_area = float(input("Kanat alanını girin (m^2): "))
        cl = float(input("Kaldırma katsayısını girin (genellikle 0.1 ile 1.5 arasında): "))
        min_velocity = float(input("Minimum hızı girin (m/s): "))
        max_velocity = float(input("Maksimum hızı girin (m/s): "))

        # Grafiği çiz
        plot_lift_vs_velocity(rho, wing_area, cl, min_velocity, max_velocity)

        print("Grafik 'lift_vs_velocity.png' olarak kaydedildi.")

    except ValueError:
        print("Hatalı giriş. Lütfen sayısal değerler girin.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
