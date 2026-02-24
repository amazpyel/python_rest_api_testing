import allure
import pytest


KNOWN_COMPETITIONS = [
    pytest.param(2001, "UEFA Champions League", id="champions-league"),
    pytest.param(2021, "Premier League", id="premier-league"),
    pytest.param(2002, "Bundesliga", id="bundesliga"),
]

VALID_COMPETITION_TYPES = {"LEAGUE", "CUP"}


@pytest.mark.smoke
@allure.feature("Competitions")
@allure.story("Retrieve all competitions")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_all_competitions(football_api_client):

    with allure.step("Call GET /competitions endpoint"):
        response = football_api_client.get_competitions()

    with allure.step("Validate count matches list length"):
        assert response.count == len(response.competitions), (
            f"Expected count {response.count}, got {len(response.competitions)} competitions"
        )
        assert response.competitions, "Competitions list is empty"

    with allure.step("Validate each competition has required fields"):
        for competition in response.competitions:
            assert competition.id > 0, (
                f"Competition id must be positive, got {competition.id}"
            )
            assert isinstance(competition.name, str) and competition.name.strip(), (
                f"Competition name must be a non-empty string, got {competition.name!r}"
            )
            assert competition.type in VALID_COMPETITION_TYPES, (
                f"Unexpected competition type: {competition.type!r}"
            )
            assert competition.area.id > 0, (
                f"Area id must be positive for competition {competition.name!r}"
            )


@pytest.mark.smoke
@pytest.mark.parametrize("competition_id,expected_name", KNOWN_COMPETITIONS)
@allure.feature("Competitions")
@allure.story("Retrieve competition by ID")
@allure.severity(allure.severity_level.NORMAL)
def test_get_competition_by_id(football_api_client, competition_id, expected_name):

    with allure.step(f"Call GET /competitions/{competition_id}"):
        competition = football_api_client.get_competition(competition_id)

    with allure.step("Validate competition identity"):
        assert competition.id == competition_id, (
            f"Expected id {competition_id}, got {competition.id}"
        )
        assert competition.name == expected_name, (
            f"Expected name {expected_name!r}, got {competition.name!r}"
        )

    with allure.step("Validate competition structure"):
        assert competition.type in VALID_COMPETITION_TYPES, (
            f"Unexpected competition type: {competition.type!r}"
        )
        assert competition.area.id > 0
        assert competition.area.name.strip(), "Area name must not be empty"