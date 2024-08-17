Maintaining a Conda Feedstock
=============================
This section explains within the context of the Tudat project how to maintain a Conda feedstock. It will not cover
everything possible with a ``conda-build`` recipe, and there are most probably some more ways you as a developer could
improve the recipe using the ``conda-build`` documentation. However, this guide will provide you with what you need for
our current feedstocks, and it should be a good starting point for going further.

Keeping things `<DRY>`_
-----------------------
The easiest solution to reducing repetition of values in a ``conda-build`` recipe is to use take advantage of Jinja
templating which is widely used in python for site generation, and so is it a natural fit for ``conda-build`` recipes.
You will either (1) want to generate multiple build variants given a set of parameters, or (2) you simply want to
replace a few values within the recipe metadata definition: ``meta.yaml``.

.. _dry: https://en.wikipedia.org/wiki/Don%27t_repeat_yourself

.. todo: Finish this page