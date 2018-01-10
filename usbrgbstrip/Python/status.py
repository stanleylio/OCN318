import requests, time, traceback
from datetime import datetime


ep = 'https://grogdata.soest.hawaii.edu/poh/data/dashboard.json'

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
    from strip import Strip

    # - - - - -
    # uncomment these two lines to look under the hood.
    #print(get_state())
    #exit()
    # Currently it returns one of these for each node: {'online','bad_sensor','offline'}
    # so just check for those.
    # - - - - -

    LENGTH = 8
    PORT = 'COM10'

    BRIGHTNESS = 0.03

    with Strip(LENGTH,PORT) as strip:
        while True:
            try:
                state = get_state()
                for k in range(LENGTH):
                    strip.clear_bit(k)
                print('- - - - -')
                print(datetime.now())
                nodes = sorted(state.keys())
                nodes = nodes[:LENGTH]
#                nodes = reversed(nodes)
                for k,node in enumerate(nodes):
                    print(node,state[node])
                   
                    if 'online' == state[node]:
                        strip.set_bit(k,color=[0,BRIGHTNESS,0])
                    elif 'bad_sensor' == state[node]:
                        strip.set_bit(k,color=[BRIGHTNESS,BRIGHTNESS,0])
                    elif 'offline' == state[node]:
                        strip.set_bit(k,color=[BRIGHTNESS,0,0])
            except KeyboardInterrupt:
                break

            time.sleep(60)
