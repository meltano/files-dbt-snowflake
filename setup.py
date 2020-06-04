from setuptools import setup, find_packages

setup(
    name="files-dbt",
    version="0.1",
    description="Meltano project files for dbt",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/models/my_meltano_project/.gitkeep",
            "transform/profile/profiles.yml",
            "transform/.gitignore",
            "transform/dbt_project.yml",
        ]
    },
)
