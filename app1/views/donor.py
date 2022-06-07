from django.shortcuts import render, redirect

from app1.models import Donor, Request_donor
from .common import homepage


def user_home(request):
    donor_id = request.session['user']
    if not donor_id:
        return redirect(user_logout)
    donor = Donor.objects.get(id=donor_id)
    return render(request, 'Userpage1.html', { 'Name': donor.Name })


def saving_form_data(request):
    name = request.POST['name1']
    age = request.POST['age1']
    gender = request.POST['gender1']
    blood_group = request.POST['blood1']
    district = request.POST['district1']
    mobile_number = request.POST['number1']
    email_id = request.POST['emailID1']
    photo = request.FILES['photo1']
    health_issue = request.POST['health1']
    username = request.POST['username1']

    password = request.POST['pswd1']
    validate = False
    save_data = Donor(Name=name, Age=age, Gender=gender, Blood_group=blood_group, District=district,
                      Mobile_number=mobile_number, Mail_id=email_id, Photo=photo, Health_issue=health_issue,
                      Username=username, Password=password, Validation=validate)
    if(Donor.objects.filter(Username=username)):
        return render(request,'Registrationpage.html',{'error':'Username "'+username+'" already exist'})
    save_data.save()
    return render(request, 'Homepage.html', {'message': 'Registration successfull.Please login after you receive an '
                                                        'approval mail'})


def user_logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return homepage(request)


def accept_request(request):
    donor_id = request.session['user']
    if not donor_id:
        return user_logout(request)
    change_status = Request_donor.objects.filter(donor_id=donor_id).first()
    change_status.status = 2
    change_status.save()
    return user_home(request)


def reject_request(request):
    donor_id = request.session['user']
    if not donor_id:
        return user_logout(request)
    change_status = Request_donor.objects.filter(donor_id=donor_id).first()
    change_status.status = 3
    change_status.save()
    return user_home(request)


def update_profile(request):
    donor_id = request.session['user']
    if not donor_id:
        return user_logout(request)
    donor_data = Donor.objects.filter(id=donor_id)
    return render(request, 'Updatepage.html', {'DonorData': donor_data})


def updation(request):
    donor_id = request.session['user']
    if not donor_id:
        return user_logout(request)
    name = request.POST['name1']
    age = request.POST['age1']
    gender = request.POST['gender1']
    blood_group = request.POST['blood1']
    district = request.POST['district1']
    mobile_number = request.POST['number1']
    email = request.POST['emailID1']
    health_issue = request.POST['health1']
    username = request.POST['username1']
    password = request.POST['pswd1']
    Donor.objects.filter(id=donor_id).update(Name=name, Age=age, Gender=gender, Blood_group=blood_group,
                                             District=district, Mobile_number=mobile_number, Mail_id=email,
                                             Health_issue=health_issue, Username=username, Password=password)
    return user_home(request)
