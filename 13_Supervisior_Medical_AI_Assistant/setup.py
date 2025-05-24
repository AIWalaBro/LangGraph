from  setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    with open("requirements.txt", "r") as file:
        requirements_list = [line.strip() for line in file.readlines()
        if line.strip() and line.strip() != "-e ."]
        return requirements_list


setup(
    name="doctor-appointment-agentic",
    version="0.0.1",
    author="Bharatbhushan",
    author_email="bkbhushan111@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
    python_requires=">=3.10",  # Ensure compatible Python version
)