import english_terms
import spacy

def get_ancer(details, type, text,second,debug):
    #this is the function that is actually called
    #defindes some things
    word_list=[]
    sentence_list=[]
    found=False
    ancer_text=[]
    END_LETTERS=english_terms.END_LETTERS
    word=''
    sentence=[]

    #first the text is put into a list of words
    for i in range(len(text)):
        if text[i] not in END_LETTERS:
            try:
                word=word+str(text[i])
            except:
                pass
        elif text[i] in END_LETTERS:
            word_list.append(word)
            if text[i]!=' ':
                word_list.append(str(text[i]))
            word=''
    word_list.append(word)

    #then the words are taken to a list of sentences
    for i in range(len(word_list)):
        if word_list[i]!='.':
            sentence.append(word_list[i])
        elif word_list[i]=='.':
            sentence_list.append(sentence)
            sentence=[]
    sentence_list.append(sentence)

    check=False
    check_num=0
    end=False
    #checks if the sentence contains the keyword and
    #then goes to another function to find the ancer.
    a=30
    for i in range(len(sentence_list)):
        sentence=sentence_list[i]
        for i in range(len(sentence)):
            word=sentence[i]
            details=str(details)
            if word.lower()==details.lower():
                ancer=check_for_ancer(sentence, type, second, debug)
                if ancer!='':
                    return ancer
    return 'Sorry the question could not be ancered'

def what(details,ancer_text):
    #looks for a Noun
    compound=''
    ancer=''
    subj=''
    for i in range(len(ancer_text)):
        word=ancer_text[i]
        if word.dep_==u'compound':
            compound=str(word.text).lower()+'_'
        if word.pos_==u'PROPN' or word.pos_==u'NOUN':
            subj=word.text
            if compound!='':
                ancer=compound+str(word.text).lower()
            else:
                ancer=str(word.text).lower()
    return ancer

def where(details,ancer_text):
    #looks for location
    for ent in ancer_text.ents:
        if ent.label_==u'GPE':
            return ent.text
    return ''
def when(details,ancer_text):
    #finds a date
    month=''
    day=''
    year=''
    check=False
    MONTHS=english_terms.MONTHS
    for i in range(len(ancer_text)):
        word=ancer_text[i]
        prev_numm=ancer_text[i-1]
        try:
            num=int(word.text)
        except:
            num=0
        try:
            prev_num=int(prev_numm.text)
        except:
            prev_num=0
        if word.text in MONTHS and month=='':
            month=word.text
            check=True
        if prev_numm.pos_==u'NUM' and prev_num<=31 and prev_num>0 and day=='' and check==True:
            day=prev_numm.text
        if word.pos_==u'NUM' and num>0 and num>40 and year=='' and check==True:
            year=word.text
        if month!='' and day!='' and year!='':
            check=False
    if day!='' and month!='' and year!='':
        return day+' '+month+' '+year
    else:
        return ''

def why(details,ancer_text):
    #looks for a because and then finds something after it
    check=False
    ancer=''
    compound=''
    subj=''
    CONJ=english_terms.CONJ

    for i in range(len(ancer_text)):
        word=ancer_text[i]
        if word.text in CONJ:
            check=True
        if word.dep_==u'compound':
            compound=str(word.text).lower()+'_'
        if word.pos_ in english_terms.WHY_POS and check==True:
            subj=word.text
            if compound!='':
                ancer=compound+str(word.text).lower()
            else:
                ancer=str(word.text).lower()
    return ancer

def who(details,ancer_text):
    #looks for a person
    for ent in ancer_text.ents:
        if ent.label_==u'ORG' or ent.label_==u'PERSON':
            return ent.text
    return ''

def check_for_ancer(text,type,second,debug):
    #this function is calles when there is a sentance that could have tha ancer.

    if debug==True:
        print(text)
    ancer=''
    new_text=''
    details=''
    passed=True
    #adjusts if there is secondary information provided
    if second!='':
        passed=False
        for word in text:
            if word==second:
                passed=True
    if second=='':
        passed=True
    #adds spaces between words
    for word in text:
        new_text=new_text+word+' '
    text=new_text

    if passed==True:
        #puts the sentence into spacy and then calls the
        #appropiate function for the question word.
        lang=spacy.load('en_core_web_sm')
        ancer_text=lang(unicode(text,'utf-8'))
        if type!='':
            #type is called like a function for one of them above
            ancer=eval(type)(details,ancer_text)
    return ancer

if __name__=='__main__':
    a=get_ancer('material','who','the material is mined by St. David Mining Company')
    print(a)
