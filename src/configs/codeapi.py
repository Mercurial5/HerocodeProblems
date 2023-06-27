from os import environ

from sqlalchemy import URL
from urllib.parse import urljoin


class HostConfig:
    FLASK_HOST = environ["FLASK_HOST"]
    FLASK_PORT = environ["FLASK_PORT"]

    @staticmethod
    def get_server_url() -> URL:
        base_url = f"http://{HostConfig.FLASK_HOST}:{HostConfig.FLASK_PORT}"
        server_url = urljoin(base_url, "/")

        return server_url
