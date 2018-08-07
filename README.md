# Quiz-chatbot
Questions in Trivial Pursuit and pub quizzes

The main file is question_ancerer.py. If you run that then you will have the program. The way it works is that it will ask for input and you ask a question. If it is good than it should provide a decent ancer from the internet.

This thing works by decoding the question into the subject, details, question word and secondary information. Then it looks for a wikipedia article on the topic and then searches that for the ancer.
There are three types of questions that I have made it process. In the code I sort them and process it depending on the type.
The first one is questions like ‘Who is Trump’. These questions will most probably ancer with the actual subject of the sentence because the Who makes it look for people. This is somewhat wrong but it can also work in questions like ‘Where is London?’. These types work most of the time but they might not provide correct ancer or limited information.
The second is questions like ‘Who bought Minecraft?’. These questions normally could get the ancer but there is an error with the tense of the verb. The question stated above would not work because the article does not have the word in that tense. The question ‘Who buy Minecraft?’ (which isn’t normal English) would work.
The third type of question that I created was questions like ‘When was the Berlin Wall built?’ or ‘Where was Donald Trump born?’ These questions the bot anceres by far the best and to a surprising level of accuracy.
A problem that I have identified was that sometimes the two word subjects are not getting identified. It is very difficult for the computer to merge the words as it can get confused with other formats. It cannot work for three word subjects and just about works for two.
One of the worst problems is that the different tenses in the article and the question mean that the ancer could not be identified. For example the question ‘Who bought Minecraft’ does not work but ‘Who buy Minecraft?' does. The fix would be to convert all verbs to base form. This problem appears on random questions and depends on how the wikipedia article is written. This improvement would mean that you can ask questions in correct English.
