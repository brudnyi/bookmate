import importlib
import os

def test_top_level_packages_import():
    pkgs = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, '__init__.py'))]
    assert pkgs, 'No top-level packages found in repository root'
    for p in pkgs:
        m = importlib.import_module(p)
        if hasattr(m, '__version__'):
            assert isinstance(m.__version__, str)
