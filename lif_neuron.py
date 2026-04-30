import matplotlib.pyplot as plt
import matplotlib.animation as ani
from matplotlib.widgets import Button 


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
        self.fired = False

        # neuron is born -> timer =1000; 2 =! > 1000 -> process.
        # reset once timer is <= cooldown duration.


    def step(self, i_input):
        #increment cooldown timer
        # if in cooldown, hold at reset voltage
        #else update voltage, checkk for update
        # return whether it fired
      
        self.cooldown_timer += 1.0
        if(self.cooldown_duration >= self.cooldown_timer): # if in cooldown
            self.volt = self.reset_volt
            self.fired =  False # previously return False
            return self.fired
        
        #fire event
        else:
            dv = (self.resting_volt - self.volt + (self.resistance * i_input))/self.leak_speed
            self.volt += dv
            # if the voltage leaks past threshold, reset and 
            if (self.volt > self.tvn):
                self.volt = self.reset_volt
                self.cooldown_timer = 0
                self.fired = True 
                return self.fired
             
            self.fired = False #no spike, not in cooldown, volt didn't reach threshold
            return self.fired # log parameter

class Synapse:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    def transmit(self):
        if self.source.fired: 
            return self.weight
        return 0

voltages_a = []
voltages_b = []

stepvolt = 1.7
weight = 5
neuron_a = LIF_Neuron()
neuron_b = LIF_Neuron()

synapse = Synapse(neuron_a, neuron_b, weight)
plt.ion()  # interactive mode on

running = True
# stop button
def stop(event):
    global running 
    running = False
fig, ax = plt.subplots()
button_ax = plt.axes([0.8, 0.01, 0.15, 0.05])  # [left, bottom, width, height]
btn = Button(button_ax, 'Stop')
btn.on_clicked(stop)


while running: 

    neuron_a.step(stepvolt) #feeding x nA (nano-amps) of current into the neuron
    step_synapse = synapse.transmit()
    neuron_b.step(step_synapse)
    voltages_a.append(neuron_a.volt)
    voltages_b.append(neuron_b.volt)

    ax.clear()
    ax.axhline(y=-50.0, color = 'r', linestyle= '-', label = 'threshold')
    ax.plot(voltages_a[-500:], label = 'neuron_a')
    ax.plot(voltages_b[-500:], label = 'neuron_b')
    ax.set_title(f"LIF neuron of {stepvolt} Nano Amps")
    ax.legend(loc = 'upper left', bbox_to_anchor = (0, -0.05))
    plt.pause(0.01)

plt.ioff()
plt.show()

