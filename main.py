from src.io import read_customers
from src.distance import distance_between_points

DUBLIN_OFFICE_COORDINATES = (53.339428, -6.257664)

if __name__ == "__main__":
    customers = read_customers("https://s3.amazonaws.com/intercom-take-home-test/customers.txt#")
    matching = []

    for customer in customers:
        # Calculates distance between 'customer' and Intercom's Dublin office
        distance = distance_between_points(
            DUBLIN_OFFICE_COORDINATES[0], DUBLIN_OFFICE_COORDINATES[1],
            customer["latitude"], customer["longitude"])

        # Adds customer to 'matching' list if distance is 100KM maximum
        if distance <= 100:
            matching.append(customer)

    # Sorts 'matching' list in-place, by 'user_id' in asceding order
    matching.sort(key=lambda k: k["user_id"])
