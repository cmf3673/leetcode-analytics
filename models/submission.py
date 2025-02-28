from datetime import datetime
from models.enums import SubmissionStatus

class Submission:
    def __init__(self, id: int, questionSlug: str, status: SubmissionStatus, submitted_at: datetime):
        self.id = id
        self.questionSlug = questionSlug
        self.status = status
        self.submitted_at = submitted_at

    def __str__(self) -> str:
        return f"Submission(id={self.id}, questionSlug={self.questionSlug}, status={self.status.name}, timestamp={self.submitted_at})" 