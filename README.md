# sleep-analysis
Learning to program by analyzing some sleep data!


# Starting a package!

To make a new package, we first handle some preliminary structing things
- Package structure (using [poetry](https://python-poetry.org/))
  - Also see [PyOpenSci Packaging Guide](https://www.pyopensci.org/python-package-guide/)
  - And the python docs - https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - Learned about the pyproject.toml file and poetry.lock file (see poetry docs)
- Docs (using [sphinx](https://www.sphinx-doc.org/en/master/) and [readthedocs](https://readthedocs.org/))
  - read the docs tutorial https://docs.readthedocs.io/en/stable/tutorial/
  - Add repository to automatically build on commit - https://docs.readthedocs.io/en/stable/integrations.html
  - Configuration https://docs.readthedocs.io/en/stable/config-file/v2.html
  - Furo theme! https://pypi.org/project/furo/
  - Poetry groups and readthedocs: https://browniebroke.com/blog/specify-docs-dependency-groups-with-poetry-and-read-the-docs/
  - Graphviz for making diagrams!
    - usage with sphinx https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
    - graphviz documentation https://graphviz.org/docs/
  - MyST for using markdown in sphinx - https://myst-parser.readthedocs.io/en/latest/
  - TODO: research relationship between Aaron Swartz and Markdown
    - https://en.wikipedia.org/wiki/Guerilla_Open_Access_Manifesto
  - Different docstring formats with napoleon - https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
- Tests (maybe next time!)
- Notebooks (just putting them in a specific place and showing how to import from the package)
- Using the package
  - `poetry shell`

# Additional resources

- Semantic versioning (why most version numbers are the way they are) - https://semver.org/

## Programming Concepts

- "[Information hiding](https://en.wikipedia.org/wiki/Information_hiding)" - making modularity and clear division of labor