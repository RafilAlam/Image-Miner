# 🪨⛏️Image-Miner (Sieve of Routes)

>This project is a fun little **CLI tool** that benefits internet archaeologists by exploring random URL routes on a domain (such as `prnt.sc`, a website with random screenshots submitted by people from as far back as 2010) to determine if they lead to valid screenshots. It acts as a **scraper** to filter out routes with non-useful content, like placeholders or broken images, and identifies working URLs with screenshots and logs them. This gets rid of the manual labour and hassle of individually trying out many routes and keeping track of which ones work and not — keeping the joy of discovery alive!

---
## 🎥 Demo


https://github.com/user-attachments/assets/b3cc964b-eb60-49cf-8241-5891a30b7005


---


## 🛠️Features

- **Randomized URL generation**: The program generates random routes of 6 characters to try on the domain.
- **Content validation**: It checks if the URL leads to a real screenshot by:
  - Validating HTTP response codes (`200 OK`).
  - Checking for meaningful image size.
  - Ensuring the content isn’t a placeholder.
- **Speed and efficiency**: The tool uses optimized checks to avoid downloading unnecessary content.

---

## 📦Tech Stack
**Language**: Python
- requests module

## Getting Started

### Prerequisites

To use this tool, ensure you have the following installed:

- Python 3.7+
- `requests` library for Python
