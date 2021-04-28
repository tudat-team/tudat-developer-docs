
Sphinx
======

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