from .models import  Report, ReportImages
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportImages
        fields = ('user', 'image', 'report')

# user would be added in views
class ReportDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'content', 'location', 'type')

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'content', 'location', 'type')

