import os

def test_readme_exists():
    readme_files = ['README.md', 'README.rst', 'README']
    assert any(os.path.exists(f) for f in readme_files), "README file not found (expected one of: {})".format(readme_files)
