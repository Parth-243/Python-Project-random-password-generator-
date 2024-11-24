import random
import string
import os

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def generate_password(self, length=12, use_os_random=False):
        """
        Generate a random password of specified length.
        
        Args:
            length (int): Length of the password (default: 12)
            use_os_random (bool): Whether to use os.urandom() for generation (default: False)
            
        Returns:
            str: Generated password
        """
        if length < 8:
            raise ValueError("Password length must be at least 8 characters")
            
        if use_os_random:
            # Using os.urandom() for cryptographically secure random generation
            return ''.join(self.characters[i % len(self.characters)] 
                         for i in os.urandom(length))
        else:
            # Using random.choice() for simple random generation
            return ''.join(random.choice(self.characters) for _ in range(length))

def main():
    generator = PasswordGenerator()
    try:
        password = generator.generate_password()
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()