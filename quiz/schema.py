import graphene
from graphene_django import DjangoObjectType
from quiz.models import Quiz, Category, Question, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizType(DjangoObjectType):
    class Meta:
        model = Quiz
        fields = ("id", "title", "category", "date_created")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

schema = graphene.Schema(query=Query)