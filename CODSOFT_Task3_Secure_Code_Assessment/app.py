"""
CODSOFT Cyber Security Internship — Task 3
Secure Code Assessment (educational demonstration)

Run:
    python app.py

This demo uses only Python's standard library. It shows a small secure
login example with input validation, password hashing, and safe messages.
It is not intended for production use.
"""
import hashlib
import hmac
import secrets
import getpass

# Demonstration account only. In a real application, store account records
# in a protected database and use a dedicated password-hashing library
# such as Argon2id, scrypt, or bcrypt with per-user salts.
DEMO_USERNAME = "student"
DEMO_SALT = b"codsoft-demo-salt-change-in-real-app"
DEMO_PASSWORD_HASH = hashlib.pbkdf2_hmac(
    "sha256", b"DemoPass123!", DEMO_SALT, 200_000
)

MAX_USERNAME_LENGTH = 50
MAX_PASSWORD_LENGTH = 128


def validate_username(username: str) -> bool:
    """Allow a simple username format and limit input length."""
    if not username or len(username) > MAX_USERNAME_LENGTH:
        return False
    return all(ch.isalnum() or ch in "._-" for ch in username)


def verify_password(password: str) -> bool:
    """Compare password hashes using a constant-time comparison."""
    if not password or len(password) > MAX_PASSWORD_LENGTH:
        return False
    candidate = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), DEMO_SALT, 200_000
    )
    return hmac.compare_digest(candidate, DEMO_PASSWORD_HASH)


def authenticate(username: str, password: str) -> bool:
    """Return success only when the username and password are valid."""
    if not validate_username(username):
        return False
    # Generic failure messages help avoid revealing which field was wrong.
    return hmac.compare_digest(username, DEMO_USERNAME) and verify_password(password)


def main() -> None:
    print("=" * 48)
    print(" SECURE CODE ASSESSMENT — DEMO LOGIN")
    print("=" * 48)
    print("Demo username: student")
    print("Demo password: DemoPass123!")
    print("Use these sample credentials only for this local demonstration.\n")

    username = input("Username: ").strip()
    password = getpass.getpass("Password: ")

    if authenticate(username, password):
        print("\nLogin successful. Welcome to the demo.")
    else:
        print("\nLogin failed. Check your credentials and try again.")

    print("\nSecurity note: this is a learning sample, not a production login system.")


if __name__ == "__main__":
    main()
