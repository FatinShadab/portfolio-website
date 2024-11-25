from django.contrib import admin
from .models import (
    personalData, SocialLink, Biography, QuickFact,
    TeachingProtfolio, AwardsAndRecognition, Publication,
    EducationalBackground, ResearchInterest, ProfessionalExperience
)

admin.site.register(personalData)
admin.site.register(SocialLink)
admin.site.register(Biography)
admin.site.register(TeachingProtfolio)
admin.site.register(AwardsAndRecognition)
admin.site.register(Publication)
admin.site.register(EducationalBackground)
admin.site.register(ResearchInterest)
admin.site.register(ProfessionalExperience)
admin.site.register(QuickFact)
