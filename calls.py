from gql import gql, Client
from auth import get_transport
from models import Difficulty, QuestionStatus, Problem

transport = get_transport()

async def get_problems(skip: int = 0, limit: int = 1000, status: QuestionStatus = QuestionStatus.SOLVED):
    variables = {
        "filters": {
            "skip": skip,
            "limit": limit,
            "questionStatus": status.value
        }
    }

    query = gql("""
        query userProgressQuestionList($filters: UserProgressQuestionListInput) {
            userProgressQuestionList(filters: $filters) {
                totalNum
                questions {
                    frontendId
                    titleSlug
                    title
                    difficulty
                    questionStatus
                }
            }
        }
    """)

    async with Client(transport=get_transport()) as session:
        question_json = await session.execute(query, variable_values=variables)

    if question_json and question_json["userProgressQuestionList"]["totalNum"] > 0:
        problems = [Problem(question["frontendId"], question["titleSlug"], question["title"], 
                          Difficulty(question["difficulty"])) 
                   for question in question_json["userProgressQuestionList"]["questions"]]
        
        for problem in problems:
            await problem.set_solved_date()
            
        return problems
    else:
        print("No problems found.")
        return []
