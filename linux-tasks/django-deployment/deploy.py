#!/usr/bin/env python3
"""
Django Application Deployment Script

This script automates the deployment of a Django application by:
- Checking system prerequisites (Python 3.7+, MySQL 8.0+, Git)
- Creating a virtual environment
- Cloning the application repository
- Installing dependencies
- Setting up the database
- Configuring the application
- Running migrations
- Starting the development server

Usage:
    python3 deploy.py --version <version>

Example:
    python3 deploy.py --version master
    python3 deploy.py --version v1.0.0
"""
import argparse
import platform
import sys
import subprocess
import re
import os
import shutil
import getpass


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
    except BaseException:
        return "unsupported"


def check_prerequisites():
    """Checks for Python and MySQL"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7+ required")
        sys.exit(1)

    try:
        result = subprocess.run(["mysql", "--version"],
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("Error: MySQL required")
            sys.exit(1)
    except FileNotFoundError:
        print("Error: MySQL is not installed")
        sys.exit(1)

    text = result.stdout
    version = re.search(r'(\d+\.\d+\.\d+)', text)

    if version:
        version_str = version.group(0)
        major_minor = '.'.join(version_str.split('.')[:2])
        if float(major_minor) < 8.0:
            print(f"Error: MySQL 8.0+ required, found version {major_minor}")
            sys.exit(1)
    else:
        print("Error: Could not determine MySQL version")

    print("Prerequisites check passed (MySQL check skipped for testing)")

    try:
        result = subprocess.run(["git", "--version"],
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("Error: Git command failed")
            sys.exit(1)
    except FileNotFoundError:
        print("Error: Git is not installed")
        sys.exit(1)


def create_directory(app_dir="project-dir"):
    """Creating a working directory - for a virtual environment"""
    if os.path.exists(app_dir):
        print("Removing old deployment directory...")
        shutil.rmtree(app_dir)

    os.makedirs(app_dir)
    print("Deployment directory created")
    return app_dir


def create_virtualenv(app_dir):
    """Creating virtualenv - an isolated Python environment"""
    venv_path = os.path.join(app_dir, "venv")
    print("Creating virtual environment...")

    try:
        result = subprocess.run(["python3", "-m", "venv", venv_path],
                                capture_output=True,
                                text=True)
        if result.returncode != 0:
            print("Error: Failed to create virtual environment")
            sys.exit(1)

    except Exception:
        print(result.stderr)
        sys.exit(1)

    activate_script = os.path.join(venv_path, "bin", "activate")
    if not os.path.exists(activate_script):
        print("Error: Virtual environment was not created properly")
        sys.exit(1)

    print("Virtual environment created")
    return venv_path


def pull_code(app_dir, version):
    """Downloading code - git clone of a specific version"""
    repo_url = "https://github.com/Manisha-Bayya/simple-django-project.git"
    code_dir = os.path.join(app_dir, "simple-django-project")

    result = subprocess.run(["git",
                             "clone",
                             "--branch",
                             version,
                             repo_url,
                             code_dir],
                            capture_output=True,
                            text=True)
    if result.returncode != 0:
        print(
            f"Error: Failed to clone repository (version '{version}' not found?)")
        print(f"Git error: {result.stderr}")
        sys.exit(1)
    return code_dir


def install_dependencies(venv_path, code_dir):
    """Installing dependencies - pip install -r requirements.txt"""
    pip_path = os.path.join(venv_path, "bin", "pip")
    requirements_path = os.path.join(code_dir, "requirements.txt")

    if not os.path.exists(requirements_path):
        print("Error: requirements.txt not found")
        sys.exit(1)

    result = subprocess.run([pip_path, "install", "-r",
                            requirements_path],
                            capture_output=True,
                            text=True)
    if result.returncode != 0:
        print("Error: Failed to install dependencies")
        print(result.stderr)
        sys.exit(1)


def db_setting(code_dir):
    """Database Setup - Import world.sql into MySQL"""
    print("=== DB SETTING FUNCTION CALLED ===")
    print("Setting up database...")

    db_user = input("Enter MySQL username (default: root): ") or "root"
    db_password = getpass.getpass("Enter MySQL password: ")
    db_name = input("Enter database name (default: world): ") or "world"

    sql_file = os.path.join(code_dir, "world.sql")

    if not os.path.exists(sql_file):
        print("Error: world.sql not found")
        sys.exit(1)

    try:
        result = subprocess.run([
            "mysql",
            f"-u{db_user}",
            f"-p{db_password}",
            db_name
        ], stdin=open(sql_file),
            capture_output=True,
            text=True)

        if result.returncode != 0:
            print("Error: Failed to import database")
            print(result.stderr)
            sys.exit(1)

        print("Database imported successfully!")
    except FileNotFoundError:
        print("Warning: MySQL not installed, skipping database import")
        print(
            "On production, this would run: mysql -u{user} -p {db} < world.sql")

    return db_user, db_password


def application_configuration(code_dir, db_user, db_password):
    """Application Configuration - settings.py Editing"""
    settings_path = os.path.join(code_dir, "panorbit", "settings.py")
    db_host = "localhost"
    db_port = "3306"

    if not os.path.exists(settings_path):
        print("Error: settings.py not found")
        sys.exit(1)

    try:
        with open(settings_path, 'r') as file:
            data = file.read()
    except Exception as e:
        print(f"Error reading settings.py: {e}")
        sys.exit(1)

    data = data.replace('<mysql-user>', db_user)
    data = data.replace('<mysql-password>', db_password)
    data = data.replace('<mysql-host>', db_host)
    data = data.replace('<mysql-port>', db_port)
    with open(settings_path, 'w') as file:
        file.write(data)
    print("Application configuration updated successfully!")


def run_migrations(venv_path, code_dir):
    """Starting migrations - manage.py migrate"""
    python_path = os.path.join(venv_path, "bin", "python3")

    if not os.path.exists(python_path):
        print("Error: python not found")
        sys.exit(1)

    manage_path = os.path.join(code_dir, "manage.py")

    if not os.path.exists(manage_path):
        print("Error: manage.py not found")
        sys.exit(1)

    result = subprocess.run([python_path, manage_path, "makemigrations"],
                            capture_output=True,
                            text=True)
    if result.returncode != 0:
        print("Error: makemigrations failed")
        print(result.stderr)
        sys.exit(1)

    result = subprocess.run([python_path, manage_path, "migrate"],
                            capture_output=True,
                            text=True)
    if result.returncode != 0:
        print("Error: migrate failed")
        print(result.stderr)
        sys.exit(1)

    result = subprocess.run([python_path, manage_path, "rebuild_index"],
                            capture_output=True,
                            text=True)
    if result.returncode != 0:
        print("Warning: rebuild_index failed (non-critical)")
    else:
        print("Search index rebuilt successfully")

    print("Migrations completed successfully!")


def start_server(venv_path, code_dir):
    """The Runserver - manage.py Runserver"""
    python_path = os.path.join(venv_path, "bin", "python3")
    manage_path = os.path.join(code_dir, "manage.py")

    print("Starting Django server on port 8001...")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)

    subprocess.run([python_path, manage_path, "runserver", "0:8001"])


def main():
    """Main deployment workflow"""
    version = parse_arguments()
    print(f"Deploying version: {version}")

    os_type = check_os()
    print(f"Detected OS: {os_type}")

    check_prerequisites()

    app_dir = create_directory()
    venv_path = create_virtualenv(app_dir)
    code_dir = pull_code(app_dir, version)

    install_dependencies(venv_path, code_dir)

    db_user, db_password = db_setting(code_dir)

    application_configuration(code_dir, db_user, db_password)

    run_migrations(venv_path, code_dir)

    start_server(venv_path, code_dir)

    print("All prerequisites checked successfully!")


if __name__ == "__main__":
    main()
