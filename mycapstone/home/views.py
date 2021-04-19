from django.shortcuts import render, HttpResponse
from django.shortcuts import render
import pandas as pd
import csv

data = pd.read_csv('./home/COVID19.csv')
count = data['Death'].count()
df = pd.DataFrame(data)

totalPositive = len(data)
totalDeath = df[df["Death"] == 1]["Death"].count()
totalMortality = round((totalDeath / totalPositive) * 100, 2)

malePositive = df[df["Gender"] == 1]["Gender"].count()
maleDeath = df[(df["Gender"] == 1) & (df["Death"] == 1)]["Gender"].count()
malemortality = round((maleDeath / malePositive) * 100, 2)


femalePositive = df[df["Gender"] == 2]["Gender"].count()
femaleDeath = df[(df["Gender"] == 2) & (df["Death"] == 1)]["Gender"].count()
femalemortality = round((femaleDeath / femalePositive) * 100, 2)

gendermortality = 100-(femalemortality+malemortality)


# ageGroups = {}

# ageGroups[1] = "0 to 19 Years"
# ageGroups[2] = "20 to 29 Years"
# ageGroups[3] = "30 to 39 Years"
# ageGroups[4] = "40 to 49 Years"

# ageGroups[5] = "50 to 59 Years"
# ageGroups[6] = "60 to 69 Years"
# ageGroups[7] = "70 to 79 Years"
# ageGroups[8] = "80 to 89 Years"

# for ageGroup in ageGroups:

#     age_positiveCount = df[(df["Age group"] == ageGroup)]["Age group"].count()
#     age_deathCount = df[(df["Age group"] == ageGroup) & (df["Death"] == 1)]["Age group"].count()

#     age=ageGroups[ageGroup]
#     age_death=round((age_deathCount / age_positiveCount) * 100,2)

totalDeath = maleDeath + femaleDeath
totalPositive = malePositive + femalePositive

# Create your views here.


def home(request):
    return render(request, 'home.html')


def upload(request):
    context = {
        'loaded_data': count,
        'male_death': malemortality,
        'female_death': femalemortality,
        'totalDeath': totalMortality,
        'gender_death': gendermortality,
        'male_positive': malePositive,
        'female_positive': femalePositive,
        'total_positive': totalPositive,
    }

    return render(request, "upload.html", context)


def download_csv_template(request):

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="covid-template.csv"'

    writer = csv.writer(response)
    writer.writerow(["Case identifier number", "Region", "Episode week", "Episode week group", "Episode year", 'Gender', 'Age group', "Occupation",
                    "Asymptomatic",	'Onset week of symptoms', "Onset year of symptoms",	"Hospital status", "Recovered",	"Recovery week", "Recovery year", "Death", "Transmission"])
    return response

def custom_csv_operations(request):

    download_url = "http://" + request.get_host() + "/download_csv_template"
    context = {

        "url": download_url
    }

    return render(request, "file.html", context)


###################################################################

# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from .forms import UploadFileForm

# # Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'file.html', {'form': form})

# def upload(request):
#     context = {
#         'Form': form,
#     }
