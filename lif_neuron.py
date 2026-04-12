import matplotlib.pyplot as plt


#current voltage of neuron = cvn
#threshold voltage of neuron = tvn

#leaky integrate and fire neuron model, or a cell that accumpulates voltage until it reaches a threshold, then it fires and resets
class LIF_Neuron:
    def __init__(self):
        self.resting_volt = -65.0 
        self.volt = self.resting_volt 
        self.tvn = -50.0
        self.reset_volt = -70.0 # after firing, voltage resets to this value
        self.resistance = 10.0
        self.leak_speed = 20.0
        self.cooldown_duration = 2.0
        self.cooldown_timer = 1000.0

        # neuron is born -> timer =1000; 2 =! > 1000 -> process.
        # reset once timer is <= cooldown duration.


    def step(self, i_input):
        #increment cooldown timer
        # if in cooldown, hold at reset voltage
        #else update voltage, checkk for update
        # return whether it fired
      
        self.cooldown_timer += 1.0
        if(self.cooldown_duration >= self.cooldown_timer):
            self.volt = self.reset_volt
            return False # in cooldown
        #fire event
        else:
            dv = (self.resting_volt - self.volt + (self.resistance * i_input))/self.leak_speed
            self.volt += dv
            # if the voltage leaks past threshold, reset and 
            if (self.volt > self.tvn):
                self.volt = self.reset_volt
                self.cooldown_timer = 0
                return True # 
            return False # not in cooldown, volt didn't reach threshold
voltages = []
stepvolt = 1.7
neuron = LIF_Neuron()
for i in range(500):
    neuron.step(stepvolt) #feeding x nA (nano-amps) of current into the neuron
    voltages.append(neuron.volt)
plt.axhline(y=-50.0, color = 'r', linestyle= '-', label = 'threshold')
plt.plot(voltages)
plt.title(f"LIF neuron of {stepvolt} Nano Amps")
plt.legend(loc = 'upper left', bbox_to_anchor = (0, -0.05))
plt.show()

