#“All vanity plates must start with at least two letters.”

#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”

#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
 # AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

#“No periods, spaces, or punctuation marks are allowed.”


def main():
    s = input("Enter your No: ")

    while len(s)>=2 or len(s)<=6:
        if s[0]=='0':
            break
        for i in range(0,len(s)):
            if s[i].isalpha() and s[i+1].isdigit:
               pass
            else:
                break
        
        

    