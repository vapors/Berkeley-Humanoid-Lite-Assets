"""Installation script for the 'berkeley_humanoid_lite_assets' python package."""

from setuptools import setup

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    # NOTE: Add dependencies
    "psutil",
]

# Installation operation
setup(
    name="berkeley_humanoid_lite_assets",
    packages=["berkeley_humanoid_lite_assets"],
    author="Berkeley Humanoid Project Developers",
    maintainer="Berkeley Humanoid Project Developers",
    url="https://github.com/hybridrobotics/berkeley-humanoid-lite-assets",
    version="2025.03.17",
    description="Description files for Berkeley Humanoid Lite",
    keywords=["extension", "isaaclab"],
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.10",
        "Isaac Sim :: 4.5.0",
    ],
    zip_safe=False,
)
