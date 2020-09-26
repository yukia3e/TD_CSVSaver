# me - this DAT
# scriptOp - the OP which is cooking
import csv

filename = parent().par.Fileprefix + 'sequenceData.csv'
startFlgStore = op('startFlgStore')

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.
def onSetupParameters(scriptOp):
	return

# called whenever custom pulse parameter is pushed
def onPulse(par):
	if par.name == 'Init':
		startFlgStore.par.value1 = 1
	return

def onCook(scriptOp):
	#print('start script1')
	if startFlgStore.par.value0 == 1:
		input = scriptOp.inputs[1]
		scriptOp.copy(input)
	
		if startFlgStore.par.value1 == 1:
			header = []
			with open(filename, 'w') as f:
				writer = csv.writer(f, lineterminator='\n')
				for chan in scriptOp.chans():
					header.append(chan.name)
				writer.writerow(header)
				startFlgStore.par.value1 = 0
	
		with open(filename, 'a') as f:
			writer = csv.writer(f, lineterminator='\n')
			
			list = []
			for (count, chan) in enumerate(scriptOp.chans()):
				#for i in range(0, scriptOp.numSamples):
				if count < 4:
					list.append(int(chan[0]))
				else:
					list.append(chan[0])
			writer.writerow(list)
	else:
		startFlgStore.par.value1 = 1
	#print('end script1')
	scriptOp.clear()
	return
