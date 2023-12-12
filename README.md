# rastree2

Sistema de Gestión para Activos Móviles.
-----------------------------------------

Autor: Jorge Alonso Toro Hoyos [jolthgs@gmail.com, jolth@esdebian.org]

## Virtual Environments

```
pip2 install virtualenv
# create a python virtual environment
virtualenv venvpy2.7
# activate
source venvpy2.7/bin/activate
# install dependencies
pip2 install -r requirements.txt
```

## Dependencies
Another option that seems to provide a newer version of `psycopg2` than the one 
in the `python3-psycopg2` package (at least when I wrote this):

```
sudo apt install pip3
sudo apt install libpq-dev
sudo pip3 install psycopg2
```
