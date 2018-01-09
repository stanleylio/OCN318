import requests,time,traceback
from twisted.internet.task import LoopingCall
from twisted.internet import reactor


ep = 'http://grogdata.soest.hawaii.edu/poh/data/dashboard.json'

TIMEOUT = 3600

# node,variable,unit,range

def get_state():
    r = requests.get(ep)

    state = {}

    if 200 == r.status_code:
        r = r.json()
        nodes = r['nodes']
        for node in sorted(nodes.keys()):
            latest = nodes[node]['latest_non_null']

            # when is a node considered "online"?
            #   1. all readings are fresh
            #   2. any reading is fresh
            # using 2.
            #
            # all fresh reading:
            #goodtime = max([time.time() - latest[var][0] for var in latest.keys()]) <= TIMEOUT
            # any fresh reading:
            goodtime = min([time.time() - latest[var][0] for var in latest.keys()]) <= TIMEOUT
            # ... but wait. kph nodes have both seafet messages and dongle messages, and I only
            # care about the seafet messages. After all, if seafet messages managed to get
            # through, both the sensor and the dongle are online.
            # So need some kind of hierarchy with per-node overriding policy... man this is
            # complicated. An "is_node_online(node)" function that inherits some global policy
            # when per-node policy is not defined?
            # What does XMPP's presence detection say?

            # Is the node online?
            if not goodtime:
                # all readings are stale -> node offline
                state[node] = 'offline'
                continue

            # At least one reading is fresh. Check, per variable, for
            #   1. Range (if defined)
            #   2. Freshness
            def withinbound(v,bound):
                bound = [float('nan') if b is None else b for b in bound]
                return not (v < bound[0] or v > bound[1])
            def isgoodtime(t):
                return time.time() - t < TIMEOUT
            goodread = all([withinbound(latest[var][1],latest[var][3]) and isgoodtime(latest[var][0]) for var in latest.keys()])
            if not goodread:
                state[node] = 'bad_sensor'
                continue

            # All readings are fresh and within bound
            state[node] = 'online'
                
    return state


if '__main__' == __name__:
    import time
    from bar import Bar

    # - - - - -
    # HERE, uncomment these two lines to see magic.
    # Currently it returns one of these for each node: {'online','bad_sensor','offline'}
    # so just check for those.
    #print get_state()
    #exit()
    # - - - - -

    brightness = 0.03

    with Bar(8,'COM41') as bar:
        def f():
            try:
                state = get_state()
                print '- - - - -'
                for k,node in enumerate(sorted(state.keys(),reverse=True),1):
                    print node,state[node]

                    #bar.wink(k,duration=0.1)
                    
                    if 'online' == state[node]:
                        bar.set_bit(k,color=[0,brightness,0])
                    elif 'bad_sensor' == state[node]:
                        bar.set_bit(k,color=[brightness,brightness,0])
                    elif 'offline' == state[node]:
                        bar.set_bit(k,color=[brightness,0,0])
                #for i in range(60):
                    #time.sleep(1)
            except:
                traceback.print_exc()

        LoopingCall(f).start(60)
        reactor.run()

        for k in range(8):
            bar.clear_bit(k+1)
