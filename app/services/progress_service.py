from app.database import SessionLocal

from app.models.progress import Progress


def save_progress(data):

    db = SessionLocal()

    record = Progress(
        role=data.role,
        module=data.module,
        chapter=data.chapter,
        status=data.status
    )

    db.add(record)

    db.commit()

    db.close()

    return {
        "message": "Progress saved successfully"
    }

def get_progress():

    db = SessionLocal()

    records = db.query(
        Progress
    ).all()

    result = []

    for record in records:

        result.append(
            {
                "id": record.id,
                "role": record.role,
                "module": record.module,
                "chapter": record.chapter,
                "status": record.status
            }
        )

    db.close()

    return result