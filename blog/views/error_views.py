from django.shortcuts import render
from django.http import HttpResponse 
import os, json
def handler404(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "errors/404.html")
    a = {
        "status":False,
        "env": os.environ.get("ENV_NAME")
    }
    return HttpResponse(json.dumps(a), status=404, content_type = "application/json")
