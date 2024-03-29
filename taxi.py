def taxi_fare(distance):
    return(round((base + add * distance/140), 2))
base = 4
add = 0.25
distance = int(input("Введите расстояние в м:"))
print('Стоимость поездки: ', taxi_fare(distance))
