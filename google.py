from googletrans import Translator
import googletrans


def translateText(input_text,user_name):

  translator = Translator()
  r=input_text#hi
  #result=''
  try:

    if r.find('/start')!=-1:
     return "Hello, {}. 🤖\n\nTry the /help command for assistance.".format(user_name)

    elif r.find('/help')!=-1:
     return "\nHow do I translate ?\n\n>  Destination Language: Text \n> Example:\n \t  ja: I am still learning.\n\n To see the languages try the /lang command.\n"

    elif r.find('/lang')!=-1:
     return googletrans.LANGUAGES

    elif r.find(':')==-1:
     result = translator.translate(input_text,dest='bn')

    elif r[2]==':': 
     s=r[3:]
     lan=r[0:2]
     result = translator.translate(s, dest=lan)  
       
    elif r[3]==':':
     s=r[4:]
     lan=r[0:2]
     result = translator.translate(s,dest=lan)
     #googletrans.LANGUAGES
     
    return result.text  

  except:
    return "Failed to translate. 🛑\nTry the /help command for guidelines."  
    


