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
        city = str(input("Enter city name: ").lower())
        if city in ["chicago", "new york city", "washington"]:
            break
        print("Enter city as Chicago, New York City or Washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Enter month: ").lower())
        if month in ["all","january", "february","march","april","may", "june"]:
            break
        print("Enter a month from January to June or 'all' to see no month filter")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Enter day: ").lower())
        if day in ["all","monday", "tuesday","wednesday","thursday","friday", "saturday", "sunday"]:
            break
        print("Enter a valid day or 'all' to see no day filter")

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
    # Load data file into dataframe
    df = pd.read_csv(CITY_DATA.get(city))

    # convert Start time into dateframe
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Apply month filter
    if month != 'all':
        months = ["january", "february","march","april","may", "june"]
        month = months.index(month) + 1

        #filter by month
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print("Most common month is: ", common_month)
    print("Most common day is: ",common_day)
    print("Most common hour is: ",common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_to_End'] = df['Start Station'] + " to " + df['End Station']
    common_start_to_end = df['Start_to_End'].mode()[0]



    print("Most common start station is: ", common_start_station)
    print("Most common end station is: ", common_end_station)
    print("Most common start and end station combination (respectively) is: ", common_start_to_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()

    print("The total travel time is: ", total_travel_time)
    print("The average travel time is: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
    else:
        gender_count = "gender data not present"

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode())
    else:
        earliest_birth_year = "Birth Year data not present"
        recent_birth_year = "Birth Year data not present"
        common_birth_year = "Birth Year data not present"

    print("User type counts are as follows:")
    print("\n",user_types_count)
    print("\nGender counts are as follows:")
    print("\n", gender_count)

    print("\nEarliest birth year is: ", earliest_birth_year)
    print("Most recent birth year is: ", recent_birth_year)
    print("Most common birth year is: ", common_birth_year)

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

        while True:
            display_raw_data = input("\nDo you want to see see 5 line of raw data? Enter Yes or No.\n")
            if display_raw_data.lower() == 'yes':
                print(df.head())
                break

            elif display_raw_data.lower() =='no':
                break

            elif display_raw_data.lower() !='no':
                print("Please answer Yes or No.")



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()
