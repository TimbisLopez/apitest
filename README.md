# apitest

# install
pip install virtualenv
(dentro de carpeta raiz del proyecto)
virtualenv env 
. env/bin/activate
pip install flask-restful
pip install flask-limiter
pip install flask-sqlalchemy

# use
(dentro de carpeta raiz del proyecto)
. env/bin/activate
python api.py

# test
curl --header "apiKey: 12345678" http://127.0.0.1:5000/v1/


