from django.shortcuts import render
import speedtest

# Create your views here.
def home(request):
    return render(request,'speed/index.html',{})

def results(request):
    st=speedtest.Speedtest()
    ds=round((st.download()/1000000),2)
    du=round((st.upload()/1000000),2)
    print(st.download())
    print(st.upload())
    servernames =[]  
  
    print(st.get_servers(servernames))
  
    print(st.results.ping)  
  

    return render(request,'speed/results.html',{'ds':ds,'st':st,'du':du})
