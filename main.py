from src.io import read_customers, write_to_file
from src.distance import distance_between_points

DUBLIN_OFFICE_COORDINATES = (53.339428, -6.257664)

if __name__ == "__main__":
    # reads URL and returns a list of customers
    customers = read_customers("https://s3.amazonaws.com/intercom-take-home-test/customers.txt#")
    matching = []

    # for every 'customer' in 'customers'
    for customer in customers:
        # calculates distance between 'customer' and Intercom's Dublin office
        distance = distance_between_points(
            DUBLIN_OFFICE_COORDINATES[0], DUBLIN_OFFICE_COORDINATES[1],
            customer["latitude"], customer["longitude"])

        # adds customer to 'matching' list if distance is 100KM maximum
        if distance <= 100:
            matching.append(customer)

    # sorts 'matching' list in-place, by 'user_id' in ascending order
    matching.sort(key=lambda k: k["user_id"])

    # writes 'matching' customers to a file named 'output.txt'
    write_to_file(matching, "output.txt")
