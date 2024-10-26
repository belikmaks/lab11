import csv

flag = False
try:
    with open("lab11_1.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        print("Country Name: 2019")
        for row in reader:
            print(row['Country Name'], ': ', row["2019"])
except FileNotFoundError:
    print("Файл 'lab11_1.csv' не знайдено!")


country_names = input("Введіть назви країн через кому: ").split(',')
country_names = [name.strip() for name in country_names]

found_countries = []

try:
    with open("lab11_1.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        for row in reader:
            if row['Country Name'] in country_names:
                found_countries.append({'Country Name': row['Country Name'], '2019': row['2019']})

    if found_countries:
        with open("found_countries.csv", "w") as new_csvfile:
            fieldnames = ['Country Name', '2019']
            writer = csv.DictWriter(new_csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for country in found_countries:
                writer.writerow(country)

        print("Результати пошуку збережено у файл 'found_countries.csv'.")
    else:
        print("Введені країни не знайдено в базі даних.")

except FileNotFoundError:
    print("Файл 'lab11_1.csv' не знайдено!")
