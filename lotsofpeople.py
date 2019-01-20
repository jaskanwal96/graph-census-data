from mongoengine import connect,Q
from models import adults
import csv

connect('test3')


with open ('adult.csv', 'r') as f:
    reader = csv.reader(f)
    bulk_people = []
    for rows in reader:
        bulk_people.append(adults(age=rows[0], workclass=rows[1], fnlgwt=rows[2], education=rows[3],education_num=rows[4], martial_status=rows[5],occupation=rows[6],relationship=rows[7],race=rows[8],sex=rows[9],capital_gain=rows[10],capital_loss=rows[11],hours_per_week=rows[12],native_country=rows[13],salary=rows[14]))

adults.objects.insert(bulk_people)
print(bulk_people)