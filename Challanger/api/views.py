from django.shortcuts import render, redirect
from .models import Person, Room


def invite(request):
    if request.method == 'POST':
        inviter = Person.objects.get(email=request.POST['inviter_email'])
        invitee = Person.objects.get(email=request.POST['invitee_email'])
        room = Room.objects.create(
            name=request.POST['room_name'],
            description=request.POST['room_description'],
            challenge=request.POST['room_challenge'],
            inviter=inviter,
            invitee=invitee,
            status='pending'
        )
        return redirect('invite_sent')
    else:
        return render(request, 'invite.html')


def invite_sent(request):
    return render(request, 'invite_sent.html')


def accept_invite(request, room_id):
    room = Room.objects.get(id=room_id)
    room.status = 'accepted'
    room.save()
    return redirect('invite_accepted')


def invite_accepted(request):
    return render(request, 'invite_accepted.html')


def reject_invite(request, room_id):
    room = Room.objects.get(id=room_id)
    room.status = 'rejected'
    room.save()
    return redirect('invite_rejected')


def invite_rejected(request):
    return render(request, 'invite_rejected.html')
