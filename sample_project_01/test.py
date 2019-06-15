import requests as rq
response = rq.get("http://localhost:9031/api/std/")
print(response.json())

payload={
       "rno": 106612862003,
        "sname": "Archana",
        "category": "general",
        "city": "Hyderabad",
        "result": "pass"
    }
response = rq.put("http://localhost:9031/api/std/9",payload)

if response.status_code==201:
    print("Successfully created")
else:
    print("creation failed")