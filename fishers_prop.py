def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    for x in fishers:
        prob = x / total_fishers

    for country, fisher in zip(countries, fishers):
        print("%s %.2f%%" % (country, fisher / total_fishers * 100))


main()
