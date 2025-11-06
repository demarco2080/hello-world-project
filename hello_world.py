#!/usr/bin/env python3
"""
Hello World script with colorful output and timestamp
"""

from datetime import datetime


# ANSI color codes
class Colors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # Get current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Print colorful welcome message
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 50}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}⚠️  Tony CHANGED IT!!!!  ⚠️{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 50}{Colors.END}\n")

    print(f"{Colors.YELLOW}Current timestamp: {Colors.BOLD}{timestamp}{Colors.END}\n")

    print(f"{Colors.PURPLE}Hello, World! {Colors.RED}❤️{Colors.END}")
    print(f"{Colors.BLUE}Greetings from Python!{Colors.END}\n")


if __name__ == "__main__":
    main()
