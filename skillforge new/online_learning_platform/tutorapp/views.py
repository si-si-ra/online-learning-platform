from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from.forms import  Customuserform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .forms import VideoUploadForm
from .models import Video

def tutor_dashboard(request):
    return render(request,'tutorapp/tutor_dashboard.html')


def tutor_register(request):
    form=Customuserform()
    if request.method == 'POST':
        form=Customuserform(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)

            return redirect('tutor_login')
    context={'form':form}
    return render(request,'tutorapp/tutor_register.html',context)


def tutor_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('tutor_dashboard')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'tutorapp/tutor_login.html')

    return render(request,'tutorapp/tutor_login.html')


def tutor_logout(request):
    logout(request)
    return redirect('tutorapp/tutor_login.html')

    
def python(request):
    return render(request,'tutorapp/python.html')
def fullstack(request):
    return render(request,'tutorapp/fullstack.html')
def datascience(request):
    return render(request,'tutorapp/datascience.html')



# <------------------------------------------------------------------------------------------------------------------------>


from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoUploadForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'tutorapp/upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'tutorapp/video_list.html', {'videos': videos})

def video_list_view(request):
    videos = Video.objects.all()
    return render(request, 'tutorapp/video_list_view.html', {'videos': videos})

def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'tutorapp/python_confirm_delete.html', {'video': video})



from .forms import NoteUploadForm
from .models import Note

def upload_note(request):
    if request.method == 'POST':
        form = NoteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteUploadForm()
    return render(request, 'tutorapp/upload_note.html', {'form': form})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.note_file.delete()  # Delete the note file from storage
        note.delete()  # Delete the database entry
        return redirect('note_list')
    return render(request, 'tutorapp/delete_note.html', {'note': note})

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'tutorapp/note_list.html', {'notes': notes})

def note_list_view(request):
    notes = Note.objects.all()
    return render(request, 'tutorapp/note_list_view.html', {'notes': notes})


from .models import Assignment, Answer
from .forms import AssignmentForm, AnswerUploadForm

def create_assignment(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'tutorapp/create_assignment.html', {'form': form})

def assignment_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'tutorapp/assignment_list.html', {'assignments': assignments})

def assignment_list_view(request):
    assignments = Assignment.objects.all()
    return render(request, 'tutorapp/assignment_list_view.html', {'assignments': assignments})

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'tutorapp/delete_assignment.html', {'assignment': assignment})

