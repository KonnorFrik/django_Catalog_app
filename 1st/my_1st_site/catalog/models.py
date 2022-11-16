from django.db import models
from django.contrib.auth.models import User


class IUser(User):
    first_name = None
    last_name = None
    email = None
    is_staff = None
    

class UserNote(models.Model):
    note_title = models.CharField(max_length=100)
    note_description = models.CharField(max_length=300, blank=True, default="")

    user = models.ForeignKey(IUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_title


class AnyFile(models.Model):
    title = models.CharField(max_length=25)
    file = models.FileField(upload_to="catalog/any_files/")

    user_note = models.ForeignKey(UserNote, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


# class TextNote(models.Model):
#     txt_title = models.CharField(max_length=20, default="")
#     txt_text = models.CharField(max_length=250)
#
#     user_note = models.ForeignKey(UserNote, on_delete=models.CASCADE)
