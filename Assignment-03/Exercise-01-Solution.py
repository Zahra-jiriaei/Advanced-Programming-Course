#Zahra Jiriaei 98300065
# Library

class Book:
    totalcount=0
    # BooK_list={Book_id=[book_name,count]}
    Book_list={}
    
    def addBook(self,Book_Name,Book_ID,count=1):
        self.Book_Name=Book_Name
        self.Book_ID=Book_ID
        self.count=count
        
        # Number of all book in library
        self.__class__.totalcount=self.__class__.totalcount+self.count
        
        # Add book to library
        __class__.Book_list[self.Book_Name]=[self.Book_ID,self.count]
    
class LibraryMember:
    # Members_dict={member_id=member_name}
    Members_dict={}
    def addMember(self,Member_ID,Member_Name):
        self.Member_ID=Member_ID
        self.Member_Name=Member_Name
        
        #Add member to library
        __class__.Members_dict[self.Member_ID]=self.Member_Name
        
        # Add member to member_Book
        Library.member_Book[Member_ID]=[]
        
class Library:
    #memberbook={member_id:[book_ids]}
    member_Book={}
    
    def Get(self,Member_ID,Book_ID):
        self.Member_ID=Member_ID
        self.Book_ID=Book_ID
        
        # Can not get mor that five books
        if len(Library.member_Book[self.Member_ID])==6:
            return 'MaxReached : {} {}'.format(LibraryMember.Members_dict[self.Member_ID],self.Member_ID)
        
        # Book avalibility
        elif Book.Book_list[self.Book_ID][1]==0:
            return 'NotAvailable : {} {}'.format(Book.Book_list[self.Book_ID][0],self.Book_ID)
        
        else:
            # add book to member book
            self.__class__.member_Book[self.Member_ID]=self.__class__.member_Book[self.Member_ID]+[self.Book_ID] 
            # deleting book from book list
            Book.Book_list[self.Book_ID][1]=Book.Book_list[self.Book_ID][1]-1

        
    def Return(self,Member_id,Book_id):
        self.Member_id=Member_id
        self.Book_id=Book_id
        
        # deleting book from member book
        self.__class__.member_Book[self.Member_id]=self.__class__.member_Book[self.Member_id].remove(self.Book_id)
        
        # add book to library
        Book.Book_list[self.Book_id][1]=Book.Book_list[self.Book_id][1]+1
    
    def memberStat(self):
        for member in Library.member_Book:
            print("{} {}".format(LibraryMember.Members_dict[member],member))
            if Library.member_Book[member] != None:
                for books in Library.member_Book[member]:
                    print("{} {}".format(Book.Book_list[books][0],books))