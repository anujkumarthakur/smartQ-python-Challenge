import csv
from django.shortcuts import render
#from django.template import loader
#your views here.

def index(request):
    filename = "restaurant_addc9a1430.csv"
    fields = []
    rows = []
    with open(filename , 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = csvreader.next()
        for row in csvreader:
            rows.append(row)
    for row in rows:
        for col in row:
            return render(request, 'index.html', col)
    #args = {}
    #file_url = urllib.request.urlopen("restaurant_addc9a1430.csv")
    #file_url_response = urllib.urlopen(file_url)
    #pre_reader = csv.reader(file_url)
    #args['list'] = pre_reader
    #csv_dict = {rows[0]:rows[1] for rows in pre_reader}
    #args['csv_dict'] = csv_dict
    #return render(request, 'index.html', args)
    #return render(request,'index.html')

    
    
