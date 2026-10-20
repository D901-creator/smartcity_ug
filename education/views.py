from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Q
import uuid

from .models import (
    EducationInstitution,
    EducationRequest,
    EducationProgramme,
    ScholarshipOpportunity,
    TeacherService,
    AdministratorService,
    EducationFunding,
    ExaminationInformation,
    EducationService,
    GovernmentEducationProgramme,
    EducationApplication,
    EducationProject,
    EducationNotice,
    EducationProblemReport,
    EducationInformation,
    EducationStatistic,
     LearningResource
)

from .forms import (
    EducationRequestForm,
    EducationApplicationForm,
    EducationProblemReportForm,
)


# =========================================================
# EDUCATION HOME
# =========================================================

def education_home(request):
    search = request.GET.get("search", "").strip()
    selected_district = request.GET.get("district", "").strip()
    selected_institution_type = request.GET.get("institution_type", "").strip()

    institutions = EducationInstitution.objects.filter(
        is_active=True
    )

    if search:
        institutions = institutions.filter(
            Q(name__icontains=search)
            | Q(description__icontains=search)
            | Q(programs__icontains=search)
        )

    if selected_district:
        institutions = institutions.filter(
            district=selected_district
        )

    if selected_institution_type:
        institutions = institutions.filter(
            institution_type=selected_institution_type
        )

    districts = (
        EducationInstitution.objects
        .filter(is_active=True)
        .values_list("district", flat=True)
        .distinct()
        .order_by("district")
    )

    context = {
        "institutions": institutions,
        "districts": districts,
        "institution_types": EducationInstitution.INSTITUTION_TYPES,
        "search": search,
        "selected_district": selected_district,
        "selected_institution_type": selected_institution_type,
        "active": "education",
    }

    return render(
        request,
        "education/education_home.html",
        context
    )


# =========================================================
# INSTITUTION DETAILS
# =========================================================

def institution_detail(request, pk):
    institution = get_object_or_404(
        EducationInstitution,
        pk=pk,
        is_active=True
    )

    programmes = EducationProgramme.objects.filter(
        institution=institution,
        is_published=True
    ).order_by("title")

    context = {
        "institution": institution,
        "programmes": programmes,
        "active": "education",
    }

    return render(
        request,
        "education/institution_detail.html",
        context
    )


# =========================================================
# EDUCATION PROGRAMMES & COURSES
# =========================================================

def programmes(request):
    items = EducationProgramme.objects.filter(
        is_published=True
    ).select_related("institution")

    search = request.GET.get("search", "").strip()

    if search:
        items = items.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(programme_type__icontains=search)
        )

    context = {
        "programmes": items,
        "search": search,
        "active": "education",
    }

    return render(
        request,
        "education/programmes.html",
        context
    )


# =========================================================
# SCHOLARSHIPS
# =========================================================

def scholarships(request):
    items = ScholarshipOpportunity.objects.filter(
        is_published=True
    )

    context = {
        "scholarships": items,
        "active": "education",
    }

    return render(
        request,
        "education/scholarships.html",
        context
    )


# =========================================================
# TEACHERS' SERVICES
# =========================================================

def teacher_services(request):
    items = TeacherService.objects.filter(
        is_published=True
    )

    context = {
        "teacher_services": items,
        "active": "education",
    }

    return render(
        request,
        "education/teacher_services.html",
        context
    )


# =========================================================
# SCHOOL ADMINISTRATORS' SERVICES
# =========================================================

def administrator_services(request):
    items = AdministratorService.objects.filter(
        is_published=True
    )

    context = {
        "administrator_services": items,
        "active": "education",
    }

    return render(
        request,
        "education/administrator_services.html",
        context
    )


# =========================================================
# EDUCATION FUNDING
# =========================================================

def education_funding(request):
    items = EducationFunding.objects.filter(
        is_published=True
    )

    context = {
        "funding": items,
        "active": "education",
    }

    return render(
        request,
        "education/funding.html",
        context
    )


# =========================================================
# EXAMINATIONS & ACADEMIC INFORMATION
# =========================================================

def examinations(request):
    items = ExaminationInformation.objects.filter(
        is_published=True
    ).order_by("-published_date", "title")

    context = {
        "examinations": items,
        "active": "education",
    }

    return render(
        request,
        "education/examinations.html",
        context
    )


# =========================================================
# EDUCATION SERVICES & REQUIREMENTS
# =========================================================

def education_services(request):
    items = EducationService.objects.filter(
        is_published=True
    )

    context = {
        "services": items,
        "active": "education",
    }

    return render(
        request,
        "education/services.html",
        context
    )


# =========================================================
# GOVERNMENT EDUCATION PROGRAMMES
# =========================================================

def government_programmes(request):
    items = GovernmentEducationProgramme.objects.filter(
        is_published=True
    )

    context = {
        "programmes": items,
        "active": "education",
    }

    return render(
        request,
        "education/government_programmes.html",
        context
    )


# =========================================================
# EDUCATION APPLICATIONS
# =========================================================

def education_application(request):
    if request.method == "POST":
        form = EducationApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)

            application.reference_number = (
                f"EDU-{timezone.now().strftime('%Y%m%d')}-"
                f"{uuid.uuid4().hex[:8].upper()}"
            )

            application.save()

            messages.success(
                request,
                f"Application submitted successfully. "
                f"Reference: {application.reference_number}"
            )

            return redirect("education:application_success")
    else:
        form = EducationApplicationForm()

    return render(
        request,
        "education/application.html",
        {
            "form": form,
            "active": "education",
        }
    )


