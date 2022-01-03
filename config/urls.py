
from django.contrib import admin
from django.urls import include, path
from posts.views import UserReportList, UserReportDetail, ImageDetail, ImageUpload
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import settings

urlpatterns = [

path('admin/', admin.site.urls),

# posting report
path('user/report/', UserReportList.as_view()),

# report detail - changing and updating report
path('user/report_detail/<int:pk>/', UserReportDetail.as_view()),

# uploading one image
path('user/image_upload/<int:pk>/', ImageUpload.as_view()),

# chnaging one image
path('user/image_change/<int:pk>/', ImageDetail.as_view()),

# login and logout
path('user/', include('dj_rest_auth.urls')),

]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

