import logging
import sys

from application import app


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


if __name__ == '__main__':
	app.run()
