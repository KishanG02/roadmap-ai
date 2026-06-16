from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class LearningPath(Base):

    __tablename__ = "learning_paths"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role = Column(String)

    module = Column(String)

    chapter = Column(String)

    chapter_order = Column(Integer)