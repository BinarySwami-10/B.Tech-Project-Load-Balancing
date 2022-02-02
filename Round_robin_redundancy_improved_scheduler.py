import random


class Node:

	def __init__(self, id):
		self.id = id  # set the given id as initialization number passed
		self.state = 'working'  # node works by default
		print(f"INFO: node with ID={self.id} is created")

	def get_status(self):
		if self.state == 'working':
			return 'working'  # everything is fine
		else:
			return 'dead'

	def process_data(self, data):  # this function just adds the given numbers
		print(f'LOG: NODE_ID={self.id} is processing', data)

		if self.state == "dead":  # attempt repair if dead
			self.state = 'working'  # 100% repair chance is enforced
			print(f'NODE_ID={self.id} has been repaired')

		if random.random() < FAILURE_CHANCE:
			print(f'ERROR:NODE_ID={self.id} has DIED')
			self.state = 'dead'
			return False
		else:
			result = sum(data)  # store and return result
			print(f'{"LOG:":5}NODE_ID={self.id} result', result)
			return result


def robin_scheduler(NODE_ARRAY, data):
	global ROBIN_COUNTER
	# XNODE it is the current node which the robin will dispatch work to
	XNODE = NODE_ARRAY[ROBIN_COUNTER % NODE_ARRAY_LENGTH]
	result = XNODE.process_data(data)  # try processing the data
	ROBIN_COUNTER += 1  # increment counter so that next node will be used
	if XNODE.state == 'dead' or result is False:
		print(f'INFO: Passing load={data} of NODE_ID={XNODE.id} to next node')
		robin_scheduler(NODE_ARRAY, data)  # using recursion to repeat scheduling if node fails
	return result


NODE1 = Node(1)  # nodes will be initiated according to ids
NODE2 = Node(2)
NODE3 = Node(3)
NODE4 = Node(4)

FAILURE_CHANCE = 0.25  # this is failure rate of node, ie node will not process this

NODE_ARRAY = [NODE1, NODE2, NODE3, NODE4]
NODE_ARRAY_LENGTH = len(NODE_ARRAY)

SAMPLE_DATA = [
    [random.randint(0, 100) for x in range(4)] for y in range(4)
    ]  # SAMPLE_DATA is a 2D[4x4] matrix generate random numbers from 0 to 99
print("SAMPLE_DATA =", SAMPLE_DATA)

ROBIN_COUNTER = 0

if __name__ == '__main__':
	for data in SAMPLE_DATA:
		robin_scheduler(NODE_ARRAY, data)
