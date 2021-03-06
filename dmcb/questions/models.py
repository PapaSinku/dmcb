from django.db import models


class Question(models.Model):
    DIFFICULTY_CHOISES = (
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
        ("A", "Alan Turing"),
    )
    question_id = models.CharField(
        max_length=30, unique=True, blank=False, primary_key=True
    )
    question_text = models.CharField(max_length=200, blank=True)
    difficulty = models.CharField(choices=DIFFICULTY_CHOISES, max_length=2, blank=False)
    solve_count = models.IntegerField(default=0)
    sell_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question_id
