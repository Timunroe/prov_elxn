config = {
    # could reduce db name to just project_name.json
    "project_name": "prov_elxn",
    "db_name": "prov_elxn.json",
    "db_fields_dflt": {
        'desc_user': '',
        'draft_user': 0,  # published
        'rank': 0,
        'rank_time': 0,
        'label_user': '',
        'title_user': '',
        'region_user': ''
    },
    "db_fields": ['asset_id', 'author_api', 'label_api', 'source_api', 'desc_api', 'draft_api', 'link', 'img_api', 'img_api_thumb', 'pubdate_api', 'region_api', 'site_api', 'timestamp', 'title_api'],
    "name": "spec",
    "apis":
        [
            {
                "url": 'http://api.zuza.com/search/article/default?q=KeywordsAlias:"spec_prov_elxn"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5',
                "filter": ["searchResultView"]
            },
            {
                "url": 'http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=hamilton&sort=datedesc&pageSize=30&startindex=1&endindex=30',
                "filter": ["searchResultView"]
            },
            {
                "url": 'http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=niagara&sort=datedesc&pageSize=12&startindex=1&endindex=12',
                "filter": ["searchResultView"]
            },
            {
                "url": 'http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=halton&sort=datedesc&pageSize=8&startindex=1&endindex=8',
                "filter": ["searchResultView"]
            },
    ],
    "munge":
        [
            # ( key, test, regex, action)
            ("author_api", 'contains', "Kevin Werner",
             {
                 'action': 'set_key',
                 'section': 'draft_api',
                 'value': True
             }
             ),
            ("source_api", 'contains', "Examiner",
             {
                 'action': 'set_key',
                 'section': 'draft_api',
                 'value': True
             }
             ),
            ('site_api', 'contains', r'Niagara|Catharines|Grimsby',
             {
                 'action': 'set_key',
                 'section': 'region_api',
                 'value': 'niagara'}
             ),
            ('site_api', 'contains', r'Burlington|Milton|Oakville|Guelph',
             {
                 'action': 'set_key',
                 'section': 'region_api',
                 'value': 'halton'
             }
             )
    ]
}

# http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=niagara&sort=datedesc&pageSize=10&startindex=1&endindex=10
# http://api.zuza.com/search/article/default?&category=news&subcategory=provincial-election&pageIndex=1&location=halton&sort=datedesc&pageSize=10&startindex=1&endindex=10
#####
# municipal election
# http://api.zuza.com/search/article/default?&category=news&subcategory=municipal-election&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
