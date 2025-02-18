def city_country(city, country, *,population=None, language=None):
    result = f"{city.upper()}, {country.upper()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f" - language {language}" if language else ""
    return result
#testing the function
print(city_country("TOKYO", "JAPAN", population=1400000, language="Japanese"))
print(city_country("SEOUL", "SOUTH KOREA", population=1000000))
print(city_country("NEW YORK", "USA"))