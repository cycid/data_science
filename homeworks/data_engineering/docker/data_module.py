class Data:

    def __init__(self) -> None:
        self.request_list=[]


    def add(self, new_files:str):
        self.request_list.append(new_files)
        return True
    
    def get(self):
        return self.request_list[-10:]
    

    def delete(self, id):
        self.request_list=[x for x in self.request_list if x['id']!=id]        
        return True
    

