country = input().split(', ')
capital = input().split(', ')
[print(f'{country[co]} -> {capital[ca]}') for co in range(len(country)) for ca in range(len(capital)) if co == ca]