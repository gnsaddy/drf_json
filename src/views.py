from .models import Course, Content, Day
from .serializers import CourseSerializer, ContentSerializer, DaySerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    # print(queryset.values())
    serializer_class = CourseSerializer
    # print(serializer_class)


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()  # join
    print(queryset.values())
    serializer_class = ContentSerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()  # join
    print(queryset.values())
    serializer_class = DaySerializer
