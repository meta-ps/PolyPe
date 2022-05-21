from django.shortcuts import render,redirect
from polype.models import User
import qrcode
import qrcode.image.svg
from io import BytesIO
import requests

#https://docs.polygonscan.com/v/mumbai-polygonscan/
API_KEY='26HRQTXB2S9AF97GPBT6RHTEUAEQA7HQUI'

# Create your views here.
def Home(request):
    if request.POST:
        username = request.POST.get('username')
        walletAddress = request.POST.get('coinBaseWalletAddress')
        print(username)
        print(walletAddress)
       
        if User.objects.filter(username=username).exists():
            print('userfound not saved again')
        else:
            user = User()
            user.username = username
            user.walletAddress = walletAddress
            user.save()
        return redirect('userview',username)

    return render(request,'home.html')



def UserView(request,username):
    if User.objects.filter(username=username).exists():
        obj = User.objects.get(username=username)
    else:
        obj=None
    
    context = {'walletAddress':obj.walletAddress,'username':obj.username}

    factory = qrcode.image.svg.SvgImage
    img = qrcode.make(obj.walletAddress, image_factory=factory, box_size=20)
    stream = BytesIO()
    img.save(stream)
    context["svg"] = stream.getvalue().decode()

    BASE_URL = 'https://api-testnet.polygonscan.com/api?module=account&action=txlist&address='
    END_URL = '&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=26HRQTXB2S9AF97GPBT6RHTEUAEQA7HQUI'

    url = BASE_URL + str(obj.walletAddress) + END_URL
    print(url)
    response = (requests.get(url)).json()
    print(response)
    context['txnHistory'] = response

    return render(request,'user.html',context)
