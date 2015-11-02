import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from testapp.models import ForTest


# def testappinwork(request):
#     informatin = ForTest.objects.get(id=2)
#     html = "{}".format(informatin.name)
#     return HttpResponse(html)


def processed(request, id):
    getinf = get_object_or_404(ForTest, pk=id)
    if not getinf.processed:
        getinf.processed = True
        getinf.save()
        html = ("<html><body>0</body></html>")
    else:
        html = ("<html><body>1</body></html>")
    return HttpResponse(html)
