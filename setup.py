import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

PY3 = sys.version_info > (3,)


VERSION = '0.0.1'

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
    name='AuthSession',
    version=VERSION,
    description='用于处理鉴权的session，只适用于特殊情况，没有特殊需求的话还是推荐使用requests自带的auth模块',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='zzsuki',
    author_email='zzsuki@163.com',
    maintainer='zzsuki',
    maintainer_email='zzsuki@163.com',
    url='https://github.com/zzsuki/AuthSession.git',
    license='MIT',
    keywords='Session Auth token',  # 也可使用列表的方式
    platforms='any',
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    packages=['AuthSession'],   # 项目package名称
    install_requires=read_requirements("requirements.txt"),
    include_package_data=True,      # MANIFEST.in
    setup_requires=[
        "setuptools",
    ],
    extras_require={
        'test': TEST_REQUIRE
    }
)