import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RaspberryPi3B_Sensors_doubleecpu", # Replace with your own username
    version="0.0.1",
    author="Gilbert Medel",
    author_email="doubleecpu@outlook.com",
    description="Setup for Sensor Kit on Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gilmedel/RaspberryPi3B_Sensors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)