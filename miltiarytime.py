def numToWords(num):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0:
        words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)//3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    words = ' '.join(words)
    if num < 10:
        words = f"zero {words}"
    return words

def convert_time_to_military(time):
    hours, minutes = time.split(':')
    minutes = int(minutes[:-2])

    # Convert the hours to military time
    if hours == '12':
        military_hours = '00'
    elif 'PM' in time:
        military_hours = int(hours) + 12
    else:
        military_hours = int(hours)
    if minutes > 0:
        minutes = numToWords(minutes)    
    else:
        minutes = "hundred hours"
    # Construct the military time
    return numToWords(military_hours) + " " + minutes

assert convert_time_to_military("4:00PM") == "sixteen hundred hours"
assert convert_time_to_military("11:00AM") == "eleven hundred hours"
assert convert_time_to_military("11:23AM") == "eleven twenty three"
assert convert_time_to_military("6:45PM") == "eighteen forty five"
assert convert_time_to_military("7:45AM") == "zero seven forty five"
assert convert_time_to_military("5:05PM") == "seventeen zero five"
assert convert_time_to_military("4:09AM") == "zero four zero nine"
