.. release procedure

Prepare newest packages:

* setuptools
* wheel
* twine

Procedure:

1. tagging with version name that MUST following semver. e.g.: ``git tag 1.0.1``
2. build distribution files: ``python setup.py sdist bdist_wheel``
3. make a test release: ``twine upload --repository-url https://test.pypi.org/legacy dist/<new-version-files>``
4. make a release: ``twine upload dist/<new-version-files>``
5. check PyPI page: https://pypi.org/p/sphinxcontrib-ogp
6. bump version in ``CHANGES.rst`` and commit/push them onto GitHub
