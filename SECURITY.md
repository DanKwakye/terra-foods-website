# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Terra Foods, please email us at security@terrafoods.com.

**Please do NOT open a public issue.**

We take security seriously and will respond within 48 hours.

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Security Measures

- All passwords are hashed using Django's PBKDF2 algorithm
- HTTPS enforced in production
- CSRF protection enabled
- XSS protection headers
- SQL injection prevention via Django ORM
- Environment variables for sensitive data
- Regular dependency updates

## Best Practices

- Never commit `.env` files
- Never commit `db.sqlite3`
- Never commit API keys
- Always use HTTPS in production
- Keep dependencies updated