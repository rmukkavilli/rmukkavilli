patient = {

"id":"131707439",

"resourceType":"Patient",

"name":[

{

"family":"Smith",

"given":["John"]

}

],

"communication":[

{

"language":{

"display":"Spanish"

}

}

]

}

print( patient["name"][0]["given"][0]," ",patient["name"][0]["family"])
print(patient["communication"][0]["language"]["display"])