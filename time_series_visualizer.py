import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data by filtering out top 2.5% and bottom 2.5%
lower_percentile = df['page_views'].quantile(0.025)
upper_percentile = df['page_views'].quantile(0.975)

df_cleaned = df[(df['page_views'] >= lower_percentile) & (df['page_views'] <= upper_percentile)]

# Function to draw line plot
def draw_line_plot():
    df_copy = df_cleaned.copy()
    plt.figure(figsize=(12, 6))
    plt.plot(df_copy.index, df_copy['page_views'], color='blue')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.savefig('line_plot.png')
    plt.show()

# Function to draw bar plot
def draw_bar_plot():
    df_copy = df_cleaned.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    monthly_avg = df_copy.groupby(['year', 'month'])['page_views'].mean().unstack()
    monthly_avg.plot(kind='bar', figsize=(12, 6))
    plt.title('Average Daily Page Views per Month')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    plt.savefig('bar_plot.png')
    plt.show()

# Function to draw box plot
def draw_box_plot():
    df_copy = df_cleaned.copy()
    df_copy['year'] = df_copy.index.year
    df_copy['month'] = df_copy.index.month
    plt.figure(figsize=(12, 6))

    # Year-wise Box Plot (Trend)
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='page_views', data=df_copy)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='page_views', data=df_copy)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.xticks(range(12), [calendar.month_name[i] for i in range(1, 13)])

    plt.savefig('box_plot.png')
    plt.show()
