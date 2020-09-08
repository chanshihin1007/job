def main():
    arr=[]
    x="The new patients were an 18-year-old female student who returned from Britain on Friday, and a 61-year-old man whose granddaughter and domestic helper was infected previously, according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s communicable disease branch."
    up="abcdefghijklmnopqrstuvwxyz"
    low="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in up:
        y=i,x.count(i)
        arr.append(y)
    for u in low:
        z=u,x.count(u)
        arr.append(z)
    print(arr)
main()
