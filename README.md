# MixEngine

A website where users can enter a song that they like and be given a playlist generated with songs similar to it. 

## Site Access 
https://mixengine.netlify.app/

*As the site is still in development mode on Spotify it will only work for users who are explicitly given access* 

## Set-up through an IDE 

Run the following commands to set up all dependencies. 

```
pip install -r requirements.txt
```
In order to start the site, both the backend and the frontend need to be running. 

Start by running the backend server with these commands. 

```
cd react-flask
cd flask-server
python main.py
```

Then in another terminal start up the frontend by running. 

```
cd react-flask
cd playlist 
npm run start
```

This will take you to the running site. 

## Site Demo  

Home Page: 
![img/home.png](https://github.com/mkro298/playlistGen/blob/main/img/home.png?raw=true)

Search Function: 
![img/search.png](https://github.com/mkro298/playlistGen/blob/main/img/search.png?raw=true)

Getting Access: 
![img/auth.png](https://github.com/mkro298/playlistGen/blob/main/img/auth.png?raw=true)

Resulting Playlist: 
![img/play.png](https://github.com/mkro298/playlistGen/blob/main/img/play.png?raw=true)
