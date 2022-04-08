from setuptools import setup, find_packages

setup(
    name="files-dbt-snowflake",
    version="0.1",
    description="Meltano project files for dbt-snowflake",
    packages=find_packages(),
    package_data={
        "bundle": [
            "transform/.gitignore",
            "transform/dbt_project.yml",
            "transform/models/.gitkeep",
            "transform/profiles/snowflake/profiles.yml",
        ]
    },
)
