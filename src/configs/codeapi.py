from os import environ


class HostConfig:
    FLASK_HOST = environ["FLASK_HOST"]
    FLASK_PORT = environ["FLASK_PORT"]

    @staticmethod
    def get_server_url() -> str:
        return f"http://{HostConfig.FLASK_HOST}:{HostConfig.FLASK_PORT}/"
