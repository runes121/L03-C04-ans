import requests

p1 = requests.get("https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
p2 = requests.get("https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
p3 = requests.get("https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
p4 = requests.get("https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")
p5 = requests.get("https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D")

link_first_half = r"https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string="
second_half = ""

def put_together(code):
	return f"{link_first_half}{code}{second_half}"

text = f"{p1.text}{p2.text}{p3.text}{p4.text}{p5.text}"

print(text)

with open("response.txt", "w") as f:
	to_request = put_together(text)
	print(to_request)
	f.write(requests.get(to_request).text)
	
