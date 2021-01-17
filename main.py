import COVID19Py

covid19 = COVID19Py.COVID19()

latest = covid19.getLatest()

location = covid19.getLocationByCountryCode("US")

print(location)

