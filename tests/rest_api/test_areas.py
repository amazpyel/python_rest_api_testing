import pytest


@pytest.mark.smoke
def test_get_all_areas_returns_consistent_payload(rest_api_client):
    areas = rest_api_client.get_areas()

    assert isinstance(areas, dict), "Response must be a dictionary"

    count = areas.get("count")
    area_list = areas.get("areas")

    assert isinstance(area_list, list), "'areas' must be a list"
    assert count == len(area_list), "Count mismatch with actual items"
