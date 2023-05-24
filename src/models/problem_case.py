from sqlalchemy import Text, Column, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class ProblemCase(Base):
    __tablename__ = 'problem_case'
    problem_id = Column(ForeignKey('problem.id'))

    input = Column(Text)
    output = Column(Text)

    problem = relationship('Problem', back_populates='cases')
