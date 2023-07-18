# modules
from tabulate import tabulate
import numpy

# txt export
def exporter():
    # fucntions for removing before and after the schedule positioning strings
    def remove_string_before_index(string, index):
        return string[index:]

    def remove_string_after_index(string, index):
        return string[:index + 1]

    # html --> ini --> merging
    def htmr(): 
        # raw string
        raw = str(open(fr"data.ini", "r", encoding="utf-8").read())
        raw = raw.upper()

        # token finding
        tokn = raw.index("NGCONTENT-")
        token = f"{raw[tokn + 10]}{raw[tokn + 11]}{raw[tokn + 12]}".upper()

        # schedule positioning strings
        craw0 = str(f"</thead><tbody _ngcontent-{token}-c185=\"\"><tr _ngcontent-{token}-c185=\"\" class=\"reg-courses "
                f"ng-star-inserted\"><td _ngcontent-{token}-c185=\"\"><strong _ngcontent-{token}-c185=\"\">").upper()
        craw1 = str("</span></td></tr><!----></tbody></table>").upper()

        # indexing
        try:
            # determining the indexes of schedule positioning strings
            craw0_i = raw.index(craw0)
            craw1_i = raw.index(craw1)
        except:
            # if there is no schedule positioning strings then the login is not successfull!
            print("Error: Wrong Credentials!\n")
            return

        # replacing excecive elements with "*" and "|" and ""
        raw = remove_string_before_index(raw, craw0_i)
        raw = remove_string_after_index(raw, craw1_i)
        raw = raw.replace(craw0, "")
        raw = raw.replace(f"</STRONG></TD><TD _NGCONTENT-{token}-C185=\"\" CLASS=\"COURSE-TEXT\">", "*")
        raw = raw.replace(f"</TD><TD _NGCONTENT-{token}-C185=\"\">", "*")
        raw = raw.replace(f"<SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-SUCCESS\">", "")
        raw = raw.replace(f"</SPAN><SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-WARNING\">", "*")
        raw = raw.replace(f"</SPAN>*<SPAN _NGCONTENT-{token}-C185=\"\" CLASS=\"LABEL RS-TEXT LABEL-WARNING\">", "*")
        raw = raw.replace(f"</SPAN></TD></TR><TR _NGCONTENT-{token}-C185=\"\" CLASS=\"REG-COURSES NG-STAR-INSERTED\"><TD "
                        f"_NGCONTENT-{token}-C185=\"\"><STRONG _NGCONTENT-{token}-C185=\"\">", "|")
        
        # helps to determine if a course is successfully graded or in Z
        try:
            raw = raw.replace(f"</SPAN>", "")
        except:
            pass
        
        # final touch
        raw = remove_string_after_index(raw, raw.index("<") - 1)

        return raw
    
    try:
        htmr_str = htmr() # new raw string
    except:
        return 0

    # data storage 0
    dat0 = [[], [], [], [], []]

    # isolate schedule elements and inserting in data storage 0
    def isoler(dat0):
        cs = 0 # counting stars
        cb = 0 # counting bars
        for letter in htmr_str: # reads every word in string and isolate creates words by isolating letters via "*" and isolating row via "|"
            if letter == "|":
                cs = 0
                cb += 1
            if letter != "*":
                if letter != "|":
                    for j in range(0, 5):
                        dat0[j].append("")
                        if cs == j:
                            dat0[j][j + cb] += letter # replacing the "" it with the joint strings including spaces
            else:
                cs += 1

        # removes all empty elements
        for idx in range(5):
            while "" in dat0[idx]:
                dat0[idx].remove("")

        return dat0
    
    # isolated data
    dat0 = isoler(dat0) # data stored in data storage 0

    t_dat0 = numpy.transpose(dat0) # transposing data storage

    # using tabulate
    head = ["COURSE NO", "COURSE NAME", "SECTION", "ROOM", "TIME"]
    table = tabulate(t_dat0, headers=head, tablefmt="grid")

    # exporting schedulue
    print(table, file=open(fr"schedule.txt", "w", encoding="utf-8"))
