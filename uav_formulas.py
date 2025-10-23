import numpy as np

def calculate_lift(rho, velocity, wing_area, cl):
    """
    Kaldırma kuvvetini hesaplar.

    Args:
        rho (float): Hava yoğunluğu (kg/m^3)
        velocity (float): Hız (m/s)
        wing_area (float): Kanat alanı (m^2)
        cl (float): Kaldırma katsayısı

    Returns:
        float: Kaldırma Kuvveti (N)
    """
    return 0.5 * rho * velocity**2 * wing_area * cl

def calculate_drag(rho, velocity, wing_area, cd):
    """
    Sürükleme kuvvetini hesaplar.

    Args:
        rho (float): Hava yoğunluğu (kg/m^3)
        velocity (float): Hız (m/s)
        wing_area (float): Kanat alanı (m^2)
        cd (float): Sürükleme katsayısı

    Returns:
        float: Sürükleme Kuvveti (N)
    """
    return 0.5 * rho * velocity**2 * wing_area * cd

def calculate_thrust_required(rho, velocity, wing_area, cd):
    """
    Gerekli itkiyi hesaplar (Düz ve sabit hızlı uçuş için Sürüklemeye eşittir).

    Args:
        rho (float): Hava yoğunluğu (kg/m^3)
        velocity (float): Hız (m/s)
        wing_area (float): Kanat alanı (m^2)
        cd (float): Sürükleme katsayısı

    Returns:
        float: Gerekli İtki (N)
    """
    return calculate_drag(rho, velocity, wing_area, cd)

def calculate_power_required(rho, velocity, wing_area, cd):
    """
    Gerekli gücü hesaplar.

    Args:
        rho (float): Hava yoğunluğu (kg/m^3)
        velocity (float): Hız (m/s)
        wing_area (float): Kanat alanı (m^2)
        cd (float): Sürükleme katsayısı

    Returns:
        float: Gerekli Güç (Watt)
    """
    thrust_required = calculate_thrust_required(rho, velocity, wing_area, cd)
    return thrust_required * velocity

def calculate_wing_loading(weight, wing_area):
    """
    Kanat yüklemesini hesaplar.

    Args:
        weight (float): Uçağın ağırlığı (N)
        wing_area (float): Kanat alanı (m^2)

    Returns:
        float: Kanat Yüklemesi (N/m^2)
    """
    return weight / wing_area

def calculate_stall_speed(weight, rho, wing_area, cl_max):
    """
    Perdövites hızını hesaplar.

    Args:
        weight (float): Uçağın ağırlığı (N)
        rho (float): Hava yoğunluğu (kg/m^3)
        wing_area (float): Kanat alanı (m^2)
        cl_max (float): Maksimum kaldırma katsayısı

    Returns:
        float: Perdövites Hızı (m/s)
    """
    return np.sqrt((2 * weight) / (rho * wing_area * cl_max))

def calculate_aspect_ratio(wingspan, wing_area):
    """
    Kanat açıklık oranını hesaplar.

    Args:
        wingspan (float): Kanat açıklığı (m)
        wing_area (float): Kanat alanı (m^2)

    Returns:
        float: Kanat Açıklık Oranı
    """
    return wingspan**2 / wing_area

def calculate_reynolds_number(rho, velocity, chord_length, viscosity):
    """
    Reynolds sayısını hesaplar.

    Args:
        rho (float): Hava yoğunluğu (kg/m^3)
        velocity (float): Hız (m/s)
        chord_length (float): Ortalama aerodinamik veter uzunluğu (m)
        viscosity (float): Dinamik viskozite (Pa.s)

    Returns:
        float: Reynolds Sayısı
    """
    return (rho * velocity * chord_length) / viscosity
