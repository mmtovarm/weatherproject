import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    new_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return new_date.strftime("%A %d %B %Y")

#google how to change the formmat
    


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    celsius = (float(temp_in_farenheit)-32)*5.0/9.0
    return round(float(celsius),1)
    #calculation
    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total= 0
    number_data = len(weather_data)
    new_weather_data = []
    for temp in weather_data:
        new_weather_data.append(float(temp)) 
    for temp in new_weather_data:
        total = total + temp
    return float(total/number_data)

    #calculation



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_list = []
    with open(csv_file) as weather_data:
        reader = csv.reader(weather_data)
        header = next(reader)
        for data in reader:
            if len(data)!= 0:
                weather_list.append([data[0],int(data[1]),int(data[2])])
            else:
                pass
    return weather_list
#skip the headers
#skip empty lines


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list.
    """
   
    count = 0
    if len(weather_data)!=0:
        mintemp = float(weather_data[0])
        for index,temp in enumerate(weather_data):
            if float(temp) <= mintemp:
                mintemp = float(temp)
                count = index
    else:
        return()
    return mintemp,count
    


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    count = 0
    if len(weather_data)!=0:
        maxtemp = float(weather_data[0])
        for index,temp in enumerate(weather_data):
            if float(temp) >= maxtemp:
                maxtemp = float(temp)
                count = index
    else:
        return()
    return maxtemp,count
    


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    ndays = len(weather_data)
    # print(weather_data[2][0])
    # min_temp = value[1]
    min_list = [] 
    max_list = []
    for value in weather_data:
         min_list.append(float(value[1]))
         max_list.append(float(value[2]))
    
    lowest_temp, index = (find_min(min_list))  # (49.0, 0)
    convert_date(weather_data[index][0])
    max_temp, index1 = (find_max(max_list))  #(68.0, 1)
    convert_date(weather_data[index1][0])
    calculate_mean(min_list)
    calculate_mean(max_list)

    output = f"{ndays} Day Overview\n"
    output += f"  The lowest temperature will be {format_temperature(convert_f_to_c(lowest_temp))}, and will occur on { convert_date(weather_data[index][0])}.\n"
    output += f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on { convert_date(weather_data[index1][0])}.\n"
    output += f"  The average low this week is {format_temperature(convert_f_to_c(calculate_mean(min_list)))}.\n"
    output += f"  The average high this week is {format_temperature(convert_f_to_c(calculate_mean(max_list)))}.\n"
    return output






def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    output = ""
    for row_weatherdata in weather_data:
           output += f"---- {convert_date(row_weatherdata[0])} ----\n"
           output += f"  Minimum Temperature: {format_temperature(convert_f_to_c(row_weatherdata[1]))}\n"
           output += f"  Maximum Temperature: {format_temperature(convert_f_to_c(row_weatherdata[2]))}\n\n"
    return output

example_one = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]


print(generate_daily_summary(example_one))


    

# print (f"---- {Friday 02 July 2021} ----\
#          Minimum Temperature: {9.4°C}\
#          Maximum Temperature: {19.4°C}")
 
 
