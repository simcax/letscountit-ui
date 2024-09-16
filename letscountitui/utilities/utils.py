"""Utily module for the UI to retrieve things from the backend and similar tools."""

import requests
from os import environ
from loguru import logger


class DataRetrievalError(Exception):
    """Error when retrieving data from the backend."""

    pass


class DataRetrieval:
    """Class to retrieve data from the backend."""

    def __init__(self, api_host: str = None) -> None:
        self.api_host = api_host if api_host else environ.get("API_HOST")
        self.counter_list_api = self.api_host + "/counters/list"

    def get_data(self) -> dict:
        """Get data from the backend."""
        logger.debug(f"Getting data from the backend. API: {self.counter_list_api}")
        response = requests.get(self.counter_list_api)
        if response.status_code != 200:
            logger.debug(
                f"Could not retrieve data from the backend. Response: {response.text}"
            )
            raise DataRetrievalError("Could not retrieve data from the backend.")
        return response.json()

    def increase_counter(self, counter_id: str) -> dict:
        """Increase a counter on the backend."""
        increase_counter_api = self.api_host + f"/counter/increase/{counter_id}"
        logger.debug(f"Increasing counter on the backend. API: {increase_counter_api}")
        response = requests.post(increase_counter_api)
        if response.status_code != 200:
            logger.debug(
                f"Could not increase counter on the backend. Response: {response.text}"
            )
            raise DataRetrievalError("Could not increase counter on the backend.")
        return response.json()

    def decrease_counter(self, counter_id: str) -> dict:
        """Decrease a counter on the backend."""
        decrease_counter_api = self.api_host + f"/counter/decrease/{counter_id}"
        logger.debug(f"Decreasing counter on the backend. API: {decrease_counter_api}")
        response = requests.post(decrease_counter_api)
        if response.status_code != 200:
            logger.debug(
                f"Could not decrease counter on the backend. Response: {response.text}"
            )
            raise DataRetrievalError("Could not decrease counter on the backend.")
        return response.json()

    def create_counter(self, name: str, initial_value: int = 0) -> dict:
        """Create a counter on the backend."""
        create_counter_api = self.api_host + f"/counter/create/{name}/{initial_value}"
        logger.debug(f"Creating counter on the backend. API: {create_counter_api}")
        response = requests.post(create_counter_api)
        if response.status_code != 200:
            logger.debug(
                f"Could not create counter on the backend. Response: {response.text}"
            )
            raise DataRetrievalError("Could not create counter on the backend.")
        return response.json()

    def update_counter(self, counter_id: str, new_count: int) -> dict:
        """Update a counter on the backend."""
        update_counter_api = self.api_host + f"/counter/update/{counter_id}/{new_count}"
        logger.debug(f"Updating counter on the backend. API: {update_counter_api}")
        response = requests.post(update_counter_api)
        if response.status_code != 200:
            logger.debug(
                f"Could not update counter on the backend. Response: {response.text}"
            )
            raise DataRetrievalError("Could not update counter on the backend.")
        return response.json()
