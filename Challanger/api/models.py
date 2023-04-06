from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Room(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    challenge = models.TextField()
    inviter = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='sent_invites')
    invitee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='received_invites')
    status = models.CharField(max_length=10, choices=(('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')))