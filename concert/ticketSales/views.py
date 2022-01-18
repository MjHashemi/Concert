from django.http import HttpResponseRedirect
from django.shortcuts import render
import ticketSales
from ticketSales.models import concertModel,locationModel,timeModel
from django.urls import reverse
import accounts
from ticketSales.forms import SearchForm,ConcertForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def concertListView(request):
   searchForm=SearchForm(request.GET)
   if searchForm.is_valid():
      SearchText=searchForm.cleaned_data['SearchText']
      concerts=concertModel.objects.filter(Name__contains=SearchText)
   else:
      concerts=concertModel.objects.all()

   context={
      'concertlist':concerts,
      'concertcount':concerts.count(),
      'searchForm':searchForm
   }

   return render(request,'ticketSales/concertlist.html',context)
   
@login_required
def locationListView(request):
   locations=locationModel.objects.all()
   context={
      'locationlist':locations
   }

   return render(request,'ticketSales/locationlist.html',context)

def concertDetailsView(request,concert_id):
   concert=concertModel.objects.get(pk=concert_id)
   context={
      'concertdetails':concert
   } 
   return render(request,'ticketSales/concertDetails.html',context)

@login_required
def timeView(request):  
   times=timeModel.objects.all()
   context={
      'timelist':times
   }
   return render(request,'ticketSales/timeList.html',context)

def concertEditView(request,concert_id):
   concert=concertModel.objects.get(pk=concert_id)
   if request.method=='POST':
      concertForm = ConcertForm(request.POST,request.FILES,instance=concert)
      if concertForm.is_valid:
         concertForm.save()
         return HttpResponseRedirect(reverse(ticketSales.views.concertListView))

   else:   
      concertForm = ConcertForm(instance=concert)
   context={
      'concertForm':concertForm,
      'PosterImage':concert.Poster,
   }
   return render(request,'ticketSales/concertEdit.html',context)


   
