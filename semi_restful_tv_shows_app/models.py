from django.db import models


class ShowManager(models.Manager):
    def getErrors(self, postData):
        errors = {}

        # *** Works exactly like lines 13, 16, 21, 26!!
        # for key in postData.keys():
        #     if len(postData[key]) == 0:
        #         errors[key] = "all fields are required!"

        if len(postData['release_date']) == 0:
            errors['release_date'] = "Please include a release date."

        if len(postData['title']) == 0:
            errors['title'] = "Please include a title."
        elif len(postData['title']) < 2:
            errors['title'] = "Title must contain at least 2 characters."

        if len(postData['network']) == 0:
            errors['network'] = "Please include a network."
        elif len(postData['network']) < 3:
            errors['network'] = "Network must contain at least 3 characters."

        if len(postData['description']) == 0:
            errors['description'] = "Please include a description."
        elif len(postData['description']) < 10:
            errors['description'] = "Description must contain at least 10 characters."

        return errors


class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

