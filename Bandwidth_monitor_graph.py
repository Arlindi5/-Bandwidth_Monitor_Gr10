import time
import matplotlib.pyplot as plt
import threading
import subprocess

from Tracker import Tracker
from datetime import datetime

# Data shown on the plot represents the last 5 minutes
DATA_DURATION = 5
# The data variable
speeds_recv = []
speeds_sent = []
times = []
