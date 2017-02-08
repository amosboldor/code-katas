"""Forbes katas."""

import json


def get_oldest_and_youngest_billionaire(file_location):
    """Given a file path gets lowest and highest age billionaire."""
    with open(file_location) as f:
        data = json.load(f)

    billionaire_with_lowest_age = data[0]
    billionaire_with_highest_age = data[0]

    for billionaire in data:
        if billionaire['age'] < 80 and billionaire['age'] > 20:
            if billionaire['age'] < billionaire_with_lowest_age['age']:
                billionaire_with_lowest_age = billionaire
            if billionaire['age'] > billionaire_with_highest_age['age']:
                billionaire_with_highest_age = billionaire

    del billionaire_with_lowest_age["age"], billionaire_with_highest_age["age"]
    del billionaire_with_lowest_age["country"], billionaire_with_highest_age["country"]
    del billionaire_with_lowest_age["rank"], billionaire_with_highest_age["rank"]
    billionaire_with_lowest_age["industry"] = billionaire_with_lowest_age.pop("source")
    billionaire_with_highest_age["industry"] = billionaire_with_highest_age.pop("source")

    format_data = {"Billionaire with Lowest Age": billionaire_with_lowest_age,
                   "Billionaire with Highest Age": billionaire_with_highest_age}
    return format_data
