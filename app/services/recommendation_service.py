from app.database import SessionLocal
from app.models.learning_path import LearningPath
from app.models.progress import Progress


def get_next_chapter():

    db = SessionLocal()

    completed = db.query(
        Progress
    ).filter(
        Progress.status == "completed"
    ).all()

    completed_names = [
        item.chapter
        for item in completed
    ]

    chapters = db.query(
        LearningPath
    ).order_by(
        LearningPath.chapter_order
    ).all()

    for chapter in chapters:

        if chapter.chapter not in completed_names:

            db.close()

            return {
                "next_chapter": chapter.chapter,
                "module": chapter.module
            }

    db.close()

    return {
        "message": "Roadmap Completed"
    }