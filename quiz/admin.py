from django.contrib import admin
from quiz.models import (
    Question,
    Quiz,
    Category,
    Answer
)


admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Category)
admin.site.register(Answer)
