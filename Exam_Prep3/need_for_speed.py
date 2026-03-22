number_of_cars = int(input())

car_collection = {}
for _ in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    car_collection[car] = [int(mileage), int(fuel)]

command = input()
while command != "Stop":
    parts = command.split(" : ")
    type_of_command = parts[0]
    car = parts[1]

    if type_of_command == "Drive":
        distance = int(parts[2])
        fuel = int(parts[3])

        if fuel > car_collection[car][1]:
            print(f"Not enough fuel to make that ride")
        else:
            car_collection[car][1] -= fuel
            car_collection[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_collection[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del car_collection[car]

    elif type_of_command == "Refuel":
        fuel = int(parts[2])
        last_car_fuel = car_collection[car][1]
        car_collection[car][1] += fuel
        if car_collection[car][1] > 75:
            car_collection[car][1] = 75
            fuel = car_collection[car][1] - last_car_fuel
        print(f"{car} refueled with {fuel} liters")


    elif type_of_command == "Revert":
        kilometers = int(parts[2])
        car_collection[car][0] -= kilometers
        if car_collection[car][0] < 10000:
            car_collection[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for car, values in car_collection.items():
    mileage = values[0]
    fuel = values[1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")