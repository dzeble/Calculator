from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty 
from kivy.lang import Builder
from kivy.core.window import Window
import re
import os
import sys


#set the app size
Window.size = (500, 600)
Builder.load_file('calc.kv') #this is another way to link the kv file

class MyLayout(Widget):

    # function from youtube trouble shooting
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)



    def clear(self):
        self.ids.calc_input.text = "0"
        
   
    #creat button pressing function
    def button_press(self, button):
        #create a variable with what was in the text box
        prior = self.ids.calc_input.text

        #test for error first
        if"Error" in prior:
            prior = " "

        # check if 0 is there
        if prior == "0":
            self.ids.calc_input.text = " "
            self.ids.calc_input.text = f"{ button }"
        else:
            self.ids.calc_input.text = f"{ prior}{button}"

#function to remove last character in text box
    def remove(self):
        prior = self.ids.calc_input.text
        #remove last item
        prior = prior[:-1]
        #output
        self.ids.calc_input.text = prior

#create function to toggle from positive to negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        #check for negative sign
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", " ")}'
        else:
            self.ids.calc_input.text = f'-{prior}'


#create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
    #split text box by + 
        num_list = prior.split("+") 
        #num_list = re.split('+ | - | * | /', prior)
        
        if "+"  in prior  and "." not in num_list[-1] :
            prior = f'{prior}.'

            self.ids.calc_input.text = prior
        

        elif "." in prior:
            pass
        else:
    # add a decimal point to the end of the text
            prior = f"{prior}."
    #output back to the text box
            self.ids.calc_input.text = prior 


# create math sign function
    def math_sign(self,sign):
        prior = self.ids.calc_input.text
        # add a plus symbol
        self.ids.calc_input.text = f"{ prior }{sign}"




#creat "equals to"  function
    def equals(self):
        prior = self.ids.calc_input.text

#error handling
        try:

#evaluate the math from the text box
            answer = eval(prior)
            #output
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"
'''''
    #addition
        if "+" in prior:
            num_list = prior.split("+")  # turns numbers into list of strings
            answer = 0.0 
            #loop through our list
            for number in num_list:
                answer = answer + float(number)

            #print answer in textbox
            self.ids.calc_input.text =  str(answer)

'''
    


class SkokumCalculatorApp(App):  #since we are using a different method to link the kv file ,the name doesn't need 
    def build(self):       #to match the app file 
        return MyLayout()

if __name__ == '__main__':
    SkokumCalculatorApp().run()