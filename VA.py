def response = get('https://respiro.atlassian.net/rest/api/3/search?jql=project=%22NAMS%22&assignee=Haritha%20Sallepalli&fields=key&maxResults=1000').asObject(Map)
def issuelist = response.body
def total = issuelist['total']
def issuekeys = issuelist['issues']['key']

//logger.info("total issues in NAMS are ${total}")
//logger.info("nams issues list is ${issuekeys}")

def today = new Date()
def targetmonth = today.toMonth()
def targetyear = today.toYear()
targetyear = targetyear.toString()

switch(targetmonth){
case "JANUARY": targetmonth = "00"; break;
case "FEBRUARY": targetmonth = "01"; break;
case "MARCH": targetmonth = "02"; break;
case "APRIL": targetmonth = "03"; break;
case "MAY": targetmonth = "04"; break;
case "JUNE": targetmonth = "05"; break;
case "JULY": targetmonth = "06"; break;
case "AUGUEST": targetmonth = "07"; break;
case "SEPTEMBER": targetmonth = "08"; break;
case "OCTOBER": targetmonth = "09"; break;
case "NOVEMBER": targetmonth = "10"; break;
case "DECEMBER": targetmonth = "11"; break;
}
logger.info("target month & year to get activity info ${targetmonth} & ${targetyear}")
