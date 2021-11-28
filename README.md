# Massmine-For-The-Masses

Massmine-For-The-Masses is an open-source, proof of concept tool. It extends the functionality of Massmine, a command-line interface which is a data gathering tool. This Massmine-For-The-Masses has a graphical user interface which allows users to see the data being collected from different platforms like Twitter, Tumblr. The collected data will also be presented in a simple user interface to allow for basic analysis. This project is an improvement of the existing project(https://github.com/AnushaVanama/Massmine-for-the-Masses) where all web pages are redesigned  and rearranged to enhance the user experience and offer smooth navigation throughout its design.
<br>
## Run with Docker
### MacOS:
1) Install Docker Desktop by following the instructions at https://docs.docker.com/desktop/mac/install/ (you will need to create an account)
2) Once the Docker Desktop app is running, click "Skip Tutorial" to navigate to main dashboard (if applicable)
3) Go to the following url and click DOWNLOAD ALL in the upper right hand corner. Save the zip file to your desktop and unzip it.
https://drive.google.com/drive/folders/1ngUce_muJ2QPnB72f0Z0HKFTm45cSBFS

4) Go to your desktop. Right click on the icon of the folder you just downloaded and select: `New Terminal at Folder`
5) In the Terminal window paste the following command, and then press enter: `docker compose up -d`


6) Allow 1-2 minutes for container to start, then open you web browser and type `localhost:8000` into your search bar. This could take longer depending on your internet speed.

    #### To Stop or Restart the App:
    Open the Docker Desktop app, Click "Containers/Apps" in the sidebar. Hover over the row with your running container and either click the "Play" or "Stop" icon near the right
    
<br>

### Windows 10 and 11:
1) Install Docker Desktop by following the instructions at this link. Make sure your system meets the requirements. You will need to create an account. https://docs.docker.com/desktop/windows/install/ 
    - if having trouble, refer to this YouTube tutorial: https://www.youtube.com/watch?v=_9AWYlt86B8
2) Once the Docker Desktop app is running, navigate to main dashboard
3) Go to the following url and click DOWNLOAD ALL in the upper right hand corner. Save the zip file to your desktop and unzip it.
https://drive.google.com/drive/folders/1ngUce_muJ2QPnB72f0Z0HKFTm45cSBFS
4) Go to your desktop. While holding down Shift, Right click on the icon of the folder you just downloaded and select: `Open command window here`
5) In the Command window paste the following command, and then press enter: `docker compose up -d`

    (be sure the Docker Desktop app is open at this point)

6) Allow 1-2 minutes for container to start, then open you web browser and type `localhost:8000` into your search bar. This could take longer depending on your internet speed.

    #### To Stop or Restart the App:
    Open the Docker Desktop app, Click "Containers/Apps" in the sidebar. Hover over the row with your running container and either click the "Play" or "Stop" icon near the right

<br>

### Linux

1) Install Docker Engine for your distribution by following these instructions https://docs.docker.com/engine/install/#server

2) Go to the following url and click DOWNLOAD ALL in the upper right hand corner. Save the zip and unzip it.
https://drive.google.com/drive/folders/1ngUce_muJ2QPnB72f0Z0HKFTm45cSBFS

3) Open a terminal window and navigate to within the folder you just downloaded.

4) Type the following command, and then press enter: `docker compose up -d`


5) Allow 1-2 minutes for container to start, then open you web browser and type `localhost:8000` into your search bar. This could take longer depending on your internet speed.

    #### To Stop or Restart the App:
    to stop the container run `docker kill $(docker ps -a -q)`  
    to start it again run `docker start $(docker ps -a -q)`


    
<br>
<br>
<br>

## Developer Guidelines (for helping maintain Docker image)
- If you add a new python dependency, be sure it is entered into the Pipfile
- If you add a system-wide dependency, be sure to notify the person who maintains the docker image, so they can add it to the Dockerfile

## Instructions for Maintaining Docker Image
### Initial Steps
- Create a Dockerhub account if you do not already have one
- Contact Andy Kawabata (andykawabata@gmail.com) so you can be added as a collaborator on Dockerhub
### Building the Image
- Pull latest commit from this GitHub repository
- To build the image, run  `docker build -t andykawabata/massmine .`  
if you are using an M1 Mac, instead run `docker buildx build --platform linux/amd64 -t amdbuild .`
### Get the docker-compose file
- Download the folder with the docker-compose file and unzip it. Be sure to click "Download All" to download the whole folder. https://drive.google.com/drive/folders/1ngUce_muJ2QPnB72f0Z0HKFTm45cSBFS
### Test the image by running the docker-compose file
- Open a new terminal window and navigate to inside the folder containing the docker-compose.yml file.
- Run `docker-compose up` to run the container in interactive mode
### Push to Dockerhub
- Make sure you are added as a collaborator on Dockerhub for the repo andykawabata/massmine
- run `docker push andykawabata/massmine` to push the new image to Dockerhub


### Team Members
#### 1. Sadhana Thummalapenta
#### 2. Gowthami Chinta
#### 3. Andy Kawabata


```python

```


```python

```
