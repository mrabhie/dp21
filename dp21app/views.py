from django.shortcuts import render
from django.http import HttpResponse
from dp21app import utilities
from dp21app import forms

#whats new: In this we have created botcatcher and also we have wrote clean_fieldname to validate form in class itself

def home(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES)
        if form.is_valid()==False:
            return render(request,"dp21app/sample.html",{'form':form})
        else:
            data=form.cleaned_data
            propic=data['propic']
            utilities.storeimage(propic)
            print(form.cleaned_data)
    form=forms.SampleForm()
    return render(request,"dp21app/sample.html",{'form':form})
