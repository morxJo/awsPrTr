import csv


def generate_csv(file_name):
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ]

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV файл '{file_name}' успешно создан.")


csv_file_name = 'example.csv'
generate_csv(csv_file_name)
