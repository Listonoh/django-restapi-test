This app views data from https://faktury.mzcr.cz/rest/organizations/ with 5 organizations per page.

simple result of rest api call:
``` JSON
[
    {
        "id_organization": 1,
        "name": "Ministerstvo zdravotnictví",
        "description": "",
        "url": "",
        "created_at": "2019-10-08 13:40:27",
        "last_modified_at": "2020-08-10 08:58:37",
        "rozpoctova_skladba": 1,
        "ico": "00024341"
    },
    {
        "id_organization": 3,
        "name": "Hygienická stanice hlavního města Prahy",
        "description": "",
        "url": "http://www.hygpraha.cz/",
        "created_at": "2020-01-03 11:49:23",
        "last_modified_at": "2020-08-10 09:01:16",
        "rozpoctova_skladba": 1,
        "ico": "71009256"
    }
]
```

The site views name, ico, description and url for every site it got.

For performance it get only the pages it needs from rest api (so in this case only 5).
With the result comes how many pages it has, so it is easy to calculate the number of pages and current page to display it properly on paginator.