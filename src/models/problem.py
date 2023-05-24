from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Problem(Base):
    __tablename__ = 'problem'

    group_id = Column(ForeignKey('problem_group.id'), nullable=False)

    name = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    group = relationship('ProblemGroup', back_populates='problems')
    cases = relationship('ProblemCase', back_populates='problem')

    def __repr__(self):
        return f'<Problem {self.name}>'
