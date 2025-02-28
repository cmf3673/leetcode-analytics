from datetime import datetime
from gql import gql, Client
from auth import get_transport
from models.enums import Difficulty, SubmissionStatus
from models.submission import Submission

class Problem:
    def __init__(self, id: int, slug: str, name: str, difficulty: Difficulty, solved_date: datetime = None) -> None:
        self.id = id
        self.slug = slug
        self.name = name
        self.difficulty = difficulty
        self.solved_date = solved_date

    def __str__(self) -> str:
        return f"Problem(id={self.id}, slug={self.slug}, name={self.name}, difficulty={self.difficulty.value}, solved_date={self.solved_date})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    async def get_submissions(self, offset: int = 0, limit: int = 100) -> list[Submission]:
        print("Getting submissions for", self.slug)
        query = gql("""
            query userProgressSubmissionList(
                $offset: Int!,
                $limit: Int!,
                $questionSlug: String!
            ) {
                userProgressSubmissionList(
                    offset: $offset
                    limit: $limit
                    questionSlug: $questionSlug
                ) {
                    submissions {
                        id
                        status
                        timestamp
                    }
                    totalNum
                }
            }
        """)

        variables = {
            "offset": offset,
            "limit": limit,
            "questionSlug": self.slug
        }

        async with Client(transport=get_transport()) as session:
            submissions = (await session.execute(query, variable_values=variables))["userProgressSubmissionList"]["submissions"]

        return [Submission(submission["id"], self.slug, SubmissionStatus(submission["status"]), datetime.fromtimestamp(int(submission["timestamp"]))) for submission in submissions]
        
    async def set_solved_date(self) -> datetime:
        submissions = await self.get_submissions()
        for s in submissions:
            if s.status == SubmissionStatus.ACCEPTED:
                self.solved_date = s.submitted_at
                return s.submitted_at
        return None 