from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class personalData(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    short_bio = models.CharField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        try:
            this = personalData.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except personalData.DoesNotExist:
            pass
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
        
    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''
    
    def __str__(self):
        return self.name
    

class SocialLink(models.Model):
    CHOICE = (
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('LinkedIn', 'LinkedIn'),
        ('Instagram', 'Instagram'),
        ('GitHub', 'GitHub'),
        ('GitLab', 'GitLab'),
        ('Bitbucket', 'Bitbucket'),
        ('StackOverflow', 'StackOverflow'),
        ('ResearchGate', 'ResearchGate'),
        ('GoogleScholar', 'GoogleScholar'),
        ('CodeForces', 'CodeForces'),
        ('LeetCode', 'LeetCode'),
        ('Kaggle', 'Kaggle'),
        ('YouTube', 'YouTube'),
        ('HackerRank', 'HackerRank'),
    )
    
    name = models.CharField(max_length=100, choices=CHOICE)
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name


class Biography(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(null=False, blank=False)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    

class EducationalBackground(models.Model):
    CHOICE = (
        ('Current', 'Current'),
        ('Completed', 'Completed'),
    )
    program = models.CharField(max_length=100)
    provider = models.CharField(max_length=100)
    provider_link = models.URLField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=10, choices=CHOICE, default='Completed')
    result = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.program
    
    
class ResearchInterest(models.Model):
    field = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.field
    
    
class ProfessionalExperience(models.Model):
    position = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    organization_link = models.URLField(max_length=200, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField(null=True, blank=True)
    at_present = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.position} at {self.organization}"
    

class TeachingProtfolio(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class AwardsAndRecognition(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class Publication(models.Model):
    title = models.CharField(max_length=100)
    publication_body = models.CharField(max_length=100)
    link = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title
    

class QuickFact(models.Model):
    title = models.CharField(max_length=20)
    content = RichTextField(null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title