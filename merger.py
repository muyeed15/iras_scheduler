# merge data
def merger():
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
    
    # time defininer
    def time_sorter(week_day):
        if week_day == "S":
            pd = week_day
            ad = "T"
        elif week_day == "T":
            pd = week_day
            ad = "S"
        elif week_day == "M":
            pd = week_day
            ad = "W"
        elif week_day == "W":
            pd = week_day
            ad = "M"
        elif week_day == "A":
            pd = week_day
            ad = "R"
        elif week_day == "R":
            pd = week_day
            ad = "A"

        # time sorting algorithms
        day_time = []
        day_idx = []
        for day_dat in dat0[4]:
            if pd in day_dat:
                day_time.append(day_dat)
                day_idx.append(dat0[4].index(day_dat))

        day_s0 = []
        for day_dat_s0 in day_time:
            day_dat_s0 = day_dat_s0.replace(" ", "")
            day_dat_s0 = day_dat_s0.replace(pd, "")
            try:
                day_dat_s0 = day_dat_s0.replace(ad, "")
            except:
                pass
            day_dat_s0 = day_dat_s0.replace(":", "")
            day_dat_s0 = remove_string_after_index(day_dat_s0, 3)
            day_s0.append(int(day_dat_s0))
        
        day_s1 = sorted(day_s0)
        day_time_idx = []
        for day_dat_s1 in day_s1:
            day_time_idx.append(day_s0.index(day_dat_s1))

        day_sc_raw = [[], [], [], [], []]

        day_sc_sort = [[], [], [], [], []]
        
        for i in range(5):
            c = 0
            for item in dat0[i]:
                if c in day_idx:
                    day_sc_raw[i].append(item)
                c += 1

        for j in range(5):
            for num in day_time_idx:
                day_sc_sort[j].append(day_sc_raw[j][num])

        if day_sc_sort == [[], [], [], [], []]:
            return None
        
        return day_sc_sort
    
    # defining the state of storage
    try:
        sat_dat = time_sorter("A")
    except:
        sat_dat = None

    try:
        sun_dat = time_sorter("S")
    except:
        sun_dat = None

    try:
        mon_dat = time_sorter("M")
    except:
        mon_dat = None

    try:
        tue_dat = time_sorter("T")
    except:
        tue_dat = None

    try:
        wed_dat = time_sorter("W")
    except:
        wed_dat = None

    try:
        thu_dat = time_sorter("R")
    except:
        thu_dat = None

    return sat_dat, sun_dat, mon_dat, tue_dat, wed_dat, thu_dat
