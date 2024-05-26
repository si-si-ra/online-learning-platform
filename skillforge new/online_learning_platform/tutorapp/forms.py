from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Customuserform(UserCreationForm):
    course = forms.CharField(max_length=100, required=False)
    class Meta:
        model=User
        fields=['username','email','course','password1','password2']

from .models import Video

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']



from .models import Note

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'note_file']


from .models import Assignment, Answer

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'questions', 'deadline']

class AnswerUploadForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['assignment', 'student_name', 'answer_file']


from .models import QuizQuestion

class QuizUploadForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = '__all__'



# <----------------------------------------------------------------------------------------------------------------------->


from .models import Full_video

class Full_videoUploadForm(forms.ModelForm):
    class Meta:
        model = Full_video
        fields = ['title', 'video_file']



from .models import Full_note

class FullnoteUploadForm(forms.ModelForm):
    class Meta:
        model = Full_note
        fields = ['title', 'file']



from .models import Full_Assignment, Full_Answer

class Full_AssignmentForm(forms.ModelForm):
    class Meta:
        model = Full_Assignment
        fields = ['title', 'questions', 'deadline']

class Full_AnswerUploadForm(forms.ModelForm):
    class Meta:
        model = Full_Answer
        fields = ['assignment', 'student_name', 'answer_file']


from .models import Full_QuizQuestion

class Full_QuizUploadForm(forms.ModelForm):
    class Meta:
        model = Full_QuizQuestion
        fields = '__all__'