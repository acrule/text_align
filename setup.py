import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_align",
    version="0.0.1",
    author="Adam Rule",
    author_email="rulea@ohsu.edu",
    description="A package for aligning text sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/acrule/text_align",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
