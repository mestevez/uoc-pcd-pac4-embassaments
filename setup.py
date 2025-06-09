from setuptools import setup, find_packages

setup(
    name="uoc-pcd-pac4-embassaments",
    version="0.1.0",
    description="Estudi de les estadistiques de la quantitat d'aigua als embassaments de les Conques internes de Catalunya.",
    author="Marc Estévez Amén",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
)
