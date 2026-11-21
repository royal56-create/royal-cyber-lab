# Lab: Review HTTP Security Headers on Your Own Local App

## Goal

Learn what common HTTP response headers do and record gaps in an application you own. This is a manual, read-only review; it does not scan remote hosts.

## Scope and safety

- Target: an application you own, running on your own machine.
- Use only the loopback address shown below.
- Do not replace it with a public IP, domain, or third-party service.
- Do not add credentials, cookies, or private data to shared reports.

## Steps

1. Start your own development application on `127.0.0.1:8000`.
2. Request only its local response headers:

   ```bash
curl --head --max-time 5 http://127.0.0.1:8000/
```

3. Record whether the response includes the headers below. A missing header is a review finding, not proof that the application is exploitable.
4. Check the framework's official documentation before changing configuration.
5. Re-test locally after making a change.

## Review checklist

| Header | Purpose | Review question |
|---|---|---|
| Content-Security-Policy | Restricts permitted content sources | Is a policy designed for this app rather than copied blindly? |
| X-Content-Type-Options | Helps prevent MIME sniffing | Is `nosniff` present? |
| Referrer-Policy | Limits referrer information | Is a privacy-appropriate policy configured? |
| Strict-Transport-Security | Tells browsers to use HTTPS | Is HTTPS correctly deployed before enabling it? |
| Permissions-Policy | Restricts selected browser features | Are unneeded features disabled? |

## Record your result

- Application and version:
- Local test date:
- Headers observed:
- Missing or weak settings:
- Recommended change:
- Re-test result:
- Limitations:

## Cleanup

Stop the local development server. Keep reports free of secrets, session cookies, and personal information.
