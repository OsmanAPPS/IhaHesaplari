
from flask import Flask, render_template, request, url_for
import uav_formulas as formulas
import matplotlib.pyplot as plt
import numpy as np
import os
import time

app = Flask(__name__)

# Statik dosyalar için önbellekleme sorununu önle
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def get_form_value(form, name, default=0.0):
    """Formdan değeri float olarak alır, yoksa default döner."""
    return float(form.get(name, default))

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None
    calculation_details = {}

    if request.method == 'POST':
        calculation_type = request.form.get('calculation_type')
        calculation_details = {key: val for key, val in request.form.items()}

        if calculation_type == 'lift':
            rho = get_form_value(request.form, 'rho', 1.225)
            velocity = get_form_value(request.form, 'velocity', 20)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            cl = get_form_value(request.form, 'cl', 0.8)
            lift = formulas.calculate_lift(rho, velocity, wing_area, cl)
            result = f"Hesaplanan Kaldırma Kuvveti: {lift:.2f} N"

        elif calculation_type == 'drag':
            rho = get_form_value(request.form, 'rho', 1.225)
            velocity = get_form_value(request.form, 'velocity', 20)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            cd = get_form_value(request.form, 'cd', 0.04)
            drag = formulas.calculate_drag(rho, velocity, wing_area, cd)
            result = f"Hesaplanan Sürükleme Kuvveti: {drag:.2f} N"

        elif calculation_type == 'thrust':
            rho = get_form_value(request.form, 'rho', 1.225)
            velocity = get_form_value(request.form, 'velocity', 20)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            cd = get_form_value(request.form, 'cd', 0.04)
            thrust = formulas.calculate_thrust_required(rho, velocity, wing_area, cd)
            result = f"Hesaplanan Gerekli İtki: {thrust:.2f} N"

        elif calculation_type == 'power':
            rho = get_form_value(request.form, 'rho', 1.225)
            velocity = get_form_value(request.form, 'velocity', 20)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            cd = get_form_value(request.form, 'cd', 0.04)
            power = formulas.calculate_power_required(rho, velocity, wing_area, cd)
            result = f"Hesaplanan Gerekli Güç: {power:.2f} Watt"

        elif calculation_type == 'stall_speed':
            weight = get_form_value(request.form, 'weight', 50)
            rho = get_form_value(request.form, 'rho', 1.225)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            cl_max = get_form_value(request.form, 'cl_max', 1.2)
            stall_speed = formulas.calculate_stall_speed(weight, rho, wing_area, cl_max)
            result = f"Hesaplanan Perdövites Hızı: {stall_speed:.2f} m/s"

        elif calculation_type == 'wing_loading':
            weight = get_form_value(request.form, 'weight', 50)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            wing_loading = formulas.calculate_wing_loading(weight, wing_area)
            result = f"Hesaplanan Kanat Yüklemesi: {wing_loading:.2f} N/m²"

        elif calculation_type == 'aspect_ratio':
            wingspan = get_form_value(request.form, 'wingspan', 2)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            ar = formulas.calculate_aspect_ratio(wingspan, wing_area)
            result = f"Hesaplanan Kanat Açıklık Oranı: {ar:.2f}"

        elif calculation_type == 'reynolds':
            rho = get_form_value(request.form, 'rho', 1.225)
            velocity = get_form_value(request.form, 'velocity', 20)
            chord_length = get_form_value(request.form, 'chord_length', 0.25)
            viscosity = get_form_value(request.form, 'viscosity', 0.0000181)
            re = formulas.calculate_reynolds_number(rho, velocity, chord_length, viscosity)
            result = f"Hesaplanan Reynolds Sayısı: {re:,.0f}"

        elif calculation_type == 'lift_plot' or calculation_type == 'drag_plot':
            rho = get_form_value(request.form, 'rho', 1.225)
            wing_area = get_form_value(request.form, 'wing_area', 0.5)
            min_v = get_form_value(request.form, 'min_v', 5)
            max_v = get_form_value(request.form, 'max_v', 50)

            velocities = np.linspace(min_v, max_v, 100)
            fig, ax = plt.subplots()

            if calculation_type == 'lift_plot':
                cl = get_form_value(request.form, 'cl', 0.8)
                values = [formulas.calculate_lift(rho, v, wing_area, cl) for v in velocities]
                ax.set_title('Kaldırma Kuvveti vs. Hız')
                ax.set_ylabel('Kaldırma Kuvveti (N)')
            else: # drag_plot
                cd = get_form_value(request.form, 'cd', 0.04)
                values = [formulas.calculate_drag(rho, v, wing_area, cd) for v in velocities]
                ax.set_title('Sürükleme Kuvveti vs. Hız')
                ax.set_ylabel('Sürükleme Kuvveti (N)')

            ax.plot(velocities, values)
            ax.set_xlabel('Hız (m/s)')
            ax.grid(True)

            # Grafiği statik bir dosyaya kaydet
            plot_filename = f"plot_{int(time.time())}.png"
            plot_path = os.path.join('static', plot_filename)
            fig.savefig(plot_path)
            plt.close(fig)
            plot_url = url_for('static', filename=plot_filename)

    return render_template('index.html', result=result, plot_url=plot_url)

if __name__ == '__main__':
    # Gerekli klasörlerin varlığını kontrol et
    if not os.path.exists('static'):
        os.makedirs('static')

    # statik klasöründeki eski grafikleri temizle
    for f in os.listdir('static'):
        if f.endswith('.png'):
            os.remove(os.path.join('static', f))
    app.run(debug=True, port=8080)
