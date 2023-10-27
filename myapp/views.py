from django.shortcuts import render
import requests

def reverse_contact_view(request):
    url = "https://api.reversecontact.com/enrichment"

    querystring = {"apikey":"sk_live_6533c6d6faf61105ee272487_key_ifits0xzgx","mail":"shah.jalal.ju.bd@gmail.com"}

    headers = {
        'accept': "application/json",
        'content-type': "application/json"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    context = {
        'response': response.text
    }

    return render(request, 'reverse_contact.html', context)