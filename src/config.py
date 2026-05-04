"""Configuration management for Telco AI Fraud Detection."""
from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Application settings."""

    # Anthropic API
    anthropic_api_key: str

    # Temporal
    temporal_host: str = "localhost:7233"
    temporal_namespace: str = "default"
    temporal_task_queue: str = "fraud-verification"

    # Database
    postgres_uri: str = "postgresql://user:password@localhost:5432/fraud_detection"
    redis_url: str = "redis://localhost:6379"

    # Message Queue
    rabbitmq_url: str = "amqp://user:password@localhost:5672"

    # APIs
    sim_swap_api_url: str
    sim_swap_api_key: str
    number_verification_api_url: str
    number_verification_api_key: str
    network_api_url: str
    network_api_key: str
    device_api_url: str
    device_api_key: str

    # Observability
    jaeger_host: str = "jaeger"
    jaeger_port: int = 6831
    prometheus_port: int = 9090

    # Application
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    max_retries: int = 3
    timeout_seconds: int = 30

    # Decision thresholds
    risk_score_high: int = 80
    risk_score_review: int = 50
    confidence_threshold_review: float = 0.7

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
