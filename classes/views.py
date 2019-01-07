from django.shortcuts import render
from django.http import JsonResponse
from .models import Classroom, Student
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import StudentListSerializer, ClassroomListSerializer
from django.db.models import Q


class ClassroomList(ListAPIView):
    serializer_class = ClassroomListSerializer

    def get_queryset(self):
        queryset = Classroom.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(Q(name__icontains=query))
        return queryset

# def classroom_list(request):
#     my_classroom = []
#     for eachclass in Classroom.objects.all():
#         my_classroom.append({
#             'Name': eachclass.name,
#             'Subject': eachclass.subject,
#             'Year': eachclass.year,
#             'Teacher': eachclass.teacher.id,
#         })
#     return JsonResponse(my_classroom, safe=False)


# def class_detail(request, class_id):
#     class_obj = Classroom.objects.get(id=class_id)
#     print(class_obj)
#     my_class = {
#         'Name:': rest_obj.name,
#         'Subject:': class_obj.subject,
#         'Year:': class_obj.year,
#         'Teacher:': class_obj.teacher,
#     }
#     return JsonResponse(my_class, safe=False)


# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     query = self.request.GET.get('q')

#     if query:
#         queryset = queryset.filter(Q(name__icontains=query))
#     return queryset


# def get_queryset(self):
#     class_id = self.kwargs['class_id']
#     classroom = Classroom.objects.get(id=class_id)
#     return classroom.teacher.all()


# def Student_detail(request, student_id):
#     student_obj = Student.objects.get(id=student_id)
#     my_student = {
#         'date_of_birth': student_obj.description,
#         'Name': student_obj.name,
#         'Price:': student_obj.price,
#         'Restaurant:': student_obj.restaurant,
#     }
#     return JsonResponse(my_item, safe=False)


# def item_list(request):
#     my_items = []
#     for item in Item.objects.all():
#         my_items.append({
#             'Name: ': item.name,
#             'Description:': item.description,
#             'Price:': item.price,
#             'Restaurant': item.restaurant,
#         })
#     return JsonResponse(my_items, safe=False)
