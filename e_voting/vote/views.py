from django.views import View
import json
from .models import Party, Vote
from django.core.serializers import serialize
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from e_voting.settings.base import DEBUG

class VoteView(View):
    double_vote_message = "Oops! Only one vote allowed, buddy. Be a nice child, just like your mom taught you!"

    def get_response(self, request, cookies=None):
        data = self.format_serialized_data(self.serialize_parties())
        context = {"DATA": data}
        response  = render(request=request, template_name="vote.html", context=context)
        if(cookies):
            response.set_cookie(**cookies)


        return response
    
    def serialize_parties(self):
        data = serialize('json', Party.objects.all(), fields=('name', 'code'))
        return json.loads(data)

    def format_serialized_data(self, data):
        return [data_dict['fields'] for data_dict in data]

    def post(self, request):
        email = request.POST.get('email')
        voter_name = request.POST.get('voterName')
        party_option = request.POST.get('partyOptions')
        if(DEBUG=="True"):
            ip_address = request.META.get('REMOTE_ADDR')
        else:      
            ip_address = request.META.get('HTTP_X_REAL_IP')

        cookie_value = request.COOKIES.get('d')

        if None in [email, voter_name, party_option, ip_address] or any(len(value) == 0 for value in [email, voter_name, party_option]):
            if not email:
                messages.add_message(request, messages.ERROR, "Please enter a valid email.", extra_tags='email')
            elif not voter_name:
                messages.add_message(request, messages.ERROR, "Please enter your full name.", extra_tags='voterName')

        elif Vote.objects.filter(Q(voter_ip=ip_address) | Q(voter_email=email)) or (cookie_value and cookie_value == "1"):
            messages.add_message(request, messages.INFO, self.double_vote_message )

            
        else:
            voted_party = Party.objects.filter(code=party_option).first()
            Vote.objects.create(voter_name=voter_name, voter_ip=ip_address, voter_email=email, voted_party=voted_party)
            messages.add_message(request, messages.INFO, f"Vote added. Hmm, {party_option}! Nice Choice.")
            return self.get_response(request=request, cookies={"key": "d", "value": "1"})

        return self.get_response(request=request)

    def get(self, request):
        return self.get_response(request=request)
