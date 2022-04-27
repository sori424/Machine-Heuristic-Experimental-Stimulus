# Machine-Heuristic-Experimental-Stimulus
This is a repository for experimental stimulus to explore machine heuristic in using recommendation systems. The "Are you aware of what you are watching? Role of machine heuristic in online content recommendations" paper has been accepted on the International Workshop on [Cyber Social Threats (CySoc)](https://cysoc2022.github.io/) at the International Conference on Web and Social Media (ICWSM).


## Setup
* ubuntu 18.04.5 LTS
* python 3.7.6
* flask 1.1.1
* [ngrok](https://ngrok.com/)

## How to run
Run command at folder that has ``app.py``:
```
python app.py
```
Then, if you want to run the experiment at a remote server which allows users to access the experiment anywhere, run command in terminal as below and access through the url it provides:
```
ngrok http 5000
```

If you do not have a remote server, then just run ``app.py`` in your local terminal and access through localhost url ``127.0.0.1:5000``.

## Running example of the stimulus
The whole process of the experiment (korean). The participants experienced a recommendation system which is divided by the type of recommender (machine vs human). Below is the process of human recommendation system.  


<img src="https://user-images.githubusercontent.com/47997074/146498094-4226d626-903e-4af5-9f99-964eb0daddf9.jpg" width="900px" height="500px"/>
