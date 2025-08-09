from django.db import models

class InterviewFeedback(models.Model):
    question = models.TextField()
    answer = models.TextField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback on: {self.question[:50]}"
