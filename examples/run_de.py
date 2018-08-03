# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

import random
import logging
from NiaPy.algorithms.basic import DifferentialEvolutionAlgorithm
from NiaPy.benchmarks.utility import TaskConvPrint, TaskConvPlot

logging.basicConfig()
logger = logging.getLogger('examples')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)

class MyBenchmark(object):
	def __init__(self):
		self.Lower = -5.12
		self.Upper = 5.12

	def function(self):
		def evaluate(D, sol):
			val = 0.0
			for i in range(D): val = val + sol[i] * sol[i]
			return val
		return evaluate

def simple_example(runs=10):
	for i in range(10):
		algo = DifferentialEvolutionAlgorithm(D=10, NP=40, nFES=10000, F=0.5, CR=0.9, seed=i, benchmark=MyBenchmark())
		Best = algo.run()
		logger.info('%s %s' % (Best[0], Best[1]))

def logging_example():
	task = TaskConvPrint(D=50, nFES=50000, nGEN=50000, benchmark=MyBenchmark())
	algo = DifferentialEvolutionAlgorithm(NP=40, F=0.5, CR=0.9, seed=None, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))

def plot_example():
	task = TaskConvPlot(D=50, nFES=50000, nGEN=10000, benchmark=MyBenchmark())
	algo = DifferentialEvolutionAlgorithm(NP=40, F=0.5, CR=0.9, seed=None, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))
	input('Press [enter] to continue')

if __name__ == '__main__':
	if len(sys.argv) <= 1: simple_example(1)
	elif sys.argv[1] == 'plot': plot_example()
	elif sys.argv[1] == 'log': logging_example()
	else: simple_example(10)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
