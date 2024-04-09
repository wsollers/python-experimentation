print("hello world")
print(ord('Z'))

# TODO: Write recursive draw_triangle() function here.
def draw_triangle(base_length):
    spaces_length = 19 - base_length  #member we are capped byt the instructions at 19*'s
    if base_length == 1:
        #basee  case for last row. 1 star and 9 spaces
        print(" "*(spaces_length//2)+"*")
        return
    else:
        #print spaces for current base length 19=>0, 17=>1, 15=>2, 13=>3, 11=>4, 9=>5, 7=>6, 5=>7, 3=>8, 1=>9 etc..
        spaces = print(" "*(spaces_length//2), end = "")
        asters = print("*"*base_length)  
        #recursive call to draw triangle with base length -2, the -2 is because you lose a star from the front and back everyt time1
        draw_triangle(base_length-2)
        return

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length)

