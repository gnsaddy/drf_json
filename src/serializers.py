from rest_framework_json_api import serializers
from .models import Content, Course, Day


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = "__all__"


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    day = DaySerializer(many=True)

    class Meta:
        model = Content
        fields = ['id', 'week_id', 'url', 'day']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Course
        fields = ['url', 'title', 'subContent', 'duration', 'price',
                  'coordinator', 'created_at', 'updated_at', 'content']
