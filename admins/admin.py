from django.contrib import admin
from .models import Course,StudentDetail,CourseDownload,CertificateDetail
# Register your models here.

class StudentDetailAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'std_name',
        'std_email',
        'std_number',
        'std_qualification',
        'std_course'
        
    ]
class CourseDownloadAdmin(admin.ModelAdmin):
    list_display = [
        'std_name',
        'std_email',
        'std_number',
        'std_qualification',
        'std_download_course',
        'date',
    ]

class CertificateDetailAdmin(admin.ModelAdmin):
    list_display = [
        'cert_number',
        'name',
        'gender',
        'Course_name',
        'date',
    ]


admin.site.register(Course)
admin.site.register(StudentDetail,StudentDetailAdmin)
admin.site.register(CourseDownload,CourseDownloadAdmin)
admin.site.register(CertificateDetail,CertificateDetailAdmin)