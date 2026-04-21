"""
Normalize semi-structured JSON data into a flat table.
pandas.json_normalize(data, record_path=None, meta=None, meta_prefix=None, record_prefix=None, errors='raise', sep='.', max_level=None)

ref: https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
"""
import pandas as pd

data = [
    {"id": 1, "name": {"first": "Coleen", "last": "Volk"}},
    {"name": {"given": "Mark", "family": "Regner"}},
    {"id": 2, "name": "Faye Raker"},
]
df = pd.json_normalize(data)
print(df)

# record_path - path in each object to list of records. If not passed, data will be assumed to be an array of records.
data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]
result = pd.json_normalize(
    data, "counties", ["state", "shortname", ["info", "governor"]]
)
print(result)


# Scenario 3
input = [
    { "index": 25, "creation_set_id": "34536565-64564-647567-657", "person_id": "215346546", "last_upload_ts": "2023-08-01 12:50:05", "country": "GB" }
]
df = pd.json_normalize(input)
print(df)
