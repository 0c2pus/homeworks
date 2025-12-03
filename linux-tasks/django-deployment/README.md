# Django Application Deployment Script

Automated Python script for deploying Django applications on Linux servers.

## Description

This script automates the deployment process of a Django application by handling environment setup, dependency installation, database configuration, and server startup.

## Prerequisites

Before running this script, ensure the following are installed on your Linux system:

- **Operating System**: RHEL-like, Debian-like, or Ubuntu-like distributions
- **Python**: Version 3.7 or higher
- **MySQL**: Version 8.0 or higher
- **Git**: Any recent version

## Installation

1. Clone or download the `deploy.py` script
2. Make it executable (optional):
```bash
   chmod +x deploy.py
```

## Usage

Run the script with the required `--version` argument:
```bash
python3 deploy.py --version <version>
```

### Examples

Deploy the master branch:
```bash
python3 deploy.py --version master
```

Deploy a specific tag:
```bash
python3 deploy.py --version v1.0.0
```

Deploy a specific commit:
```bash
python3 deploy.py --version a3f5b2c
```

## What the Script Does

1. **Checks Prerequisites**: Verifies Python 3.7+, MySQL 8.0+, and Git are installed
2. **Creates Deployment Directory**: Sets up a clean working directory (`project-dir/`)
3. **Creates Virtual Environment**: Isolates Python dependencies
4. **Clones Repository**: Downloads the Django application code
5. **Installs Dependencies**: Installs required Python packages from `requirements.txt`
6. **Configures Database**: Imports SQL data and configures MySQL connection
7. **Updates Settings**: Edits Django settings with database credentials
8. **Runs Migrations**: Applies database migrations
9. **Starts Server**: Launches Django development server on port 8001

## Interactive Prompts

During execution, you'll be prompted for:

- **MySQL Username** (default: root)
- **MySQL Password**
- **Database Name** (default: world)

## Output

The script will:
- Display progress messages for each step
- Show errors if prerequisites are missing
- Start the Django server at `http://0.0.0.0:8001`

To stop the server, press `Ctrl+C`.

## Project Structure

After successful deployment:
```
project-dir/
├── venv/                    # Virtual environment
└── simple-django-project/   # Django application code
    ├── manage.py
    ├── requirements.txt
    ├── world.sql
    └── panorbit/
        └── settings.py
```

## Limitations

- Designed for Linux systems only (not Windows or macOS)
- Assumes MySQL is already installed and configured
- Uses Django development server (not production-ready)
- Removes existing `project-dir/` on each run

## Troubleshooting

**"Error: MySQL is not installed"**
- Install MySQL 8.0+ on your system

**"Error: Failed to clone repository"**
- Check internet connection
- Verify the version/branch exists

**"Error: Failed to install dependencies"**
- Ensure MySQL development headers are installed
- On Debian/Ubuntu: `sudo apt-get install libmysqlclient-dev`
- On RHEL/CentOS: `sudo yum install mysql-devel`