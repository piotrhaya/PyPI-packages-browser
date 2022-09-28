from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import fetch_packages_data


def start():
    scheduler = BackgroundScheduler(timezone="Europe/Warsaw")
    scheduler.add_job(fetch_packages_data, trigger='cron', hour='12', minute='30')
    scheduler.start()
