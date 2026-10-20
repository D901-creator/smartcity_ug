from django.db import models


class TourismDestination(models.Model):

    DESTINATION_TYPES = [
        ("national_park", "National Park"),
        ("wildlife_reserve", "Wildlife Reserve"),
        ("wildlife_area", "Wildlife Area"),
        ("waterfall", "Waterfall"),
        ("mountain", "Mountain"),
        ("lake", "Lake"),
        ("river", "River"),
        ("cultural_site", "Cultural Site"),
        ("historical_site", "Historical Site"),
        ("museum", "Museum"),
        ("game_drive", "Game Drive"),
        ("nature_site", "Nature & Nature Site"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    destination_type = models.CharField(
        max_length=50,
        choices=DESTINATION_TYPES
    )

    district = models.CharField(max_length=100)

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    attractions = models.TextField(
        blank=True,
        help_text="Main attractions or things visitors can see."
    )

    activities = models.TextField(
        blank=True,
        help_text="Activities available at the destination."
    )

    visitor_information = models.TextField(
        blank=True,
        help_text="Important information for visitors."
    )

    opening_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="tourism_destinations/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "title"]

    def __str__(self):
        return self.title
    
class TourismService(models.Model):

    SERVICE_TYPES = [
        ("accommodation", "Accommodation"),
        ("hotel", "Hotel"),
        ("lodge", "Lodge"),
        ("guest_house", "Guest House"),
        ("camping", "Camping"),
        ("tour_operator", "Tour Operator"),
        ("travel_agency", "Travel Agency"),
        ("tour_guide", "Tour Guide"),
        ("transport", "Tourism Transport"),
        ("visitor_service", "Visitor Service"),
        ("other", "Other Tourism Service"),
    ]

    title = models.CharField(max_length=200)

    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    services_offered = models.TextField(
        blank=True,
        help_text="Services provided to tourists or visitors."
    )

    facilities = models.TextField(
        blank=True,
        help_text="Facilities available."
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="tourism_services/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "title"]

    def __str__(self):
        return self.title


class CulturalHeritageSite(models.Model):

    SITE_TYPES = [
        ("cultural_site", "Cultural Site"),
        ("historical_site", "Historical Site"),
        ("museum", "Museum"),
        ("heritage_site", "Heritage Site"),
        ("traditional_site", "Traditional Site"),
        ("monument", "Monument"),
        ("archaeological_site", "Archaeological Site"),
        ("cultural_landscape", "Cultural Landscape"),
        ("other", "Other Heritage Site"),
    ]

    title = models.CharField(
        max_length=200
    )

    site_type = models.CharField(
        max_length=50,
        choices=SITE_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    historical_information = models.TextField(
        blank=True
    )

    cultural_significance = models.TextField(
        blank=True
    )

    visitor_information = models.TextField(
        blank=True
    )

    activities = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="cultural_heritage/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["district", "title"]

    def __str__(self):
        return self.title
    
class TourismEvent(models.Model):

    EVENT_TYPES = [
        ("tourism_event", "Tourism Event"),
        ("festival", "Festival"),
        ("cultural_event", "Cultural Event"),
        ("wildlife_event", "Wildlife Event"),
        ("exhibition", "Exhibition"),
        ("conference", "Tourism Conference"),
        ("adventure", "Adventure Activity"),
        ("community_event", "Community Tourism Event"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255
    )

    summary = models.TextField()

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    start_time = models.TimeField(
        blank=True,
        null=True
    )

    end_time = models.TimeField(
        blank=True,
        null=True
    )

    organizer = models.CharField(
        max_length=200,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="tourism_events/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["start_date", "title"]

    def __str__(self):
        return self.title


class WildlifeConservationInformation(models.Model):

    CONSERVATION_TYPES = [
        ("wildlife_protection", "Wildlife Protection"),
        ("habitat_conservation", "Habitat Conservation"),
        ("endangered_species", "Endangered Species"),
        ("community_conservation", "Community Conservation"),
        ("anti_poaching", "Anti-Poaching"),
        ("environmental_awareness", "Environmental Awareness"),
        ("conservation_programme", "Conservation Programme"),
        ("research", "Wildlife Research"),
        ("other", "Other"),
    ]

    title = models.CharField(
        max_length=200
    )

    conservation_type = models.CharField(
        max_length=50,
        choices=CONSERVATION_TYPES
    )

    district = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    wildlife_information = models.TextField(
        blank=True
    )

    conservation_actions = models.TextField(
        blank=True
    )

    community_information = models.TextField(
        blank=True
    )

    important_information = models.TextField(
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    image = models.ImageField(
        upload_to="wildlife_conservation/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class TourismProjectOpportunity(models.Model):

    OPPORTUNITY_TYPES = [
        ("tourism_project", "Tourism Project"),
        ("investment", "Tourism Investment"),
        ("community_tourism", "Community Tourism"),
        ("conservation_project", "Conservation Project"),
        ("hospitality", "Hospitality Development"),
        ("cultural_tourism", "Cultural Tourism"),
        ("eco_tourism", "Eco-Tourism"),
        ("employment", "Tourism Employment Opportunity"),
        ("partnership", "Partnership Opportunity"),
        ("other", "Other Opportunity"),
    ]

    STATUS_CHOICES = [
        ("planned", "Planned"),
        ("open", "Open"),
        ("ongoing", "Ongoing"),
        ("completed", "Completed"),
        ("closed", "Closed"),
        ("cancelled", "Cancelled"),
    ]

    title = models.CharField(
        max_length=200
    )

    opportunity_type = models.CharField(
        max_length=50,
        choices=OPPORTUNITY_TYPES
    )

    district = models.CharField(
        max_length=100
    )

    location = models.CharField(
        max_length=255,
        blank=True
    )

    summary = models.TextField()

    description = models.TextField()

    objectives = models.TextField(
        blank=True
    )

    benefits = models.TextField(
        blank=True
    )

    requirements = models.TextField(
        blank=True
    )

    implementing_organization = models.CharField(
        max_length=200,
        blank=True
    )

    contact_information = models.TextField(
        blank=True
    )

    website = models.URLField(
        blank=True
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    closing_date = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planned"
    )

    image = models.ImageField(
        upload_to="tourism_opportunities/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title