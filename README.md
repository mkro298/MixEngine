# playlistGen

scope: website where users can enter a song that they like, then log into their spotify and be given a playlist generated based on it 

components needed: 
    - spotify API to build playlist
    - ML to extract songs based on theme 

tools: 
    - front end: react 
    - back-end: python
    - databases: SQL, AWS 

project timeline (deadline: July 31):
    - June 20 to June 25: scoping + researching 
    - June 26 to July 11: ML aspect 
    - July 12 - July 19: spotify API + rough front end 
    - July 20 - July 25: front end polish 
    - July 26 - July 31: polish + deploy/host 

initial thoughts: 
    - feed prompt through openAI to get certain songs then use ML to get recs based off those songs 


dataset: https://www.kaggle.com/datasets/amitanshjoshi/spotify-1million-tracks

references: https://medium.com/web-mining-is688-spring-2021/content-based-movie-recommendation-system-72f122641eab
https://medium.com/geekculture/creating-content-based-movie-recommender-with-python-7f7d1b739c63