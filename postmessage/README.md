# PostMessage Vulnerability Lab

This lab demonstrates a medium severity vulnerability related to the improper implementation of the `window.postMessage()` API. The lab simulates a banking application that incorrectly uses postMessage to communicate between windows, allowing sensitive data to be intercepted by malicious websites.

## Vulnerability Description

The `window.postMessage()` API enables secure cross-origin communication between browser windows, iframes, or tabs. However, improper implementation can lead to significant security risks:

1. Using a wildcard origin (`*`) when sending messages, which allows any website to receive the messages
2. Lack of origin validation when receiving messages, which allows processing data from untrusted sources

This lab demonstrates how these vulnerabilities can be exploited to steal sensitive information.

## Lab Setup

### Prerequisites

- Docker installed on your system
- Basic understanding of web security concepts

### Setting Up the Lab

1. Clone or download this repository
2. Navigate to the project directory
3. Build and run the Docker container:

```bash
docker build -t postmessage-vuln-lab .
docker run -p 3000:3000 -p 3001:3001 postmessage-vuln-lab
```

Alternatively, you can run the lab without Docker:

```bash
npm install
npm start
```

4. The lab will start two servers:
   - Main application: http://localhost:3000
   - Attacker application: http://localhost:3001

### Lab Components

- **Main Application (Port 3000)**: A mock banking portal with a dashboard that displays sensitive information
- **Attacker Application (Port 3001)**: A malicious website designed to steal sensitive data from the main application

## Challenge Description

**Objective**: Exploit the postMessage vulnerability to steal the secret flag from the banking portal.

**Difficulty**: Medium

**Scenario**: You are a security researcher who has discovered a potential vulnerability in a banking portal. Your task is to:

1. Identify the vulnerability in the application
2. Create an HTML file that exploits the vulnerability to steal the secret flag
3. Document your approach with a video demonstration

### Steps to Complete the Challenge

1. Explore the banking portal at http://localhost:3000
2. Analyze the communication between components
3. Identify how the postMessage vulnerability is implemented
4. Create an HTML exploit file that can steal the secret flag
5. Demonstrate the exploit with a video recording

## Submission Requirements

1. An HTML file that demonstrates the exploit
2. A video recording showing:
   - The vulnerability being exploited
   - The secret flag being stolen
   - An explanation of how the exploit works

## Solution

A solution template is provided in the `solution` directory. However, try to solve the challenge on your own first!

## Security Implications

This lab demonstrates several real-world security implications:

- How sensitive data can be leaked through improper communication channels
- Why validating message origins is crucial for secure web applications
- The importance of following security best practices when using browser APIs

## Remediation

To fix the vulnerabilities demonstrated in this lab:

1. Never use wildcard origins (`*`) with postMessage when sending sensitive data
2. Always validate the origin of incoming messages before processing them
3. Implement proper message format validation
4. Consider using more secure alternatives when handling highly sensitive information

## Disclaimer

This lab is created for educational purposes only. The techniques demonstrated should only be used for legitimate security testing with proper authorization.
