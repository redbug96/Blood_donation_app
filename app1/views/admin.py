from django.core.mail import send_mail
from django.shortcuts import render

from app1.models import Donor, Request_donor
from .common import homepage


def search_donor(request):
    admin_id = request.session['admin']
    if not admin_id:
        return admin_logout(request)

    district = request.POST['district1']
    blood_group = request.POST['blood1']
    searching = Donor.objects.filter(District=district, Blood_group=blood_group)
    return render(request, 'searchedData.html', {'required_donors': searching})

def requesting(request):
    get_id = request.POST['id']
    email_row = Donor.objects.filter(id=get_id).first()
    get_email = email_row.Mail_id
    try:
        send_mail(
            'Urgently Require Blood Donor!!',
            'We need blood donor Urgently.Please login your blood donating site and accpet the request if you are able to donate the blood',
            'sakrk.dev@gmail.com',
            [get_email],
            fail_silently=False,
        )
    except Exception as e:
        print("Mail couldn't send" + {e})
    try:
        donor = Request_donor.objects.get(donor_id=get_id)
        donor.status = 1
        donor.save()

    except Request_donor.DoesNotExist:
        store_request = Request_donor(donor_id=get_id, status=1)
        store_request.save()
    return render(request, 'RequestSend.html')


def approve_donors(request):
    admin_id = request.session['admin']
    if not admin_id:
        return admin_logout(request)
    user_data1 = Donor.objects.filter(Validation=False)
    return render(request, 'DonorApprove.html', {'donors': user_data1})


def approve(request):
    admin_id = request.session['admin']
    if not admin_id:
        return admin_logout(request)
    donor_id = request.POST['id']
    donor = Donor.objects.filter(id=donor_id).first()

    if donor:
        donor.Validation = True
        donor.save()
        try:
            send_mail(
                '[Rapid Red Bucket] : Registration approved!!',
                'Your registration was successfully done.Please login your account',
                'sakrk.dev@gmail.com',
                [donor.Mail_id],
                fail_silently=False,
            )
        except Exception as e:
            print("Mail couldn't send" + {e})
    return approve_donors(request)


def admin_logout(request):
    try:
        del request.session['admin']
        return homepage(request)
    except KeyError:
        pass
