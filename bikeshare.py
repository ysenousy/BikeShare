import time
import pandas as pd
import numpy as np
import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAY_DATA = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input("Please write a city from the following: Chicago, New York City or Washington! ")
            print('*'*40)
            city.lower()
            if city in CITY_DATA:
                break
            else:
                print("Error! Please Enter From The City List.")
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
            month = input("By Which Month you want January, Feburary, March, April, May, June, or All? ")
            print('*'*40)
            month.lower()
            if month in MONTH_DATA:
                break
            else:
                print("Error! Please A Valid Month.")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
            day = input("Which day you want? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All? ")
            print('*'*40)
            day.lower()
            if day in DAY_DATA:
                break
            else:
                print("Error! Please A Valid Day.")

    print ('You Choose City: '+city+' and Month: '+month+' and Day: '+day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load Data to Dataframe
    while True:
        df = pd.read_csv(CITY_DATA[city])

        # convert the Start Time column to datetime
        df['Start Time'] = pd.to_datetime(df['Start Time'])

        # extract month and day of week and hour from Start Time and create new columns(months,day of week and hour)
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        df['hour'] = df['Start Time'].dt.hour

        # filter by month if applicable
        if month != 'all':
            month =  MONTH_DATA.index(month) + 1
            df = df[ df['month'] == month ]

        # filter by day of week if applicable
        if day != 'all':
            print(day)
            # filter by day of week to create the new dataframe
            df = df[ df['day_of_week'] == day.title()]

            #print(tabulate.tabulate(df, tablefmt='grid', showindex=False))
            return df
    else:
        print('We can\'t read the file')

def hour_12_converter(hour):
    """
    Converts an int hour to AM or PM
    """

    if hour == 0:
        AM_PM_hour = '12 AM'
    elif hour == 12:
        AM_PM_hour = '12 PM'
    else:
        AM_PM_hour = '{} AM'.format(hour) if hour < 12 else '{} PM'.format(hour - 12)

    return AM_PM_hour

        
def time_stats(df, city):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    try:
        pop_month_num = df['Start Time'].dt.month.mode()[0]
        pop_month = MONTH_DATA[pop_month_num-1].title()
        print('The most popular month in', city, 'is:', pop_month)
    except Exception as ex:
        print('Can\'t calculate as an Error occurred: {}'.format(ex))

        # display the most common day of week
    try:
            pop_day_of_week = df['day_of_week'].mode()[0]
            print('The most popular weekday in', city, 'is:',pop_day_of_week)
    except Exception as ex:
            print('Can\'t calculate as an Error occurred: {}'.format(ex))

        # display the most common start hour
    try:
            pop_start_hour = hour_12_converter(df['hour'].mode()[0])
            print('The most popular starting hour in', city, 'is:',pop_start_hour)
    except Exception as ex:
            print('Can\'t calculate as an Error occurred: {}'.format(ex))
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('-'*40)
     # display most commonly used start station
    comm_start_station = df['Start Station'].mode()[0]    
    print("The most commonly used start station is ", comm_start_station, "\n")
    print('-'*40)    
    # display most commonly used end station
    comm_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is ", comm_end_station, "\n")
    print('-'*40)
    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + "to " + df['End Station']
    comm_str_end_station = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ", comm_str_end_station)
    print('-'*40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

# display total travel time
    Sum_Travel_Time = df['Trip Duration'].sum()

    print('Sum of Travel Time:', Sum_Travel_Time)

    # display mean travel time
    Average_Travel_Time = df['Trip Duration'].mean()

    print('Mean Travel Time:', Average_Travel_Time)
     
    # display mean travel time
    Max_Travel_Time = df['Trip Duration'].max()
    print("Max travel time :", Max_Travel_Time)
    
    # display mean travel time
    Min_Travel_Time = df['Trip Duration'].min()
    print("Min travel time :", Min_Travel_Time)
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # Display counts of user types
    print('User Stats...')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    print('Gender Stats:')
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("No information...")


    # Display earliest, most recent, and most common year of birth
    print('The Year of Birth...')
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print('The Earliest one :'+earliest)
        recent = df['Birth_Year'].max()
        print('The Most Recent : '+recent)
        comm_birth = df['Birth Year'].mode()[0]
        print('The Most Common: '+comm_birth)
    else:
        print("No information...")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
