# url-shortener
simple url shortener written in python.

### install

#### dependencies
* python3
* pipenv

```bash
$ git clone https://github.com/girish946/url-shortener
$ cd url-shortener
$ pipenv install
$ python url-short.py
```

### Usage

* Go to `localhost:5000/` from the browser.

* Using curl

```bash
$ curl -F "url=something.com" localhost:5000/shorten
```

