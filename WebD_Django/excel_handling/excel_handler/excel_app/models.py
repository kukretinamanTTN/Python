from django.db import models
from django.contrib import admin

#store excel
class ExcelUpload(models.Model):
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

#store poll questions
class PollQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)