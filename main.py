from car import Car


def main():
    car_list = []
    while True:
        brand = input('Marke > ')
        if brand != '':
            model = input('Modell > ')
            construction = input('Baujahr > ')
            car = Car(brand, model, construction)
            car_list.append(car)
        else:
            break

    for car in car_list:
        print(car.construction)
        print(car.brand)
        print(car.model)


if __name__ == '__main__':
    main()
