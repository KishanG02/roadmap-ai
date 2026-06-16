from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class Progress(Base):

    __tablename__ = "progress"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    role = Column(String)

    module = Column(String)

    chapter = Column(String)

    status = Column(String)

    completed_at = Column(
        DateTime,
        default=datetime.utcnow
    )