import random


def race_car():
    ############### variable ##############
    car_count = 0
    cars_names = []
    index_cars = []
    road = ''
    #######################################

    try:
        n = int(input('count of cars : '))

        while car_count != n:
            name = input('your cars names : ')
            cars_names.append(name)
            index_cars.append(random.randint(1, 10))
            car_count += 1

        while len(road) != 300:
            road += '-'

        for num in range(0, car_count):
            road = road[:index_cars[num]] + \
                str(cars_names[num]) + road[index_cars[num]+1:]

        print(road)
        print(index_cars)

        while max(index_cars) <= 300:

            for car in cars_names:
                new_ind = road.index(car) + random.randint(1, 10)
                print(road.index(car))
                index_cars.clear()
                index_cars.append(new_ind)
                road = road.replace(car, '-')
                road = road[:new_ind] + str(car) + road[new_ind + 1:]

                for car in cars_names:
                    if car not in road:
                        road = road[:0] + str(car) + road[1:]

            print(road)
        print(index_cars)

        print(road[-1], ' is winner')

    except NameError and ValueError:
        print('this is not number!')


race_car()
