# Web Security Fundamentals

This module introduces defensive web security concepts. It is a learning guide, not an instruction to test public websites.

## Core topics

- **Input validation:** accept only expected formats, lengths, and ranges; validate on the server.
- **Output encoding:** encode untrusted data for its exact output context to reduce injection risk.
- **Authentication:** use established libraries, secure password hashing, MFA, and safe recovery flows.
- **Authorization:** check permissions on every protected server-side action; default to deny.
- **Session safety:** use HTTPS and secure, HttpOnly, and appropriate SameSite cookie attributes.
- **Transport security:** use TLS in production and redirect HTTP to HTTPS.
- **Security headers:** understand Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, and Strict-Transport-Security.
- **Error handling:** show users generic errors while recording useful, privacy-conscious server diagnostics.
- **Dependencies:** keep frameworks and packages updated; review advisories and remove unused packages.
- **Logging:** record security-relevant events without logging passwords, tokens, or unnecessary personal data.

## OWASP learning map

Study the current OWASP Top 10 categories as a risk-awareness framework. For each category, write down: the trust boundary, the possible impact, a preventive control, and a way to verify the control in an application you own.

## Safe practice

1. Use a deliberately vulnerable training application only in an isolated local VM or an explicitly authorized training platform.
2. Keep the target bound to localhost or an isolated host-only network.
3. Use fictional accounts and data.
4. Do not test public websites, third-party accounts, or networks without written permission and a defined scope.
5. Prefer code review, secure configuration, and remediation exercises.

## Completion checklist

- [ ] Explain the difference between authentication and authorization.
- [ ] Describe why output encoding is context-specific.
- [ ] Identify the purpose of four common security headers.
- [ ] Explain why secrets must not appear in logs or source control.
- [ ] Produce a short remediation report using the project template.
