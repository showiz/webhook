import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import pprint

@csrf_exempt
@require_POST
def example(request):
    jsondata = request.body
    data = json.loads(jsondata)['notifications']
    pprint.pprint(data)
            
   
    

    return HttpResponse(status=200)


'''
Steps:
    1) Runserver: python3 manage.py runserver 127.0.0.1:8888
    2) Send Curl: 

            curl --header "Content-Type: application/json" \
            --request POST \
            --data '{"notifications": [
                {
                "channel": "customer",
                "tokens": ["6572764131ce2ec1594bb39f45546f362b2c3149ede045f3763d27fb7215cd0b"]
                }
            ]}' \
            http://localhost:8888/webhooks/example/

'''