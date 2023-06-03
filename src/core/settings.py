import os

from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    server_host: str = os.getenv('server_host', '127.0.0.1')
    server_port: int = os.getenv('server_port', 8000)

    db_scheme: str = os.getenv('db_scheme', '')
    db_username: str = os.getenv('db_username', '')
    db_password: str = os.getenv('db_password', '')
    db_host: str = os.getenv('db_host', '')
    db_port: int = os.getenv('db_port', '')
    db_name: str = os.getenv('db_name', '')
    db_url: str = os.getenv('db_url', '')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @classmethod
    def build_connection_string(cls, values):
        return '{}://{}:{}@{}:{}/{}'.format(
            values['db_scheme'],
            values['db_username'],
            values['db_password'],
            values['db_host'],
            values['db_port'],
            values['db_name'],
        )

    @root_validator
    def set_database_url(cls, values):
        if not values['db_url']:
            values['db_url'] = cls.build_connection_string(values)
        return values


settings = Settings()
