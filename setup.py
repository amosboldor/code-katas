"""Setup local envirement for this repo."""


from setuptools import setup

setup(
    name="code-katas",
    description="www.codewars.com katas I finished",
    version=0.1,
    author=["Amos Boldor"],
    author_email=["amosboldor@gmail.com"],
    licencse="MIT",
    package_dir={'': 'src'},
    py_modules=[
        "double_char",
        "even_or_odd",
        "sum_of_positive",
        "reversed_list_of_digits",
        "opposite_number",
        "counting_sheep",
        "jennys_secret_message",
        "needle_in_the_haystack",
        "sum_without_high_and_low",
        "grasshopper_summation",
        "count_the_monkeys",
        "count_positives_sum_negatives",
        "squared_sum",
        "bool_to_yes_or_no",
        "alternating_case",
        "are_you_playing_the_banjo",
        "sum_nth_term_series",
        "parenthetics"
    ],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
