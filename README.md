setup local env
```shell
while read ver; do pyenv install --skip-existing "$ver"; done < .python-version
pyenv local 2.7.18
python2.7 -m virtualenv .virtualenv/py27
source .virtualenv/py27/bin/activate
pip install -r requirements.txt
```


run tests
```shell
pytest tests/test_schema.py 
pytest tests/test_schema_future.py 
```
