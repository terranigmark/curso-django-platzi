"""Platzigram views"""
# Django
from django.http import HttpResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Returns a greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    # return HttpResponse('Hello, world!')
    return HttpResponse(f'Oh, hi! Current server time is {str(now)}')

def sort_integers(request):
    """Return a JSON response with sorted numbers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }

    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = f"Sorry {name.title()}, you're not allowed here."
    else:
        message = f"Hello {name.title()}, welcome to Platzigram!"
    return HttpResponse(message)