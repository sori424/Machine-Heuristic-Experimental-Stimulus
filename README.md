# Machine-Heuristic-Experimental-Stimulus
This is a repository for experimental stimulus for the paper ["Are you aware of what you are watching? Role of machine heuristic in online content recommendations"](http://workshop-proceedings.icwsm.org/pdf/2022_66.pdf) on the International Workshop on [Cyber Social Threats (CySoc)](https://cysoc2022.github.io/) at the International Conference on Web and Social Media (ICWSM).


## Setup
* python 3.7.6
* flask 1.1.1

## How to run
Run command at folder that has ``app.py``:
```
python app.py
```
You can access webpage through local machine.


## Run with remote server
If you want to run the experiment at a remote server which allows users to access the experiment anywhere, please download [ngrok](https://ngrok.com/) in your server and run command below in an another terminal which will give you the url to access from anywhere. (Port number can be changed at your convenience by editing ``app.py`` script)  

```
ngrok http 5000
```


## Running example of the stimulus
The whole process of the experiment (korean). The participants experienced a recommendation system which is divided by the type of recommender (machine vs human). Below is the process of machine recommendation system.  
* (caution) Some videos contain offensive contents. And some videos of the list might be deleted by YouTube which cannot be accessible. 

<img src="https://user-images.githubusercontent.com/47997074/165882131-f98e685b-3680-4250-b037-4fb12225ccf7.png" width="900px" height="500px"/>
<img src="https://user-images.githubusercontent.com/47997074/165882217-e4e48e6f-1bdf-414a-9c83-f13f4b22df54.png" width="900px" height="500px"/>
