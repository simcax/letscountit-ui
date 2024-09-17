"""Tests the API data retrieval module"""

from unittest.mock import patch

from letscountitui.utilities.utils import DataRetrieval


def test_get_api_data():
    """Tests getting data from the API listing counters available"""
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
        dr_obj = DataRetrieval("http://localhost:8000")
        data = dr_obj.get_data()
        assert data == [
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


def test_increase_counter_api_call():
    """Tests increasing a counter using the API"""
    with patch("letscountitui.utilities.utils.DataRetrieval.get_data") as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 10,
            }
        ]
    with patch("letscountitui.utilities.utils.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        dr_obj = DataRetrieval()
        data = dr_obj.increase_counter("123e4567-e89b-12d3-a456-426614174000")
        assert data == mock_post.return_value.json()


def test_decrease_counter_api_call():
    """Tests decreasing a counter using the API"""
    with patch("letscountitui.utilities.utils.DataRetrieval.get_data") as mock_get_data:
        mock_get_data.return_value = [
            {
                "uuid": "123e4567-e89b-12d3-a456-426614174000",
                "name": "test",
                "count": 10,
            }
        ]
    with patch("letscountitui.utilities.utils.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        dr_obj = DataRetrieval()
        data = dr_obj.decrease_counter("123e4567-e89b-12d3-a456-426614174000")
        assert data == mock_post.return_value.json()


def test_create_counter_api_call():
    """Tests creating a counter using the API"""
    with patch("letscountitui.utilities.utils.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        dr_obj = DataRetrieval()
        data = dr_obj.create_counter("test")
        assert data == mock_post.return_value.json()


def test_update_counter_data_retrieval():
    """Test updating a counter using the API"""
    with patch("letscountitui.utilities.utils.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        dr_obj = DataRetrieval()
        data = dr_obj.update_counter("123e4567-e89b-12d3-a456-426614174000", 10)
        assert data == mock_post.return_value.json()
