import pandas as pd 
df = pd.read_csv('adult.data.csv')
df
race_count = df['race'].value_counts() #Contamos cuántas personas de cada raza hay en el set de datos
print(race_count)
input("Presiona Enter para continuar...")
average_age_men = df[df['sex'] == 'Male']['age'].mean()  #Averiguamos la edad promedio de los hombres
print(average_age_men)
input("Presiona Enter para continuar...")
percentage_bachelors = (df[df['education'] == "Bachelors"].shape[0] / df.shape[0]) * 100  #Porcentaje de personas que tienen un grado de licenciatura (Bachelor's degree)
print(percentage_bachelors)
input("Presiona Enter para continuar...")
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_advanced_edu_rich = (df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100
print(percentage_advanced_edu_rich) 
  #porcentaje de personas con una educación avanzada (Bachelors, Masters o Doctorate) que ganan más de 50k

input("Presiona Enter para continuar...")
non_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_non_advanced_edu_rich = (df[non_advanced_education & (df['salary'] == '>50K')].shape[0] / df[non_advanced_education].shape[0]) * 100
print(percentage_non_advanced_edu_rich)
 #Porcentaje de personas sin una educación avanzada que generan más de 50k
input("Presiona Enter para continuar...")

min_work_hours = df['hours-per-week'].min()
print(min_work_hours)
 #Mínimo número de horas que una persona trabaja por semana
input("Presiona Enter para continuar...")

num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100
print(rich_percentage)
 #Porcentaje de personas que trabajan el mínimo de horas por semana que tiene un salario de más de 50k
input("Presiona Enter para continuar...")

country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
country_count = df['native-country'].value_counts()
highest_earning_country = (country_salary / country_count * 100).idxmax()
highest_earning_country_percentage = (country_salary / country_count * 100).max()
print(highest_earning_country, highest_earning_country_percentage) 
  #País que tiene el porcentaje más alto de personas que ganan >50k y cuál es ese porcentaje
input("Presiona Enter para continuar...")

india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
print(india_occupation) #Ocupación más popular de aquellos que ganan >50k en India
input("Presiona Enter para finalizar...")






