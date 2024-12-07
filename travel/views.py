from django.shortcuts import render, redirect, get_object_or_404
from .models import Travel


def travel_list(request):
    travel = Travel.objects.all()
    ctx = {'travel': travel}
    return render(request, 'travel/travel-list.html', ctx)

def travel_form(request):
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        popular_season = request.POST.get('popular_season')
        if destination_name and country and description and popular_season:
            Travel.objects.create(
                destination_name=destination_name,
                country=country,
                description=description,
                popular_season=popular_season
            )
            return redirect('travel:list')
    return render(request, 'travel/travel-form.html')

def travel_detail(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    ctx = {'travel': travel}
    return render(request, 'travel/travel-detail.html', ctx)

def travel_update(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    if request.method == 'POST':
        destination_name = request.POST.get('destination_name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        popular_season = request.POST.get('popular_season')
        if destination_name and country and description and popular_season:
            travel.destination_name=destination_name
            travel.country=country
            travel.description=description
            travel.popular_season=popular_season
            travel.save()
            return redirect(travel.get_detail_url())
    ctx = {'travel': travel}
    return render(request, 'travel/travel-form.html', ctx)

def travel_delete(request, pk):
    travel = get_object_or_404(Travel, pk=pk)
    travel.delete()
    return redirect('travel:list')























