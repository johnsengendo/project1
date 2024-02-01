from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.log import setLogLevel

class LinearTopology(Topo):
    def __init__(self):
        Topo.__init__(self)

        # Add nodes
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')

        # Add links
        self.addLink(host1, switch1)
        self.addLink(switch1, switch2)
        self.addLink(switch2, host2)

def create_linear_topology():
    # Create an instance of the linear topology
    topo = LinearTopology()

    # Start the Mininet network using the created topology
    net = Mininet(topo)

    # Start the network
    net.start()
        # Open the Mininet command line interface for h1 and h2
    h1, h2 = net.get('h1', 'h2')
    h1.cmd('xterm -title h1 &')
    h2.cmd('xterm -title h2 &')

    # Open the Mininet command line interface
    CLI(net)

    # Stop the network once the CLI is closed
    net.stop()

if __name__ == '__main__':
    # Set the log level to info to avoid excessive output
    setLogLevel('info')

    # Create the linear topology and start the Mininet network
    create_linear_topology()
