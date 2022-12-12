import json
from typing import Tuple
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ConnectDB:
    """Class for connection database"""

    def __init__(self, path) -> None:
        self.path = path
        self.file = open(path)
        self.config = json.load(self.file)
        self.file.close()

    def show(self) -> Tuple[str, str, str, int, str, str]:
        """To Show Evronment Database"""
        return (
            self.config["rdbms"],
            self.config["user"],
            self.config["host"],
            self.config["port"],
            self.config["name"],
            self.config["password"],
        )

    def session(self):
        """To get session"""
        _, username, host, port, database, password = self.show()
        engine = create_engine(
            f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}",
            pool_size=20,
            max_overflow=0,
            pool_timeout=300,
        )
        Session = sessionmaker(engine, future=True)

        return Session
