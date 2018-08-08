import spacy
import english_terms

def subj(ques):
    #This category is for questions like this 'Who bought Minecraft'.

    compound=''
    subj=''
    subject=''
    details=''
    second=''
    if_compound=False

    for token in ques:
        if token.dep_==u'compound':
            subject=token.text
            if_compound=True
        if token.dep_==u'ROOT':
            details=token.text
        if token.dep_==u'dobj' and if_compound==False:
            subject=token.text
        if token.dep_==u'dobj' and if_compound==True:
            second=token.text

    return subject, details, second

def attr(ques,type):
    #This category is for questions like 'Who is Trump'

    compound=''
    subj=''
    subject=''
    details=''
    second=''
    attr_second=False
    for token in ques:
        if token.dep_==u'compound':
            compound=token.text
            attr_second=True
            subject=token.text
            details=token.text
        if token.dep_==u'nsubj' and token.text.lower() not in english_terms.QUESTION_WORDS and subject=='' and details=='':
            subject=token.text
            details=token.text
        if token.text.lower() not in english_terms.QUESTION_WORDS and token.dep_==u'attr' and attr_second==False:
            second=token.text
        elif token.text.lower() not in english_terms.QUESTION_WORDS and token.dep_==u'nsubj' and attr_second==True:
            second=token.text
        if token.dep_==u'attr' and token.text.lower() not in english_terms.QUESTION_WORDS and attr_second==False and subject=='' and details=='':
            subject=token.text
            details=token.text
        if token.dep_==u'nsubj' and type=='what':
            second=token.text

    return subject, details, second

def advmod(ques):
    #This is for questions like 'When was the Berlin Wall built'

    compound=''
    subj=''
    subject=''
    details=''
    second=''
    if_compound=False
    compound=''

    for token in ques:
        if token.dep_==u'compound':
            if_compound=True
            compound=token.text
        if token.dep_==u'nsubjpass' or token.dep_==u'nsubj':
            subject=token.text
            if if_compound==True:
                subject=compound+' '+token.text
        if token.dep_==u'ROOT' and if_compound==False:
            details=token.text
        if token.dep_==u'ccomp' and if_compound==True:
            details=token.text
        if token.dep_==u'dep' and if_compound==True:
            details=token.text

    return subject, details, second

def decode_question(question,debug):
    #converts the text into spacy
    lang=spacy.load('en_core_web_sm')
    ques=lang(unicode(question, "utf-8"))

    #defines some things

    QUESTION_WORDS=english_terms.QUESTION_WORDS
    BE=english_terms.BE
    noun_det=False

    subject=''
    type=''
    details=''
    second=''
    attr_pos=False

    for token in ques:
        if debug==True:
            print(token.text,token.pos_,token.dep_,spacy.explain(token.dep_))
        if token.pos_=='VERB':
            attr_pos=False
        if token.text in english_terms.BE and token.dep_==u'ROOT':
            attr_pos=True
        if token.text.lower() in QUESTION_WORDS:
            #this catorises the questions into three categories
            #and then goes to the function.
            type=token.text.lower()
            if token.dep_==u'nsubj':
                subject, details, second=subj(ques)
            if token.dep_==u'attr':
                subject, details, second=attr(ques,type)
            if token.dep_==u'advmod':
                subject, details, second=advmod(ques)
    if attr_pos==True:
        subject, details, second=attr(ques,type)
    if debug==True:
        print(subject, details, type, second)
    return subject, details, type, second

if __name__=='__main__':
    a=decode_question('Where was hitle born')
