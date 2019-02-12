from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Courses.models import Course
from ToolsApp.models import Tool
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import *



def get_courses():
    return Course.objects.all()

def get_tools():
    return Tool.objects.all()

def project_index(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'projects/index.html', context)



def project_courses(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('Projects:index')

# def project_courses(request, project_name):
#     project = Project.objects.get(project_title=project_name)
#
#     context = {
#         'project_courses': project.projectcourse_set.all(),
#         'project_title': project.project_title,
#         'project_description': project.project_description,
#         'courses': get_courses(),
#         'tools': get_tools(),
#     }
#
#     return render(request, 'projects/project_courses.html', context)

def project_courses(request, project_name):
    project = Project.objects.get(project_title=project_name)
    project_courses = ProjectCourse.objects.all()
    context = {
        'project_title': project.project_title,
        'project_description': project.project_description,
        'project_courses': project_courses,
        'courses': get_courses(),
        'tools': get_tools(),
    }

    return render(request, 'projects/project_courses.html', context)

@login_required
def project_course_topics(request, course_id, topic_id):
    try:
        course = ProjectCourse.objects.get(id=course_id)
    except ProjectCourse.DoesNotExist:
        return redirect('Projects:index')

    try:
        topic = ProjectCourseTopic.objects.get(topic_id=topic_id,topic_course__id=course_id)
    except ProjectCourseTopic.DoesNotExist:
        return redirect('Projects:index')

    #Permissions
    if request.user.role >= 1 and request.user.role <= 3:
        pass
    elif request.user.role == 4:
        try:
            perm = ProjectPermission.objects.get(user=request.user,course=course)
            if perm:
                pass
            else:
                return redirect("home:tryfree",'standardPlan')
        except ProjectPermission.DoesNotExist:
            return redirect("home:tryfree",'standardPlan')
    else:
        return redirect("home:tryfree",'standardPlan')

    context = {
        'course_topics': course.projectcoursetopic_set.all(),
        'course_title': course.course_title,
        'course_description': course.course_description,
        'project_title': course.course_project.project_title,
        'project_id': course.course_project.id,
        'course_id': course.id,
        'topic': topic,
    }

    return render(request, 'projects/project_course_topics.html', context)
    
@login_required
def project_course_notes(request, course_id, topic_id):
    try:
        course = ProjectCourse.objects.get(id=course_id)
    except ProjectCourse.DoesNotExist:
        return redirect('Projects:index')

    try:
        topic = ProjectCourseTopic.objects.get(topic_id=topic_id,topic_course__id=course_id)
    except ProjectCourseTopic.DoesNotExist:
        return redirect('Projects:index')

    try:
        note = CourseTopicNote.objects.get(topic=topic)
    except CourseTopicNote.DoesNotExist:
        return redirect('Projects:index')

    #Permissions
    if request.user.role >= 1 and request.user.role <= 3:
        pass
    elif request.user.role == 4:
        try:
            perm = ProjectPermission.objects.get(user=request.user,course=course)
            if perm:
                pass
            else:
                return redirect("home:tryfree",'standardPlan')
        except ProjectPermission.DoesNotExist:
            return redirect("home:tryfree",'standardPlan')
    else:
        return redirect("home:tryfree",'standardPlan')

    context = {
        'course_title': course.course_title,
        'course_description': course.course_description,
        'project_title': course.course_project.project_title,
        'project_id': course.course_project.id,
        'course_id': course.id,
        'topic': topic,
        'note': note,
    }

    return render(request, 'projects/project_course_note.html', context)

@login_required
def project_course_labs(request, course_name):
    course = ProjectCourse.objects.get(course_title=course_name.replace("_", " "))

    context = {
        'course_labs': course.courselab_set.all(),
        'course_title': course.course_title,
        'course_description': course.course_description,
        'courses': get_courses(),
        'tools': get_tools(),
    }

    if request.user.role == 4:
        if course.course_project.project_id != request.user.allowed_project:
            return render(request, 'projects/project_access_denied.html') #you are not allowed to view this page
        else:
            contx = {
                'course_labs': course.courselab_set.all(),
                'course_title': course.course_title,
                'course_description': course.course_description,
                'courses': get_courses(),
                'tools': get_tools(),
            }
            return render(request, 'projects/project_course_labs.html', contx)
    elif request.user.role == 3:
        return render(request, 'projects/project_course_labs.html', context)
    else:
        return redirect("home:tryfree",'standardPlan')


@login_required
def lab_task(request, topic_id):
    #course = ProjectCourse.objects.get(course_title=course_name.replace("_", " "))
    topic = ProjectCourseTopic.objects.get(topic_id=topic_id)
    task = LabTask.objects.all()
    context = {
        'topic': topic.topic_title,
        'lab_tasks': topic.labtask_set.all(),
        'courses': get_courses(),
        'tools': get_tools(),
        'task_status': UsersLabTaskStatus.objects.filter(user=request.user)
    }

    return render(request, 'projects/course_lab_tasks.html', context)


# @login_required
# def course_lab_tasks(request, lab_title):
#     lab = CourseLab.objects.get(lab_title=lab_title.replace("_", " "))
#
#     context = {
#         'lab': lab,
#         'lab_tasks': lab.courselabtask_set.all(),
#         'courses': get_courses(),
#         'tools': get_tools(),
#         'task_status': UsersLabTaskStatus.objects.filter(user=request.user)
#     }
#
#     return render(request, 'projects/course_lab_tasks.html', context)