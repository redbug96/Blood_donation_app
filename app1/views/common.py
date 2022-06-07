from django.shortcuts import render

from app1.models import Donor, Login, Request_donor


# Create your views here.
def homepage(request):
    return render(request, 'Homepage.html')


def registerpage(request):
    return render(request, 'Registrationpage.html')


def loginpage(request):
    return render(request, 'Loginpage.html')


def check_login(request):
    username2 = request.POST['username2']
    password2 = request.POST['pswd2']
    try:
        fetch_row = Donor.objects.get(Username=username2)
        if fetch_row.Password == password2:
            if fetch_row.Validation == True:
                donor_id = fetch_row.id
                group = fetch_row.Blood_group
                blood_request = Request_donor.objects.filter(donor_id=donor_id).first()
                request.session['user'] = donor_id

                if blood_request and blood_request.status == 1:
                    return render(request, 'Userpage2.html', {'BloodGroup': group, 'id': donor_id})
                else:
                    return render(request, 'Userpage1.html', {'Donor_id': donor_id, 'Name': fetch_row.Name})

            else:
                return render(request, 'Loginpage.html',
                              {'error': 'Your registration has not approved ..please try later'})
        else:
            return render(request, 'Loginpage.html',
                          {'error': 'Login Failed'})

    except Donor.DoesNotExist:
        pass

    try:
        fetch_admin = Login.objects.get(username=username2)
        if (fetch_admin.password == password2):
            if (fetch_admin.role == 1):
                request.session['admin'] = fetch_admin.id
                return render(request, 'Adminpage1.html')
            return render(request, 'Loginpage.html',
                          {'error': 'Login Failed'})
        else:
            return render(request, 'Loginpage.html',
                          {'error': 'Login Failed'})

    except Login.DoesNotExist:
        return render(request, 'Loginpage.html',
                      {'error': 'Login Failed'})
