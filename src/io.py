import urllib.request
import json


def bytes_to_json(line):
    # converts 'line' from bytes to string
    decoded = line.decode('utf-8')
    # deserializes 'decoded' string to a JSON obj
    return json.loads(decoded)


def read_customers(url):
    """ Reads from Intercom's customer URL and returns a list
    with JSON objects for each customer
    Parameters:
        url (string): URL to read customers
    Returns:
        customers (list): List with each customer (JSON object)
    """
    # opens 'url' using urllib
    data = urllib.request.urlopen(url)
    # customers to be returned
    customers = []

    # iterate each 'line' of data
    for line in data:
        # converts 'line' to a JSON object
        customer_json = bytes_to_json(line)
        # inserts 'customer_jon' to 'customers' list
        customers.append(customer_json)

    return customers
