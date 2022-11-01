from urllib.request import urlopen
import re

def check_function(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    prod1 = re.search('<h1 itemprop="name" content="(.*)">', html)
    prod1_name = prod1.group(1)
    prod1p = re.search('<meta itemprop="price" content="(.*)"/>', html)
    prod1_price = prod1p.group(1)
    stanje = html.count("Nema na stanju")
    
    # Menu
    
    print ("| Naziv Proizvoda | ", prod1_name, "|")
    print ("| Cena            | ", prod1_price, "rsd                                        |")
    if stanje == 5:
        print ("| Stanje          |  Nema Nigde!                                     |")
    else:
        print ("| Stanje          |  Ima negde, pogledaj na:", url)
    print ("|====================================================================|")

print ("|===========================[Chaos Check]============================|")
check_function("https://www.computerlandshop.rs/akcione-figure/warhammer-start-collecting-chaos-space-marines.html")
check_function("https://www.computerlandshop.rs/warhammer/chaos-space-marine-raptors.html")
check_function("https://www.computerlandshop.rs/warhammer/chaos-space-marine-terminators.html")
check_function("https://www.computerlandshop.rs/warhammer/chaos-space-marines-havocs.html")
check_function("https://www.computerlandshop.rs/akcione-figure/warhammer-start-collecting-beasts-of-chaos.html")
check_function("https://www.computerlandshop.rs/warhammer/chaos-space-marines-dark-apostle.html")
check_function("https://www.computerlandshop.rs/warhammer/warhammer-chaos-knights-knight-desecrator.html")
check_function("https://www.computerlandshop.rs/warhammer/aos-grand-alliance-chaos-dice-set.html")