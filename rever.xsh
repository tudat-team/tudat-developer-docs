$PROJECT = 'Tudat Developer'
$ACTIVITIES = [
              'authors', # authors must have commit before executing Rever, otherwise he/she will be omitted.
              'version_bump',  # Changes the version number in various source files (setup.py, __init__.py, etc)
              'changelog',  # Uses files in the news folder to create a changelog for release
              'tag',  # Creates a tag for the new version number
              'push_tag',  # Pushes the tag up to the $TAG_REMOTE
              'bibtex',  # Pushes the tag up to the $TAG_REMOTE
               # 'pypi',  # Sends the package to pypi
               # 'conda_forge',  # Creates a PR into your package's feedstock
               # 'ghrelease'  # Creates a Github release entry for the new tag
               ]
$VERSION_BUMP_PATTERNS = [  # These note where/how to find the version numbers
                         ('source/conf.py', r'release\s*=.*', "release='$VERSION'")
                         ]

$CHANGELOG_FILENAME = 'CHANGELOG.rst'  # Filename for the changelog
$CHANGELOG_TEMPLATE = 'TEMPLATE.rst'  # Filename for the news template
$CHANGELOG_AUTHORS_TITLE = 'Authors'
$CHANGELOG_AUTHORS_FORMAT = '* {name}\n'
$PUSH_TAG_REMOTE = 'https://github.com/tudat-team/tudat-developer-docs.git'  # Repo to push tags to

$GITHUB_ORG = 'tudat-team'  # Github org for Github releases and conda-forge
$GITHUB_REPO = 'tudat-developer-docs'  # Github repo for Github releases  and conda-forge

# Author related -------------------------------------------------------------#
with open('AUTHORS', 'r') as f:
    lines = f.read().splitlines()
    $BIBTEX_AUTHORS =  [line.strip() for line in lines if line.strip().startswith('*')]

$BIBTEX_PROJECT_NAME = $PROJECT