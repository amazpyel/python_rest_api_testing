# REST API Testing Framework

A comprehensive REST API testing framework demonstrating professional testing practices with Python, pytest, and Docker. Features automated testing with Allure reporting and CI/CD integration.

## Features

- ✅ **API Test Automation** - Tests for GoRest and Football-Data APIs
- 🐳 **Docker Support** - Fully containerized test execution
- 📊 **Allure Reports** - Beautiful test reports with history and trends
- 🔄 **CI/CD Integration** - Automated testing with GitHub Actions
- 🎯 **Performance Testing** - Load testing with Locust
- 🏗️ **Clean Architecture** - Reusable API clients with proper separation of concerns
- 🔧 **Environment Management** - Support for multiple test environments
- 📝 **Type Safety** - Pydantic models for request/response validation

## Tech Stack

- **Python 3.14** - Latest Python version
- **pytest** - Test framework
- **Poetry** - Dependency management
- **Docker & Docker Compose** - Containerization
- **Allure** - Test reporting
- **Locust** - Performance testing
- **httpx** - Modern HTTP client
- **Pydantic** - Data validation
- **Faker** - Test data generation

## Prerequisites

Choose one of the following setups:

### Option 1: Docker (Recommended)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Option 2: Local Python
- Python 3.11+ (3.14 recommended)
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

### Using Docker (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd python_rest_api_testing
```

2. Copy environment file:
```bash
cp .env.example .env
```

3. Add your API tokens to `.env`:
```bash
GOREST_TOKEN=your_gorest_token_here
FOOTBALL_DATA_TOKEN=your_football_data_token_here
```

Get tokens from:
- GoRest: https://gorest.co.in/
- Football-Data: https://www.football-data.org/

### Using Local Python

1. Clone and navigate to the repository

2. Install dependencies:
```bash
poetry install
```

3. Activate virtual environment:
```bash
poetry shell
```

4. Configure environment variables (same as Docker setup)

## Running Tests

### Using Docker Compose

**Run all tests:**
```bash
docker compose run test
```

**Run specific test file:**
```bash
docker compose run test tests/gorest_api/test_end_to_end.py
```

**Run with markers:**
```bash
docker compose run test -m "smoke"
docker compose run test -m "not destructive"
```

**Run performance tests:**
```bash
docker compose up performance
# Access Locust UI at http://localhost:8089
```

### Using Local Python

**Run all tests:**
```bash
poetry run pytest
```

**Run with Allure results:**
```bash
poetry run pytest --alluredir=allure-results
```

**Run specific markers:**
```bash
poetry run pytest -m smoke
```

## Allure Reports

### Local Allure Reports with Docker Service

**Start Allure service:**
```bash
docker compose up -d allure
```

**Run tests:**
```bash
docker compose run test
```

**View reports:**
Open http://localhost:5050/allure-docker-service/latest-report

Reports include:
- ✅ Test results with detailed steps
- 📈 Historical trends and comparisons
- ⏱️ Duration trends
- 🔄 Retry and flaky test detection
- 🌍 Environment information

**Stop Allure service:**
```bash
docker compose down
```

### GitHub Pages Reports

Automated reports are published to GitHub Pages on every push:
- **URL**: `https://<username>.github.io/<repository-name>/`
- **Auto-updated** on every CI run
- **Historical data** preserved across builds

## Configuration

### Environment Variables

Configure via `.env` file:

```bash
# Required: API Tokens
GOREST_TOKEN=your_token_here
FOOTBALL_DATA_TOKEN=your_token_here

# Test Environment (dev, staging, production)
TEST_ENV=production

# Optional: Allure Report Configuration
REPORT_NAME=REST API Test Suite
BUILD_NUMBER=1
EXECUTOR_NAME=pytest
EXECUTOR_TYPE=pytest
```

### Test Markers

Available pytest markers:

- `smoke` - Quick smoke tests
- `destructive` - Tests that modify data
- `negative` - Negative test cases
- `end2end` - End-to-end test scenarios

**Example:**
```bash
# Run only smoke tests
docker compose run test -m smoke

# Skip destructive tests
docker compose run test -m "not destructive"
```

## Project Structure

```
.
├── src/
│   └── rest_api_client/          # Reusable API clients
│       ├── base_client.py         # Base HTTP client
│       ├── gorest_api/            # GoRest API client
│       └── football_api/          # Football-Data API client
├── tests/
│   ├── conftest.py                # Pytest configuration & fixtures
│   ├── factories/                 # Test data factories
│   ├── gorest_api/                # GoRest API tests
│   └── football_api/              # Football-Data API tests
├── performance/
│   └── locustfile.py              # Load testing scenarios
├── .github/
│   └── workflows/
│       └── tests.yml              # CI/CD pipeline
├── docker-compose.yml             # Docker services configuration
├── Dockerfile                     # Test container image
├── pyproject.toml                 # Poetry dependencies
└── README.md                      # This file
```

## CI/CD Pipeline

### GitHub Actions Workflow

The project includes automated CI/CD that:

1. ✅ Runs tests on every push/PR
2. 📊 Generates Allure reports
3. 🚀 Deploys reports to GitHub Pages
4. 📝 Shows test summary in Actions
5. 🔄 Preserves historical data

### Setting Up CI/CD

1. **Add Repository Secrets:**
   - Go to Settings → Secrets → Actions
   - Add `GOREST_TOKEN`
   - Add `FOOTBALL_DATA_TOKEN`

2. **Enable GitHub Pages:**
   - Go to Settings → Pages
   - Source: Deploy from branch
   - Branch: `gh-pages`
   - Folder: `/` (root)

3. **Push to trigger:**
```bash
git push origin main
```

4. **View results:**
   - Actions tab: See test execution
   - Pages URL: View Allure reports

### Workflow Features

- **Environment Detection** - Automatically detects CI vs Local execution
- **Test Continuation** - Workflow succeeds even if some tests fail
- **Historical Trends** - Preserves Allure history across runs
- **Dynamic Build Info** - Links back to GitHub Actions run
- **Summary Report** - Shows test status in Actions summary

## Development

### Adding New Tests

1. Create test file in appropriate directory
2. Use existing fixtures (`gorest_client`, `football_api_client`)
3. Add Allure annotations for better reporting
4. Mark with appropriate pytest markers

**Example:**
```python
import allure
import pytest

@pytest.mark.smoke
@allure.feature("User Management")
@allure.story("Get Users")
def test_get_users(gorest_client):
    with allure.step("Fetch all users"):
        users = gorest_client.get_users()
        assert len(users) > 0
```

### Adding New API Clients

1. Create client in `src/rest_api_client/<api_name>/`
2. Extend `BaseRestApiClient`
3. Define Pydantic models for validation
4. Add pytest fixture in `tests/conftest.py`

## Troubleshooting

### Common Issues

**Tests fail in CI but pass locally:**
- Check if API blocks CI/CD IPs (CloudFlare protection)
- Verify environment variables are set in GitHub Secrets
- Review the execution location in Allure reports

**Docker build fails:**
- Ensure Docker daemon is running
- Clear Docker cache: `docker compose build --no-cache`
- Check Docker disk space

**Allure reports show "DEFAULT":**
- Verify `REPORT_NAME` environment variable is set
- Check `tests/conftest.py` executor configuration

**No history in Allure reports:**
- First run won't have history (expected)
- History builds after 2+ test runs
- Check `gh-pages` branch exists

## License

This project is for educational and portfolio purposes.

## Contributing

This is a portfolio project demonstrating testing skills. Feel free to use as reference or template for your own projects.

## Contact

For questions or feedback, please open an issue in the repository.