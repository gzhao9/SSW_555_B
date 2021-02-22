"""
Project 02
Name:Gengwu Zhao
"""
def get_file_str(file_path:str=None)->str:
    if file_path is None or file_path is '':
        file_path='Project01_Gengwu_Zhao.ged'
        print("No input path, default test document will be used: Project01_Gengwu_Zhao.ged")        
    file_str=open(file_path,'r').readlines()
    #if the txt is empty, raise a valueError
    if len(file_str)==0:
        raise ValueError
    return file_str

#get the averages of the confidences
def get_result(txt_str)->None:
    #use tag1 and tag2 to record the tags, the tag 1 is FAM and INDI which is below the id. The tag2 is on the second point of each lines.
    tag1={"FAM":0,"INDI":0}
    tag2={"HEAD":0,"NOTE":0,"TRLR":0,"BIRT":1,"CHIL":1,"DEAT":1,"DIV":1,"FAMC":1,"FAMS":1,"HUSB":1,"MARR":1,"NAME":1,"SEX":1,"WIFE":1,"DATE":2}
    
    for line in txt_str:    #get the each line of the txt.
        print(f"--> {line}",end='') #print the input line begin with "-->"
        
        #remove the enter in the end of each lines
        if line[-1]=='\n':
            l=line[:-1].split()
        else:
            l=line.split()
        
        #if the second part is a tag, and match the leve. print the result as the format.
        if l[1] in tag2.keys():
            if tag2[l[1]]==int(l[0]):
                print(f"<-- {l[0]}|{l[1]}|Y|",end='')
                if len(l)>2:
                    print(' '.join(l[2:]),end='')
                print()
                continue
        #if the third is a tag. print the fomat
        elif len(l)>2 and l[2] in tag1.keys():
            if tag1[l[2]]==int(l[0]):
                print(f"<-- {l[0]}|{l[2]}|Y|{l[1]}")
                continue
        #ohter cases do not mathch the format, print the reuslt.
        print(f"<-- {l[0]}|{l[1]}|N|",end='')
        if len(l)>2:
            print(' '.join(l[2:]),end='')
        print()

def main():
    while True:
        #give three chance to enter the path of the file
        for i in range(3):
            try:
                file_path=input('Press enter only to use the default test file, \nor enter the file path:')
                find_str=get_file_str(file_path)
                get_result(find_str)
            except ValueError:
                print('The file is empty,try again.')
            except FileNotFoundError as e:
                print(f"{e}. try again.")
            else:
                #if there is no error, print the result and break the for loop to exit.
                break
            #if there is an error, not break, tell the left times to the user instead.
            print(f'You have left {2-i} times')
        user_choose=input("\nEnter 'q' to exit, any other key to continue:")
        #if user enter 'q', break
        if user_choose.lower()=='q':
            break
if __name__=='__main__':
    main()
