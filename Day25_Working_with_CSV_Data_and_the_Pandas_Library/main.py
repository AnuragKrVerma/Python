# import csv

# with open("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/226 weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] !="temp":
#             temperature.append(int(row[1]))
#     print(temperature)
        
import pandas

data = pandas.read_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/226 weather-data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# print(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# # get data in column
# print(data["condition"])
# print(data.condition)

# # get data in row
# print(data[data.temp == 12]) 
# print(data[data.day == "Tuesday"]) 
# print(data[data.condition == "Sunny"]) 

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# # converting monday temperature celsius into fehranheit
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp *9/5 +32
# print(monday_temp_F)

# # create a data frame from scratch
# data_dict = {
#     "student" : ["Def" , "Efg" , "Abc"],
#     "scores" : [76,24,58]
# }

# data_frame = pandas.DataFrame(data_dict)
# print(data_frame)
# data_frame.to_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/raw_data.csv")

data = pandas.read_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color" : ["Gray" , "Cinnimon","Black"],
    "Count" : [grey_squirrels_count , red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/squirrels_count.csv")