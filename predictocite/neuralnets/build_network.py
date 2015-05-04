from pybrain.structure import FeedForwardNetwork, LinearLayer, SigmoidLayer, FullConnection

#init network
network = FeedForwardNetwork()

#construct layers
inLayer = LinearLayer(2, name='frequency_vectors')
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)

#add them to network
network.addInputModule(inLayer)
network.addModule(hiddenLayer)
network.addOutputModule(outLayer)

in__to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)

network.addConnection(in__to_hidden)
network.addConnection(hidden_to_out)

network.sortModules()