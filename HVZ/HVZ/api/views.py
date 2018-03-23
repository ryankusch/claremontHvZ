import json

from django.http import HttpResponse, HttpRequest
from HVZ.main.models import Player

def json_get_all_emails(request):
    """A function that displays every players email
    in the current game.
    """

    # Check out HVZ/main/models.py for helper functions relating to Players.
    # Player.current_players() returns all Players in the current Game.
    emails = [(str(p.user.first_name) + " " + str(p.user.last_name), p.mailbox) for p in Player.current_players()]

    # json.dumps creates a string from a Python object. You can then
    # read the string and convert it into an Objective-C data
    # structure using NSJSONSerialization in Objective-C.
    json_data = json.dumps(emails)

    return HttpResponse(
        json_data,
        content_type="application/json"
    )
