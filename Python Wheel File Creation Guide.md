# Python Wheel File Creation Guide

A comprehensive guide for creating Python wheel files and deploying them to AWS Glue or other Python environments.

## What is a Wheel File?
A wheel file (`.whl`) is a built package format for Python that allows you to distribute your project as a single installable archive. It's faster to install than source distributions and ensures consistent deployment across environments.

---

## Step 1: Set Up Your Project Structure

Ensure your project is structured properly with `__init__.py` files in each package directory:

```
my_project/
│
├── setup.py
├── README.md
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── subpackage/
│       ├── __init__.py
│       └── module3.py
└── tests/
    └── test_module1.py
```

**Key Points:**
- Each directory containing Python modules should have an `__init__.py` file (can be empty)
- Keep your project files organized in logical packages
- Separate tests from main code

---

## Step 2: Create setup.py

Create a `setup.py` file in the root of your project:

```python
from setuptools import setup, find_packages

setup(
    name='my_project_name',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of your project',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.21.0',
        'requests>=2.26.0',
        # Add other dependencies here
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
```

**Parameters Explained:**
- `name`: Your project name (will be used in the wheel filename)
- `version`: Semantic version (e.g., 1.0.0)
- `packages`: Use `find_packages()` to auto-discover all packages
- `install_requires`: List of dependencies (pip will install these automatically)
- `python_requires`: Minimum Python version required

---

## Step 3: Build the Wheel

Navigate to the root directory of your project in the terminal and run:

```bash
# Install wheel package if not already installed
pip install wheel setuptools

# Build the wheel file
python setup.py bdist_wheel
```

This will create a `dist/` directory containing the wheel file:
```
dist/my_project_name-1.0.0-py3-none-any.whl
```

**Naming Convention:**
- `my_project_name`: Your project name
- `1.0.0`: Version number
- `py3`: Python 3 compatible
- `none`: No specific ABI
- `any`: Works on any platform

---

## Step 4: Upload the Wheel File to S3 (for AWS Glue)

Upload the generated wheel file to an S3 bucket:

```bash
aws s3 cp dist/my_project_name-1.0.0-py3-none-any.whl s3://your-bucket-name/python-libraries/my_project_name-1.0.0-py3-none-any.whl
```

**Best Practices:**
- Use a dedicated folder for Python libraries (e.g., `/python-libraries/`)
- Include version numbers in paths for version control
- Set appropriate S3 bucket permissions

---

## Step 5: Use in AWS Glue Job

When creating or editing your AWS Glue job:

1. Navigate to **Job details** → **Advanced properties**
2. In the **Python library path** field, add:
   ```
   s3://your-bucket-name/python-libraries/my_project_name-1.0.0-py3-none-any.whl
   ```
3. For multiple wheel files, separate with commas:
   ```
   s3://bucket/lib1.whl,s3://bucket/lib2.whl
   ```

---

## Step 6: Import in Your Code

In your Glue job or Python script, import your modules normally:

```python
from my_package.module1 import MyClass
from my_package.subpackage.module3 import my_function

# Use your imported modules
obj = MyClass()
result = my_function()
```

---

## Additional Notes

### Package Requirements
- Ensure `__init__.py` files exist in all package directories
- Python version in Glue job must match the version used to build the wheel
- Test imports locally before deploying to Glue

### Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Build wheel
python setup.py bdist_wheel
```

---

## Troubleshooting Common Errors

### 1. ModuleNotFoundError for Dependencies

**Problem:** AWS Glue doesn't automatically resolve transitive dependencies from `install_requires`.

**Solution:**
```bash
# Download dependency as wheel file
pip download your-dependency --no-deps -d ./dependencies

# Upload to S3
aws s3 cp dependencies/your_dependency-1.0.0-py3-none-any.whl s3://your-bucket/python-libraries/

# In Glue job, include both wheels:
s3://bucket/my_project.whl,s3://bucket/your_dependency.whl
```

### 2. Import Errors After Installing Wheel

**Problem:** Modules not found even though wheel is specified.

**Possible Causes:**
- Missing `__init__.py` files
- Incorrect package structure
- Python version mismatch

**Solution:** Extract and validate wheel contents (see section below)

### 3. Version Conflicts

**Problem:** Multiple versions of the same package causing conflicts.

**Solution:**
- Use specific version pins in `install_requires`
- Test in a clean virtual environment before deploying

---

## How to Download and Extract a Wheel File for Validation

### 1. Download the wheel file from S3
```bash
aws s3 cp s3://your-bucket/python-libraries/my_project-1.0.0-py3-none-any.whl ./my_project-1.0.0-py3-none-any.whl
```

### 2. Extract the wheel file

Wheel files are ZIP archives. You can extract them using `unzip`:
```bash
unzip my_project-1.0.0-py3-none-any.whl -d extracted_wheel
```

Or use Python:
```python
import zipfile

with zipfile.ZipFile('my_project-1.0.0-py3-none-any.whl', 'r') as zip_ref:
    zip_ref.extractall('extracted_wheel')
```

### 3. Inspect the extracted contents

Check the `extracted_wheel` directory to validate:
- All expected Python modules are present
- `__init__.py` files exist in package directories
- Metadata in `*.dist-info/` directory is correct

Expected structure:
```
extracted_wheel/
├── my_package/
│   ├── __init__.py
│   ├── module1.py
│   └── subpackage/
│       ├── __init__.py
│       └── module3.py
└── my_project_name-1.0.0.dist-info/
    ├── METADATA
    ├── WHEEL
    ├── top_level.txt
    └── RECORD
```

### 4. Repackage the Wheel File After Making Changes

If you made changes to the extracted files and want to repackage:

```bash
cd extracted_wheel
zip -r ../my_project-1.0.0-py3-none-any.whl .
cd ..
```

**Important:** Zip the contents, not the directory itself.

---

## Alternative: Using Local Wheel Files

For local development or non-AWS environments:

```bash
# Install wheel file locally
pip install dist/my_project-1.0.0-py3-none-any.whl

# Or install in editable mode during development
pip install -e .
```

---

## Best Practices

1. **Version Control:** Increment version numbers for each release
2. **Testing:** Test the wheel file in a clean environment before deploying
3. **Documentation:** Include README and CHANGELOG in your project
4. **Dependencies:** Pin dependency versions to avoid breaking changes
5. **Security:** Don't include sensitive data (credentials, keys) in wheel files
6. **Size:** Keep wheel files small; use external dependencies when possible

---

## Quick Reference Commands

```bash
# Build wheel
python setup.py bdist_wheel

# Install wheel locally
pip install dist/my_project-1.0.0-py3-none-any.whl

# Upload to S3
aws s3 cp dist/my_project-1.0.0-py3-none-any.whl s3://bucket/path/

# Download from S3
aws s3 cp s3://bucket/path/my_project-1.0.0-py3-none-any.whl ./

# Extract wheel
unzip my_project-1.0.0-py3-none-any.whl -d extracted_wheel

# Repackage wheel
cd extracted_wheel && zip -r ../my_project-1.0.0-py3-none-any.whl . && cd ..
```

---

## Resources

- [Python Packaging User Guide](https://packaging.python.org/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [AWS Glue Python Shell Jobs](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html)
- [Wheel File Format Specification](https://www.python.org/dev/peps/pep-0427/)
