FHIR API Client & Test Automation Framework



A reusable Python and PyTest framework for authenticated integration testing of FHIR REST APIs. The project creates isolated Patient test data for every run, validates read and search operations, and removes the generated data during teardown.

Features

Reusable FHIRClient built on requests.Session

Configurable FHIR base URL and bearer-token authentication

Request timeouts for all supported operations

Patient create, read, search, and delete operations

Dependency injection through PyTest fixtures

Unique Patient data generated for every test run

Automatic cleanup with a PyTest yield fixture

Search polling for environments with delayed indexing

GitHub Actions execution on pushes and pull requests

Test lifecycle

flowchart LR
    A[Create Patient] --> B[Read Patient]
    B --> C[Search by family]
    C --> D[Validate results]
    D --> E[Delete Patient]

The module-scoped fixture creates one uniquely named Patient before the tests. The generated Patient ID and family name are shared with the tests. Cleanup runs from the fixture's finally block, including when a test fails.

Project structure

pytest-fhir/
├── api_client.py
├── conftest.py
├── token_manager.py
├── pytest.ini
├── requirements.txt
└── tests/
    └── test_fhir_api.py

Requirements

Python 3.10 or newer

Access to a FHIR R4 test server

An access token if required by the configured server

The default environment is the public HAPI FHIR R4 test server. Do not run create/delete integration tests against a production FHIR environment.

Local setup

From the pytest-fhir directory, create and activate a virtual environment.

Windows PowerShell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

macOS or Linux

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt

Environment variables

Windows PowerShell

$env:FHIR_BASE_URL = "https://hapi.fhir.org/baseR4"
$env:FHIR_ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

macOS or Linux

export FHIR_BASE_URL="https://hapi.fhir.org/baseR4"
export FHIR_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"

FHIR_ACCESS_TOKEN is optional when the selected test server does not require authentication. A fixed Patient ID is not required because the fixture creates new test data for each run.

Run the tests

python -m pytest -v

Run only tests marked as API tests:

python -m pytest -v -m api_test

Continuous integration

The GitHub Actions workflow:

Checks out the repository.

Configures Python 3.12.

Installs the project dependencies.

Runs the live FHIR integration tests.

Repository secrets:

FHIR_BASE_URL

FHIR_ACCESS_TOKEN when authentication is required

The workflow does not require FHIR_TEST_PATIENT_ID.

View FHIR CI runs

Current test coverage

Create a uniquely identified Patient

Retrieve the Patient by its server-generated ID

Validate the returned FHIR resource type and Patient data

Search for the Patient by family name

Confirm that the search Bundle contains the generated Patient

Delete the Patient during teardown

Possible future enhancements

Retry and exponential-backoff policies for 429 and transient 5xx responses

One-time token refresh after 401 Unauthorized

Structured API exception types

Deterministic unit tests using mocked HTTP responses

Additional FHIR resources and negative test scenarios

Reference

HL7 FHIR R4 REST API