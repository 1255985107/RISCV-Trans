from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def gethex(filename: str):
	with open(filename, "r+") as f:
		coestr = f.read()
	cmds = coestr.split(',')
	cmds[0] = cmds[0][-8:]
	return [str.strip(" ,;\n") for str in cmds]

def getasm(filename: str):
	with open(filename, "r+") as f:
		coestr = f.read()
	cmds = coestr.split('\n')
	return cmds

riscvfilename = "inst.asm"
coefilename = "inst.coe"
webdriver_path = "D:/Python312/msedgedriver.exe"

service = Service(webdriver_path)
options = webdriver.EdgeOptions()
options.add_argument("--headless")
options.page_load_strategy = "eager"

browser = webdriver.Edge(service=service, options=options)
browser.get("https://luplab.gitlab.io/rvcodecjs/")
kw_input = browser.find_element(By.ID, 'search-input')

attrs = {"id" : "asm-data"}
cmds = gethex(coefilename)
log = open(riscvfilename, "w+")

for inst in cmds:
	kw_input.clear()
	kw_input.send_keys(inst)
	kw_input.send_keys('\r\n')
	html = browser.page_source

	soup = BeautifulSoup(html, 'html.parser')
	data = soup.find_all('div', attrs)
	for item in data:
		log.write(item.text + '\n')