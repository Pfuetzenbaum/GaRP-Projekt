from setuptools import setup, find_packages

setup(
    name='GaRP',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'py4j',
        'customtkinter',
        'tkinter',
        'tk',
        'pdfminer',
        'pdfminer.six',
        # Füge hier weitere Abhängigkeiten hinzu
    ],
    entry_points={
        'console_scripts': [
            'garp=app.main:main',  # Definiere den Einstiegspunkt
        ]
    },
    package_data={
        # Beinhaltet die JAR-Datei im finalen Paket
        '': ['app/integrations/lib/original-demo-1.0.jar']
    }
)
