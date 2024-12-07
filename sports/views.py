from django.shortcuts import render, redirect, get_object_or_404
from .models import Sport


def sport_list(request):
    sports = Sport.objects.all()
    ctx = {'sports': sports}
    return render(request, 'sports/sport-list.html', ctx)

def sport_form(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if event_name and location and date and sport_type:
            Sport.objects.create(
                event_name=event_name,
                location=location,
                date=date,
                sport_type=sport_type,
            )
            return redirect('sports:list')
    return  render(request, 'sports/sport-form.html')

def sport_detail(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    ctx = {'sport':sport}
    return render(request, 'sports/sport-detail.html', ctx)

def sport_update(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        sport_type = request.POST.get('sport_type')
        if event_name and location and date and sport_type:
            sport.event_name=event_name
            sport.location=location
            sport.date=date
            sport.sport_type=sport_type
            sport.save()
            return redirect(sport.get_detail_url())
    ctx = {'sport': sport}
    return render(request, 'sports/sport-form.html', ctx)

def sport_delete(request, pk):
    sport = get_object_or_404(Sport, pk=pk)
    sport.delete()
    return redirect('sports:list')







































