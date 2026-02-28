import allure
import pytest


@allure.feature("Areas")
@allure.story("Retrieve all areas")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_get_all_areas(football_api_client):

    with allure.step("Call GET /areas endpoint"):
        areas_response = football_api_client.get_areas()

    with allure.step("Validate response consistency"):
        assert areas_response.count == len(areas_response.areas), (
            f"Expected count {areas_response.count}, but got {len(areas_response.areas)} areas"
        )

        assert areas_response.areas, "Areas list is empty"

    with allure.step("Validate first area structure"):
        first_area = areas_response.areas[0]

        assert first_area.id > 0, f"Area id must be positive, got {first_area.id}"

        assert isinstance(first_area.countryCode, str), (
            f"Invalid countryCode: {first_area.countryCode}"
        )
        assert len(first_area.countryCode) == 3, f"Invalid countryCode: {first_area.countryCode}"
        assert first_area.countryCode.isalpha(), f"Invalid countryCode: {first_area.countryCode}"

        assert isinstance(first_area.name, str), "Area name must be non-empty string"
        assert first_area.name.strip(), "Area name must be non-empty string"
