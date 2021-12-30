import os,bs4
from requests_html import HTMLSession

class Explorer:
    def __init__(self) -> None:
        self.useragent = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        self.bscURL = "https://bscscan.com/address/"
        self.ethURL = "https://etherscan.com/address/"
        self.maticURL = "https://polygonscan.com/address/"
        self.hecoURL = "https://hecoinfo.com/address/"
        self.ftmURL = "https://ftmscan.com/address/"

    def document(self, filename):
        self.file = filename
        with open(self.file, "r") as groups:
            contains = groups.readlines()
            return contains 

    def main(self, url,choose,options):
        self.nftvalue = 0
        self.url = url 
        self.choose = choose 
        self.options = options 
        if self.options == "all":   
            for looping in range(len(self.document(self.file))):
                akun = self.document(self.file)[looping].strip()
                with HTMLSession() as sesi:
                    page = sesi.get(self.url+akun, headers=self.useragent)
                    soup = bs4.BeautifulSoup(page.content, 'html.parser')
                    self.addressHeader = soup.find("span", class_="text-size-address text-secondary text-break mr-1").text
                    self.address = soup.findAll("a", class_="link-hover d-flex justify-content-between align-items-center", href=True)
                    self.value = soup.findAll("div", class_='col-md-8')
                    self.est = self.value[0].text
                    self.unknown = soup.find("span", class_='list-amount link-hover__item hash-tag hash-tag--md text-truncate text-monospace')
                    try:
                        self.jumlahToken = soup.find("span", class_="badge badge-primary mx-1").text
                        self.IsiToken = soup.findAll("span", class_="list-amount link-hover__item hash-tag hash-tag--md text-truncate")
                        print("\n Address ke-{} -> {}".format(looping+1, self.addressHeader))
                        print(" Token:")
                        if self.choose in ["bsc", "matic", "heco", "ftm"]:
                            self.increment = 0 
                            for i in range (int(self.jumlahToken)):
                                self.increment += 1
                                try:
                                    nft = False
                                    print("   [{}] {}  Sc -> {}".format(
                                            self.increment, 
                                            self.IsiToken[i].text, 
                                            self.address[i]["href"].replace("?a="+akun, "").replace("/token/", ""))
                                            )
                                except:
                                    nft = True
                                    self.nftvalue += 1
                                    print(" Nft:")
                                    print("   [{}] {} Sc -> {}".format(
                                            self.increment,
                                            self.unknown.text,
                                            self.address[i]["href"].replace('?a='+akun,"").replace('/token/', ''))
                                            )
                        elif self.choose == "eth":
                            self.increment = 0 
                            for i in range (int(self.jumlahToken)):
                                self.increment += 1 
                                print("   [{}] {} Sc -> {}".format(
                                        self.increment,
                                        self.IsiToken[i].text,
                                        self.address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', ''))
                                        )
                        try:
                            self.proof = soup.find("div", class_='position-relative w-100 mr-1')
                            self.a = self.proof.find('a').text.strip()
                            self.span = soup.find("span", class_="badge badge-primary mx-1").text
                            with HTMLSession() as key:
                                res = key.get('https://www.google.com/search?q='+self.a.replace(self.span, "").strip())
                                sop = bs4.BeautifulSoup(res.content, 'html.parser')
                                r = sop.find("span", class_="DFlfde SwHCTb").text 
                            if nft == False:
                                print("\nEstimasi(BNB): {}\nJumlah token: {}\nEstimasi($): {} ~ {}".format(
                                        self.est,
                                        len(self.IsiToken),
                                        self.a.replace(self.span, "").strip(),"Rp."+r)
                                        )
                            elif nft == True:
                                print("\nEstimasi(BNB): {}\nJumlah token: {}\nJumlah NFT: {}\nEstimasi($): {} ~ {}".format(
                                        self.est,
                                        len(self.IsiToken),
                                        self.nftvalue,
                                        self.a.replace(self.span, "").strip(),"Rp."+r)
                                        )
                            print("-"*70)
                        except:
                            pass
                    except AttributeError:
                        try: 
                            print("\n\nAddress ke-{} -> {}\n [!] Tidak ada token".format(
                                    looping,
                                    self.addressHeader)
                                    )
                            print("-"*70)
                        except:
                            error_handle = soup.find("h1", class_="h4 mb-0").text.strip()
                            print(error_handle+": "+akun)
        elif self.options == "sort":
            for looping in range(len(self.document(self.file))):
                akun = self.document(self.file)[looping].strip()
                with HTMLSession() as sesi:
                    page = sesi.get(self.url+akun, headers=self.useragent)
                    soup = bs4.BeautifulSoup(page.content, 'html.parser')
                    self.addressHeader = soup.find("span", class_="text-size-address text-secondary text-break mr-1").text
                    self.address = soup.findAll("a", class_="link-hover d-flex justify-content-between align-items-center", href=True)
                    self.value = soup.findAll("div", class_='col-md-8')
                    self.est = self.value[0].text
                    self.unknown = soup.find("span", class_='list-amount link-hover__item hash-tag hash-tag--md text-truncate text-monospace')
                try: 
                    self.jumlahToken = soup.find("span", class_="badge badge-primary mx-1").text
                    self.IsiToken = soup.findAll("span", class_="list-amount link-hover__item hash-tag hash-tag--md text-truncate")
                    print("\n Address ke-{} -> {}".format(
                            looping+1, 
                            self.addressHeader)
                            )
                    print(" Token:")
                    if self.choose in ["bsc", "matic", "heco", "ftm"]:
                        self.increment = 0 
                        for i in range (int (self.jumlahToken)):
                            self.increment += 1
                            if i == 0:
                                nft = False
                                print("   [{}] {} Sc -> {}".format(
                                        self.increment,
                                        self.IsiToken[i].text,
                                        self.address[i]["href"].replace('?a='+akun,"").replace('/token/', ''))
                                        )
                            elif i > 0:
                                try:
                                    print("   [{}] {} Sc -> {}".format(
                                        self.increment,
                                        self.IsiToken[i].text,
                                        self.address[i]["href"].replace('?a='+akun,"").replace('/token/', ''))
                                        )
                                except:
                                    nft = True
                                    self.nftvalue += 1
                                    print(" Nft:")
                                    print("   [{}] {} Sc -> {}".format(
                                            self.increment,
                                            self.unknown.text,
                                            self.address[i]["href"].replace('?a='+akun,"").replace('/token/', ''))
                                            )
                    elif self.choose == "eth":
                        self.increment = 0 
                        for i in range(int(self.jumlahToken)):
                            self.increment += 1
                            if i == 0:
                                print("   [{}] {} Sc -> {}".format(
                                        self.increment,
                                        self.IsiToken[i].text,
                                        self.address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', ''))
                                        )
                            elif i > 0:
                                print("   [{}] {} Sc -> {}".format(
                                        self.increment,
                                        self.IsiToken[i].text,
                                        self.address[i]["href"].replace('?a='+akun.lower(),"").replace('/token/', ''))
                                        )
                    try:
                        self.proof = soup.find("div", class_='position-relative w-100 mr-1')
                        self.a = self.proof.find('a').text.strip()
                        self.span = soup.find("span", class_="badge badge-primary mx-1").text
                        with HTMLSession() as key:
                            res = key.get('https://www.google.com/search?q='+self.a.replace(self.span, "").strip())
                            sop = bs4.BeautifulSoup(res.content, 'html.parser')
                            r = sop.find("span", class_="DFlfde SwHCTb").text 
                        if nft == False:
                            print("\nEstimasi(BNB): {}\nJumlah token: {}\nEstimasi($): {} ~ {}".format(
                                    self.est,
                                    len(self.IsiToken),
                                    self.a.replace(self.span, "").strip(),"Rp."+r)
                                    )
                        elif nft == True:
                            print("\nEstimasi(BNB): {}\nJumlah token: {}\nJumlah Nft: {}\nEstimasi($): {} ~ {}".format(
                                    self.est,
                                    len(self.IsiToken),
                                    self.nftvalue,
                                    self.a.replace(self.span, "").strip(),"Rp."+r)
                                    )
                        print("-"*70) 
                    except:
                        pass
                except AttributeError:
                    pass
    def menu(self):
        os.system('cls')
        print("-- BLOCKSCAN --")
        print('[1] BSC\n[2] ETH\n[3] POLYGON\n[4] HECO Chain\n[5] FANTOM')
        a = int(input(">:"))
        if a == 1:
            print("-- PILIHAN --")
            print("[1] Tampilkan Semua Address") 
            print("[2] Tampilkan Address yang ber-isi saja")
            print("[3] Back")
            input_op = int(input("->"))
            if input_op == 1:
                os.system('cls')
                print("\n --- Binance Chain -- ")
                self.main(url=self.bscURL, choose="bsc", options="all")
            elif input_op == 2:
                os.system('cls')
                print("\n --- Binance Chain (sort) -- ")
                self.main(url=self.bscURL, choose="bsc", options="sort")
            elif input_op == 3:
                self.menu()
            else:
                print("[!] Salah!")
                self.menu()
        elif a == 2:
            print("-- PILIHAN --")
            print("[1] Tampilkan Semua Address")
            print("[2] Tampilkan Address yang ber-isi saja")
            print("[3] Back")
            input_op = int(input("->"))
            if input_op == 1:
                os.system('cls')
                print("\n --- Ethereum -- ")
                self.main(url=self.ethURL, choose="eth", options="all")
            elif input_op == 2:
                os.system('cls')
                print("\n --- Ethereum (sort)-- ")
                self.main(url=self.ethURL, choose="eth", options="sort")
            elif input_op == 3:
                self.menu()
            else:
                print("[!] Salah!")
                self.menu()
        elif a == 3:
            print("-- PILIHAN --")
            print("[1] Tampilkan Semua Address")
            print("[2] Tampilkan Address yang ber-isi saja")
            print("[3] Back")
            input_op = int(input("->"))
            if input_op == 1:
                os.system('cls')
                print("\n --- Polygon Scan -- ")
                self.main(url=self.maticURL, choose="matic", options="all")
            elif input_op == 2:
                os.system('cls')
                print("\n --- Polygon (sort)-- ")
                self.main(url=self.maticURL, choose="matic", options="sort")
            elif input_op == 3:
                self.menu()
            else:
                print("[!] Salah!")
                self.menu()
        elif a == 4:
            print("-- PILIHAN --")
            print("[1] Tampilkan Semua Address")
            print("[2] Tampilkan Address yang ber-isi saja")
            print("[3] Back")
            input_op = int(input("->"))
            if input_op == 1:
                os.system('cls')
                print("\n --- HECO Scan -- ")
                self.main(url=self.hecoURL, choose="heco", options="all")
            elif input_op == 2:
                os.system('cls')
                print("\n --- HECO (sort)-- ")
                self.main(url=self.hecoURL, choose="heco", options="sort")
            elif input_op == 3:
                self.menu()
            else:
                print("[!] Salah!")
                self.menu()
        elif a == 5:
            print("-- PILIHAN --")
            print("[1] Tampilkan Semua Address")
            print("[2] Tampilkan Address yang ber-isi saja")
            print("[3] Back")
            input_op = int(input("->"))
            if input_op == 1:
                os.system('cls')
                print("\n --- FTM Scan -- ")
                self.main(url=self.ftmURL, choose="ftm", options="all")
            elif input_op == 2:
                os.system('cls')
                print("\n --- FTM (sort)-- ")
                self.main(url=self.ftmURL, choose="ftm", options="sort")
            elif input_op == 3:
                self.menu()
            else:
                print("[!] Salah!")
                self.menu()
        i = input("Back? (y/t)")
        if i in ['y','ya','Y']:
            self.menu()
        else:
            exit()

a = Explorer()
a.document("address.txt")
a.menu()
