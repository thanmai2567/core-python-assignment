def calculate_fare(distance):
    base_fare = 50  # Base fare
    distance_fare = 10  # Fare per km
    return base_fare + (distance * distance_fare)


num_trips = int(input("Enter the number of trips: "))


trips = []
for i in range(num_trips):
    distance = float(input(f"Enter the distance for trip {i + 1} (in km): "))
    trips.append(distance)

total_fare = 0

for i, distance in enumerate(trips, 1):
    fare = calculate_fare(distance)
    total_fare += fare
    print(f"Trip {i}: ${fare}")


print(f"Total Fare: ${total_fare}")
