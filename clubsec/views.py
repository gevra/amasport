from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.timezone import utc
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from fixtures.models import Match
from club.models import Club

# Create your views here.


def register_goal(request):
    print("hello there")

    try:
        score_host = request.GET.get('score_host')
    except:
        print("can't get the host score")
        score_host = 0

    try:
        score_guest = request.GET.get('score_guest')
    except:
        print("can't get the guest score")
        score_guest = 0

    try:
        scorer_host = request.GET.get('scorer_host')
    except:
        print("can't get the scorer against the hosts")
        scorer_host = 0

    try:
        score_guest = request.GET.get('scorer_guest')
    except:
        print("can't get the scorer against the guests")
        scorer_guest = 0


    # update the scores
    match = Match.objects.filter(id=4).first()

    # load the page again
    return render(request, 'club_sec_main.html',
                  {
                      'club_name_short': "bluebell",
                      'host_name': Club.objects.filter(id=match.host_id).first().name,
                      'guest_name': Club.objects.filter(id=match.guest_id).first().name,
                      'host_score': match.host_score+1,
                      'guest_score': match.guest_score
                  }
          )

def load_club_sec_main(request):
    match = Match.objects.filter(id=4).first()

    return render(request, 'club_sec_main.html',
                  {
                      'club_name_short': "bluebell",
                      'host_name': Club.objects.filter(id=match.host_id).first().name,
                      'guest_name': Club.objects.filter(id=match.guest_id).first().name,
                      'host_score': match.host_score,
                      'guest_score': match.guest_score
                  }
          )

def load_club_sec_input_page(request):
    return render(request, 'club_sec_input_page.html',
                  {
                      'host': "UCD",
                      'guest': "Manchester United",
                  }
          )