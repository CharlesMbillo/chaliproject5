from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import User

def User(request):
    form = User()

    if request.method == 'POST':
        form = User(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    context = {
        "form": form,
    }

    return render(request, 'user_form.html', context)

#import phonenumbers
#from phonenumbers import PhoneNumberFormat
#from phonenumbers.phonenumberutil import NumberParseException
#from django.shortcuts import render, redirect
#from .forms import forms

#def User(request):
#    if request.method == 'POST':
        # If the form was submitted, process the data
 #       forms = User(request.POST)
  #      if forms.is_valid():
           # Form data is valid, save the user profile
  #          forms.save()
   #         return redirect('success')  # Redirect to a success page
   # else:
    #    # If it's a GET request, display the empty form
     #   forms = User()

    #return render(request, 'user_form.html', {'forms': forms})

def success(request):
    # You can create a success page template or handle it as needed
    return render(request, 'success.html')


#from django.shortcuts import render, redirect
#from .forms import User

#def User(request):
 #   if request.method == 'POST':
      # If the form was submitted, process the data
   #     form = User(request.POST)
    #    if forms.is_valid():
            # Form data is valid, save the user profile
  #          forms.save()
   #         return redirect('success')  # Redirect to a success page
    #else:
        # If it's a GET request, display the form with any previous user input
     #   forms = User()

   # return render(request, 'user_form.html', {'forms': forms})
