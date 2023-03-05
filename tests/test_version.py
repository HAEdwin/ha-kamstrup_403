"""Test for versions."""
import json

from custom_components.kamstrup_403.const import VERSION

with open(
    file="custom_components/kamstrup_403/manifest.json", mode="r", encoding="UTF-8"
) as manifest_file:
    data = manifest_file.read()

manifest = json.loads(data)


async def test_component_version():
    """Verify that the version in the manifest and const.py are equal"""
    assert manifest["version"] == VERSION


async def test_component_requirements():
    """Verify that all requirements in the manifest.json are defined as in the requirements files"""
    requirements_files = ["requirements.txt", "requirements_test.txt"]
    for requirements_file in requirements_files:
        with open(file=requirements_file, mode="r", encoding="UTF-8") as file:
            lines = [line.rstrip("\n") for line in file]

            for requirement in manifest["requirements"]:
                assert requirement in lines
