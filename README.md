# Fetch Websites
**Easily Fetch and Store Webpages along with basic metadata**


## How to run
You can either use Docker to run this or setup local python environment and install requirements .

Install the dependencies and devDependencies and start the server.

### Docker
**To fetch webpages**
```sh
cd fetch_webpages
docker build . 
docker run -it -v ${PWD}:/usr/src/app --rm 38e50e0cf07f https://www.facebook.com
```

**To check metadata of fetched website**
```sh
cd fetch_webpages
docker build . 
docker run -it -v ${PWD}:/usr/src/app --rm 38e50e0cf07f --metadata https://www.facebook.com
```

### Local
**Installation**
```sh
cd fetch_webpages
pip install -r requirements.txt
```

**To fetch webpages**
```sh
cd fetch_webpages
python fetch.py https://www.google.com
```

**To check metadata of fetched website**
```sh
cd fetch_webpages
python fetch.py --metadata https://www.google.com
```

### Check fetch_websites.errors.log for any errors encountered

### Further Improvements
To use selenium to load dynamic websites and then fetch assets and html of given websites
