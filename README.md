# Integration Test Suite

A comprehensive REST API integration test suite built with Python, pytest, and requests. This project demonstrates best practices for testing HTTP APIs with a custom API client, fixture-based testing, and CI/CD automation via GitHub Actions.

## 📋 Overview

This project provides a robust integration testing framework for REST APIs with the following features:

- **Reusable API Client** – Custom wrapper around the `requests` library for consistent API interactions
- **pytest Fixtures** – Session-scoped fixtures for efficient test setup and teardown
- **Environment Management** – Support for local `.env` files and GitHub Secrets for configuration
- **Docker Support** – Containerized test execution for CI/CD pipelines
- **GitHub Actions CI/CD** – Automated test runs on push and pull requests

## 📁 Project Structure

```
IntegrationTest/
├── src/
│   └── client/
│       └── api_client.py           # REST API client wrapper
├── tests/
│   ├── conftest.py                 # pytest configuration & fixtures
│   └── test_users.py               # API integration tests
├── data/
│   └── .env                        # Environment variables (local only)
├── docker/
│   └── Dockerfile                  # Docker image for test execution
├── .github/
│   └── workflows/
│       └── tests.yml               # GitHub Actions CI/CD workflow
├── makefile                        # Build automation commands
├── pytest.ini                      # pytest configuration
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🧪 Test Coverage

The test suite validates the following endpoints from the JSONPlaceholder API:

| Test | Endpoint | Description |
|------|----------|-------------|
| `test_get_users` | `GET /users` | Retrieve all users and validate list structure |
| `test_get_single_user` | `GET /users/{id}` | Fetch individual user by ID |
| `test_get_user_has_required_fields` | `GET /users/{id}` | Verify required fields are present |
| `test_get_nonexistent_user` | `GET /users/99999` | Verify 404 for non-existent resources |
| `test_get_users_response_structure` | `GET /users` | Validate response structure and all fields |

## 🚀 Quick Start

### Prerequisites
- Python 3.12+ (or 3.10+ for compatibility)
- pip or conda
- Docker (optional, for containerized testing)

### Installation

**One-command setup:**
```bash
make install
```

**Manual setup:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Configuration

### Local Development

Create a `data/.env` file with your API base URL:

```env
BASE_URL=***
```

### GitHub Actions

1. Go to your repository settings → **Secrets and variables** → **Actions**
2. Create a repository secret named `BASE_URL` with your API endpoint
3. The secret is automatically passed to the Docker container during CI/CD runs

## 🧪 Running Tests

### Run all tests:
```bash
make test
```

### Run with pytest directly:
```bash
source .venv/bin/activate
pytest                           # Run all tests
pytest -v                        # Verbose output
pytest tests/test_users.py      # Run specific test file
pytest -k test_get_users        # Run tests matching pattern
```

### Run in Docker:
```bash
docker build -t integration-tests -f docker/Dockerfile .
docker run -e BASE_URL=<your-api-url> integration-tests
```

## 🧬 Project Architecture

### API Client (`src/client/api_client.py`)
A lightweight wrapper around `requests` for:
- Consistent base URL handling
- Reusable HTTP methods
- Error handling and response management

### Test Fixtures (`tests/conftest.py`)
Session-scoped pytest fixtures that:
- Load environment variables from `.env`
- Initialize the API client once per test session
- Provide clean setup/teardown

### CI/CD Pipeline (`.github/workflows/tests.yml`)
Automated workflow that:
- Builds a Docker image from the Dockerfile
- Passes GitHub Secrets to the container
- Runs pytest inside the isolated environment
- Validates all tests on push and pull requests

## 📦 Dependencies

- **pytest** – Testing framework
- **requests** – HTTP client library
- **python-dotenv** – Environment variable management

## 🛠️ Development

### Clean up virtual environment:
```bash
make clean
```

### Project commands:
```bash
make install    # Create venv and install dependencies
make test       # Run test suite
make clean      # Remove venv
```

## 🔐 Security Notes

- Never commit `data/.env` files with real credentials
- Use GitHub Secrets for sensitive configuration in CI/CD
- `.env` files are gitignored by default
- Ensure the `BASE_URL` secret is set in GitHub for CI/CD to work

## 📝 License

This project is provided as-is for educational and testing purposes.