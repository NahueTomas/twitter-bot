from crontab import CronTab
from config import CRON_TIME, USER

def get_cron():
    my_cron = CronTab(user=USER)
    return my_cron

def run_cron_jobs(cron):
    job = cron.new(command="python main.py")
    job.setall(CRON_TIME)
    cron.write()

def remove_cron_jobs(cron):
    cron.remove_all()

if(__name__ == "__main__"):
    cron = get_cron()
    run_cron_jobs(cron)

    for job in cron:
        print(job)
