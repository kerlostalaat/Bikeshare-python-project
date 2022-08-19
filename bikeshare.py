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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Please, choose a city? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Wrong choice, please choose again")


    # get user input for month (all, january, february, ... , june)
    while True:
        months= ['January','February','March','April','June','May','All']
        month = input("\n Which month would you like to choose? (January, February, March, April, May, June, all)?\n").title()
        if month in months:
            break
        else:
            print("\n Wrong choice, please choose again")    




    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
        day = input("\n Which day of the week would you like to choose? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, all)?\n").title()         
        if day in days:
            break
        else:
            print("\n Wrong choice, please choose again")    



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


    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'All':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)


    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_station= df['Start Station'].mode()[0]
    print('The most commonly used Start Station is ' , start_station)



    # display most commonly used end station

    end_station= df['End Station'].mode()[0]
    print('The most commonly used End Station is ' , end_station)



    # display most frequent combination of start station and end station trip

    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    combination = df['combination'].mode()[0]
    print('The most frequent combination of Start and End Station is ' , combination )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in hours

    Total = sum(df['Trip Duration'])
    print('Total travel time:', Total/3600 , " hours")


    # display mean travel time in minutes

    Mean = df['Trip Duration'].mean()
    print('Mean travel time:', Mean/60 , " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types Are :\n', user_types)


    # Display counts of gender

    print('Gender Details :')

    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are given below:\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # Display earliest, most recent, and most common year of birth

    print('Birth Year Details :')
    
    try:
        m_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',m_common_year)
    
        m_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',m_recent_year)

        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)

    except:
        
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start=0
    end=5
    while True:
        response=['yes','no']
        choice= input("Would you like to view individual trip data (5 rows)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice=='yes':          
                data = df.iloc[start:end,:10]
                print(data)
                start+=5
                end+=5

            else:    
                break     
        else:
            print("Please enter a valid response")
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()