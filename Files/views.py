from django.shortcuts import render
from .models import files
def index(request):
    Phy=files.objects.order_by('-N').filter(subject='Physics')
    Chem=files.objects.order_by('-N').filter(subject='Chemistry')
    context={
        'phy':Phy,
        'chem':Chem
    }
    return render(request,'startup/index.html',context)
def physics(request):
    Phy=files.objects.order_by('-N').filter(subject='Physics')
    context={
        'phy':Phy,
    }
    return render(request,'startup/physics.html',context)
def chemistry(request):
    Chem=files.objects.order_by('-N').filter(subject='Chemistry')
    context={
        'chem':Chem,
    }
    return render(request,'startup/chemistry.html',context)
import mimetypes
def download(request,file_name):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as F:
            response = HttpResponse(fh.read(), content_type="application/adminupload" )
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path) 
            return response
    raise Http404