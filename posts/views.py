from rest_framework import generics, permissions
from .models import CustomUser, Report, ReportImages
from .serializers import ReportSerializer, ReportDetailSerializer, ImageSerializer
from rest_framework.response import Response
from rest_framework import status

# list of reports and create them
class UserReportList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ReportSerializer

    def get_queryset(self):
        my_user = CustomUser.objects.get(id=self.request.user.id)
        my_report = Report.objects.filter(user=my_user)
        return my_report

    def get(self, request, format=None):
        my_user = CustomUser.objects.get(id=self.request.user.id)
        my_report = Report.objects.filter(user=my_user)
        serializer = ReportSerializer(my_report, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # user is saving in this function and not getting from the web
    #so the autherized person could register

# report seeing detail & update & change
class UserReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        my_user = CustomUser.objects.get(id=self.request.user.id)
        my_report = Report.objects.filter(user=my_user)
        return my_report

# report seeing detail & update & change
class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        my_user = CustomUser.objects.get(id=self.request.user.id)
        my_image = ReportImages.objects.filter(user=my_user)

        return my_image

# create image of a report
class ImageUpload(generics.CreateAPIView):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        my_user = CustomUser.objects.get(id=self.request.user.id)
        my_image = ReportImages.objects.filter(user=my_user)

        return my_image
