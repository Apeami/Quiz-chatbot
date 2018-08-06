import ancer_finder
import question_decoder
import requests
import bs4

def get_text(url,subject,debug):
    #This part gets the information from the internet
    if debug==True:
        print(url)
    try:
        page=requests.get(url)
    except:
        #If the page cant get found
        print('Sorry ur internet connection is trash')
        return None
    soup=bs4.BeautifulSoup(page.text,'lxml')
    #if there is no artice on the subject
    try:
        text=soup.select('.mw-parser-output')[0].text
    except:
        text=None
        print('There is no such thing as '+ subject)
    return text

def main(debug, question=None):
    if question==None:
        #gets question input
        question=raw_input('Type the question here: ')
        if debug==True:
            print(question)
    print('We are processing ur request, please wait ...')
    #the question decoder will get the subject,details,type and secondary information
    subject,details,type,second=question_decoder.decode_question(question,debug)
    url='https://en.wikipedia.org/wiki/'+subject
    #gets the information
    text=get_text(url,subject,debug)
    if text!=None:
        #uses ancer finder to search the text and find the ancer
        ancer=ancer_finder.get_ancer(details,type,text,second,debug)
        if subject!=details:
            print(subject+' was '+details+' : '+ancer)
        if subject==details:
            print(subject+' : '+ancer)

if __name__=='__main__':
    #just something to print information. If it is true you will see information.
    #True it just shows the input box.
    debug=False
    #call the main function
    main(debug)
