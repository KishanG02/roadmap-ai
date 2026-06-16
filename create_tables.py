from app.database import Base
from app.database import engine

from app.models.progress import Progress
from app.models.learning_path import LearningPath

Base.metadata.create_all(bind=engine)

print("Tables created successfully")