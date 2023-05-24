from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import Base


class ProblemGroup(Base):
    __tablename__ = 'problem_group'

    name = Column(String(255), unique=True, nullable=False)

    problems = relationship('Problem', back_populates='group')

    def __repr__(self):
        return f'<ProblemGroup {self.name}>'
