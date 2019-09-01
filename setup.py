import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="micropython_event_bus",
    version="0.0.4",
    author="Jacob Richter",
    author_email="jaycorichter@gmail.com",
    description="Micropython compatible producer/subscriber event bus system with optional threading.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaycosaur/micropython-event-bus",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
