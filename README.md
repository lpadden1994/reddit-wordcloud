# reddit-wordcloud
This program will create a wordcloud using the post titles on the front page of reddit.


To begin, make sure to import the necessary python libraries into a directory of your choice.

``` cd desktop \n
    mkdir python-projects
    cd python-projects
```

then you will want to import the libraries using pip, pythons package manager.

``` pip install workcloud
    pip install beautifulsoup4
    pip install requests
```


Next off, make a file called reddit_scraper.py inside the directory you just created.

```
    touch reddit_scraper.py
```

Now open this file and import the necessary libraries.

```python
    from bs4 import BeautifulSoup
    import requests
```
    