def application_success(request):
    return render(
        request,
        "education/application_success.html",
        {
            "active": "education",
        }
    )


# =========================================================
# EDUCATION PROJECTS & INFRASTRUCTURE
# =========================================================

def education_projects(request):
    items = EducationProject.objects.filter(
        is_published=True
    ).order_by("-start_date", "title")

    context = {
        "projects": items,
        "active": "education",
    }

    return render(
        request,
        "education/projects.html",
        context
    )


# =========================================================
# EDUCATION UPDATES & NOTICES
# =========================================================

def education_notices(request):
    items = EducationNotice.objects.filter(
        is_published=True
    ).order_by(
        "-is_important",
        "-published_date"
    )

    context = {
        "notices": items,
        "active": "education",
    }

    return render(
        request,
        "education/notices.html",
        context
    )


# =========================================================
# REPORT AN EDUCATION PROBLEM
# =========================================================

def report_education_problem(request):
    if request.method == "POST":
        form = EducationProblemReportForm(request.POST)

        if form.is_valid():
            report = form.save(commit=False)

            report.reference_number = (
                f"EDU-REP-{timezone.now().strftime('%Y%m%d')}-"
                f"{uuid.uuid4().hex[:8].upper()}"
            )

            report.save()

            messages.success(
                request,
                f"Problem reported successfully. "
                f"Reference: {report.reference_number}"
            )

            return redirect(
                "education:problem_report_success"
            )
    else:
        form = EducationProblemReportForm()

    return render(
        request,
        "education/report_problem.html",
        {
            "form": form,
            "active": "education",
        }
    )


def problem_report_success(request):
    return render(
        request,
        "education/problem_report_success.html",
        {
            "active": "education",
        }
    )


# =========================================================
# GENERAL EDUCATION REQUEST
# =========================================================

def education_request(request):
    if request.method == "POST":
        form = EducationRequestForm(request.POST)

        if form.is_valid():
            education_request_obj = form.save(commit=False)

            education_request_obj.reference_number = (
                f"EDU-REQ-{timezone.now().strftime('%Y%m%d')}-"
                f"{uuid.uuid4().hex[:8].upper()}"
            )

            education_request_obj.save()

            messages.success(
                request,
                f"Education request submitted successfully. "
                f"Reference: {education_request_obj.reference_number}"
            )

            return redirect(
                "education:request_success"
            )
    else:
        form = EducationRequestForm()

    return render(
        request,
        "education/request.html",
        {
            "form": form,
            "active": "education",
        }
    )


def request_success(request):
    return render(
        request,
        "education/request_success.html",
        {
            "active": "education",
        }
    )


# =========================================================
# EDUCATION INFORMATION & GUIDANCE
# =========================================================

def education_information(request):
    items = EducationInformation.objects.filter(
        is_published=True
    )

    context = {
        "information": items,
        "active": "education",
    }

    return render(
        request,
        "education/information.html",
        context
    )


# =========================================================
# EDUCATION STATISTICS & REPORTS
# =========================================================

def education_statistics(request):
    statistics = EducationStatistic.objects.filter(
        is_published=True
    ).order_by(
        "-year",
        "title"
    )

    context = {
        "statistics": statistics,
        "active": "education",
    }

    return render(
        request,
        "education/statistics.html",
        context
    )
    
def learning_sources(request):
    """
    Main Learning Sources & Materials page.

    Shows only published learning resources and allows
    students to search and filter them.
    """

    resources = LearningResource.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    education_level = request.GET.get("education_level", "").strip()
    class_level = request.GET.get("class_level", "").strip()
    subject = request.GET.get("subject", "").strip()
    resource_type = request.GET.get("resource_type", "").strip()

    # Search
    if search:
        resources = resources.filter(
            Q(title__icontains=search)
            | Q(subject__icontains=search)
            | Q(topic__icontains=search)
            | Q(description__icontains=search)
            | Q(source_organization__icontains=search)
        )

    # Education level filter
    if education_level:
        resources = resources.filter(
            education_level=education_level
        )

    # Class/Form filter
    if class_level:
        resources = resources.filter(
            class_level__iexact=class_level
        )

    # Subject filter
    if subject:
        resources = resources.filter(
            subject__icontains=subject
        )

    # Resource type filter
    if resource_type:
        resources = resources.filter(
            resource_type=resource_type
        )

    # Subjects available in the current published resources
    subjects = (
        LearningResource.objects
        .filter(is_published=True)
        .exclude(subject="")
        .values_list("subject", flat=True)
        .distinct()
        .order_by("subject")
    )

    context = {
        "resources": resources,
        "subjects": subjects,

        "education_levels": (
            LearningResource.EDUCATION_LEVEL_CHOICES
        ),

        "resource_types": (
            LearningResource.RESOURCE_TYPE_CHOICES
        ),

        "search": search,
        "selected_education_level": education_level,
        "selected_class_level": class_level,
        "selected_subject": subject,
        "selected_resource_type": resource_type,

        "active": "education",
    }

    return render(
        request,
        "education/learning_sources.html",
        context
    )
    
def learning_resource_detail(request, pk):
    """
    Display one published learning resource.
    """

    resource = get_object_or_404(
        LearningResource,
        pk=pk,
        is_published=True
    )

    return render(
        request,
        "education/learning_resource_detail.html",
        {
            "resource": resource,
            "active": "education",
        }
    )