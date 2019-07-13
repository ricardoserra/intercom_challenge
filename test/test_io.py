from pytest import raises

from src.io import bytes_to_json, read_customers


def test_simple_bytes_to_json():
    result = bytes_to_json(b'{"a":1}')
    assert 'a' in result
    assert result['a'] == 1


def test_customer_bytes_to_json():
    customer = bytes_to_json(b'{\"latitude\": \"52.986375\", \"user_id\": 12, \"name\": \
                             \"Christina McArdle\", \"longitude\": \"-6.043701\"}')
    assert len(customer.keys()) == 4
    assert customer['user_id'] == 12
    assert customer['name'] == "Christina McArdle"


def test_invalid_bytes_to_json():
    with raises(AttributeError):
        bytes_to_json('{\"latitude\": \"52.986375\"}')


def test_valid_customers_url():
    customers = read_customers("https://s3.amazonaws.com/intercom-take-home-test/customers.txt#")
    assert len(customers) == 32
    assert customers[0]["name"] == "Christina McArdle"
    for customer in customers:
        assert len(customer) == 4
        assert 'user_id' in customer
        assert 'name' in customer
        assert 'latitude' in customer
        assert 'longitude' in customer
