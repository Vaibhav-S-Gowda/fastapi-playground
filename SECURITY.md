# Security Policy

## Supported Versions

We actively provide security updates for the following versions of **fastapi-playground**:

| Version | Supported |
|---------|-----------|
| 5.x     | ✅ Yes     |
| 4.x     | ✅ Yes     |
| 3.x     | ❌ No      |
| < 3.0   | ❌ No      |

Only versions marked as supported above will receive security patches and advisories. Users should upgrade to the newest supported release to benefit from security fixes.

---

## Reporting a Vulnerability

We take vulnerability reporting seriously and aim to make secure disclosure straightforward and private.

### How to Report

Please report potential security issues **privately** via one of the following:

- **GitHub Private Security Advisory:**  
  - Go to the repository’s **Security → Advisories → New draft security advisory**.
  - Provide details, including affected versions, reproduction steps, and impact.

- **Email:**  
  - Send a report to **vaibhav.satheesh23@gmail.com**.  
  - Please encrypt sensitive details using PGP when possible.

### What to Include

To help with rapid triage and resolution, include:

- Description of the issue
- Steps to reproduce or a minimal proof-of-concept
- Affected versions
- Suggested fixes or mitigations (optional)
- Screenshots or logs (if relevant)

⚠️ **Do not publicly disclose a vulnerability before we have had the opportunity to assess and fix it.**

---

## Response Timeline

We are committed to prompt communication with reporters:

- **Acknowledgment:** Within **48 hours** of receipt.
- **Triage & Initial Assessment:** Typically within 72 hours.
- **Fix or Mitigation:** Provided based on severity and complexity; public disclosure will follow coordinated timelines.

If additional time is needed, we will communicate expected timelines clearly.

---

## Disclosure Policy

We follow responsible disclosure principles. By reporting issues through the channels above and not disclosing them publicly prematurely:

- We commit to **not pursue legal action** against researchers who act in **good faith** and comply with this policy.
- We aim to credit contributors appropriately once a fix is released, unless anonymity is requested.

---

## Security Best Practices (Optional)

While **fastapi-playground** provides the framework for experimenting with FastAPI patterns, users should apply standard API security controls in their deployments, including:

- Enforcing HTTPS/TLS
- Input validation and sanitization
- Strong authentication and authorization
- Limiting CORS origins
- Regular dependency updates

See FastAPI security guidance in the official docs for framework-specific recommendations. :contentReference[oaicite:2]{index=2}

---

Thank you for helping keep this project and its users safe!  
