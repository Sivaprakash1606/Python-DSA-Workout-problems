def find_itinerary(tickets):
    def find(allticket, i,res):
        # if not res:
        #     res.append(allticket[i][0])
        #     res.append(allticket[i][1])
        #     allticket.pop(i)
        # else:

        for j in range(len(allticket)):
            find=False
            for k in range(len(allticket)):
                if res[-1]==allticket[k][0]:
                    res.append(allticket[k][0])
                    res.append(allticket[k][1])
                    allticket.pop(k)
                    find=True
                    break
            if find==False:
                res=[]
                return False
        if not allticket:
            return res

    allticket = tickets[:]
    res=[]
    for i in range(len(tickets)):
        # result = find(allticket, i,res)
        res.append(allticket[i][0])
        res.append(allticket[i][1])
        allticket.pop(i)
        result = find(allticket, i, res)
        if result == False:
            allticket=tickets[:]
            res=[]
        else:
            return res

tickets1 = [
    ["Madurai", "Coimbatore"],
    ["Bangalore", "Pondicherry"],
    ["Pune", "Kolkatta"],
    ["Coimbatore", "Pune"],
    ["Kolkatta", "Pondicherry"],
    ["Pondicherry", "Bangalore"],
    ["Pondicherry", "Madurai"],
]
tickets2 = [
    ["Chennai", "Banglore"],
    ["Bombay", "Delhi"],
    ["Goa", "Chennai"],
    ["Delhi", "Goa"]
]
print(find_itinerary(tickets1))
print(find_itinerary(tickets2))
