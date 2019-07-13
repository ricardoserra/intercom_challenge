import json
import os

from pytest import raises

from src.io import bytes_to_json, read_customers, write_to_file


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


def test_invalid_customers_url():
    with raises(json.JSONDecodeError):
        read_customers("https://www.intercom.com")


def test_valid_write_to_file():
    file_name = 'test.txt'
    array = [{"index": 1, "name": "foo"}, {"index": 2, "name": "bar"}]
    # make sure 'file_name' doesn't exist
    if os.path.exists(file_name):
        os.remove(file_name)

    write_to_file(array, file_name)
    # 'file_name' must exist
    assert os.path.exists(file_name)
    f = open(file_name, 'r')
    # first line should the array[0] plus \n
    assert f.readline() == '{\"index\": 1, \"name\": \"foo\"}\n'
    f.close()
    
    os.remove(file_name)


def test_write_to_file_wrong_array():
    file_name = 'test.txt'
    array = 12345
    with raises(TypeError):
        write_to_file(array, file_name)

    os.remove(file_name)
