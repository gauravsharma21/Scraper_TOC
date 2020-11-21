from Scraper import Scraper

sc = Scraper("https://www.monster.com/jobs/search/?q=Software-Developer&where=NY")

q = sc.find(_tag="div", _id="SearchResults")
tree = sc.parse(sc.getSubstring(q[0]))

for section in tree.children.tags:
    if(section.props["class"] == '"card-content "'):
        summary = section.find(_tag = "div")[0].children.tags[1]
        title = summary.children.tags[0].children.children.getString()[0]
        company = summary.children.tags[1].children.tags[0].getString()[0]
        location = summary.children.tags[2].children.getString()[0]
        print("Title: ", title)
        print("Company: ",company)
        print("Location: ", location)
