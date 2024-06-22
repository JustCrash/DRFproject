from rest_framework.serializers import ModelSerializer, SerializerMethodField
from materials.models import Course, Lesson
from rest_framework import serializers


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    information_all_lessons = LessonSerializer(many=True, source="course")
    number_of_lessons = serializers.SerializerMethodField(read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def create(self, validated_data):
        lesson = validated_data.pop("information_all_lessons")
        course = Course.objects.create(**validated_data)
        for lesson in lesson:
            Lesson.objects.create(course=course, **lesson)
            return course

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "number_of_lessons",
            "information_all_lessons",
        ]


class CourseDitailSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField(read_only=True)
    information_all_lessons = LessonSerializer(many=True, source="course")
    subscription = serializers.SerializerMethodField(read_only=True)

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "number_of_lessons",
            "information_all_lessons",
        ]
