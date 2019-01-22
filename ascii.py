ascii_none = " _____ \n" \
             "|     |\n" \
             "|     |\n" \
             "|_____|"

ascii_1 = " _____ \n" \
          "|     |\n" \
          "|  o  |\n" \
          "|_____|"

ascii_2 = " _____ \n" \
          "|o    |\n" \
          "|     |\n" \
          "|____o|"

ascii_3 = " _____ \n" \
          "|o    |\n" \
          "|  o  |\n" \
          "|____o|"

ascii_4 = " _____ \n" \
          "|o   o|\n" \
          "|     |\n" \
          "|o___o|"

ascii_5 = " _____ \n" \
          "|o   o|\n" \
          "|  o  |\n" \
          "|o___o|"

ascii_6 = " _____ \n" \
          "|o   o|\n" \
          "|o   o|\n" \
          "|o___o|"

ascii_list = [ascii_none, ascii_1, ascii_2, ascii_3, ascii_4, ascii_5, ascii_6]
ascii_list = [ascii.splitlines() for ascii in ascii_list]
