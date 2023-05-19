# Twitter Bot

This site makes a web scraping and search for the team (football team) that you selected to determinate if that team plays today or not

This bot uses "https://www.promiedos.com.ar" to see the matches

## Setup

### 1) Clone repository

```
git clone
```

### 2) Create the python venv

```
python3 -m venv env
```

### 3) Execute the venv

```
source env/bin/activate
```

### 4) Install all dependencies, their are at the "requirements.txt" file

```
pip install -r requirements.txt
```

### 5) Create the .env file.

In .env.example you will find all the variables that will be used for the project, you have to complete some variables and there are others that you have to complete with your data.

```.env
USER=user                                         <- User to excecute cron jobs

CRON_TIME=2 0 * * *                               <- Cronjob timmer

SCRAPING_URL=https://www.promiedos.com.ar         <- Web where we get the data making scraping
SCRAPING_TEAM=BOCA JUNIORS                        <- Team that you want to see if plays today

TWITTER_BEARER=                                   <- Twitter API stuff
TWITTER_API_KEY=                                  <- Twitter API stuff
TWITTER_API_KEY_SECRET=                           <- Twitter API stuff
TWITTER_ACCESS_TOKEN=                             <- Twitter API stuff
TWITTER_ACCESS_TOKEN_SECRET=                      <- Twitter API stuff
```

## Run

Once you have setup the project you can run it in two ways, executing once or with the cronjob

### Execute once

```
python main.py
```

### Execute with cron

When you execute the project with cron it use the timmer defined at the .env file, specifically at the "CRON_TIME" variable so if you want to change the frequency I recommend to use this page: https://crontab.guru/

```
python cron_job.py
```

Remember that this use "crontab", if you want to check what cron jobs are running in your computer try this:

```
crontab -l
```

If you want to kill all the cronjobs you can try this:

```
crontab -r
```
