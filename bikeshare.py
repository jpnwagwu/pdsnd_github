import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
        cities = ['chicago', 'new york city', 'washington']
        city = str(input('Would you like to get data for "chicago", "new york city", or "washington": ')).lower()
        if city in cities:
            valid = str(input('Please confirm that your selection is {}. Yes or No? : '.format(city.title()))).lower()
            if valid in ('yes','y'):
                break
            if valid in ('no','n'):
                continue
                   
        else:    
            print('Error: Please select valid input. Type city name in Full')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        answers = ['month', 'day of week', 'both']
        answer = str(input('Would you like to filter data by "month" or "day of week" or "both": ')).lower()
        if answer in answers:
            if answer == 'month' or answer == 'both':
                while True:
                    months = ['all','january', 'february', 'march', 'april', 'may', 'june'] 
                    month = str(input('Which month? january, february, march, april, may or june or "all" for no filter: ')).lower()
                    if month in months:
                        break
                    else:
                        print('Error: Please select valid input. Type month in Full')
                if answer == 'month':
                    day = 0
            

                # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            if answer == 'day of week' or answer == 'both':
                while True:
                    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
                    day = str(input('Which day? monday, tuesday, wednesday, thursday, friday, saturday or sunday or "all" for no filter: ')).lower()
                    if day in days:
                        break
                    else:
                        print('Error: Please select valid input. Type day of week in Full')
                if answer == 'day of week':
                    month= 0
            break            
        else:
            print('Error: Please select valid input. Type "month" or "day of week" or "both"in Full')
        
     
            
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
    #load data file for city input into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #Convert Start Time colum to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #Extract Month and Weekday from Start Time column and creates a new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all' and month != 0:
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all' and day != 0:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is ", common_month)
  
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is ", common_day)

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common start hour is ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most Common Start Station is ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most Common End Station is ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The most common frequent combination of start station and end station trip is ", frequent)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is ", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user = df['User Type'].value_counts()
    print("The count of user types is ", count_user)

    # TO DO: Display counts of gender
    while True:
        try:
            gender_count = df['Gender'].value_counts()
            print("The most count of gender is ", gender_count)
        except Exception as e:
            print("The most count of gender is unavailable")
            
        break

    while True:
        try:
            earliest = df['Birth Year'].min()
            print("The Earliest year of birth is ", earliest)
            recent = df['Birth Year'].max()
            print("The most recent year of birth is ", recent)
            most_common_year = df['Birth Year'].value_counts().idxmax()
            print("The most common birth year is ", most_common_year)
        except Exception as e:
            print("The Earliest year of birth is unavailable")
            print("The most recent year of birth is unavailable")
            print("The most common birth year is unavailable")
        break
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    '''Displays the first five rows of data and then the next five based on input
    '''
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display first five rows of data
    display = str(input('Would you like to see the first five rows of raw data? Type "yes" or "no": ')).lower()
    if display in ('yes','y'):
        n = 0
        print(df.iloc[n:n+5])
    

    # TO DO: Display next five rows of data
    display = str(input('Would you like to see the next five rows of raw data? Type "yes" or "no": ')).lower()
    if display in ('yes','y'):
        n = 5
        print(df.iloc[n:n+5])
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
