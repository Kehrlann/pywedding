__author__ = 'daniel@garnier.wf'

from setuptools import setup, find_packages

setup(
    name="pywedding",
    description='Minimalist wedding website with gift list and two static pages',
    packages=find_packages(),
    include_package_data=True,
    version='0.1',
    long_description=__doc__,
    zip_safe=False,
    author_email='daniel@garnier.wf',
    install_requires=   [   'Flask',
                            'gdata'
                        ],
    license='MIT License',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    )
)