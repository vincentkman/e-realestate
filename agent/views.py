from django.shortcuts import render, get_object_or_404

from .models import Agent

def about(request):
    agents = Agent.objects
    return render(request, 'agent/about.html', {'agents': agents})

def detail(request, agent_id):
    detailagent = get_object_or_404(Agent, pk=agent_id)
    return render(request, 'agent/detail.html', {'agent':detailagent})

