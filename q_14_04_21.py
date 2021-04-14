#q_14_04_21
value="100"
t=({"Gift_id":"00012","Name":"XBOX","Remarks":"ON DISCOUNT","Price":"900"}, 
	{"Gift_id":"00011","Name":"PS5","Remarks":"FULL","Price":value})
def BUMPER(t):
	for x in t:
		for y in x:
			if y=="Remarks":
				if x["Remarks"]=="ON DISCOUNT":
					print(x)
BUMPER(t)