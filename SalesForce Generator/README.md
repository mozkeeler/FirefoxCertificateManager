## Generator Script ##

Given a file describing the CA certificates in Mozilla's CA program, Generates a JSON file for use by the extension.

#### Howto:
* Install [https://www.python.org/downloads/release/python-2710/ Python 2.7]
* Save the new [https://mozillacaprogram.secure.force.com/CA/IncludedCACertificateReportCSVFormat included CA certificate report] as `BuiltInCAs.csv` in this folder
* On Windows, navigate to this folder and run `generate.sh` by double clicking 
* On other platforms, use a terminal to navigate to this folder and run `python generator.py`
* Copy the resulting `SalesForceData.js` file generated in this folder into the `../addon/lib` folder (overwritting the old one)
