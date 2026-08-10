# Contributing

Contributions are welcome through focused issues and pull requests.

## Development

1. Create a branch from `main`.
2. Run `python -m pip install -r requirements-dev.txt`.
3. Edit canonical source files rather than generated runtime packets, indexes, fixtures, or worked examples.
4. Run the relevant build scripts.
5. Run `python scripts/run_release_checks.py`.
6. Explain the user-visible outcome, affected schemas, test coverage, and compatibility impact in the pull request.

Generated files must be committed and reproducible. New routes require a compiled route packet and worked example. New profiles require passing and blocking fixtures plus a compiled profile packet. New playbooks require valid gates, a route, a tool contract, and example coverage.

Do not include private user material, credentials, unlicensed content, direct-imitation instructions, or organization-specific defaults.
