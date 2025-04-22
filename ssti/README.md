# Server-Side Template Injection (SSTI) Lab

This lab demonstrates a Server-Side Template Injection vulnerability in a greeting card generator application.

## Lab Setup

The lab consists of two services:
1. **Vulnerable App**: A Flask application with an SSTI vulnerability (port 8080)
2. **Flag Service**: An internal service hosting the flag at `/secret` path (not exposed directly)

### Prerequisites

- Docker and Docker Compose installed
- Basic understanding of web security concepts

### Running the Lab

1. Clone or download this repository
2. Navigate to the lab directory
3. Start the lab:

```bash
docker-compose up --build
```

4. Access the vulnerable application at http://localhost:8080

## Lab Components

- **CustomCards Application**: A greeting card generator that allows users to create personalized messages
- **Flag Service**: An internal service that hosts the flag at `http://flag-service:5000/secret`

## Challenge

Exploit the Server-Side Template Injection vulnerability to:
1. Execute arbitrary code on the server
2. Make a request to the internal flag service
3. Retrieve and display the flag

## Hints

1. The application uses Jinja2 templating without proper sanitization
2. You can leverage Python's object introspection capabilities
3. The flag service is accessible as `flag-service` hostname from the vulnerable app
4. Consider using Python's `urllib` or `requests` module to make HTTP requests

Good luck!
