import hashlib
import re
from typing import Tuple
class SecureLoginSystem:
    """A secure login system with password hashing and validation."""
    def __init__(self):
        # In production, use a database instead of in-memory storage
        self.users = {}
    def _hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
    def _validate_password_strength(self, password: str) -> Tuple[bool, str]:
        """Validate password meets security requirements."""
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r"[A-Z]", password):
            return False, "Password must contain uppercase letters"
        if not re.search(r"[a-z]", password):
            return False, "Password must contain lowercase letters"
        if not re.search(r"[0-9]", password):
            return False, "Password must contain digits"
        if not re.search(r"[!@#$%^&*]", password):
            return False, "Password must contain special characters"
        return True, "Password is strong"
    def register(self, username: str, password: str) -> Tuple[bool, str]:
        """Register a new user with password validation."""
        if not username or len(username) < 3:
            return False, "Username must be at least 3 characters"
        if username in self.users:
            return False, "Username already exists"
        is_strong, message = self._validate_password_strength(password)
        if not is_strong:
            return False, message
        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password
        return True, "Registration successful"
    def login(self, username: str, password: str) -> Tuple[bool, str]:
        """Authenticate user with username and password."""
        if username not in self.users:
            # Generic error message prevents username enumeration
            return False, "Invalid credentials"
        hashed_input = self._hash_password(password)
        if hashed_input == self.users[username]:
            return True, f"Login successful for {username}"
        
        return False, "Invalid credentials"
# Example usage
if __name__ == "__main__":
    login_system = SecureLoginSystem()
    # Test registration
    print("=== Registration Tests ===")
    print(login_system.register("john_doe", "weak"))
    print(login_system.register("john_doe", "Secure@Pass123"))
    print(login_system.register("jane_smith", "SecurePass@123"))
    # Test login
    print("\n=== Login Tests ===")
    print(login_system.login("john_doe", "Secure@Pass123"))
    print(login_system.login("john_doe", "WrongPassword"))
    print(login_system.login("unknown_user", "SomePass@123"))