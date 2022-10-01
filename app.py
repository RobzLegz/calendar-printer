def print_days_names():
    day_names = ["Pi", "Ot", "Tr", "Ce", "Pk", "Se", "Sv"]

    ds = ""

    for dn in day_names:
        if dn == "Pi":
            ds = dn
        else:
            ds = f"{ds} {dn}"

    print(ds)

def print_days():
    days = []

    i = 1

    while i < 32:
        days.append(i)
        i += 1

    d_n = []

    for day in days:
        if day % 7 == 0:
            d_k = day - 6

            ds = ""

            f_d = True

            while d_k < day + 1:
                if f_d:
                    if d_k < 10:
                        ds = f" {d_k}"
                    else:
                        ds = d_k

                    f_d = False
                else:
                    if d_k < 10:
                        ds = f"{ds}  {d_k}"
                    else:    
                        ds = f"{ds} {d_k}"

                d_k += 1
            d_n.append(ds)
        elif day == 29:
            ds = ""

            d_c = day

            while d_c < 32:
                if d_c == 29:
                    ds = d_c
                else:
                    ds = f"{ds} {d_c}"
                
                d_c += 1

            d_n.append(ds)

    for ds in d_n:
        print(ds)

def main():
    print_days_names()

    print_days()

main()
