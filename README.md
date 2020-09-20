# Pygw2
Python wrapper for Guild Wars 2 api.

## How to use

Basic principle is that every endpoint needing IDs to fetch, allow `0` to `n`
 positional arguments (IDs). But due to API limitation it will be from `0
 ` to `200` as it is the maximum number objects the API will return.
 
This wrapper is structured as follows:
```
api.<CATEGORY>.<ENDPOINT>(<ID(s)>)
```
or
```
api.<CATEGORY>.<SUBCATEGORY>.<ENDPOINT>(<ID(s)>)
```

Categories and endpoints somewhat match the Guild Wars 2 Wiki documentation
 of the API.
 
For example:
You can access the items-endpoint from items-category:
```
api.items.get()
```
or you can access skins-endpoint from the items-category aswell:
```
api.items.skins()
```

The whole stucture will be documented later.

### Example
```python
from pygw2.api import api

# Get one achievement by ID
achievement = api.achievements.get(1)

# Get all achievement IDs
all_achievement_ids = api.achievements.get()

# Get multiple items
some_items = api.items.get(6542, 6, 24)

# Setup API key
api.setup(api_key="YOUR API KEY HERE")
```

From the setup -function, the API key will be forwarded for 'deeper' API
 classes and functions.
 
 
## Missing endpoint
If you find that there is one or more endpoints not covered by this API
 wrapper and the endpoints would provide some useful information, please
  create an Issue and I will take care of it or if you want to, you could do
   it yourself, but be sure to follow the same structure.
   
   
## API coverage
TODO come up with a nice table or something.




