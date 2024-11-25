from django.shortcuts import render
from .models import (
    personalData,
    SocialLink,
    Biography,
    EducationalBackground,
    ResearchInterest,
    ProfessionalExperience,
    TeachingProtfolio,
    AwardsAndRecognition,
    Publication,
    QuickFact
)

def index(request):
    # Query all active data from models
    personal_info = personalData.objects.filter(active=True).first()
    quick_fact = QuickFact.objects.filter(active=True).first()
    social_links = SocialLink.objects.all()
    biography = Biography.objects.filter(active=True).first()
    education = EducationalBackground.objects.all()
    research_interests = ResearchInterest.objects.filter(active=True)
    experiences = ProfessionalExperience.objects.all()
    teaching_portfolio = TeachingProtfolio.objects.all()
    awards = AwardsAndRecognition.objects.all()
    publications = Publication.objects.all()

    # Pass data to the context
    context = {
        'personal_info': personal_info,
        'social_links': social_links,
        'biography': biography,
        'education': education,
        'research_interests': research_interests,
        'experiences': experiences,
        'teaching_portfolio': teaching_portfolio,
        'awards': awards,
        'publications': publications,
        'quick_fact': quick_fact
    }
    
    return render(request, 'index.html', context)
