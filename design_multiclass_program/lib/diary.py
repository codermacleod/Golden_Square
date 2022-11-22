import re
class Diary():
    def __init__(self):
        self.entries = []
        
    def add(self,diary_entry):
        self.entries.append(diary_entry)

    def read_all_entries(self):
        return self.entries

    def reading_material_finder(self,wpm,mins):
        valid_list=[]
        for entry in self.entries:
            if len(entry.contents.split())<=(wpm*mins):
                valid_list.append(entry.contents)
        count_list=[entry.count(" ")  +  1 for entry in valid_list]
        return valid_list[count_list.index(max(count_list))]
    
    def get_phone_numbers(self):
        phone_numbers=[]
        for entry in self.entries:
            phone_numbers += re.findall(r"0\d\d\d\d\d\d\d\d\d\d",entry.contents)
        return phone_numbers

        
        
       
    
    


