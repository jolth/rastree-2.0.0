import math

def distance(lat_start, lng_start, lat_end, lng_end):
    """Calculate the distance of kilometers between two points""" 
    radius_earth = 6371
    lat = (lat_end - lat_start) * (math.pi / 180)
    lng = (lng_end - lng_start) * (math.pi / 180)
    a = math.sin(lat / 2) * math.sin(lat / 2) + math.cos(lat_start * (math.pi /
        180)) * math.cos(lat_end * (math.pi / 180)) * math.sin(lng / 2) *\
        math.sin(lng / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c


if __name__ == '__main__':
    lt_s = input("Ingrese el lat_start:") # 42.990967 
    lg_s = input("Ingrese el lng_start:") # -71.463767
    lt_e = input("Ingrese el lat_end:") # 41.990967 
    lg_e = input("Ingrese el lng_end:") # -70.463767
    print(distance(float(lt_s), float(lg_s), float(lt_e), float(lg_e)))

