from enum import Enum

class Difficulty(Enum):
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'

class QuestionStatus(Enum):
    SOLVED = 'SOLVED'
    ATTEMPTED = 'ATTEMPTED'

class SubmissionStatus(Enum):
    ACCEPTED = 10
    WRONG_ANSWER = 11
    RUNTIME_ERROR = 13
    TIME_LIMIT_EXCEEDED = 14
    OUTPUT_LIMIT_EXCEEDED = 15
    OTHER = 99

    @classmethod
    def _missing_(cls, value: int):
        return cls.OTHER