
.. _Managing Access Tokens:

Managing Access Tokens
======================

Generating Access Tokens
------------------------

In this section, we will provide step-by-step instructions for generating access tokens on Anaconda and GitHub.

Generating Organization Tokens on Anaconda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   This section is intended for maintainers of the feedstock repositories (at current). If you are not a maintainer, you can safely ignore this section.

1. Navigate to https://anaconda.org/ and sign in

.. image:: graphics/anaconda_org_token_1.jpeg

2. Go to the organization page, for example, if the organization is named "tudat-team", the URL would be https://anaconda.org/tudat-team
3. Click on the organization profile ("tudat-team") at the top-right of the page, followed by "Settings".

.. image:: graphics/anaconda_org_token_2.jpeg

4. Fill in the details for creating a new token: name your token, provide the appropriate scope, and specify an expiration date. Then, click "Create".

.. image:: graphics/anaconda_org_token_3.jpeg

5. The newly created organization token will be displayed. Copy the token and keep it safe, as it will only be shown once.

.. image:: graphics/anaconda_org_token_4.jpeg

.. important::
   It is crucial to keep the organization token private and secure. Ensure that you do not share it or commit it to a public repository, as this could lead to security issues.

Generating User Tokens on GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Navigate to `GitHub <https://github.com>`__. After this, go to step 3 if you are already signed in, otherwise, click "Sign in" at the top-right of the landing page.

.. image:: graphics/github_user_token_1.jpeg

2. Enter your details and click "Sign in".

.. image:: graphics/github_user_token_2.jpeg

.. note::
    Dark mode makes you a better developer.

3. Click on your profile picture at the top-right of the page to reveal a drop-down menu, select "Settings".

.. image:: graphics/github_user_token_3.jpeg

4. Click on "Developer settings".

.. image:: graphics/github_user_token_4.jpeg

5. Click on "Personal access tokens".

.. image:: graphics/github_user_token_5.jpeg

.. note::
    Currently, we use the classic tokens. Any developer is free to use the new fine-grained tokens, which are in Beta at the time of writing the current documentation, so long as it works. That developer must just modify the documentation accordingly.

6. Click on "Generate new token (classic)".

.. image:: graphics/github_user_token_6.jpeg

.. important::
    The correct selection of the scopes is pertinent to the continued operation of the dependent systems. This may influence one to over-scope the permissions, in order to avoid having to scrutinize the required ones to save time, however over-scoping is a bad practice and should be avoided, so as to avoid any malicious attempts.  See the documentation stating the required scopes from the relevant service.

7. Name your token, set an expiration time-delta, select the appropriate scopes, and finally click "Generate token".

.. image:: graphics/github_user_token_7.jpeg

8. Click on the copy icon provided, next to the token (or copy it yourself).

.. image:: graphics/github_user_token_8.jpeg

.. important::
    It is important to never commit code with the token. If this is done, the token will be deactivated immediately, automatically in most cases by the relevant service. For example, if you commit a Github token to Github, it will be automatically deleted. This is a good safety feature to have, but if done with a token which multiple components in our system are dependent on, the amount of work to rectify this will be tedious and better avoided through taking mental note of this now.

Generating Organization Tokens on GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting Access Tokens
---------------------

Defining Access Tokens on Azure Pipelines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Link found in `Defining Environment Variables`_

Defining Tokens in GitHub Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
