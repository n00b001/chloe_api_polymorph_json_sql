from main import Cpius, Weather, Catpics


def test_cpius_instantiation():
    cpi = Cpius()


def test_weather_instantiation():
    weather = Weather(lat=0, long=0)


def test_cat_pics_instantiation():
    catpics = Catpics()

def test_cpius_get_data():
    cpi = Cpius()
    data = cpi.get_data()


def test_weather_get_data():
    weather = Weather(lat=0, long=0)
    data = weather.get_data()


def test_cat_pics_get_data():
    catpics = Catpics()
    data = catpics.get_data()
