from django.shortcuts import render, get_object_or_404

from .models import Listing

def home(request):
    listings = Listing.objects
    return render(request, 'listings/home.html', {'listings': listings})
# from .models import Agent

# def about(request):
#     agents = Agent.objects
#     return render(request, 'agent/about.html', {'agents': agents})

# def detail(request, listing_i):
#     detaillisting = get_object_or_404(Listing, pk=listing_id)
#     return render(request, 'agent/detail.html', {'listings':detaillisting})

