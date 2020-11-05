class Solution:
    def reformatDate(self, date: str) -> str:
        dic = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06',
               "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
        dates = date.split()
        aux = dates[2]+'-'+dic[dates[1]]+'-'
        temp = ''
        for d in date:
            if d in '0123456789':
                temp += d
            else:
                break
        if int(temp) < 10:
            temp = '0'+temp
        return aux+temp
