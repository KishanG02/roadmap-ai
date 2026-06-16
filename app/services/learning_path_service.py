from app.database import SessionLocal
from app.models.learning_path import LearningPath


def save_learning_path(data):

    db = SessionLocal()

    record = LearningPath(
        role=data.role,
        module=data.module,
        chapter=data.chapter,
        chapter_order=data.chapter_order
    )

    db.add(record)

    db.commit()

    db.close()

    return {
        "message": "Learning path saved"
    }