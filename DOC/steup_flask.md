#### How to create python virtual environment  

1. virtualenv --python=python3.8 venv 
2. source venv/bin/activate 
3. deactivate

**Explain** 
1. virtualenv is keyword, --python= python version number virtual environment name.  
2. source activate outside of virtual environment name.
3. deactivate outside of virtual environment name.

### Setup flask 
* Install flask app
`pip install Flask` 

### Run first flask 
* import Flask class  
`from flask import Flask`   
* Create Flask object  
`app = Flask(__name__)`   
* `__name__` is the name of the current Python module.

```   
from  flask import Flask

app = Flask(__name__)

@app.route('/')
def test1():
    return "test1"

if __name__ == '__main__':
    app.run(debug=True)
```