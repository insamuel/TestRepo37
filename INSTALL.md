
## Installing XYZ

This document gives the instructions to install a XYZ with all dependencies required. 


### All systems (Linux, Mac OS X, and Windows)


1. [Download Miniconda 64-bit for Python 2.7 corresponding to your OS](http://conda.pydata.org/miniconda.html).

    You can also download the Miniconda installer from a terminal:

    ```
    wget http://repo.continuum.io/miniconda/Miniconda-3.7.0-Linux-x86_64.sh
    ```

2. Open a terminal in the directory where you downloaded Miniconda, and type the following command (the filename might be slightly different in your case). This will install Miniconda in your user account.

    ```
    sh Miniconda-3.7.0-Linux-x86_64.sh
    ```

    On Windows, you'll have to double-click on the `.exe` Miniconda installer.

    You'll be requested to answer a few questions.

    * Press `Enter` to review the license.
    * Press `Space` several times to scroll through the license.
    * Type `yes` and press `Enter`.
    * You'll be requested to choose the installation path. You can accept the default (`~/miniconda`), so just type `Enter`.
    * At the end of the installation, you'll be requested to choose whether this Python distribution should be the default one on your account. You can type `yes` and press `Enter`.
    * Congratulations! Miniconda is now installed.

3. You may need to open a new terminal so that the `conda` command-line tool is available.

4......


## Advanced details

### Dependencies

The following libraries are required:

  * Python 2.7
  * NumPy 1.8 
  * Pandas = 0.12
  * matplotlib
