# from django.db import models

# class Course(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name    

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)  # This is not recommended for production, consider using Django's built-in authentication system
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
# class Tutor(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)  # This is not recommended for production, consider using Django's built-in authentication system
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

