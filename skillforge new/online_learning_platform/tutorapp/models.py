from django.db import models

# Create your models here.

import os

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

    def delete(self, *args, **kwargs):
        # Delete the video file from the storage
        if os.path.isfile(self.video_file.path):
            os.remove(self.video_file.path)
        super(Video, self).delete(*args, **kwargs)



class Note(models.Model):
    title = models.CharField(max_length=255)
    note_file = models.FileField(upload_to='notes/')


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    questions = models.TextField()
    deadline = models.DateTimeField()

from .models import Assignment

class Answer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    answer_file = models.FileField(upload_to='answers/')
    status = models.CharField(max_length=20, choices=[('Submitted', 'Submitted'), ('Graded', 'Graded')], default='Submitted')

    def __str__(self):
        return f"{self.student_name}'s answer for {self.assignment.title}"
    


class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

   

#    <------------------------------------------------------------------------------------------------------------------->

class Full_video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

    def delete(self, *args, **kwargs):
        # Delete the video file from the storage
        if os.path.isfile(self.video_file.path):
            os.remove(self.video_file.path)
        super(Full_video, self).delete(*args, **kwargs)


class Full_note(models.Model):
    title = models.CharField(max_length=200, default='Untitled Note')
    file = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title


class Full_Assignment(models.Model):
    title = models.CharField(max_length=255)
    questions = models.TextField()
    deadline = models.DateTimeField()

from .models import Full_Assignment

class Full_Answer(models.Model):
    assignment = models.ForeignKey(Full_Assignment, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)
    answer_file = models.FileField(upload_to='answers/')
    status = models.CharField(max_length=20, choices=[('Submitted', 'Submitted'), ('Graded', 'Graded')], default='Submitted')

    def __str__(self):
        return f"{self.student_name}'s answer for {self.assignment.title}"
    

class Full_QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)