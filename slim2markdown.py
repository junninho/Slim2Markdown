from lxml import html
from bs4 import BeautifulSoup
import requests
import subprocess
import html2text
import base64
import re


h = html2text.HTML2Text()
h.body_width = 0

urls = ["https://www.policygenius.com/", "https://www.policygenius.com/", "https://www.policygenius.com/", "https://www.policygenius.com/" ]
insurance_type = ["life-insurance", "health-insurance" ,"renters-insurance", "pet-insurance", "long-term-disability-insurance"]
extensions = ["learn", "guide", "guide/faqs", "define"]
for url in urls:
    for ins in insurance_type:
        for ext in extensions:
            final_url = url + ins + "/" + ext + "/"
            r  = requests.get(final_url)
            data = r.text

            soup = BeautifulSoup(data ,'lxml')

            for link in soup.find_all('a'):
                links = link.get('href')
                check1 = re.compile("life-insurace|health-insurance|renters-insurance|pet-insurance|long-term-disability-insurance")
                check2 = re.compile("qa|define|learn|guide|glossary|companies")
                if links is not None:
                    if check1.search(links):
                        if check2.search(links):
                            if links.startswith('/'):
                                links = "https://www.policygenius.com" + links
                                page = requests.get(links)
                                page = h.handle(page.text)
                                links = links.replace('https://www.policygenius.com', '')
                                links = links[1:]
                                if links.endswith('/'):
                                    links = links[:-1]
                                links = links.replace('/', '_')
                                print(links)
                                if links.startswith('life-insurance'):
                                    f=open('life-insurance/' + links + '.md', 'w')
                                    f.write(page)
                                    f.close()
                                elif links.startswith('health-insurance'):
                                    f=open('health-insurance/' + links + '.md', 'w')
                                    f.write(page)
                                    f.close()
                                elif links.startswith('pet-insurance'):
                                    f=open('pet-insurance/' + links + '.md', 'w')
                                    f.write(page)
                                    f.close()
                                elif links.startswith('renters-insurance'):
                                    f=open('renters-insurance/' + links + '.md', 'w')
                                    f.write(page)
                                    f.close()
                                elif links.startswith('long-term-disability-insurance'):
                                    f=open('long-term-disability-insurance/' + links + '.md', 'w')
                                    f.write(page)
                                    f.close()


# e = 'echo `slimrb -c thanks.html.slim`'
# html_output = subprocess.Popen(e, shell=True, stdout=subprocess.PIPE)
# output = html_output.stdout.read().decode('ascii')
# page = h.handle(page.text)
# print (page)

# ~/Users/jathomas/Desktop/PG/policygenius/app/views/pages/

# print(tree)