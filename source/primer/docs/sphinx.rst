
Sphinx Documentation
====================

The instructions to update the tudat developer documentation you are reading or to write new sections is available
in :ref:`Getting Started with Documentation`.

The remainder of this page is currently under construction.

.. code-block::

    sudo apt-get install  texmaker gummi texlive texlive-full texlive-latex-recommended latexdraw intltool-debian lacheck libgtksourceview2.0-0 libgtksourceview2.0-common lmodern luatex po-debconf tex-common texlive-binaries texlive-extra-utils texlive-latex-base texlive-latex-base-doc texlive-luatex texlive-xetex texlive-lang-cyrillic texlive-fonts-extra texlive-science texlive-latex-extra texlive-pstricks


.. todo::

    - Link checking is facilitated by sphinx using ``make linkcheck`` (on windows)
    - Add section on FontAwesome inline icons from ``sphinx-panels``
    - https://fontawesome.com/
    - Add tutorial/ section on maintaining a bibliography in Sphinx.

Useful Sphinx Extensions
------------------------

.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    :badge:`example,badge-primary`

    ---

    .. dropdown:: :fa:`eye,mr-1` Bottom-left panel

        Hidden content

    ---

    .. link-button:: https://example.com
        :text: Clickable Panel
        :classes: stretched-link

.. tabbed:: ReStructuredText

    .. code-block:: rst

        .. panels::

            Content of the top-left panel

            ---

            Content of the top-right panel

            :badge:`example,badge-primary`

            ---

            .. dropdown:: :fa:`eye,mr-1` Bottom-left panel

                Hidden content

            ---

            .. link-button:: https://example.com
                :text: Clickable Panel
                :classes: stretched-link

.. tabbed:: MyST Markdown

    .. code-block:: md

        ````{panels}
        Content of the top-left panel

        ---

        Content of the top-right panel

        {badge}`example,badge-primary`

        ---

        ```{dropdown} :fa:`eye,mr-1` Bottom-left panel
        Hidden content
        ```

        ---

        ```{link-button} https://example.com
        :text: Clickable Panel
        :classes: stretched-link
        ```

        ````