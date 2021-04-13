from django.shortcuts import render,HttpResponse
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
malemortality = round((maleDeath / malePositive) * 100,2)


femalePositive = df[df["Gender"] == 2]["Gender"].count()
femaleDeath = df[(df["Gender"] == 2) & (df["Death"] == 1)]["Gender"].count()
femalemortality = round((femaleDeath / femalePositive) * 100,2)

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
        'female_death':femalemortality,
        'totalDeath': totalMortality,
        'gender_death':gendermortality,
        'male_positive':malePositive,
        'female_positive':femalePositive,
        'total_positive': totalPositive,
    }

    return render(request, "upload.html", context)