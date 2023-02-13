
.. _Managing Access Tokens:

Introduction
############

This document provides an overview of the process for generating and
maintaining access tokens for Azure and GitHub. The purpose of the
document is to provide developers and users with the information they
need to efficiently and effectively manage their access tokens. The
document is intended for individuals who may not have a background in
software engineering, and provides clear and concise instructions for
generating and updating tokens, along with relevant links and references.

.. note::
    Before proceeding, it is recommended that the reader be familiar with
    interacting with environment variables on their operating system
    (Linux, MacOS, or Windows) and have a general understanding of the
    importance of defining the permission scope of tokens for safety and
    the requirements of the relevant interface.

In the following sections, we will cover the following topics:

- Concepts: An overview of important concepts that the reader should be
  familiar with before proceeding with the rest of the document.

- Generating Access Tokens: A guide to generating access tokens on Azure
  and GitHub.

- Maintaining Access Tokens: Information on the importance of maintaining
  access tokens and how to update tokens on Azure and GitHub.

- Conclusion: A summary of the information covered in the document and
  final thoughts and recommendations.

- References: A list of references used in the document.


Concepts
#########

This section provides an overview of important concepts that the reader
should be familiar with before proceeding with the rest of the document.

- API: An application programming interface (API) is a set of protocols, routines, and tools for building software and applications.
- Access token: An access token is a string that provides temporary, secure access to an API.
- Authentication: Authentication is the process of verifying a user's identity.
- Authorization: Authorization is the process of granting or denying access to resources based on the user's identity and permissions.
- Azure: Microsoft Azure is a cloud computing platform and infrastructure created by Microsoft for building, deploying, and managing applications and services through a global network of Microsoft-managed data centers.
- GitHub: GitHub is a web-based hosting service for version control repositories that use the Git version control system.

Problem Statement and Scope
##########################

Maintaining code can be difficult, especially for individuals who are
not familiar with software engineering concepts and tools. This document
addresses the difficulties in maintaining code and focuses on the scope
of access tokens (personal and organization-based) and their importance.
The document informs the audience of relevant concepts and the importance
of keeping these tokens private, and details the process of setting these
tokens for individuals and organizations on Azure and GitHub.

Generating Access Tokens
########################

In this section, we will provide step-by-step instructions for generating access tokens on Azure and GitHub.

Generating Tokens on Azure
^^^^^^^^^^^^^^^^^^^^^^^^^

`<TODO>`

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
    The correct selection of the scopes is pertinent to the continued operation of the dependent systems. This may influence one to over-scope the permissions, in order to avoid having to scrutinize the required ones to save time, however over-scoping is a bad practice and should be avoided, so as to avoid any malicious attempts.  See the documentation stating the required scopes from this service.

7. Name your token, set an expiration time-delta, select the appropriate scopes, and finally click "Generate token".

.. image:: graphics/github_user_token_7.jpeg

8. Click on the copy icon provided, next to the token (or copy it yourself).

.. image:: graphics/github_user_token_8.jpeg

.. important::
    It is important to never commit code with the token. If this is done, the token will be deactivated immediately, automatically in most cases by the relevant service. For example, if you commit a Github token to Github, it will be automatically deleted. This is a good safety feature to have, but if done with a token which multiple components in our system are dependent on, the amount of work to rectify this will be tedious and better avoided through taking mental note of this now.

Generating Organization Tokens on GitHub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`<TODO>`