def upload_answer(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = AnswerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.assignment = assignment
            answer.save()
            return redirect('assignment_list_view')
    else:
        form = AnswerUploadForm()
    return render(request, 'tutorapp/upload_answer.html', {'form': form, 'assignment': assignment})


def student_assignments(request):
    assignments = Assignment.objects.all()
    student_answers = Answer.objects.all()
    return render(request, 'tutorapp/student_assignments.html', {'assignments': assignments, 'student_answers': student_answers})

def student_progress(request):
    students = set(Answer.objects.values_list('student_name', flat=True))
    progress = {}
    for student in students:
        submitted_count = Answer.objects.filter(student_name=student, status='Submitted').count()
        graded_count = Answer.objects.filter(student_name=student, status='Graded').count()
        total_count = submitted_count + graded_count
        progress[student] = {
            'submitted_count': submitted_count,
            'graded_count': graded_count,
            'total_count': total_count,
            'progress_percentage': (graded_count / total_count) * 100 if total_count != 0 else 0
        }
    return render(request, 'tutorapp/student_progress.html', {'progress': progress})



from .forms import QuizUploadForm
from .models import QuizQuestion

def upload_quiz(request):
    if request.method == 'POST':
        form = QuizUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_quiz')
    else:
        form = QuizUploadForm()
    return render(request, 'tutorapp/upload_quiz.html', {'form': form})

def view_quiz(request):
    questions = QuizQuestion.objects.all()
    return render(request, 'tutorapp/view_quiz.html', {'questions': questions})

def answer_question(request, question_id):
    question = QuizQuestion.objects.get(pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        correct_answer = question.correct_answer
        return render(request, 'tutorapp/answer_question.html', {'answer': answer, 'correct_answer': correct_answer})
    return render(request, 'tutorapp/answer_question.html', {'question': question})



# <------------------------------------------------------------------------------------------------------------------------>

from .models import Full_video
from .forms import Full_videoUploadForm

def full_upload_video(request):
    if request.method == 'POST':
        form = Full_videoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('full_video_list')
    else:
        form = Full_videoUploadForm()
    return render(request, 'tutorapp/full_upload_video.html', {'form': form})

def full_video_list(request):
    videos = Full_video.objects.all()
    return render(request, 'tutorapp/full_video_list.html', {'videos': videos})

def full_video_list_view(request):
    videos = Full_video.objects.all()
    return render(request, 'tutorapp/full_video_list_view.html', {'videos': videos})

def delete_full_video(request, video_id):
    video = get_object_or_404(Full_video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('full_video_list')
    return render(request, 'tutorapp/confirm_delete.html', {'video': video})


from .models import Full_note
from .forms import FullnoteUploadForm

def full_upload_note(request):
    if request.method == 'POST':
        form = FullnoteUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('full_note_list')
    else:
        form = FullnoteUploadForm()
    return render(request, 'tutorapp/full_upload_note.html', {'form': form})

def full_note_list(request):
    notes = Full_note.objects.all()
    return render(request, 'tutorapp/full_note_list.html', {'notes': notes})

def full_note_list_view(request):
    notes = Full_note.objects.all()
    return render(request, 'tutorapp/full_note_list_view.html', {'notes': notes})

def delete_full_note(request, note_id):
    note = get_object_or_404(Full_note, id=note_id)
    note.delete()
    return redirect('full_note_list')


from .models import Full_Assignment, Full_Answer
from .forms import Full_AssignmentForm, Full_AnswerUploadForm

def full_create_assignment(request):
    if request.method == 'POST':
        form = Full_AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('full_assignment_list')
    else:
        form = Full_AssignmentForm()
    return render(request, 'tutorapp/full_create_assignment.html', {'form': form})

def full_assignment_list(request):
    assignments = Full_Assignment.objects.all()
    return render(request, 'tutorapp/full_assignment_list.html', {'assignments': assignments})


def full_delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Full_Assignment, id=assignment_id)
    if request.method == 'POST':
        assignment.delete()
        return redirect('full_assignment_list')
    return render(request, 'tutorapp/full_delete_assignment.html', {'assignment': assignment})


def full_assignment_list_view(request):
    assignments = Full_Assignment.objects.all()
    return render(request, 'tutorapp/full_assignment_list_view.html', {'assignments': assignments})

def full_upload_answer(request, assignment_id):
    assignment = get_object_or_404(Full_Assignment, pk=assignment_id)
    if request.method == 'POST':
        form = Full_AnswerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.assignment = assignment
            answer.save()
            return redirect('full_assignment_list_view')
    else:
        form = Full_AnswerUploadForm()
    return render(request, 'tutorapp/full_upload_answer.html', {'form': form, 'assignment': assignment})


def full_student_assignments(request):
    assignments = Full_Assignment.objects.all()
    student_answers =Full_Answer.objects.all()
    return render(request, 'tutorapp/full_student_assignments.html', {'assignments': assignments, 'student_answers': student_answers})

def full_student_progress(request):
    students = set(Full_Answer.objects.values_list('student_name', flat=True))
    progress = {}
    for student in students:
        submitted_count = Full_Answer.objects.filter(student_name=student, status='Submitted').count()
        graded_count = Full_Answer.objects.filter(student_name=student, status='Graded').count()
        total_count = submitted_count + graded_count
        progress[student] = {
            'submitted_count': submitted_count,
            'graded_count': graded_count,
            'total_count': total_count,
            'progress_percentage': (graded_count / total_count) * 100 if total_count != 0 else 0
        }
    return render(request, 'tutorapp/full_student_progress.html', {'progress': progress})


from .forms import Full_QuizUploadForm
from .models import Full_QuizQuestion

def full_upload_quiz(request):
    if request.method == 'POST':
        form = Full_QuizUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('full_view_quiz')
    else:
        form = Full_QuizUploadForm()
    return render(request, 'tutorapp/full_upload_quiz.html', {'form': form})

def full_view_quiz(request):
    questions = Full_QuizQuestion.objects.all()
    return render(request, 'tutorapp/full_view_quiz.html', {'questions': questions})

def full_answer_question(request, question_id):
    question = Full_QuizQuestion.objects.get(pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        correct_answer = question.correct_answer
        return render(request, 'tutorapp/full_answer_question.html', {'answer': answer, 'correct_answer': correct_answer})
    return render(request, 'tutorapp/full_answer_question.html', {'question': question})



# <------------------------------------------------------------------------------------------------------------------------>