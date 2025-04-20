# Bootstrap Scripts

This directory contains Python scripts used to bootstrap core AWS infrastructure components. These scripts are intended to be run early in your account setup process and are designed to be testable, modular, and cross-platform.

---

## Scripts

### `org_structure.py`

Sets up an AWS Organization based on a declarative config file.

It performs the following actions:

- Creates the organization (if not already enabled)
- Creates organizational units (OUs) such as `dev`, `prod`
- Creates accounts per environment (e.g., `dev-iac`, `prod-config`)
- Writes an SSM parameter in each account identifying the environment:
  ```
  /iac/environment = dev
  ```

The prefix (`/iac`) is configurable using either:

- the `--prefix` CLI flag, or  
- the `IAC_PREFIX` environment variable

---

### Usage

**Dry run (recommended first):**

```bash
python org_structure.py --config org_structure.json --dry-run --verbose
```

**With custom prefix:**

```bash
python org_structure.py --config org_structure.json --prefix /karma
```

**Live execution:**

```bash
python org_structure.py --config org_structure.json
```

---

## Configuration

See `org_structure.json` for the expected format:

```json
{
  "organizational_units": [
    { "environment": "dev", "email": "dev@example.com" },
    { "environment": "prod", "email": "prod@example.com" }
  ],
  "accounts": ["config", "lambda", "iac", "network"]
}
```

This results in accounts like:

- `dev-config@dev.example.com`
- `prod-iac@prod.example.com`

Each account receives a Parameter Store entry:

```
/iac/environment = dev
```

(Or `/karma/environment`, if using `--prefix /karma`.)

---

## Notes

- Requires `boto3` and valid AWS credentials with appropriate permissions.
- Supports `--dry-run` and `--verbose` flags for safe previews and detailed output.
- Modular structure allows for easy mocking and unit testing of AWS SDK calls.

---

## Tests

Unit tests live under `/tests/` and use `unittest` + `unittest.mock`.  
All AWS calls are stubbed using mocks to enable fast, isolated test runs.
