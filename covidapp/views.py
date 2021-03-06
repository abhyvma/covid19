from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "1e2450b663msh3d11a1245398627p18dac5jsnb7a585f122a3",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)
# Create your views here.
def helloworldview(request):
	
	mylist=[]
	noofresults=int(response['results'])

	for x in range(0,noofresults):
		mylist.append(response['response'][x]['country'])

    
	if request.method=="POST" and request.POST['selectedcountry']!="Select Country":
		selectedcountry=request.POST['selectedcountry']
		
		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country']:
				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)
			
		mylist.sort()
		context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
		return render(request,'index.html',context)
	mylist.sort()			
	# context={'mylist':mylist}
	new=active=critical=recovered=deaths=total=0
	context={'selectedcountry':"Please Select Country",'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
	return render(request,'index.html',context)
