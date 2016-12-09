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
    py_modules=["double_char"],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    }
)
