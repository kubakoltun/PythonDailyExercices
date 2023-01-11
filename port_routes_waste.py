def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    d = [
        [0, 8943, 8019, 3652, 10545],
        [8943, 0, 2619, 6317, 2078],
        [8019, 2619, 0, 5836, 4939],
        [3652, 6317, 5836, 0, 7825],
        [10545, 2078, 4939, 7825, 0]
    ]

    co2 = 0.020

    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    if 0 in route and 1 in route and 2 in route and 3 in route and 4 in route:
                        # distance = [d[route[i]][route[i++]] + d[route[i]][route[i++]] + d[route[i]][route[i++]] + 
                        # d[route[i]][route[i++]] for i in route] 
                        distance = d[route[0]][route[1]] + d[route[1]][route[2]] + d[route[2]][route[3]] + d[route[3]][
                            route[4]]
                        emissions = distance * co2
                        print(' '.join([portnames[i] for i in route]) + " %.1f kg" % emissions)
                        # distance = d[route[0]][route[1]] + d[route[1]][route[2]] + d[route[2]][route[3]] + d[route[
                        # 3]][route[4]] 


main()
