#!/usr/bin/env python3
"""
Test runner for MkDocs configuration property-based tests.
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Run the property-based tests for MkDocs configuration."""
    project_root = Path(__file__).parent.parent
    test_file = project_root / "tests" / "test_section_completeness.py"
    
    if not test_file.exists():
        print(f"Error: Test file not found at {test_file}")
        return 1
        
    try:
        # Install test dependencies
        print("Installing test dependencies...")
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", 
            str(project_root / "tests" / "requirements.txt")
        ], check=True)
        
        # Run the tests
        print("Running property-based tests...")
        result = subprocess.run([
            sys.executable, "-m", "pytest", str(test_file), "-v", "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
        return result.returncode
        
    except subprocess.CalledProcessError as e:
        print(f"Error running tests: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())