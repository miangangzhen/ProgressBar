import sys
import datetime

class progressBar(object):
	def __init__(self):
		self.startTimeMarkProgressBar = datetime.datetime.now()
		self.iProgressBar = 0


	def noticeProgressBar(self):

		endTimeMarkProgressBar = datetime.datetime.now()
		deltaTime = endTimeMarkProgressBar - self.startTimeMarkProgressBar
		strUsedTime = deltaTime.total_seconds()
		speed = self.iProgressBar / strUsedTime

		self.iProgressBar += 1

		strToWrite = "\r{0} 个条目已处理，耗时{1:.2f}秒，处理速度{2:.2f}条目/每秒".format(self.iProgressBar, strUsedTime, speed)
		sys.stdout.write(strToWrite)
		sys.stdout.flush()

if __name__ == '__main__':
	
	import time

	myBar = progressBar()
	for i in range(10):

		myBar.noticeProgressBar()

		time.sleep(0.5)