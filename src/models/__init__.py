from sqlalchemy import create_engine

from configs import PostgreSQLConfig
from models.base import Base

engine = create_engine(PostgreSQLConfig.create_url())

from models.problem import Problem
from models.problem_group import ProblemGroup
from models.problem_case import ProblemCase
