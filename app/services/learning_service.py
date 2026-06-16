from app.agents.lesson_agent import LessonAgent
from app.agents.practice_agent import PracticeAgent
from app.agents.quiz_agent import QuizAgent
from app.agents.assignment_agent import AssignmentAgent


def generate_learning_content(
    module,
    chapter
):

    lesson = LessonAgent().run(
        module,
        chapter
    )

    practice = PracticeAgent().run(
        module,
        chapter
    )

    quiz = QuizAgent().run(
        module,
        chapter
    )

    assignment = AssignmentAgent().run(
        module,
        chapter
    )

    return {
        "lesson": lesson,
        "practice": practice,
        "quiz": quiz,
        "assignment": assignment
    }