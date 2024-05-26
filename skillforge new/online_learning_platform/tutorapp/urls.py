from.import views
from django.urls import path


urlpatterns = [
    
    path('tutor_register/',views.tutor_register,name='tutor_register'),
    path('tutor_login/',views.tutor_login,name='tutor_login'),
    path('tutor_logout/',views.tutor_logout,name='tutor_logout'),
    path('tutor_dashboard/',views.tutor_dashboard,name='tutor_dashboard'),

    path('python/',views.python,name='python'),
    path('fullstack/',views.fullstack,name='fullstack'),
    path('datascience/',views.datascience,name='datascience'),

    path('upload/', views.upload_video, name='upload_video'),
    path('list/', views.video_list, name='video_list'),
    path('view_list/', views.video_list_view, name='video_list_view'),
    path('videos/delete/<int:video_id>/', views.delete_video, name='delete_video'),

    path('upload_note/', views.upload_note, name='upload_note'),
    path('note_list/', views.note_list, name='note_list'),
    path('note_list_view/', views.note_list_view, name='note_list_view'),
    path('delete_note/<int:pk>/', views.delete_note, name='delete_note'),

    path('create/', views.create_assignment, name='create_assignment'),
    path('assignment_list/', views.assignment_list, name='assignment_list'),
    path('assignment_list_view/', views.assignment_list_view, name='assignment_list_view'),
    path('upload/<int:assignment_id>/', views.upload_answer, name='upload_answer'),
    path('student-assignments/', views.student_assignments, name='student_assignments'),
    path('student-progress/', views.student_progress, name='student_progress'),
    path('assignments/<int:assignment_id>/delete/', views.delete_assignment, name='delete_assignment'),

    path('quiz_upload/', views.upload_quiz, name='upload_quiz'),
    path('view/', views.view_quiz, name='view_quiz'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),


#    <------------------------------------------------------------------------------>


    path('fullupload/', views.full_upload_video, name='full_upload_video'),
    path('fulllist/', views.full_video_list, name='full_video_list'),
    path('fullview_list/', views.full_video_list_view, name='full_video_list_view'),
    path('delete-video/<int:video_id>/', views.delete_full_video, name='delete_full_video'),

   
    path('full_notes/', views.full_note_list, name='full_note_list'),
    path('notes_view/', views.full_note_list_view, name='full_note_list_view'),
    path('notes_upload/', views.full_upload_note, name='full_upload_note'),
    path('notes/delete/<int:note_id>/', views.delete_full_note, name='delete_full_note'),


    path('full_create/', views.full_create_assignment, name='full_create_assignment'),
    path('full_assignment_list/', views.full_assignment_list, name='full_assignment_list'),
    path('full_assignment_list_view/', views.full_assignment_list_view, name='full_assignment_list_view'),
    path('full_upload/<int:assignment_id>/', views.full_upload_answer, name='full_upload_answer'),
    path('full_student-assignments/', views.full_student_assignments, name='full_student_assignments'),
    path('full_student-progress/', views.full_student_progress, name='full_student_progress'),
    path('assignments/delete/<int:assignment_id>/', views.full_delete_assignment, name='full_delete_assignment'),

    path('full_quiz_upload/', views.full_upload_quiz, name='full_upload_quiz'),
    path('full_view/', views.full_view_quiz, name='full_view_quiz'),
    path('full_answer/<int:question_id>/', views.full_answer_question, name='full_answer_question'),
   

    
]

