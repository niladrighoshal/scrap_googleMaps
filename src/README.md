queries = [
    {
        "keyword": "dentist in mumbai",
        "max_results" : 5,
        "min_reviews": 5 ,
        "max_reviews": 100,
        "has_phone": True,



## sort by reviews in descending order

        "sort": {
            "by": "reviews",
            "order": "desc",
        },


## Sort by main_category in ascending order:

        "sort": {
            "by": "main_category",
            "order": "asc",
        },

## Sort by title in ascending order:

        "sort": {
            "by": "title",
            "order": "asc",
        },

## Sort by rating in descending order:

        "sort": {
            "by": "rating",
            "order": "desc",
        },


    },
]


## for low end laptop (2-3), mid range(4-6), hige end laptop(6-10)

number_of_scrapers = 5     



## How to select specific Fields?   

queries = [
    {
        "keyword": "dentists in mumbai",
        "select": ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"],
    },
]


## Standard Field Seection 

        "select": ["title", "link", "main_category", "rating", "reviews",  "website", "phone" , "address"],


## Selection of all fields (Default):

        "select": "ALL",