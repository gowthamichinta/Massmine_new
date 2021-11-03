# Massmine-For-The-Masses

Massmine-For-The-Masses is an open-source, proof of concept tool. It extends the functionality of Massmine, a command-line interface which is a data gathering tool. This Massmine-For-The-Masses has a graphical user interface which allows users to see the data being collected from different platforms like Twitter, Tumblr. The collected data will also be presented in a simple user interface to allow for basic analysis. This project is an improvement of the existing project(https://github.com/AnushaVanama/Massmine-for-the-Masses) where all web pages are redisigned  and rearranged to enhance the user experience and offer smooth navigation throughout its design.

## Run with Docker
### MacOS - Running for the first time:
1) Install Docker Desktop by following the instructions at https://docs.docker.com/desktop/mac/install/
2) Once the Docker Desktop app is running, click "Skip Tutorial" to navigate to main dashboard
3) On your computer's desktop, right-click anywhere and select "New Folder" and name it `massmine-webapp `
4) Right click on the icon of the folder you just created and select `New Terminal at Folder`
5) In the terminal window paste the following command, and then press enter: `touch db.sqlite3`
6) In the terminal window paste the following command, and then press enter:   
`docker run -d -p 8000:8000 -w/app --mount type=bind,source="$(pwd)"/db.sqlite3,target=/app/webapp/db.sqlite3 andykawabata/massmine`
7) Allow 1-2 minutes for container to start, then open you web browser and type `localhost:8000` into your search bar. This could take longer depending on your internet speed.
8) To stop the webapp, go to the Docker Desktop app, Click "Containers/Apps" in the sidebar. Hover over the row with your running container and click the Stop icon near the right.

### MacOS - Running after inital installation:
1) Open Docker Desktop app
2) Click "Containers/Apps" in the sidebar.
3) Hover over the row with your container and click the 'Play' icon near the right. (If yo do not see your container listed, repeat steps 4 and 6 from the section above)
4) Allow 30 seconds for container to start, then open you web browser and type `localhost:8000` into your search bar.

<br>
<br>

    


### Team Members
#### 1. Sadhana Thummalapenta
#### 2. Gowthami Chinta



```python

```


```python

```
