<div align="center">
<h1>  Google Play Store Apps Dataset Analysis</h>
</div>
Today, 1.85 million different apps are available for users to download. Android users have even more from which to choose, with 2.56 million available through the Google Play Store. These apps have come to play a huge role in the way we live our lives today. Our Objective is to find the Most Popular Category, find the App with largest number of installs , the App with largest size etc.

The Play Store Apps Dataset, taken from Kaggle, is analysed with various Plots and Conclusions. 
The Dataset has data about more than 10,000 apps in the Store.

</br>
Dataset Link : https://www.kaggle.com/lava18/google-play-store-apps
</br>

## Description of App Dataset columns
1. App : The name of the app
2. Category : The category of the app
3. Rating : The rating of the app in the Play Store
4. Reviews : The number of reviews of the app
5. Size : The size of the app
6. Install : The number of installs of the app
7. Type : The type of the app (Free/Paid)
8. The price of the app (0 if it is Free)
9. Content Rating :The appropiate target audience of the app
10. Genres: The genre of the app
11. Last Updated : The date when the app was last updated
12. Current Ver : The current version of the app
13. Android Ver : The minimum Android version required to run the app

## Data Understanding
The dataset used to predict ratings of an application based on other codiions like app size, price , its type etc. This dataset has:
- 10841 samples or rows
- 13 features or columns 
- 1 target column (Rating).

```python
# type of Category
apps_df['Category'].unique()
```

    array(['ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY',
           'BOOKS_AND_REFERENCE', 'BUSINESS', 'COMICS', 'COMMUNICATION',
           'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS', 'FINANCE',
           'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME',
           'LIBRARIES_AND_DEMO', 'LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL',
           'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS', 'TRAVEL_AND_LOCAL',
           'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER',
           'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION',
           '1.9'], dtype=object)
           
 ```python
# type of Type
apps_df['Type'].unique()
```
     array(['Free', 'Paid', nan, '0'], dtype=object)

```python
# type of Content Rating
apps_df['Content Rating'].unique()
```

    array(['Everyone', 'Teen', 'Everyone 10+', 'Mature 17+',
           'Adults only 18+', 'Unrated', nan], dtype=object)

Target:
Rating : Prediction target column [int]

## Type of Machine Learning task : 
It is an regression problem where given a set of features we need to predict ratings obtained by an application on google Playstore.

## Performace Metric
Since it is an classification problem we will use r2 score , rmse and mse


<div align="center">
<i>TECHNOLOGY USED </i><br>
</BR>
<a target="_blank"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="Seaborn"/></a>
<a target="_blank"><img src="https://matplotlib.org/_static/logo2_compressed.svg" alt="cplusplus" width="110"/></a>
<a target="_blank"><img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn"width="110"/></a>
<a target="_blank"> <img height="50" src="https://upload.wikimedia.org/wikipedia/commons/7/7e/Spyder_logo.svg"></a>
<a target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/jupyter/jupyter-ar21.svg"></a>
<a> <img height="50" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/768px-Pandas_logo.svg.png"> </a>
<a>  <img height="50" src="https://seeklogo.com/images/S/scikit-learn-logo-8766D07E2E-seeklogo.com.png"> </a>
  
</div>