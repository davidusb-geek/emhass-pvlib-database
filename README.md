# Modules and inverters PVLib database for EMHASS

EHMASS is a Python module designed to optimize your home energy interfacing with Home Assistant.

You can find the code to this Python package here: [https://github.com/davidusb-geek/emhass](https://github.com/davidusb-geek/emhass)

In EMHASS we can use weather forecasts to then compute solar PV expected power production. To do this we use the great package **PVLib** [https://pvlib-python.readthedocs.io/en/stable/](https://pvlib-python.readthedocs.io/en/stable/). However the default database for PV modules and inverters is outdated. This webapp aims at help people find the proper models names for their application on an updated database from the **NREL SAM** simulation program [https://github.com/NREL/SAM/tree/develop/deploy/libraries](https://github.com/NREL/SAM/tree/develop/deploy/libraries)