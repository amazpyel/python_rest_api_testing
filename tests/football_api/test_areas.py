import pytest


@pytest.mark.smoke
def test_get_all_areas(football_api_client):
    areas_response = football_api_client.get_areas()

    assert areas_response.count == len(areas_response.areas), (
        "Count does not match number of returned areas"
    )

    assert areas_response.areas, "Areas list is empty"

    first_area = areas_response.areas[0]

    assert first_area.id > 0
    assert len(first_area.countryCode) == 3
    assert first_area.name