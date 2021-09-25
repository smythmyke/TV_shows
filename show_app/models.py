from django.db import models

# Create your models here.

    
class show_manager (models.Manager):
    def basic_validator (self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Title length needs to be longer"
        if len(postData['network']) < 3:
            errors["network"] = "Please make network title length longer"
        if len(postData["release_date"]) <5:
            errors["release_date"] = "Enter valid release date."
        if len(postData['description'])<=10:
            errors["description"] = "Make a longer description."
        return errors
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField (default="Enter a description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = show_manager()
    
    def __repr__(self):
        return f"<User object: {self.id} {self.title} {self.network} {self.release_date} {self.description}>"