from os import environ

from sqlalchemy import URL


class PostgreSQLConfig:
    USERNAME = environ['POSTGRESQL_USERNAME']
    PASSWORD = environ['POSTGRESQL_PASSWORD']
    HOST = environ['POSTGRESQL_HOST']
    PORT = int(environ['POSTGRESQL_PORT'])
    DATABASE = environ['POSTGRESQL_DATABASE']

    @classmethod
    def create_url(cls) -> URL:
        return URL.create(username=cls.USERNAME, password=cls.PASSWORD, host=cls.HOST, port=cls.PORT,
                          database=cls.DATABASE, drivername='postgresql+psycopg2')
