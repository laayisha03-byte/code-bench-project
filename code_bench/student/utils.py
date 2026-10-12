# pip install google-genai

from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from decouple import config

class EvaluationResult(BaseModel):
    score: int = Field(
        description="Score awarded to the student answer"
    )
    remarks: str = Field(
        description="Brief feedback explaining the score"
    )


client = genai.Client(
    api_key=config('GEMINI_API_KEY')
)


def evaluate_answer(answer):

    prompt = f"""
You are an expert programming instructor evaluating a student's answer.
Evaluate the student's answer strictly based on the given problem.
PROBLEM:
{answer.question.question}
MAXIMUM POINTS:
{answer.question.points}
STUDENT ANSWER:
{answer.answer}
Evaluation rules:
1. Give a score between 0 and {answer.question.points}.
2. Never give more than {answer.question.points}.
3. Award points based on correctness, completeness and whether the answer
   actually solves the given problem.
4. Do not award full marks for an incomplete or partially correct answer.
5. Consider minor syntax mistakes reasonably if the overall logic is correct.
6. Give concise and useful remarks.
7. Return only the requested structured output.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=EvaluationResult,
        ),
    )



    result = response.parsed

    answer.point=result.score
    
    answer.remarks=result.remarks
    
    answer.save()

def evaluate_objective_answer(answer):

    if answer.answer ==answer.question.correct_choice:

        point=answer.question.points

    else:

        point = 0 

    return point

    