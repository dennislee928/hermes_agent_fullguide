# Dependency Analyzer

## Description
Dependency Analyzer reviews a project's dependency manifest (requirements.txt, package.json, go.mod, etc.) to identify outdated packages, known vulnerabilities, license risks, and over-dependency patterns. It provides a prioritized upgrade and cleanup plan.

## Why Hermes
Hermes evaluates dependency health holistically — not just flagging outdated versions, but reasoning about whether a dependency is necessary, whether a lighter alternative exists, and whether version pinning patterns expose the project to drift or breakage.

## Quickstart
```bash
python examples/technical/devops_tools.py analyze-deps \
  --file requirements.txt \
  --ecosystem python
```

## Sample Input
```
# requirements.txt
Django==3.2.0
psycopg2==2.8.6
requests==2.25.1
Pillow==8.1.0
celery==4.4.7
redis==3.5.3
boto3==1.16.0
djangorestframework==3.12.2
pyjwt==1.7.1
python-dotenv==0.15.0
```

## Expected Output Format
```
Dependency Analysis — requirements.txt (Python)

CRITICAL — Security Vulnerabilities
| Package    | Current | CVE         | Severity | Fix Version |
|------------|---------|-------------|----------|-------------|
| pyjwt      | 1.7.1   | CVE-2022-29217 | HIGH  | >= 2.4.0    |
| Pillow     | 8.1.0   | CVE-2021-27921 | MEDIUM| >= 9.0.1    |

HIGH — End of Life / No Security Support
| Package    | Current | Latest | Status                              |
|------------|---------|--------|-------------------------------------|
| Django     | 3.2.0   | 5.0.3  | 3.2 LTS EOL April 2024 — upgrade now|
| celery     | 4.4.7   | 5.3.6  | 4.x is unmaintained                 |

MEDIUM — Significantly Outdated
| Package               | Current | Latest | Upgrade Complexity |
|-----------------------|---------|--------|--------------------|
| boto3                 | 1.16.0  | 1.34.x | Low — add-only API |
| djangorestframework   | 3.12.2  | 3.15.x | Low                |
| requests              | 2.25.1  | 2.31.0 | Low                |

UPGRADE PLAN (Recommended Order)
1. Upgrade pyjwt to >= 2.4.0 (breaking API change — review JWT encode/decode calls)
2. Upgrade Pillow to >= 9.0.1 (minimal API changes)
3. Upgrade Django to 4.2 LTS, then test; migrate to 5.x in next cycle
4. Upgrade celery to 5.x (has breaking changes — review task decorators)
5. Remaining packages: batch upgrade with regression test run

LICENSE NOTES
All current dependencies use MIT/BSD/Apache-2.0. No copyleft (GPL) issues detected.
```

## Tips
- Run `pip freeze > requirements.txt` first to capture exact installed versions.
- Use `--ecosystem node` for package.json, `--ecosystem go` for go.mod.
- Add `--licenses commercial` to flag GPL/AGPL packages that may conflict with proprietary code.
- Combine with CI/CD Pipeline Advisor to integrate automated dependency scanning into your pipeline.
