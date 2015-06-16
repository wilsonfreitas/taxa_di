# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

import textparser as tp

class DateParser(tp.PortugueseRulesParser):
    def parseDate(self, text, match):
        r'\((\d\d)/(\d\d)/(\d\d\d\d)\)'
        return '{0}-{1}-{2}'.format(match.group(3), match.group(2), match.group(1))


parser = DateParser()

# Read in a page
html = scraperwiki.scrape("http://www.cetip.com.br")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
date = root.cssselect("#ctl00_Banner_lblTaxDateDI")[0].text_content().strip()
date = parser.parse(date)
rate = root.cssselect("#ctl00_Banner_lblTaxDI")[0].text_content().strip().replace('%', '')
rate = parser.parse(rate)

# Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['date'], data={"date": date, "rate": rate})

# An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
