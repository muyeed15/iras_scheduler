from tabulate import tabulate
import numpy


def merger():
    a = str(open(fr"data.ini", "r", encoding="utf-8").read())
    a = a.upper()

    tokn = a.index("NGCONTENT-")
    token = f"{a[tokn + 10]}{a[tokn + 11]}{a[tokn + 12]}".upper()

    ax = str(f"</thead><tbody _ngcontent-{token}-c185=\"\"><tr _ngcontent-{token}-c185=\"\" class=\"reg-courses "
             f"ng-star-inserted\"><td _ngcontent-{token}-c185=\"\"><strong _ngcontent-{token}-c185=\"\">").upper()
    ay = str("</span></td></tr><!----></tbody></table>").upper()

    try:
        ax_i = a.index(ax)
        ay_i = a.index(ay)
        print("\nCreating the list! Please Wait....")
    except:
        print("Error: Wrong Credentials!\n")
        return

    def remove_string_before_index(string, index):
        return string[index:]

    def remove_string_after_index(string, index):
        return string[:index + 1]

    a1 = remove_string_before_index(a, ax_i)
    a1 = remove_string_after_index(a1, ay_i)
    a1 = a1.replace(ax, "")
    a1 = a1.replace(f"</STRONG></TD><TD _NGCONTENT-{token}-C185=\"\" CLASS=\"COURSE-TEXT\">", "*")
    a1 = a1.replace(f"</TD><TD _NGCONTENT-{token}-C185=\"\">", "*")
    a1 = a1.replace(f"<SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-SUCCESS\">", "")
    a1 = a1.replace(f"</SPAN><SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-WARNING\">", "*")
    a1 = a1.replace(f"</SPAN>*<SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-WARNING\">", "*")
    a1 = a1.replace(f"</SPAN></TD></TR><TR _NGCONTENT-{token}-C185=\"\" CLASS=\"REG-COURSES NG-STAR-INSERTED\"><TD "
                    f"_NGCONTENT-{token}-C185=\"\"><STRONG _NGCONTENT-{token}-C185=\"\">", "|")
    try:
        a1 = a1.replace(f"</SPAN>", "")
    except:
        pass

    a1 = remove_string_after_index(a1, a1.index("<") - 1)

    dat = [["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
           ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
           ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
           ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
           ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]]


    print("\nSchedule:")

    sc = 0
    sb = 0
    for x in a1:
        if x == "|":
            sc = 0
            sb += 1
        if x != "*":
            if x != "|":
                if sc == 0:
                    dat[0][0 + sb] += x
                if sc == 1:
                    dat[1][0 + sb] += x
                if sc == 2:
                    dat[2][0 + sb] += x
                if sc == 3:
                    dat[3][0 + sb] += x
                if sc == 4:
                    dat[4][0 + sb] += x
        else:
            sc += 1

    for i in range(5):
        while "" in dat[i]:
            dat[i].remove("")

    f_dat = numpy.transpose(dat)

    head = ["COURSE NO", "COURSE NAME", "SECTION", "ROOM", "TIME"]
    table = tabulate(f_dat, headers=head, tablefmt="grid")

    print(table)
