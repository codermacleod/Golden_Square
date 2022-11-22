class GrammarStats:
    def __init__(self):
        self.boolean_counter = []
        self.true_list = []
    def check(self, text):
        capital = text[0]
        end = text[-1]
        #End
        if end in "?!.":
            the_end = True
        else: the_end = False
        #First caps
        caps = capital.isupper()
        # Add result to counter for percentage calc:
        self.boolean_counter.append((caps and the_end))
        # for b in self.boolean_counter:
        #     if b == True:
        #         self.true_list.append(True)
        #Return both for boolean:
        
        return the_end and caps

            
        # if end in "?!,.":
        #     end = True
       
        # if capital and end == True:
        #     return True
        # else:
        #     return False
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
  
    def percentage_good(self):
        for b in self.boolean_counter:
            if b == True:
                self.true_list.append(True)
        
        final_int = len(self.true_list) / len(self.boolean_counter)
        return str(int(final_int*100))+'%'
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.