from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from fixtures.models import Match
from club.models import Club

# Create your views here.


def index(request):
    matches = Match.objects.filter()

    matches_processed = []

    for m in matches:
        matches_processed.append({
            'host_name': Club.objects.filter(id=m.host_id).first().name,
            'guest_name': Club.objects.filter(id=m.guest_id).first().name,
            'host_score': m.host_score,
            'guest_score': m.guest_score
        })
    return render(request, 'homepage.html',
                  {
                      'matches': matches_processed
                  }
                  )

def user_login(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        # next = request.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                redirect_to = request.POST.get('next')
                if redirect_to:
                    return HttpResponseRedirect(redirect_to)
                else:
                    return HttpResponseRedirect('/')
    return render_to_response('login.html', context_instance=RequestContext(request))