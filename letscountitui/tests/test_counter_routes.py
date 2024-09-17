"""Tests the pages retrieving the counters"""

from unittest.mock import patch

from flask import url_for


def test_list_counters_page(client):
    response = client.get(url_for("counter.list_counters"))
    assert response.status_code == 200
    assert b"Counters" in response.data


def test_list_counters_page_no_data(client):
    with patch("letscountitui.utilities.utils.DataRetrieval.get_data") as mock_get_data:
        mock_get_data.return_value = []
        response = client.get(url_for("counter.list_counters"))
        assert response.status_code == 200
        assert b"0" in response.data


def test_list_counters_page_with_counters(client):
    """Tests the list counters page with some counters"""
    with patch("letscountitui.utilities.utils.DataRetrieval.get_data") as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 0,
            },
            {
                "uuid": "80e09736-565f-43da-b2db-25a616ad3caf",
                "name": "test",
                "count": 0,
            },
            {
                "uuid": "90fb55c4-f5c7-466c-828a-8186b1bf52b1",
                "name": "test",
                "count": 0,
            },
            {
                "uuid": "7b2e2c6f-0739-46b4-9481-620d0bdeb637",
                "name": "test",
                "count": 0,
            },
        ]
        response = client.get(url_for("counter.list_counters"))
        assert response.status_code == 200
        assert b"Counters" in response.data
        assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
        assert b"80e09736-565f-43da-b2db-25a616ad3caf" in response.data
        assert b"90fb55c4-f5c7-466c-828a-8186b1bf52b1" in response.data
        assert b"7b2e2c6f-0739-46b4-9481-620d0bdeb637" in response.data
        assert b"test" in response.data
        assert b"0" in response.data


@pytest.mark.integration
def test_show_counter(client):
    """Tests the show counter page - which shows a specific counter"""
    with patch("letscountitui.utilities.utils.DataRetrieval.get_data") as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 10,
            }
        ]
    response = client.get(
        url_for(
            "counter.show_counter", counter_id="123e4567-e89b-12d3-a456-426614174000"
        )
    )
    assert response.status_code == 200
    assert b"Counter" in response.data
    assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
    assert b"test" in response.data
    assert b"10" in response.data


@pytest.mark.integration
def test_increase_counter(client):
    """Tests increasing a counter using the increase counter endpoint"""
    with patch(
        "letscountitui.utilities.utils.DataRetrieval.increase_counter"
    ) as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 10,
            }
        ]
    response = client.get(
        url_for(
            "counter.increase_counter",
            counter_id="123e4567-e89b-12d3-a456-426614174000",
        ),
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Counter" in response.data
    assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
    assert b"test" in response.data
    assert b"11" in response.data


@pytest.mark.integration
def test_decrease_counter(client):
    """Tests decreasing a counter using the decrease counter endpoint"""
    with patch(
        "letscountitui.utilities.utils.DataRetrieval.decrease_counter"
    ) as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 10,
            }
        ]
    response = client.get(
        url_for(
            "counter.decrease_counter",
            counter_id="123e4567-e89b-12d3-a456-426614174000",
        )
    )
    assert response.status_code == 200
    assert b"Counter" in response.data
    assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
    assert b"test" in response.data
    assert b"9" in response.data


@pytest.mark.integration
def test_create_counter(client):
    """Tests creating a counter using the create counter endpoint"""
    with patch(
        "letscountitui.utilities.utils.DataRetrieval.create_counter"
    ) as mock_create_counter_data:
        mock_create_counter_data.return_value = [
            {"uuid": "123e4567-e89b-12d3-a456-426614174000", "name": "test", "count": 0}
        ]
        with patch(
            "letscountitui.utilities.utils.DataRetrieval.get_data"
        ) as mock_get_data:
            mock_get_data.return_value = [
                {
                    "uuid": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "test",
                    "count": 0,
                }
            ]


@pytest.mark.integration
def test_create_counter_1(client):
    """Tests creating a counter using the create counter endpoint"""
    with patch(
        "letscountitui.utilities.utils.DataRetrieval.create_counter"
    ) as mock_create_counter_data:
        mock_create_counter_data.return_value = [
            {"uuid": "123e4567-e89b-12d3-a456-426614174000", "name": "test", "count": 0}
        ]
        with patch(
            "letscountitui.utilities.utils.DataRetrieval.get_data"
        ) as mock_get_data:
            mock_get_data.return_value = [
                {
                    "uuid": "123e4567-e89b-12d3-a456-426614174000",
                    "name": "test",
                    "count": 0,
                }
            ]
            response = client.get(url_for("counter.create_counter", name="test"))
            assert response.status_code == 200
            assert b"Counter" in response.data
            assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
            assert b"test" in response.data
            assert b"0" in response.data


@pytest.mark.integration
def test_create_counter_with_existing_name(client):
    """Tests creating a counter with an existing name"""
    with patch(
        "letscountitui.utilities.utils.DataRetrieval.create_counter"
    ) as mock_create_counter_data:
        mock_create_counter_data.side_effect = ValueError("Counter name already exists")
        response = client.get(url_for("counter.create_counter", name="test"))
        assert response.status_code == 400
        assert b"Counter name already exists" in response.data


@pytest.mark.integration
def test_create_counter_with_invalid_name(client):
    """Tests creating a counter with an invalid name"""
    response = client.get(url_for("counter.create_counter", name=""))
    assert response.status_code == 400
    assert b"Invalid counter name" in response.data
    assert response.status_code == 200
    assert b"Counter" in response.data
    assert b"123e4567-e89b-12d3-a456-426614174000" in response.data
    assert b"test" in response.data
    assert b"0" in response.data
