
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render

from .models import (
    JobOpportunity,
    SkillsOpportunity,
    EmploymentInformation,
)


def home(request):

    context = {
        "page_title": "Jobs & Employment Opportunities",

        "page_description": (
            "Find job opportunities, internships, apprenticeships, "
            "skills development, career guidance and employment "
            "information through Smart City Uganda."
        ),

        "featured_jobs": JobOpportunity.objects.filter(
            is_published=True,
            is_featured=True,
        )[:6],

        "featured_skills": SkillsOpportunity.objects.filter(
            is_published=True,
            is_featured=True,
        )[:6],
    }

    return render(
        request,
        "jobs/home.html",
        context
    )


def opportunities(request):

    jobs = JobOpportunity.objects.filter(
        is_published=True
    )

    search = request.GET.get("search", "").strip()
    employment_type = request.GET.get(
        "employment_type",
        ""
    ).strip()
    sector = request.GET.get(
        "sector",
        ""
    ).strip()
    district = request.GET.get(
        "district",
        ""
    ).strip()
    status = request.GET.get(
        "status",
        ""
    ).strip()

    if search:

        jobs = jobs.filter(
            Q(title__icontains=search)
            | Q(organization__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(district__icontains=search)
            | Q(location__icontains=search)
        )

    if employment_type:
        jobs = jobs.filter(
            employment_type=employment_type
        )

    if sector:
        jobs = jobs.filter(
            sector=sector
        )

    if district:
        jobs = jobs.filter(
            district__iexact=district
        )

    if status:
        jobs = jobs.filter(
            status=status
        )

    context = {
        "jobs": jobs,

        "employment_types": (
            JobOpportunity.EMPLOYMENT_TYPES
        ),

        "sectors": (
            JobOpportunity.SECTOR_CHOICES
        ),

        "statuses": (
            JobOpportunity.STATUS_CHOICES
        ),

        "search": search,

        "selected_employment_type": employment_type,

        "selected_sector": sector,

        "selected_district": district,

        "selected_status": status,
    }

    return render(
        request,
        "jobs/opportunities.html",
        context
    )


def opportunity_detail(request, job_id):

    job = get_object_or_404(
        JobOpportunity,
        id=job_id,
        is_published=True,
    )

    return render(
        request,
        "jobs/opportunity_detail.html",
        {
            "job": job,
        }
    )


def skills(request):

    opportunities = SkillsOpportunity.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search",
        ""
    ).strip()

    opportunity_type = request.GET.get(
        "opportunity_type",
        ""
    ).strip()

    district = request.GET.get(
        "district",
        ""
    ).strip()

    status = request.GET.get(
        "status",
        ""
    ).strip()

    if search:

        opportunities = opportunities.filter(
            Q(title__icontains=search)
            | Q(organization__icontains=search)
            | Q(summary__icontains=search)
            | Q(description__icontains=search)
            | Q(target_group__icontains=search)
            | Q(district__icontains=search)
        )

    if opportunity_type:

        opportunities = opportunities.filter(
            opportunity_type=opportunity_type
        )

    if district:

        opportunities = opportunities.filter(
            district__iexact=district
        )

    if status:

        opportunities = opportunities.filter(
            status=status
        )

    return render(
        request,
        "jobs/skills.html",
        {
            "opportunities": opportunities,

            "opportunity_types": (
                SkillsOpportunity.OPPORTUNITY_TYPES
            ),

            "statuses": (
                SkillsOpportunity.STATUS_CHOICES
            ),

            "search": search,

            "selected_type": opportunity_type,

            "selected_district": district,

            "selected_status": status,
        }
    )


def skill_detail(request, skill_id):

    opportunity = get_object_or_404(
        SkillsOpportunity,
        id=skill_id,
        is_published=True,
    )

    return render(
        request,
        "jobs/skill_detail.html",
        {
            "opportunity": opportunity,
        }
    )


def career_guidance(request):

    information = EmploymentInformation.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search",
        ""
    ).strip()

    information_type = request.GET.get(
        "information_type",
        ""
    ).strip()

    if search:

        information = information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(content__icontains=search)
            | Q(key_points__icontains=search)
        )

    if information_type:

        information = information.filter(
            information_type=information_type
        )

    return render(
        request,
        "jobs/career_guidance.html",
        {
            "information": information,

            "information_types": (
                EmploymentInformation.INFORMATION_TYPES
            ),

            "search": search,

            "selected_type": information_type,
        }
    )


def employment_information(request):

    information = EmploymentInformation.objects.filter(
        is_published=True
    )

    search = request.GET.get(
        "search",
        ""
    ).strip()

    if search:

        information = information.filter(
            Q(title__icontains=search)
            | Q(summary__icontains=search)
            | Q(content__icontains=search)
            | Q(key_points__icontains=search)
        )

    return render(
        request,
        "jobs/employment_information.html",
        {
            "information": information,
            "search": search,
        }
    )


def statistics(request):

    total_jobs = JobOpportunity.objects.filter(
        is_published=True
    ).count()

    open_jobs = JobOpportunity.objects.filter(
        is_published=True,
        status="open",
    ).count()

    closing_soon = JobOpportunity.objects.filter(
        is_published=True,
        status="closing_soon",
    ).count()

    internships = JobOpportunity.objects.filter(
        is_published=True,
        employment_type="internship",
    ).count()

    apprenticeships = JobOpportunity.objects.filter(
        is_published=True,
        employment_type="apprenticeship",
    ).count()

    total_skills = SkillsOpportunity.objects.filter(
        is_published=True
    ).count()

    open_skills = SkillsOpportunity.objects.filter(
        is_published=True,
        status="open",
    ).count()

    total_information = EmploymentInformation.objects.filter(
        is_published=True
    ).count()

    jobs_by_sector = (
        JobOpportunity.objects
        .filter(is_published=True)
        .values(
            "sector"
        )
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    jobs_by_employment_type = (
        JobOpportunity.objects
        .filter(is_published=True)
        .values(
            "employment_type"
        )
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    jobs_by_district = (
        JobOpportunity.objects
        .filter(
            is_published=True
        )
        .exclude(
            district=""
        )
        .values(
            "district"
        )
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    skills_by_type = (
        SkillsOpportunity.objects
        .filter(is_published=True)
        .values(
            "opportunity_type"
        )
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    skills_by_status = (
        SkillsOpportunity.objects
        .filter(is_published=True)
        .values(
            "status"
        )
        .annotate(
            total=Count("id")
        )
        .order_by("-total")
    )

    context = {

        "total_jobs": total_jobs,

        "open_jobs": open_jobs,

        "closing_soon": closing_soon,

        "internships": internships,

        "apprenticeships": apprenticeships,

        "total_skills": total_skills,

        "open_skills": open_skills,

        "total_information": total_information,

        "jobs_by_sector": jobs_by_sector,

        "jobs_by_employment_type": jobs_by_employment_type,

        "jobs_by_district": jobs_by_district,

        "skills_by_type": skills_by_type,

        "skills_by_status": skills_by_status,
    }

    return render(
        request,
        "jobs/statistics.html",
        context
    )
