from app.database import SessionLocal
from app.models.progress import Progress


def get_dashboard():

    db = SessionLocal()

    records = db.query(
        Progress
    ).all()

    completed = len(
        [
            r
            for r in records
            if r.status == "completed"
        ]
    )

    total = len(records)

    percentage = 0

    if total > 0:
        percentage = round(
            completed / total * 100,
            2
        )

    current = None

    if records:
        current = records[-1].chapter

    db.close()

    return {
        "completed_chapters": completed,
        "total_chapters": total,
        "progress_percentage": percentage,
        "current_chapter": current
    }