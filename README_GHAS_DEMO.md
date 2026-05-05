# GHAS MDC Demo - Security Findings Repository

This repository contains intentional security vulnerabilities, misconfigurations, and exposed secrets designed to demonstrate GitHub Advanced Security (GHAS) integration with Microsoft Defender for Cloud (MDC).

## Contents

### Vulnerabilities
- **SQL Injection** (`vulnerabilities/sql_injection.py`) - Direct query concatenation
- **Command Injection** (`vulnerabilities/command_injection.js`) - Unsanitized shell execution
- **Path Traversal** (`vulnerabilities/path_traversal.py`) - Directory traversal vulnerabilities
- **Hardcoded Credentials** (`vulnerabilities/hardcoded_credentials.js`) - Exposed AWS and database credentials

### Secrets
- **API Keys** (`secrets/api_keys.env`) - Exposed GitHub, Slack, Stripe, and other API tokens
- **Database Credentials** - PostgreSQL connection strings with passwords
- **AWS Keys** - Access and secret keys

### Misconfigurations
- **Insecure Cryptography** (`misconfigurations/insecure_crypto.py`) - Weak DES, MD5, SHA1
- **Insecure Deserialization** (`misconfigurations/insecure_deserialization.java`) - RCE vulnerability
- **Exposed API Endpoints** (`misconfigurations/exposed_api_endpoints.js`) - No authentication/rate limiting
- **Dockerfile Issues** (`misconfigurations/dockerfile_security_issues`) - Root access, unversioned images
- **Docker Compose Issues** (`misconfigurations/unsafe_yaml.yaml`) - Exposed ports, plaintext secrets
- **Weak Authentication** (`misconfigurations/weak_authentication.py`) - Weak hashing, CSRF issues

## Expected GHAS Findings

This repository is configured to trigger:

### Code Scanning
- SQL injection patterns
- Command injection risks
- Path traversal vulnerabilities
- Insecure cryptographic practices
- Hardcoded credentials
- Use of weak hashing algorithms

### Secret Scanning
- GitHub tokens
- AWS credentials
- Database connection strings
- API keys (Slack, Stripe, Twilio, etc.)
- Database passwords

### Dependabot Alerts
- Outdated and vulnerable dependencies
- Unpatched security issues

## Integration with Microsoft Defender for Cloud

When configured properly, these findings will flow through:
1. GitHub Advanced Security dashboard
2. GitHub's REST/GraphQL APIs
3. Microsoft Defender for Cloud (via GitHub integration)
4. Azure security dashboards and reports

## Notes

⚠️ **Warning**: This repository contains intentional security vulnerabilities for educational and demonstration purposes only. These examples should never be used in production code.

## Enabling GHAS Features

Ensure these are enabled in repository settings:
- Code scanning (CodeQL or third-party analyzers)
- Secret scanning
- Dependabot alerts
- Dependabot security updates

Once enabled, findings should appear in:
- Security → Code scanning alerts
- Security → Secret scanning alerts
- Security → Dependabot alerts
