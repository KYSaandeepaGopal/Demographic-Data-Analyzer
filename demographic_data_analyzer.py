import pandas as pd

def demographic_data_analyzer():
    # Read data
    df = pd.read_csv("adult.data.csv")

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education is Bachelors, Masters, or Doctorate
    higher_ed = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_ed_rich = round(df[higher_ed]['salary'].eq('>50K').mean() * 100, 1)

    # 5. Without advanced education
    lower_ed_rich = round(df[~higher_ed]['salary'].eq('>50K').mean() * 100, 1)

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage with >50K among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest % of >50K earners
    country_counts = df['native-country'].value_counts()
    rich_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_country_percentage = (rich_country_counts / country_counts * 100).dropna()
    highest_earning_country = rich_country_percentage.idxmax()
    highest_earning_country_percentage = round(rich_country_percentage.max(), 1)

    # 9. Most popular occupation for >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_ed_rich,
        'lower_education_rich': lower_ed_rich,
        'min_work_hours': min_work_hours,
        'rich_min_workers_percentage': rich_min_workers_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation,
    }
