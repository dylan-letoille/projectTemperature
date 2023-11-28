import myTemperature as t
a = input("c to f or f to c")
if a == 'c to f':
    print(t.ctof(int(input("write c"))))
if a == 'f to c':
    print(t.ftoc(int(input("write f"))))