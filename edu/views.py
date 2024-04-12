from django.http import HttpResponse
from django.shortcuts import render, redirect
from admins.models import Course,StudentDetail,CourseDownload


# Create your views here.


def Index(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_number = request.POST.get('std_number')
        std_qualification = request.POST.get('std_qualification')
        std_course = request.POST.get('std_course')
        StudentDetail(
            std_name = std_name,
            std_email = std_email,
            std_number = std_number,
            std_qualification = std_qualification,
            std_course = std_course,
        ).save()
        return render(request, 'index.html',{'courses':courses})
    else:
        return render(request, 'index.html',{'courses':courses})


def Download_course(request):
    import os
    course_title = request.GET.get('course_title')
    print('course_title:',course_title)
    course_detail = Course.objects.get(course_title=course_title)
    # file_path = course_detail.file
    # filename = file_path.file.name.split('/')[-1]
    # response = HttpResponse(file_path.file, content_type='text/plain')
    # response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return render(request, 'download_course.html',{'course_detail':course_detail})

def Save_download_course(request):
    if request.method == 'POST':
        std_name = request.POST.get('std_name')
        std_email = request.POST.get('std_email')
        std_number = request.POST.get('std_number')
        std_qualification = request.POST.get('std_qualification')
        std_download_course = request.POST.get('std_download_course')
        CourseDownload(
            std_name = std_name,
            std_email = std_email,
            std_number = std_number,
            std_qualification = std_qualification,
            std_download_course = std_download_course,
        ).save()
        std_download_course = Course.objects.get(course_title=std_download_course)
        return render(request, 'download_course.html',{'std_download_course':std_download_course})


def verify_certificate(request):
    if request.method == 'POST':
        from admins.models import CertificateDetail
        cert_number = request.POST.get('cert_number')
        try:
            CertificateDetail = CertificateDetail.objects.get(cert_number=cert_number)
            if CertificateDetail:
                return render(request, 'index.html',{'CertificateDetail':CertificateDetail})
            else:
                return render(request, 'index.html',{'NoCertificateDetail':None})
        except Exception as exeception:
                return render(request, 'index.html',{'exeception':exeception})
    else:
        pass
            


