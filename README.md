# Selenium Python Automation for Para Bank Web App

- The website: https://parabank.parasoft.com/parabank/index.htm

- The coding: https://github.com/hongtra1311/parabank-automation

### Supported/tested browsers:

- Chrome: v75 (64 bit)
- Firefox: v68 (64 bit)
- Edge: v17 and above

## Test ordering (run specific tests first)

We use the `pytest-order` plugin to control test execution order when needed. To ensure `about_page` runs before `login_page` we added ordering markers to the tests:

- `@pytest.mark.order(1)` on `tests/test_about_page.py::test_display_about_page`
- `@pytest.mark.order(2)` on `tests/test_login.py::test_invalid_login`

Install the dependency:

```bash
pip install -r requirements.txt
```

Run the whole test suite normally with `pytest` or run just the tests you want; the order markers ensure the specified order regardless of collection order.

## CI/CD Pipeline (Jenkins)

This project uses Jenkins for Continuous Integration (CI).

Pipeline steps:

1. Triggered automatically on GitHub push
2. Clone repository
3. Create Python virtual environment
4. Install dependencies
5. Run Selenium tests in headless mode
6. Generate pytest HTML report
7. Archive test reports in Jenkins

Tools:

- Jenkins
- Python + Pytest
- Selenium WebDriver
- pytest-html

## Report

![Test Jenkin Report](https://github.com/hongtra1311/parabank-automation/blob/main/screenshots/jenkin_report.png)
