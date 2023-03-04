"""
overall task:
I would like a daily email
        hint: https://stackoverflow.com/questions/31011179/converting-json-to-html-table-in-python

The email should contain:
- the maximum 'Shortwave Solar Radiation' for the day in purfleet
- the maximum 'Shortwave Solar Radiation' for the day in forest hill
- a cat fact
- the current 'CPIUS - United States - Consumer price index'

please save the email to an HTML file (json is fine)
and save a copy of the filename to a database as a record that the email has been created for today

how to:

    to get 'Shortwave Solar Radiation':
    https://open-meteo.com/en/docs#api_form

    - purfleet
        lat: 52.52
        long: 13.41
    - forest hill
        lat: 51.4431
        long: -0.04178

    to get 'CPIUS - United States - Consumer price index':
    https://www.econdb.com/api/series/?page=1&search=inflation


    lots of free APIs: (will help with cat facts)
    https://github.com/public-apis/public-apis

    sqlite:
    https://www.tutorialspoint.com/sqlite/sqlite_python.htm
"""
