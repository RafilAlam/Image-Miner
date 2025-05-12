# Screenshot Route Finder (Sieve of Routes)

>This project is a **CLI tool** that explores random URL routes on a domain (such as `prnt.sc`) to determine if they lead to valid screenshots. It acts as a **sieve** to filter out routes with non-useful content, like placeholders or broken images, and identifies working URLs with screenshots.

---

## Features

- **Randomized URL generation**: The program generates random routes of 6 characters to try on the domain.
- **Content validation**: It checks if the URL leads to a real screenshot by:
  - Validating HTTP response codes (`200 OK`).
  - Checking for meaningful image size.
  - Ensuring the content isn’t a placeholder.
- **Speed and efficiency**: The tool uses optimized checks to avoid downloading unnecessary content.

---

## Getting Started

### Prerequisites

To use this tool, ensure you have the following installed:

- Python 3.7+ or C++ compiler
- `requests` library for Python
