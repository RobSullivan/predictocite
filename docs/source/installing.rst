Installing the application
==========================

The application is a wheel file...

Here are the steps to install the application on Windows



Install virtualenv for Python 3.4 [link]
A good guide http://docs.python-guide.org/en/latest/dev/virtualenvs/

Unzip predictocite-flask-0.10 and from the command line cd into predictocite-flask-0.0.1


Create a virtual environment by entering the command `virtualenv .`

This creates a virtual environment to install the application into. Make sure it chooses Python3.4. 
If other versions of Python are installed use -p /path/to/Python3.4 venv

Activate the virtual environment with the command `Scripts\activate`



A note on installing scipy and numpy in a virtualenv on Windows
The quickest way found is to add the .exes also on the CD-ROM to the home directory and run
easy_install numpy.exe
easy_install scipy.exe 
Versions used are scipy==0.14.0 and numpy==1.9.1 (Python3.4)
Installation may be different on other operating systems.

python setup.py install

Then install the dependencies

pip install -r requirements.txt

Because of the number of dependencies this can take a while to download, unpack and install.


Errors on install.

Because of the number of dependencies errors may occur when the install command
downloads and unpacks them.

If any errors occur with individual packages, just pip install <package> to resolve.