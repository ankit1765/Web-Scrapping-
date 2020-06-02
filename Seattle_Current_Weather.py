# Resources followed
# https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
# https://www.dataquest.io/blog/web-scraping-tutorial-python/

import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=47.6036&lon=-122.3294#.XtWfe55KgWp")
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast") #seven_day is HTML code of all tags with seven-day-forecast

forecast_items = seven_day.find_all(class_="tombstone-container") #finding all tombstone-containers inside seven_day

#tonight = forecast_items[0] #Extracted HTML code for today's weather

#print(tonight.prettify())

# > print(tonight.find(class_ = "period-name")) ###this extracts that line of HTML

#day = tonight.find(class_ = "period-name").get_text() #this extracts the contents
#short_desc = tonight.find(class_ = "short-desc").get_text()
#temp = tonight.find(class_ = "temp").get_text()

#print(day)
#print(short_desc)
#print(temp)

#img = tonight.find("img")
#desc = img['title']
#print(img)

#print(desc)

#Creating lists of days, short description, temperatures, and detailed descriptions in order
day_tags = seven_day.select(".tombstone-container .period-name")
short_desc_tags = seven_day.select(".tombstone-container .short-desc")
temp_tags =  seven_day.select(".tombstone-container .temp")
desc_tags = seven_day.select(".tombstone-container img")


#Each index represents a day. Printing all info for each day.
num_of_days = len(day_tags)
count = 0

day = [0,1,2,3,4,5,6,7,8]
short_description = [0,1,2,3,4,5,6,7,8]
temperature = [0,1,2,3,4,5,6,7,8]
detailed_description = [0,1,2,3,4,5,6,7,8]

while (count != num_of_days):
    print(day_tags[count].get_text())
    day[count] = day_tags[count].get_text()

    print(short_desc_tags[count].get_text())
    short_description[count] = short_desc_tags[count].get_text()

    print(temp_tags[count].get_text())
    temperature[count] = temp_tags[count].get_text()

    var = desc_tags[count]
    descc = var['title']
    print(descc)
    detailed_description[count] = descc

    print('\n')
    count +=1


#Combining Data into Pandas DataFrame
weather = pd.DataFrame({
    "Day": day,
    "Short Description":  short_description,
    "Temperature": temperature,
    "Detailed Description": detailed_description
})



#Pull out numeraical values of temperature
temp_int = weather["Temperature"].str.extract("(?P<temp_num>\d+)", expand=False)
#There is a new column named temp_num that has only numerical values of temperature
print(temp_int)
weather["temp_num"] = temp_int.astype('int')


#Printing the average value
print(weather["temp_num"].mean())

#Exporting the data to a local file
weather.to_csv('weather.csv', index=False)