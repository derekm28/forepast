

resp = requests.get('http://www.metaweather.com/api/location/search', params = {'term': '', 'limit': 1})


class Converter():
    def convert(self):
        """converts temp from celsius to fahrenheit"""

        self = resp.data

        fahrenheit_min_temp = f'{self.min_temp * 9/5 + 32 }'
        fahrenheit_max_temp = f'{self.max_temp * 9/5 + 32 }'

        return (fahrenheit_min_temp, fahrenheit_max_temp)
