# url-shortener
simple url shortener written in python.
It used redis to store the shortened urls. You can check out the live demo
of this url-shortener at [sh.girishjoshi](https://sh.girishjoshi.io/)

    url data expires in a day at sh.girishjoshi.io

### install

#### dependencies
* python 3
* redis
* pipenv


```bash
$ git clone https://github.com/girish946/url-shortener
$ cd url-shortener
$ pipenv --python 3
$ pipenv install
$ # start the redis server 
$ python url-short.py
```

### Usage

* Go to `localhost:5000/` from the browser.

* Using curl

```bash
$ curl -F "url=something.com" localhost:5000/shorten
```

### TODO

* Create config file for string size of token.
* Handle get requests for `/shorten`.

