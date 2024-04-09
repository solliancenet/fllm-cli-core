#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) FoundationaLLM. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from codecs import open
from setuptools import setup, find_packages

VERSION = "1.0.0b6"

# If we have source, validate that our version numbers match
# This should prevent uploading releases with mismatched versions.
try:
    with open('foundationallm/cli/core/__init__.py', 'r', encoding='utf-8') as f:
        content = f.read()
except OSError:
    pass
else:
    import re
    import sys

    m = re.search(r'__version__\s*=\s*[\'"](.+?)[\'"]', content)
    if not m:
        print('Could not find __version__ in foundationallm/cli/core/__init__.py')
        sys.exit(1)
    if m.group(1) != VERSION:
        print('Expected __version__ = "{}"; found "{}"'.format(VERSION, m.group(1)))
        sys.exit(1)

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = [
    'argcomplete~=3.1.1',
    'azure-mgmt-core>=1.2.0,<2',
    'cryptography',
    # On Linux, the distribution (Ubuntu, Debian, etc) and version are logged in telemetry
    'distro; sys_platform == "linux"',
    'humanfriendly~=10.0',
    'jmespath',
    'knack~=0.11.0',
    'msal-extensions~=1.0.0',
    'msal[broker]==1.24.0b2',
    'msrestazure~=0.6.4',
    'packaging>=20.9',
    'paramiko>=2.0.8,<4.0.0',
    'pkginfo>=1.5.0.1',
    # psutil can't install on cygwin: https://github.com/solliancenet/foundationallm/issues/9399
    'psutil~=5.9; sys_platform != "cygwin"',
    'PyJWT>=2.1.0',
    'pyopenssl>=17.1.0',  # https://github.com/pyca/pyopenssl/pull/612
    'requests[socks]'
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()

setup(
    name='fllm-cli-core',
    version=VERSION,
    description='FLLM Command-Line Tools Core Module',
    long_description=README,
    license='MIT',
    author='FoundationalLLM',
    author_email='foundationallm@solliance.net',
    url='https://github.com/solliancenet/fllm-cli',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=DEPENDENCIES,
    python_requires='>=3.8.0',
    package_data={'foundationallm.cli.core': ['auth/landing_pages/*.html']}
)
