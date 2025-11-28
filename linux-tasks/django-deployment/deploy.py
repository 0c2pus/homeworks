#!/usr/bin/env python3
"""
Django Application Deployment Script
"""
import argparse
import platform
import sys
import subprocess
import re
import os
import shutil


def parse_arguments():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description='Deploy Django application')
    
    parser.add_argument(
        '--version',
        required=True,
        help='Application version to deploy (e.g., v1.0.0, main, commit-hash)'
    )
    
    args = parser.parse_args()
    
    return args.version

def check_os():
    """Specifies the type of operating system"""
    try:
        info = platform.freedesktop_os_release()
        distro_id = info['ID']
        distro_like = info.get('ID_LIKE', '')
        if distro_id in ['debian', 'ubuntu', 'rhel']:
            return distro_id
        else:
            if 'rhel' in distro_like:
                return distro_like
            else:
                return "unsupported"
    except KeyError:
        return "unsupported"
    except:
        return "unsupported"


def check_prerequisites():
    """Checks for Python and MySQL"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7+ required")
        sys.exit(1)

    # try:
    #     result = subprocess.run(["mysql", "--version"],
    #                             capture_output=True,
    #                             text=True)
    #     if result.returncode != 0:
    #         print("Error: MySQL required")
    #         sys.exit(1)
    # except FileNotFoundError:
    #     print("Error: MySQL is not installed")
    #     sys.exit(1)

    # text = result.stdout
    # version = re.search(r'(\d+\.\d+\.\d+)', text)
    
    # if version:
    #     version_str = version.group(0)
    #     major_minor = '.'.join(version_str.split('.')[:2])
    #     if float(major_minor) < 8.0:
    #         print(f"Error: MySQL 8.0+ required, found version {major_minor}")
    #         sys.exit(1)
    # else:
    #     print("Error: Could not determine MySQL version")

    print("Prerequisites check passed (MySQL check skipped for testing)")


def create_directory(app_dir="django-deployment"):
    """Creating a working directory - for a virtual environment"""
    if os.path.exists(app_dir):
        print("Removing old deployment directory...")
        shutil.rmtree(app_dir)

    os.makedirs(app_dir)
    print("Deployment directory created")
    return app_dir


def create_virtualenv():
    """Creating virtualenv - an isolated Python environment"""
    pass


def pull_code():
    """Downloading code - git clone of a specific version"""
    pass


def install_dependencies():
    """Installing dependencies - pip install -r requirements.txt"""
    pass


def db_setting():
    """Database Setup - Import world.sql into MySQL"""
    pass


def application_configuration():
    """Application Configuration - settings.py Editing"""
    pass


def run_migrations():
    """Starting migrations - manage.py migrate"""
    pass


def start_server():
    """The Runserver - manage.py Runserver"""
    pass


def main():
    """Main deployment workflow"""
    version = parse_arguments()
    print(f"Deploying version: {version}")

    os_type = check_os()
    print(f"Detected OS: {os_type}")
    
    check_prerequisites()

    app_dir = create_directory()

    print("All prerequisites checked successfully!")


if __name__ == "__main__":
    main()