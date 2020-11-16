from Scraper import Scraper

sc = Scraper("<a><div>fsfs</div><div>fess</div></a><div>ddsd</div>")


tree = (sc.parse(sc.data))
    # for x in tree.find("small"):
    #     for y in x.find("a"):
    #         print(y.props["href"])
tree.display()
