## Installation

### Install the required packages:
```
pip install -r requirements.txt
```
### Install the required browsers:
```
playwright install
```

## UI Execution

### Test task completed using Python + Playwright + Pytest

UI tests support parametrized browser execution.

Run tests in Chromium:
```
pytest --browser chromium
```

Run tests in Firefox:
```
pytest --browser firefox
```

## API Execution
### Test task completed using Python + Requests + Pytest

```
pytest petstore_tests -v
```

## Load Testing
### Test task completed using Python + Locust

```
locust -f./load_testing/locustfile.py --host=https://www.n11.com
```


