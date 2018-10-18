#!/usr/bin/python
# The goal of this scrupt is to define the topology to develop the second
# approach of
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
from functools import partial
from mininet.node import OVSSwitch


class Approach2Topo(Topo):

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)
    # Hosts and switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')

# Wire h1 and h2 to s1
        self.addLink(h1, s1)
        self.addLink(h2, s1)
# Wire h3, h4 and h5 to s2
        self.addLink(h3, s2)
        self.addLink(h4, s2)
        self.addLink(h5, s2)
# Wire h6 and h7 to s3
        self.addLink(h6, s3)
        self.addLink(h7, s3)
    # Wire switches
        self.addLink(s4, s1)
        self.addLink(s4, s2)
        self.addLink(s4, s3)


def setup():
    topo = Approach2Topo()
# We use Open vSwitch and OpenFlow 1.3
    switch = partial(OVSSwitch, protocols='OpenFlow13', datapath='user')
# controller
    net = Mininet(topo, controller=RemoteController,
                  switch=switch, cleanup=True)
# Setting up hosts
    net['h1'].setIP('10.0.1.1/24')
    net['h1'].setMAC('00:00:00:00:01:01')
    net['h1'].cmd('route add default gw 10.0.1.100')

    net['h2'].setIP('10.0.1.2/24')
    net['h2'].setMAC('00:00:00:00:01:02')
    net['h2'].cmd('route add default gw 10.0.1.100')

    net['h3'].setIP('10.0.2.3/24')
    net['h3'].setMAC('00:00:00:00:02:03')
    net['h3'].cmd('route add default gw 10.0.2.100')

    net['h4'].setIP('10.0.2.4/24')
    net['h4'].setMAC('00:00:00:00:02:04')
    net['h4'].cmd('route add default gw 10.0.2.100')

    net['h5'].setIP('10.0.2.5/24')
    net['h5'].setMAC('00:00:00:00:02:05')
    net['h5'].cmd('route add default gw 10.0.2.100')

    net['h6'].setIP('10.0.3.6/24')
    net['h6'].setMAC('00:00:00:00:03:06')
    net['h6'].cmd('route add default gw 10.0.3.100')

    net['h7'].setIP('10.0.3.7/24')
    net['h7'].setMAC('00:00:00:00:03:07')
    net['h7'].cmd('route add default gw 10.0.3.100')
# Setting up routers
    net['s1'].cmd('ifconfig s1-eth3 hw ether 00:00:00:11:11:11')
    net['s2'].cmd('ifconfig s2-eth4 hw ether 00:00:00:22:22:22')
    net['s3'].cmd('ifconfig s3-eth3 hw ether 00:00:00:33:33:33')
    net['s4'].cmd('ifconfig s4-eth1 hw ether 00:00:00:44:44:01')
    net['s4'].cmd('ifconfig s4-eth3 hw ether 00:00:00:44:44:03')

    net.start()
    CLI(net)
    net.stop


if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    setup()
