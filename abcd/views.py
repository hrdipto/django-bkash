from django.shortcuts import render

import json
from bkash_webhook import BkashWebhookListener
# Create your views here.
from django.http import HttpResponse


def homePageView(request):
    # bkash = BkashWebhookListener(json.loads("bKash Webhook Payload"))
    # res = bkash.bkash_response_process()
    return HttpResponse("HELLO WORD")