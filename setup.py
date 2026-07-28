from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mlcompare",
    version="0.1.0",
    author="Manish Kumar",
    description="Compare classification and regression ML models",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.4.0",
        "joblib>=1.3.0",
    ],
    python_requires=">=3.10",
)