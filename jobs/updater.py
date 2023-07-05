from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api


def start():
	"""Function to create a background scheduler object and schedule jobs that need to run on interval based"""
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'interval', seconds=10)
	scheduler.start()
