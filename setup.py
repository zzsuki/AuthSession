import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

PY3 = sys.version_info > (3,)


VERSION = None

CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Topic :: Software Development :: Testing
"""[1:-1]

TEST_REQUIRE = ['pytest', 'coverage', 'flake8'] if PY3 else ['pytest', 'coverage', 'flake8']



with open('README.md') as mdf:
    long_description = mdf.read()


def pip_install(packet_name: str) -> None:
    """
    Install packet

    Args:
        param packet_name (str): Packet name.

    Returns:
        void: None
    """

    os.system(f"{sys.executable} -m pip install {packet_name}")


def read_requirements(path):
    """
    Read requirements

    :param path: path
    """

    requires = []

    with open(path) as fp:
        install_requires = fp.read().split("\n")

        for ir in install_requires:
            if "-r" in ir:
                path = os.path.join(os.path.split(path)[0], ir.split(" ")[1])
                requires.extend(read_requirements(path))
            elif ir and "git" not in ir:
                requires.append(ir)

    return requires


setup(
    name='项目名称',
    version=VERSION,
    description='项目简介',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='zzsuki',
    author_email='zzsuki@163.com',
    maintainer='zzsuki',
    maintainer_email='zzsuki@163.com',
    url='项目git仓库url地址',
    license='MIT',
    keywords='项目关键字，可用于检索，以空格分隔',  # 也可使用
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    packages=['项目package名称'],   # 项目package名称
    install_requires=read_requirements("requirements.txt"),
    include_package_data=True,      # MANIFEST.in
    setup_requires=[
        "setuptools",
    ],
    extras_require={
        'test': TEST_REQUIRE
    }
)