"""Module configuring the different application environments"""

import os


class Config:
    """Base configuration for the application."""

    SECRET_KEY = os.getenv("APP_SECRET_KEY")
    SERVER_NAME = os.getenv("APP_SERVER_NAME")


class DevelopmentConfig(Config):
    """Configuration for the development environment."""

    DEBUG = True
    TESTING = True
    ENV = "development"
    API_HOST = os.getenv("API_HOST", "http://localhost:5000")


class ProductionConfig(Config):
    """Configuration for the production environment."""

    DEBUG = False
    TESTING = False
    ENV = "production"
    API_HOST = os.getenv("API_HOST")
