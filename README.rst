..
  SPDX-FileCopyrightText: 2022 Ludwig Hülk <https://github.com/Ludee> © Reiner Lemoine Institut
  SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
  SPDX-License-Identifier: MIT

.. figure:: https://user-images.githubusercontent.com/14353512/185425447-85dbcde9-f3a2-4f06-a2db-0dee43af2f5f.png
    :align: left
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/
    :alt: Repo logo

==========================
dfg-preserving-energy-data
==========================

**Securing and Preserving Energy Data from the Harvard Dataverse.**

.. list-table::
   :widths: auto

   * - License
     - |badge_license| |badge_reuse|
   * - Documentation
     - |badge_documentation| |badge_mkdocs|
   * - Tests
     - |badge_tox| |badge_codecov|
   * - Publication
     - |badge_pypi| |badge_python| |badge_pypi_downloads|
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributions| |badge_contributors| |badge_matrix| |badge_repo_counts|

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Introduction
============
The project aims to secure and preserve research data from completed international energy research
projects currently hosted on the Harvard Dataverse, with a focus on the PeopleSuN Survey Data and
related datasets published by the Reiner Lemoine Institute (RLI). These datasets represent valuable
empirical and model-based resources for the global energy research community and are at risk due
to their dependence on external, non-European infrastructure. The project will transfer, curate, and
republish the data within the Open Energy Platform (OEP), a long-standing and FAIR-compliant repository operated in Germany and integrated into the National Research Data Infrastructure
(NFDI4Energy). The work includes the enrichment of metadata using the OEMetadata standard, ensuring interoperability, transparency, and machine readability. By establishing a sustainable European mirror of these datasets, the project contributes to the long-term preservation, accessibility, and
reusability of energy research data. It strengthens data sovereignty, supports reproducible research,
and ensures that valuable scientific results remain available for future investigations.

Documentation
=============
| The documentation is created with Markdown using `MkDocs <https://www.mkdocs.org/>`_ and `mike <https://github.com/jimporter/mike>`_.
| All files are stored in the ``docs`` folder of the repository.
| A **GitHub Actions** deploys the ``develop`` branch on a **GitHub Page**.
| The documentation page is: `rl-institut.github.io/dfg-preserving-energy-data/ <https://rl-institut.github.io/dfg-preserving-energy-data/>`_

Collaboration
=============
| Everyone is invited to develop this repository with good intentions.
| Please follow the workflow described in the `CONTRIBUTING.md <https://github.com/rl-institut/dfg-preserving-energy-data/blob/production/CONTRIBUTING.md>`_.

Contributors:

.. figure:: https://contrib.rocks/image?repo=rl-institut/dfg-preserving-energy-data
    :align: left
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/graphs/contributors
    :alt: [contrib.rocks](https://contrib.rocks)

License and Citation
====================
| The code of this repository is licensed under the **MIT License** (MIT).
| See `LICENSE.txt <https://github.com/rl-institut/dfg-preserving-energy-data/blob/production/LICENSE.txt>`_ for rights and obligations.
| See the *Cite this repository* function or `CITATION.cff <https://github.com/rl-institut/dfg-preserving-energy-data/blob/production/CITATION.cff>`_ for citation of this repository.
| Copyright: `dfg-preserving-energy-data <https://github.com/rl-institut/dfg-preserving-energy-data/>`_ © `Reiner Lemoine Institut <https://reiner-lemoine-institut.de/>`_ | `MIT <LICENSE.txt>`_


.. |badge_license| image:: https://img.shields.io/github/license/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/blob/production/LICENSE.txt
    :alt: License

.. |badge_reuse| image:: https://api.reuse.software/badge/github.com/rl-institut/dfg-preserving-energy-data
    :target: https://api.reuse.software/info/github.com/rl-institut/dfg-preserving-energy-data
    :alt: REUSE

.. |badge_documentation| image:: https://img.shields.io/github/actions/workflow/status/rl-institut/dfg-preserving-energy-data/documentation.yml?branch=develop&label=documentation
    :target: https://rl-institut.github.io/dfg-preserving-energy-data/
    :alt: Documentation

.. |badge_mkdocs| image:: https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=flat&logo=MaterialForMkDocs&logoColor=white&color=grey
    :target: https://squidfunk.github.io/mkdocs-material/
    :alt: MkDocs

.. |badge_tox| image:: https://img.shields.io/github/actions/workflow/status/rl-institut/dfg-preserving-energy-data/tox.yml?label=tox
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/actions/workflows/tox.yml
    :alt: Tox Tests

.. |badge_python| image:: https://img.shields.io/pypi/pyversions/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/blob/develop/pyproject.toml
    :alt: PyPI Python Version

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/issues
    :alt: Open Issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/issues?q=is%3Aissue+is%3Aclosed
    :alt: Closed Issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/pulls
    :alt: Open PR

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/pulls?q=is%3Apr+is%3Aclosed
    :alt: Closed PR

.. |badge_contributions| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/blob/production/CONTRIBUTING.md
    :alt: Contributions

.. |badge_contributors| image:: https://img.shields.io/github/contributors/rl-institut/dfg-preserving-energy-data
    :target: https://github.com/rl-institut/dfg-preserving-energy-data/graphs/contributors
    :alt: Contributors

.. |badge_repo_counts| image:: https://hits.sh/github.com/rl-institut/dfg-preserving-energy-data.svg
    :target: https://hits.sh/github.com/rl-institut/dfg-preserving-energy-data/
    :alt: Hits
